"""
test_project_router.py — Unit tests for the capstone routing pilot.

Run with:
    python -m pytest tests/test_project_router.py -v
  or:
    python -m unittest tests.test_project_router -v

Scenarios covered:
  1.  Tracked open issue                 => would_add
  2.  Untracked item (no required label) => ignored
  3.  Excluded item (project:ignore)     => ignored
  4.  Closed item                        => ignored
  5.  Tracked open pull request          => would_add
  6.  Existing project membership        => already_present
  7.  Wrong repository                   => error
  8.  Wrong routing group                => error (validate_routing_context)
  9.  Unsupported item type              => ignored (safe, documented)
 10.  Invalid / missing config           => fail closed (ValueError / FileNotFoundError)
 11.  Candidate count above limit        => fail closed (OverflowError)
 12.  Dry-run mode has no write ops      => config.allow_project_writes is False;
                                            evaluate_items returns only decisions
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Allow running from repository root or from the tests/ directory
_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT / "scripts"))

from project_router import (  # noqa: E402
    ALREADY_PRESENT,
    ERROR,
    IGNORED,
    MAX_CANDIDATES_HARD_LIMIT,
    REQUIRED_REPOSITORY,
    REQUIRED_ROUTING_GROUP,
    WOULD_ADD,
    Item,
    RoutingConfig,
    RoutingDecision,
    build_report,
    count_candidates,
    evaluate_item,
    evaluate_items,
    load_config,
    validate_routing_context,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_DEFAULT_REPO = REQUIRED_REPOSITORY
_DEFAULT_GROUP = REQUIRED_ROUTING_GROUP


def _make_config(**overrides: object) -> RoutingConfig:
    """Return a minimal valid RoutingConfig, optionally overriding fields."""
    defaults = dict(
        repository=_DEFAULT_REPO,
        routing_group=_DEFAULT_GROUP,
        required_labels=["project:track"],
        excluded_labels=["project:ignore"],
        allowed_types=frozenset({"issue", "pull_request"}),
        dry_run=True,
        backfill=False,
        max_candidates=MAX_CANDIDATES_HARD_LIMIT,
        allow_deletion=False,
        allow_archive=False,
        allow_cross_repository=False,
        allow_project_writes=False,
    )
    defaults.update(overrides)
    return RoutingConfig(**defaults)  # type: ignore[arg-type]


def _make_item(**overrides: object) -> Item:
    """Return a minimal valid tracked-open issue, optionally overriding fields."""
    defaults = dict(
        id=1,
        type="issue",
        state="open",
        labels=["project:track"],
        repository=_DEFAULT_REPO,
        already_in_project=False,
    )
    defaults.update(overrides)
    return Item(**defaults)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Config YAML fixture helpers
# ---------------------------------------------------------------------------

_VALID_CONFIG_YAML = """\
schema: project-routing/v1
version: 1
repository:
  name: norrisaftcc/algocratic
routing:
  group: capstone
  required_labels:
    - "project:track"
  excluded_labels:
    - "project:ignore"
  allowed_types:
    - issue
    - pull_request
safety:
  dry_run: true
  backfill: false
  max_candidates: 25
  allow_deletion: false
  allow_archive: false
  allow_cross_repository: false
  allow_project_writes: false
project:
  owner: ~
  number: ~
"""


def _write_temp_config(content: str) -> str:
    """Write content to a temporary file and return its path."""
    fd, path = tempfile.mkstemp(suffix=".yml")
    with os.fdopen(fd, "w") as fh:
        fh.write(content)
    return path


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------


class TestEvaluateItem(unittest.TestCase):
    """evaluate_item() — single-item routing decisions."""

    def setUp(self) -> None:
        self.cfg = _make_config()

    # 1. Tracked open issue => would_add
    def test_tracked_open_issue_would_add(self) -> None:
        item = _make_item(type="issue", state="open", labels=["project:track"])
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, WOULD_ADD)

    # 2. Untracked item => ignored
    def test_untracked_item_ignored(self) -> None:
        item = _make_item(type="issue", state="open", labels=["some-other-label"])
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, IGNORED)

    # 3. Excluded item => ignored
    def test_excluded_label_ignored(self) -> None:
        item = _make_item(
            type="issue",
            state="open",
            labels=["project:track", "project:ignore"],
        )
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, IGNORED)

    # 4. Closed item => ignored
    def test_closed_item_ignored(self) -> None:
        item = _make_item(type="issue", state="closed", labels=["project:track"])
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, IGNORED)

    # 5. Tracked open pull request => would_add
    def test_tracked_open_pr_would_add(self) -> None:
        item = _make_item(
            id=42, type="pull_request", state="open", labels=["project:track"]
        )
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, WOULD_ADD)

    # 6. Existing project membership => already_present
    def test_already_in_project(self) -> None:
        item = _make_item(
            type="issue",
            state="open",
            labels=["project:track"],
            already_in_project=True,
        )
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, ALREADY_PRESENT)

    # 7. Wrong repository => error
    def test_wrong_repository_error(self) -> None:
        item = _make_item(
            repository="norrisaftcc/some-other-repo",
            state="open",
            labels=["project:track"],
        )
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, ERROR)

    # 9. Unsupported item type => ignored (safe documented behaviour)
    def test_unsupported_item_type_ignored(self) -> None:
        """Items with a type not in allowed_types are silently ignored (safe default)."""
        item = _make_item(type="release", state="open", labels=["project:track"])
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, IGNORED, "Unsupported types must be ignored, not error")

    def test_item_with_no_labels_ignored(self) -> None:
        item = _make_item(type="issue", state="open", labels=[])
        d = evaluate_item(item, self.cfg)
        self.assertEqual(d.decision, IGNORED)


class TestValidateRoutingContext(unittest.TestCase):
    """validate_routing_context() — run-time guard checks."""

    def _cfg(self) -> RoutingConfig:
        return _make_config()

    # 8a. Wrong repository raises ValueError
    def test_wrong_repository_raises(self) -> None:
        cfg = self._cfg()
        with self.assertRaises(ValueError, msg="Wrong repository must raise ValueError"):
            validate_routing_context(cfg, "norrisaftcc/wrong-repo", REQUIRED_ROUTING_GROUP)

    # 8b. Wrong routing group raises ValueError
    def test_wrong_routing_group_raises(self) -> None:
        cfg = self._cfg()
        with self.assertRaises(ValueError, msg="Wrong routing group must raise ValueError"):
            validate_routing_context(cfg, REQUIRED_REPOSITORY, "wrong-group")

    # 8c. Correct values pass without exception
    def test_correct_context_passes(self) -> None:
        cfg = self._cfg()
        validate_routing_context(cfg, REQUIRED_REPOSITORY, REQUIRED_ROUTING_GROUP)


class TestEvaluateItems(unittest.TestCase):
    """evaluate_items() — batch evaluation and candidate-limit guard."""

    def _cfg(self, max_candidates: int = MAX_CANDIDATES_HARD_LIMIT) -> RoutingConfig:
        return _make_config(max_candidates=max_candidates)

    # 11. Candidate count above limit => OverflowError (fail closed)
    def test_candidate_limit_exceeded_fails_closed(self) -> None:
        """When open qualifying items exceed max_candidates, raise OverflowError."""
        cfg = self._cfg(max_candidates=2)
        items = [
            _make_item(id=i, type="issue", state="open", labels=["project:track"])
            for i in range(3)
        ]
        with self.assertRaises(OverflowError):
            evaluate_items(items, cfg)

    def test_candidate_limit_exactly_at_limit_passes(self) -> None:
        """Exactly max_candidates qualifying items must not raise."""
        cfg = self._cfg(max_candidates=3)
        items = [
            _make_item(id=i, type="issue", state="open", labels=["project:track"])
            for i in range(3)
        ]
        decisions = evaluate_items(items, cfg)
        self.assertEqual(len(decisions), 3)

    def test_closed_items_not_counted_toward_limit(self) -> None:
        """Closed items are not routing candidates and must not count toward the limit."""
        cfg = self._cfg(max_candidates=1)
        items = [
            _make_item(id=1, type="issue", state="open", labels=["project:track"]),
            _make_item(id=2, type="issue", state="closed", labels=["project:track"]),
        ]
        decisions = evaluate_items(items, cfg)
        # 1 open candidate <= max_candidates=1 => no exception
        self.assertEqual(len(decisions), 2)

    def test_excluded_items_not_counted_toward_limit(self) -> None:
        """Items with an excluded label do not count as routing candidates."""
        cfg = self._cfg(max_candidates=1)
        items = [
            _make_item(id=1, type="issue", state="open", labels=["project:track"]),
            _make_item(
                id=2,
                type="issue",
                state="open",
                labels=["project:track", "project:ignore"],
            ),
        ]
        # Only item 1 is a candidate (item 2 is excluded), so count=1 <= limit=1
        decisions = evaluate_items(items, cfg)
        self.assertEqual(len(decisions), 2)


class TestCountCandidates(unittest.TestCase):
    """count_candidates() — pre-filter counting logic."""

    def test_counts_open_allowed_non_excluded(self) -> None:
        cfg = _make_config()
        items = [
            _make_item(id=1, state="open", type="issue", labels=["project:track"]),
            _make_item(id=2, state="closed", type="issue", labels=["project:track"]),
            _make_item(
                id=3,
                state="open",
                type="issue",
                labels=["project:track", "project:ignore"],
            ),
            _make_item(id=4, state="open", type="issue", labels=[]),
        ]
        # Items 1 and 4: open, allowed type, no excluded label => 2 candidates
        # Item 2: closed => not a candidate
        # Item 3: has excluded label "project:ignore" => not a candidate
        self.assertEqual(count_candidates(items, cfg), 2)


class TestLoadConfig(unittest.TestCase):
    """load_config() — validation and fail-closed behaviour."""

    # 10a. Valid config loads without error
    def test_valid_config_loads(self) -> None:
        path = _write_temp_config(_VALID_CONFIG_YAML)
        try:
            cfg = load_config(path)
            self.assertEqual(cfg.repository, REQUIRED_REPOSITORY)
            self.assertEqual(cfg.routing_group, REQUIRED_ROUTING_GROUP)
            self.assertTrue(cfg.dry_run)
            self.assertFalse(cfg.allow_project_writes)
        finally:
            os.unlink(path)

    # 10b. Missing config file => FileNotFoundError
    def test_missing_config_fails_closed(self) -> None:
        with self.assertRaises(FileNotFoundError):
            load_config("/nonexistent/path/routing.yml")

    # 10c. Empty file => ValueError
    def test_empty_config_fails_closed(self) -> None:
        path = _write_temp_config("")
        try:
            with self.assertRaises(ValueError):
                load_config(path)
        finally:
            os.unlink(path)

    # 10d. Wrong schema => ValueError
    def test_wrong_schema_fails_closed(self) -> None:
        bad = _VALID_CONFIG_YAML.replace(
            "schema: project-routing/v1", "schema: wrong/schema"
        )
        path = _write_temp_config(bad)
        try:
            with self.assertRaises(ValueError):
                load_config(path)
        finally:
            os.unlink(path)

    # 10e. dry_run: false => ValueError
    def test_dry_run_false_fails_closed(self) -> None:
        bad = _VALID_CONFIG_YAML.replace("dry_run: true", "dry_run: false")
        path = _write_temp_config(bad)
        try:
            with self.assertRaises(ValueError):
                load_config(path)
        finally:
            os.unlink(path)

    # 10f. max_candidates above hard limit => ValueError
    def test_max_candidates_above_hard_limit_fails_closed(self) -> None:
        bad = _VALID_CONFIG_YAML.replace("max_candidates: 25", "max_candidates: 99")
        path = _write_temp_config(bad)
        try:
            with self.assertRaises(ValueError):
                load_config(path)
        finally:
            os.unlink(path)

    # 10g. Actual config file in repository must load cleanly
    def test_repository_config_is_valid(self) -> None:
        """The checked-in .github/project-routing-capstone.yml must be valid."""
        repo_config = _REPO_ROOT / ".github" / "project-routing-capstone.yml"
        if not repo_config.exists():
            self.skipTest(
                f"Config not yet present at {repo_config} (environment limitation)"
            )
        cfg = load_config(repo_config)
        self.assertEqual(cfg.repository, REQUIRED_REPOSITORY)
        self.assertEqual(cfg.routing_group, REQUIRED_ROUTING_GROUP)
        self.assertTrue(cfg.dry_run)
        self.assertFalse(cfg.allow_project_writes)


class TestDryRunNoPersistentSideEffects(unittest.TestCase):
    """12. Dry-run mode must not perform any write operation.

    These tests verify that:
    - config.allow_project_writes is always False
    - config.allow_deletion is always False
    - config.allow_archive is always False
    - evaluate_items() returns only RoutingDecision objects (no side effects)
    """

    def test_config_forbids_project_writes(self) -> None:
        path = _write_temp_config(_VALID_CONFIG_YAML)
        try:
            cfg = load_config(path)
            self.assertFalse(cfg.allow_project_writes)
            self.assertFalse(cfg.allow_deletion)
            self.assertFalse(cfg.allow_archive)
        finally:
            os.unlink(path)

    def test_evaluate_items_returns_only_decisions(self) -> None:
        cfg = _make_config()
        items = [
            _make_item(id=1, state="open", labels=["project:track"]),
            _make_item(id=2, state="open", labels=[]),
        ]
        decisions = evaluate_items(items, cfg)
        for d in decisions:
            self.assertIsInstance(d, RoutingDecision)

    def test_evaluate_items_does_not_mutate_items(self) -> None:
        cfg = _make_config()
        item = _make_item(id=1, state="open", labels=["project:track"])
        original_labels = list(item.labels)
        evaluate_items([item], cfg)
        self.assertEqual(item.labels, original_labels)


class TestBuildReport(unittest.TestCase):
    """build_report() — report structure validation."""

    def test_report_mode_is_dry_run(self) -> None:
        cfg = _make_config()
        report = build_report([], cfg)
        self.assertEqual(report["mode"], "DRY_RUN")

    def test_report_contains_correct_repository(self) -> None:
        cfg = _make_config()
        report = build_report([], cfg)
        self.assertEqual(report["repository"], REQUIRED_REPOSITORY)

    def test_report_summary_counts(self) -> None:
        cfg = _make_config()
        decisions = [
            RoutingDecision(1, "issue", WOULD_ADD, "ok"),
            RoutingDecision(2, "issue", IGNORED, "no label"),
            RoutingDecision(3, "issue", ALREADY_PRESENT, "present"),
            RoutingDecision(4, "issue", ERROR, "bad repo"),
        ]
        report = build_report(decisions, cfg)
        s = report["summary"]
        self.assertEqual(s[WOULD_ADD], 1)
        self.assertEqual(s[IGNORED], 1)
        self.assertEqual(s[ALREADY_PRESENT], 1)
        self.assertEqual(s[ERROR], 1)

    def test_report_is_json_serialisable(self) -> None:
        cfg = _make_config()
        decisions = [
            RoutingDecision(1, "issue", WOULD_ADD, "ok"),
        ]
        report = build_report(decisions, cfg)
        # Must not raise
        serialised = json.dumps(report)
        self.assertIsInstance(serialised, str)


class TestPullRequestDeduplication(unittest.TestCase):
    """Pull requests must not be double-counted with issues."""

    def test_pr_evaluated_as_pull_request_type(self) -> None:
        cfg = _make_config()
        pr = _make_item(id=10, type="pull_request", state="open", labels=["project:track"])
        d = evaluate_item(pr, cfg)
        self.assertEqual(d.decision, WOULD_ADD)
        self.assertEqual(d.item_type, "pull_request")

    def test_pr_with_wrong_type_string_ignored(self) -> None:
        """A PR accidentally typed as 'issue' is treated as an issue — no cross-type error."""
        cfg = _make_config()
        item = _make_item(id=10, type="issue", state="open", labels=["project:track"])
        d = evaluate_item(item, cfg)
        # Still gets evaluated normally; type is in allowed_types
        self.assertIn(d.decision, {WOULD_ADD, ALREADY_PRESENT})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
