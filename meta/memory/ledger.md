---
id: memory-ledger
type: log
status: active
created: 2026-07-01
updated: 2026-07-13
aliases:
  - "Memory ledger"
  - "Memory change log"
tags: [memory, trust, ledger]
source_path: "meta/memory/ledger.md"
knowledge_criticality: high
verification_status: unverified
curation_mode: llm_explicit_request
---

# Memory Ledger

## Essence

Append-only log for changes to durable vault memory: current pictures, claim status, confidence, conflicts, anti-memory rules, and strategic memory decisions.

## When To Write Here

Add a record when an agent or script changes:

- an important memory claim;
- `claim_type`, `confidence`, `last_verified`, `status`, or `write_policy`;
- a current picture of a project or contour;
- a strategic decision or key constraint;
- a claim status such as stale, contradicted, superseded, archived, or restored;
- a memory conflict.

## Record Format

```md
## YYYY-MM-DD HH:MM

Changed:
- `path/to/file.md`

Action:
- created | updated | marked_stale | superseded | archived | restored | deleted | proposed

Reason:
- why this change was made

Source:
- `path/to/source.md`

Changed by:
- agent | human | script

Review:
- auto_applied | pending_deferred_review | pending_human_review | owner_requested | approved | rejected
```

## Next step

Append new records whenever memory trust, status, current picture, or conflict state changes.
