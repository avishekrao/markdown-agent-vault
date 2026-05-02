---
id: cleanup-by-design
type: rules
status: active
created: 2026-03-31
updated: 2026-04-15
aliases:
  - "Cleanup rule"
  - "Cleanup by design"
  - "Anti-wash"
tags: [rules, cleanup, vault-hygiene, lifecycle]
source_path: "meta/rules/cleanup-by-design.md"
---

# Cleanup by Design: Artifact Lifecycle Rule

## Essence

Any agent that creates a file, database, cache, or dump is **required** to specify in the same action how and when the artifact will be cleared. Without a lifecycle plan, creating an artifact is **prohibited**.

Vault is a working system, not a dump. Each artifact either lives consciously or is not created.

---

## What NOT to delete automatically

- **Logs** (`*.log`, `runs.log`) - show the project status, launch history, errors. Delete only upon explicit command of the owner.
- **Contents `00_inbox/`** is a dismantling area, not trash. The files may be valuable. Parsed manually via [vault-review](./vault-review.md).
- **Contents `01_now/`, `02_domains/`, `03_knowledge/`** - permanent storage. Archived and not deleted.
- **Data dumps** (`*-dumps/`) - may be needed for analysis. Remove only at the discretion of the owner.
- **Delegation files** (`01_now/ops/<contour>/delegations/<person-slug>.md`) - DO NOT delete automatically even if all lines have moved to `Archive`. Rotation happens through a forced owner rewrite (see [vault-lifecycle-sop.md](../vault-lifecycle-sop.md#delegation-cleanup)).
- **`01_now/personal/tasks.md`** - DO NOT automatically delete or archive. This file is rotated only by the owner through monthly forced rewrite.

---

## What CAN be deleted automatically

| Class | Where | TTL | Why is it safe |
|-------|-----|-----|-----------------|
| **temp** | `tmp/` | 7 days | Intermediate files, tests, build artifacts. Everything valuable has already been extracted. |
| **cache** | `.smart-env/multi/` | 30 days | Obsidian Smart Connections, regenerates automatically |
| **cache** | `*/.model-cache/` | 30 days | ML models will be downloaded again |
| **db records** | SQLite: `classification='trash'` | 90 days | Email metadata classified as "garbage" |
| **db records** | SQLite: `classification='fyi'` | 180 days | Email metadata "note" |

---

## Mandatory agent actions when creating an artifact

### 1. Define the class

Ask yourself: “Will this artifact be needed in a month?”
- Yes → permanent (not auto-cleaning)
- No → define TTL and cleaning method

### 2. If the artifact is NOT permanent, write it in the code

```python# LIFECYCLE: temp, TTL=7d, cleanup via vault-hygiene.py
```

Every script that creates temporary files or TTL entries must have either:
- cleanup function in the script itself, or
- write to `meta/cleanup-registry.md` so that `vault-hygiene.py` knows about this artifact

### 3. If you create a new folder

Add an entry to the [artifact registry](../cleanup-registry.md).

### 4. If you are creating SQLite

Required:
- DDL with the record creation date (`created_at` / `fetched_at`) so that there is a field for TTL filtering
- Register the database in [cleanup-registry.md](../cleanup-registry.md): path, tables, TTL records, who creates
- Define a cleanup strategy for each table:

| Data type | Strategy |
|-----------|-----------|
| Cache, intermediate data | DELETE by TTL + VACUUM |
| Metadata with classification | DELETE by classification + TTL (as email: trash=90d, fyi=180d) |
| Work entries (actionable) | Do not delete automatically, only by owner's decision |
| Processing log (processed) | Store ∞ is an audit trail |

### 5. Monitoring SQLite

The `vault-hygiene.py` script in `--report` mode shows for each registered database:
- File size
- Number of records in tables
- Number of expired records (ready to be cleared)- Date of last entry (data freshness)

---

## Prohibited

- ❌ Create files without understanding their lifecycle
- ❌ Create SQLite databases without a date field for TTL
- ❌ Automatically delete content `00_inbox/` (this is a parsing zone, not garbage)
- ❌ Automatically delete logs (they show the status of the project)
- ❌ Assume that the owner will handle the cleaning himself
- ❌ Create an artifact without checking if there is already a similar one (anti-duplication)

---

## Tools

- **Auto-clean:** `scripts/vault-hygiene.py` - cleans only safe-to-delete (tmp/, caches, expired DB records)
- **Report:** `python3 vault-hygiene.py` (without --clean) - shows disk usage and what can be cleaned
- **Manual review:** [vault-review.md](./vault-review.md) - inbox analysis, archiving of completed projects
- **Registry:** [cleanup-registry.md](../cleanup-registry.md) - what is where with what TTL

---

## Connections

- [Recording protocol](./write-protocol.md) - general rules for creating files
- [Protocol review vault](./vault-review.md) - manual cleaning
- [Save threshold](./save-and-extract.md) - when to save, when not
