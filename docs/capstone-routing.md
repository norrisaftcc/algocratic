# Capstone Routing Pilot — `norrisaftcc/algocratic`

Dry-run evaluation of which open issues and pull requests in
`norrisaftcc/algocratic` would be routed to the **capstone** GitHub Project
group.

> **This is a dry-run pilot only.**  
> No GitHub Project items are added, updated, archived, or deleted.  
> Live Project integration requires a separate approval.

---

## Routing rules

An item is evaluated as **`would_add`** only when **all** of the following are
true:

| Rule | Value |
|---|---|
| Repository | exactly `norrisaftcc/algocratic` |
| Routing group | exactly `capstone` |
| Item type | `issue` or `pull_request` |
| Item state | `open` |
| Has required label | `project:track` |
| Does not have excluded label | `project:ignore` |
| Not already in the project | `already_in_project: false` |

Failing any rule produces one of the other decisions:

| Decision | Meaning |
|---|---|
| `would_add` | Item meets all criteria; would be added in a live run |
| `ignored` | Item does not meet one or more criteria; skipped |
| `already_present` | Item is already present in the project |
| `error` | Item carries an invalid value (e.g. wrong repository) |

Ambiguous or invalid configuration **fails closed** with a non-zero exit code
and no partial processing.

---

## Configuration

File: `.github/project-routing-capstone.yml`

Key fields:

```yaml
schema: project-routing/v1
repository:
  name: norrisaftcc/algocratic
routing:
  group: capstone
  required_labels: ["project:track"]
  excluded_labels: ["project:ignore"]
  allowed_types: [issue, pull_request]
safety:
  dry_run: true          # permanently true; cannot be disabled
  backfill: false
  max_candidates: 25     # hard limit; exceeding fails closed
  allow_project_writes: false
```

`project.owner` and `project.number` are intentionally unset.
This pilot does not connect to a validated live GitHub Project.

---

## Workflow

File: `.github/workflows/capstone-routing-dryrun.yml`

**Trigger:** manual only (`workflow_dispatch`).  
The workflow does **not** respond automatically to issue or pull-request events.

**Permissions requested:**

```yaml
permissions:
  contents: read
  issues: read
  pull-requests: read
```

**Credential:** only the automatically-supplied `GITHUB_TOKEN`.  
No external secrets are required or used.

**What the workflow does:**

1. Checks out the repository.
2. Installs Python and PyYAML.
3. Runs all unit tests (`tests/test_project_router.py`).
4. Validates the routing configuration.
5. Fetches open issues via the GitHub REST API (pull requests excluded from
   this call to prevent double-counting).
6. Fetches open pull requests via a separate REST API call.
7. Merges both lists and deduplicates by `(type, id)`.
8. Runs the routing evaluator (`scripts/project_router.py`).
9. Prints a concise summary and the full JSON report.
10. Uploads the JSON report as an artifact (retained 14 days).

**No GitHub Project mutation command appears anywhere in the workflow.**

### Running the workflow

1. Go to **Actions** → **Capstone Routing Dry-Run** → **Run workflow**.
2. Enter any text in the confirmation field (or keep the default).
3. Click **Run workflow**.
4. Review the console output and download the `routing-report` artifact.

---

## Local execution

Prerequisites: Python ≥ 3.9 and PyYAML.

```bash
pip install pyyaml pytest
```

Run tests:

```bash
python -m pytest tests/test_project_router.py -v
```

Prepare a sample items file (for local testing):

```bash
cat > /tmp/items.json <<'EOF'
[
  {
    "id": 1,
    "type": "issue",
    "state": "open",
    "labels": ["project:track"],
    "repository": "norrisaftcc/algocratic",
    "already_in_project": false
  }
]
EOF
```

Run the evaluator:

```bash
python scripts/project_router.py \
    --config .github/project-routing-capstone.yml \
    --items /tmp/items.json \
    --report /tmp/report.json
```

---

## Report fields

The JSON report (`/tmp/routing-report.json` or the `routing-report` artifact)
contains:

| Field | Type | Description |
|---|---|---|
| `mode` | string | Always `"DRY_RUN"` |
| `repository` | string | `"norrisaftcc/algocratic"` |
| `routing_group` | string | `"capstone"` |
| `summary.would_add` | integer | Items that would be added |
| `summary.already_present` | integer | Items already in the project |
| `summary.ignored` | integer | Items that did not qualify |
| `summary.error` | integer | Items with data errors |
| `items` | array | Per-item `id`, `type`, `decision`, `reason` |

---

## Permissions

The workflow requests only read-only GitHub token scopes:

- `contents: read` — check out the repository.
- `issues: read` — list open issues.
- `pull-requests: read` — list open pull requests.

No `projects` scope is requested or used. No external token or secret is
needed.

---

## Limitations

- **No live Project integration.** `project.owner` and `project.number` in the
  configuration are unset. The pilot does not add items to any GitHub Project.
- **No event-driven trigger.** The workflow runs only on `workflow_dispatch`.
  Automatic routing on issue/PR creation is not implemented in this pilot.
- **Backfill is disabled.** `backfill: false` in the configuration. Historic
  items are not evaluated in bulk.
- **Maximum 25 candidates.** If more than 25 open items match the pre-filter,
  the run fails closed. Reduce qualifying items or open a separate approval to
  raise the limit.
- **Single repository scope.** The routing logic and constants hard-code
  `norrisaftcc/algocratic`. Cross-repository routing is blocked by
  `allow_cross_repository: false`.

---

## Future activation

To connect this pilot to a real GitHub Project:

1. Obtain a separate written approval from the repository owner.
2. Set `project.owner` and `project.number` in the configuration.
3. Add a `PROJECTS_TOKEN` secret with the minimum required GitHub App or token
   scope (typically `project` write for the specific project only).
4. Replace the dry-run-only evaluation path with a live mutation path after
   code review.
5. Keep `dry_run: true` for the first several runs and verify the report.
6. Enable live mode only after the report has been reviewed and approved.

---

## Rollback

To disable the routing pilot without affecting any Project data:

1. Disable the workflow:  
   **Actions** → **Capstone Routing Dry-Run** → **···** → **Disable workflow**.  
   _Or_ delete `.github/workflows/capstone-routing-dryrun.yml`.
2. Optionally revert this pull request.
3. No GitHub Project items, issues, pull requests, labels, secrets, or
   repository settings are affected by either step.

---

## Files changed by this pilot

| File | Purpose |
|---|---|
| `.github/project-routing-capstone.yml` | Routing configuration (schema, rules, safety flags) |
| `.github/workflows/capstone-routing-dryrun.yml` | `workflow_dispatch`-only evaluation workflow |
| `scripts/project_router.py` | Deterministic routing evaluator (Python, no external API calls) |
| `tests/test_project_router.py` | 33 unit tests covering all required scenarios |
| `docs/capstone-routing.md` | This document |
