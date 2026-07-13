---
id: <yyyy-mm-dd>-<project-slug>-context
type: project
status: active
created: <YYYY-MM-DD>
updated: 2026-07-01
aliases:
  - "Project context template"
tags: [project, context]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: low
verification_status: unverified
verified_by_me: false
curation_mode: none
---

# Context

## Essence

Durable project invariants in one place: terms, metrics, source of truth, and constraints.

Do not store meeting episodes here. Meeting episodes live in meeting files under `## Mentioned in passing` with canonical tags. Move something into `context.md` only when the owner or agent formulates an actual working opinion such as "we know X about Y", not because a topic was mentioned many times.

If current status starts appearing here (what matters now, what changed, what is stale), move it into a separate working context and link it from this file and `README.md`. See [vault-memory.md](../rules/vault-memory.md).

For invariants that affect decisions, deadlines, architecture, product commitments, or current picture, add a lightweight trust block:

```yaml
claim_type: observed | stated_by_user | stated_by_other | inferred | decision | assumption | hypothesis | preference | constraint | plan | risk | status | historical
source:
  - ""
evidence:
  kind: direct_user_statement | direct_quote | meeting_note | document_fact | agent_inference | repeated_pattern | external_source | unknown
  strength: high | medium | low
confidence: high | medium | low
last_verified: YYYY-MM-DD
write_policy: auto | suggest | human_review_required | locked
```

If the basis is weak or old, do not phrase the invariant as an unconditional fact. Mark it as "needs verification" or "unconfirmed assumption".

Goal, Non-goals, and Milestones do not live here; they live in [plan.md](./plan.md).

## Details

- Terms:
- Constraints:
- Success metrics:
- Source of truth (data, files, trackers):
- Working context (if any):
- Dependencies:
- Stakeholders (roles, not chronology):

## Trust Notes

- Weak or stale invariants:
- Unresolved conflicts that affect context:
- Claims based on agent inference rather than a direct source:

## Next Step
