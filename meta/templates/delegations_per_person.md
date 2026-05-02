---
id: <contour-slug>-delegations-<person-slug>
type: delegations
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
aliases:
  - "Delegations <name of surname> (<contour>)"
tags: [delegations, ops, <contour-slug>, person-<person-slug>]
source_path: "01_now/ops/<contour-slug>/delegations/<person-slug>.md"
contour: <contour-slug>
person_slug: <person-slug>
tracker_sot: <external-tracker|none>
knowledge_criticality: medium
verification_status: active
---

# Delegations: <name of surname> (<contour>)

## The essence

**Lean index* of delegates of one person in one loop. One line to the task + link to the external tracker. The file is not the source of the problem status, but the navigation index. The current status is taken from the tracker (see [live-first-audit.md](../../../../meta/rules/live-first-audit.md)]).

Methodology: [task-routing.md §delegations](../../../../meta/rules/task-routing.md)]. Rule of ownership: [AGENTS.md Rule 11](../../../../AGENTS.md)].

## Rules

- One file = one pair of `(contour, delegate)`. If a delegate works in two circuits, two files, because the SoT tracker has its own circuit.
- The source of the task truth is always in the external tracker specified in the `tracker_sot` service markup.
- Line format:
  ```
  - [ ] 2026-04-12 → the essence of the problem [TRACKER-123](url) • due: 2026-04-20 • [meeting](rel-link)]
  ```
  - The production date is mandatory.
  - The link to the tracker is necessarily a SoT.
  - `due:` - if any, serves as the basis for a grep filter (`due:` → waiting/overdue field).
  - Meet/Context Link – Optional, helps to retrieve why.
- **Sections:** `Active`, `Done (7d)`, `Archive` only. `Waiting` and `Overdue` via the `due:` and grep field.
- **Passive recall:** When a delegate name is mentioned in a fresh context, the agent displays open lines from that file. Weekly review is not being conducted.
- **Cleanup:** Lines in `Done (7d)` older than 7 days - transfer to `Archive`. Once a month – forced rewrite file.

## Active

- [ ] <YYYYY-MM-DD> → <the essence of the problem> [TRACKER-123](url) • due: <YYYY-MM-DD] >>
- [ ] <YYYYY-MM-DD> → <essence> [TRACKER-124](url)]

## Done (7d)

- [x] <YYYYY-MM-DD> → <essence> [TRACKER-120](url) ► <YYYY-MM-] DDD >>

## Archive

Historical lines are older than 7 days after closing. The form is the same, but without `[ ]`/`[x]` is just a compact record.

- <YYYYY-MM-DD> → <essence> [TRACKER-100](url) ► <YYYY-MM-] DDD >>

## Next step.

The file is supported by an ambient image. First Delegate Activity in Fresh Context: View `Active` through Passive Recall.
