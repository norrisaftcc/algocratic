"""
project_router.py — Capstone GitHub Projects routing pilot (dry-run only).

Evaluates open issues and pull requests in norrisaftcc/algocratic and
determines which would be routed to the "capstone" group.

Usage (CLI):
    python scripts/project_router.py \\
        --config .github/project-routing-capstone.yml \\
        --items items.json \\
        [--report report.json]

The items JSON file must be an array of objects with these fields:
    id            integer or string identifier
    type          "issue" or "pull_request"
    state         "open" or "closed"
    labels        array of label name strings
    repository    "owner/repo" string
    already_in_project  (optional) boolean, default false

Exit codes:
    0   Evaluation completed (see report for decisions)
    1   Configuration or validation error (fails closed)
    2   Candidate count exceeded max_candidates limit (fails closed)
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_REPOSITORY = "norrisaftcc/algocratic"
REQUIRED_ROUTING_GROUP = "capstone"
CONFIG_SCHEMA = "project-routing/v1"
MAX_CANDIDATES_HARD_LIMIT = 25

# Decision values
WOULD_ADD = "would_add"
IGNORED = "ignored"
ALREADY_PRESENT = "already_present"
ERROR = "error"

ALLOWED_ITEM_TYPES: frozenset[str] = frozenset({"issue", "pull_request"})

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class RoutingConfig:
    repository: str
    routing_group: str
    required_labels: list[str]
    excluded_labels: list[str]
    allowed_types: frozenset[str]
    dry_run: bool
    backfill: bool
    max_candidates: int
    allow_deletion: bool
    allow_archive: bool
    allow_cross_repository: bool
    allow_project_writes: bool


@dataclass
class Item:
    id: int | str
    type: str  # "issue" or "pull_request"
    state: str  # "open" or "closed"
    labels: list[str]
    repository: str
    already_in_project: bool = False

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Item":
        return Item(
            id=data["id"],
            type=str(data["type"]),
            state=str(data["state"]),
            labels=list(data.get("labels", [])),
            repository=str(data["repository"]),
            already_in_project=bool(data.get("already_in_project", False)),
        )


@dataclass
class RoutingDecision:
    item_id: int | str
    item_type: str
    decision: str  # one of WOULD_ADD, IGNORED, ALREADY_PRESENT, ERROR
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.item_id,
            "type": self.item_type,
            "decision": self.decision,
            "reason": self.reason,
        }


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------


def load_config(config_path: str | Path) -> RoutingConfig:
    """Load and validate routing configuration from a YAML file.

    Raises FileNotFoundError, ValueError, or ImportError on any problem.
    """
    try:
        import yaml  # type: ignore[import]
    except ImportError as exc:
        raise ImportError("PyYAML is required: pip install pyyaml") from exc

    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(path) as fh:
        data = yaml.safe_load(fh)

    if not data or not isinstance(data, dict):
        raise ValueError("Config file is empty or does not contain a YAML mapping")

    # Schema check
    schema = data.get("schema")
    if schema != CONFIG_SCHEMA:
        raise ValueError(
            f"Invalid config schema: expected '{CONFIG_SCHEMA}', got '{schema!r}'"
        )

    # Repository
    repo_section = data.get("repository")
    if not isinstance(repo_section, dict):
        raise ValueError("Missing required section: repository")
    repository_name = repo_section.get("name")
    if not repository_name:
        raise ValueError("Missing required field: repository.name")

    # Routing
    routing_section = data.get("routing")
    if not isinstance(routing_section, dict):
        raise ValueError("Missing required section: routing")
    routing_group = routing_section.get("group")
    if not routing_group:
        raise ValueError("Missing required field: routing.group")

    # Safety
    safety_section = data.get("safety", {})
    if not isinstance(safety_section, dict):
        raise ValueError("'safety' section must be a mapping if present")

    dry_run = safety_section.get("dry_run", True)
    if not dry_run:
        raise ValueError(
            "dry_run must be true; live Project mutation is not implemented"
        )

    for flag_name in (
        "allow_deletion",
        "allow_archive",
        "allow_cross_repository",
        "allow_project_writes",
    ):
        if bool(safety_section.get(flag_name, False)):
            raise ValueError(
                f"Safety flag '{flag_name}' must be false in dry-run mode"
            )

    max_candidates = safety_section.get("max_candidates", MAX_CANDIDATES_HARD_LIMIT)
    if not isinstance(max_candidates, int) or max_candidates < 1:
        raise ValueError(f"max_candidates must be a positive integer, got {max_candidates!r}")
    if max_candidates > MAX_CANDIDATES_HARD_LIMIT:
        raise ValueError(
            f"max_candidates ({max_candidates}) exceeds hard limit ({MAX_CANDIDATES_HARD_LIMIT})"
        )

    allowed_types_raw = routing_section.get("allowed_types", list(ALLOWED_ITEM_TYPES))
    if not isinstance(allowed_types_raw, list):
        raise ValueError(
            f"routing.allowed_types must be a list, got {type(allowed_types_raw).__name__}"
        )
    allowed_types = frozenset(str(t) for t in allowed_types_raw)
    unknown_types = allowed_types - ALLOWED_ITEM_TYPES
    if unknown_types:
        raise ValueError(
            f"Unknown item types in routing.allowed_types: {sorted(unknown_types)}"
        )

    required_labels_raw = routing_section.get("required_labels", ["project:track"])
    if not isinstance(required_labels_raw, list):
        raise ValueError(
            f"routing.required_labels must be a list, got {type(required_labels_raw).__name__}"
        )

    excluded_labels_raw = routing_section.get("excluded_labels", ["project:ignore"])
    if not isinstance(excluded_labels_raw, list):
        raise ValueError(
            f"routing.excluded_labels must be a list, got {type(excluded_labels_raw).__name__}"
        )

    return RoutingConfig(
        repository=str(repository_name),
        routing_group=str(routing_group),
        required_labels=list(required_labels_raw),
        excluded_labels=list(excluded_labels_raw),
        allowed_types=allowed_types,
        dry_run=bool(dry_run),
        backfill=bool(safety_section.get("backfill", False)),
        max_candidates=int(max_candidates),
        allow_deletion=bool(safety_section.get("allow_deletion", False)),
        allow_archive=bool(safety_section.get("allow_archive", False)),
        allow_cross_repository=bool(safety_section.get("allow_cross_repository", False)),
        allow_project_writes=bool(safety_section.get("allow_project_writes", False)),
    )


# ---------------------------------------------------------------------------
# Context validation
# ---------------------------------------------------------------------------


def validate_routing_context(
    config: RoutingConfig,
    repository: str,
    routing_group: str,
) -> None:
    """Validate run-time repository and routing group against config and constants.

    Raises ValueError on any mismatch. Fails closed.
    """
    if repository != REQUIRED_REPOSITORY:
        raise ValueError(
            f"Repository '{repository}' is not the required repository "
            f"'{REQUIRED_REPOSITORY}'"
        )
    if repository != config.repository:
        raise ValueError(
            f"Repository '{repository}' does not match config repository "
            f"'{config.repository}'"
        )
    if routing_group != REQUIRED_ROUTING_GROUP:
        raise ValueError(
            f"Routing group '{routing_group}' is not the required group "
            f"'{REQUIRED_ROUTING_GROUP}'"
        )
    if routing_group != config.routing_group:
        raise ValueError(
            f"Routing group '{routing_group}' does not match config routing_group "
            f"'{config.routing_group}'"
        )


# ---------------------------------------------------------------------------
# Item evaluation
# ---------------------------------------------------------------------------


def evaluate_item(item: Item, config: RoutingConfig) -> RoutingDecision:
    """Evaluate one item against routing rules and return a decision."""

    # Repository scope check
    if item.repository != config.repository:
        return RoutingDecision(
            item_id=item.id,
            item_type=item.type,
            decision=ERROR,
            reason=(
                f"Item repository '{item.repository}' does not match "
                f"config repository '{config.repository}'"
            ),
        )

    # Item type check
    if item.type not in config.allowed_types:
        return RoutingDecision(
            item_id=item.id,
            item_type=item.type,
            decision=IGNORED,
            reason=(
                f"Item type '{item.type}' is not in allowed types "
                f"{sorted(config.allowed_types)}"
            ),
        )

    # State check — only open items are routed
    if item.state != "open":
        return RoutingDecision(
            item_id=item.id,
            item_type=item.type,
            decision=IGNORED,
            reason=f"Item is not open (state: '{item.state}')",
        )

    # Excluded label check
    for excluded in config.excluded_labels:
        if excluded in item.labels:
            return RoutingDecision(
                item_id=item.id,
                item_type=item.type,
                decision=IGNORED,
                reason=f"Item has excluded label '{excluded}'",
            )

    # Required label check
    has_required = any(req in item.labels for req in config.required_labels)
    if not has_required:
        return RoutingDecision(
            item_id=item.id,
            item_type=item.type,
            decision=IGNORED,
            reason=(
                f"Item does not have any required label "
                f"{config.required_labels}"
            ),
        )

    # Existing project membership check
    if item.already_in_project:
        return RoutingDecision(
            item_id=item.id,
            item_type=item.type,
            decision=ALREADY_PRESENT,
            reason="Item is already present in the project",
        )

    return RoutingDecision(
        item_id=item.id,
        item_type=item.type,
        decision=WOULD_ADD,
        reason="Item meets all routing criteria",
    )


# ---------------------------------------------------------------------------
# Batch evaluation (with candidate-count guard)
# ---------------------------------------------------------------------------


def count_candidates(items: list[Item], config: RoutingConfig) -> int:
    """Count items that pass the pre-filter (open, allowed type, not excluded).

    These are the items that would be evaluated against required labels and
    membership, i.e. the routing candidates.
    """
    count = 0
    for item in items:
        if (
            item.repository == config.repository
            and item.state == "open"
            and item.type in config.allowed_types
            and not any(excl in item.labels for excl in config.excluded_labels)
        ):
            count += 1
    return count


def evaluate_items(
    items: list[Item], config: RoutingConfig
) -> list[RoutingDecision]:
    """Evaluate all items.

    Raises OverflowError (exit code 2) if the candidate count exceeds
    max_candidates — fail closed rather than processing a truncated set.
    """
    n_candidates = count_candidates(items, config)
    if n_candidates > config.max_candidates:
        raise OverflowError(
            f"Candidate count ({n_candidates}) exceeds max_candidates "
            f"({config.max_candidates}). Reduce open items matching the "
            f"routing criteria or raise max_candidates (hard limit: "
            f"{MAX_CANDIDATES_HARD_LIMIT})."
        )

    return [evaluate_item(item, config) for item in items]


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def build_report(
    decisions: list[RoutingDecision], config: RoutingConfig
) -> dict[str, Any]:
    """Build a JSON-serialisable routing report."""
    counts: dict[str, int] = {WOULD_ADD: 0, IGNORED: 0, ALREADY_PRESENT: 0, ERROR: 0}
    for d in decisions:
        counts[d.decision] = counts.get(d.decision, 0) + 1

    return {
        "mode": "DRY_RUN",
        "repository": config.repository,
        "routing_group": config.routing_group,
        "summary": counts,
        "items": [d.to_dict() for d in decisions],
    }


def print_summary(report: dict[str, Any]) -> None:
    """Print a concise human-readable summary to stdout."""
    s = report["summary"]
    print("--- Capstone Routing Dry-Run Summary ---")
    print(f"Mode:             {report['mode']}")
    print(f"Repository:       {report['repository']}")
    print(f"Routing group:    {report['routing_group']}")
    print(f"Would add:        {s.get(WOULD_ADD, 0)}")
    print(f"Already present:  {s.get(ALREADY_PRESENT, 0)}")
    print(f"Ignored:          {s.get(IGNORED, 0)}")
    print(f"Errors:           {s.get(ERROR, 0)}")
    print("No changes were made (dry-run mode).")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capstone project routing dry-run evaluator",
    )
    parser.add_argument(
        "--config",
        default=".github/project-routing-capstone.yml",
        help="Path to the routing configuration YAML file",
    )
    parser.add_argument(
        "--items",
        required=True,
        help="Path to a JSON file containing an array of items to evaluate",
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Optional path to write the JSON report",
    )
    parser.add_argument(
        "--repository",
        default=REQUIRED_REPOSITORY,
        help="Repository being processed (must equal norrisaftcc/algocratic)",
    )
    parser.add_argument(
        "--routing-group",
        default=REQUIRED_ROUTING_GROUP,
        help="Routing group (must equal capstone)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:  # noqa: C901
    """CLI entry point. Returns an exit code."""
    args = _parse_args(argv)

    # Load config — fail closed on any error
    try:
        config = load_config(args.config)
    except (FileNotFoundError, ValueError, ImportError) as exc:
        print(f"ERROR: Failed to load config: {exc}", file=sys.stderr)
        return 1

    # Validate routing context
    try:
        validate_routing_context(config, args.repository, args.routing_group)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    # Load items
    try:
        items_path = Path(args.items)
        if not items_path.exists():
            print(f"ERROR: Items file not found: {args.items}", file=sys.stderr)
            return 1
        with open(items_path) as fh:
            raw_items = json.load(fh)
        if not isinstance(raw_items, list):
            print("ERROR: Items file must contain a JSON array", file=sys.stderr)
            return 1
        items = [Item.from_dict(r) for r in raw_items]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR: Failed to parse items file: {exc}", file=sys.stderr)
        return 1

    # Evaluate
    try:
        decisions = evaluate_items(items, config)
    except OverflowError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"ERROR: Unexpected error during evaluation: {exc}", file=sys.stderr)
        return 1

    # Build report
    report = build_report(decisions, config)
    print_summary(report)

    # Optionally write report file
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w") as fh:
            json.dump(report, fh, indent=2)
        print(f"Report written to: {args.report}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
