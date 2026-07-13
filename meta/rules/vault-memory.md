---
id: vault-memory
type: rules
status: active
created: 2026-06-20
updated: 2026-07-13
aliases:
  - "Vault memory"
  - "Current memory"
tags: [rules, memory, trust, vault]
source_path: "meta/rules/vault-memory.md"
knowledge_criticality: high
verification_status: unverified
curation_mode: llm_explicit_request
---

# Vault Memory

## Essence

Archive is not current memory. Logs, meetings, drafts, imports, and old plans are evidence; they do not become current truth until a curated layer says so.

## Core Rule

Before using historical material to guide current work, the agent must ask: what is current, what is stale, what is contradicted, and what is only evidence?

This rule extends [write protocol](./write-protocol.md) and [task routing](./task-routing.md). It adds one question: what should the agent believe now?

## When `context.md` Is Enough

`context.md` can serve as current memory when:

- the project is short or medium-lived;
- stable facts fit into a compact file;
- there is no recurring stream of meetings, demos, signals, or imports;
- the agent does not need to choose the top current themes from a large archive;
- phrases like "current state" and "latest picture" do not crowd out stable concepts.

In that case, history remains in `log.md`, tasks in `tasks.md`, milestones and blockers in `plan.md`.

## When A Separate Current Picture Is Needed

A separate current-picture file is useful when several conditions hold:

- the contour is long-lived;
- new meetings, demos, feedback, imports, or external changes arrive regularly;
- old decisions can easily look current;
- the agent needs a 1-2 page answer to "what matters now";
- facts, decisions, signals, hypotheses, and problems need regular compression;
- `context.md` starts mixing stable invariants, current state, and history;
- there is a repeatable memory-rebuild procedure.

Do not create a `memory/` folder by default. If one current file is enough, place it near the data owner and link it from `README.md` and `context.md`.

## Knowledge States

Use four states for long-lived claims:

- `active` - governs current work;
- `stale` - was true, but should not govern current work;
- `archival` - kept as historical trace;
- `contradicted` - directly opposed by a newer source.

Important claims need source and confidence when they come from observation, interpretation, or field material.

## Trust Layer

Memory is not truth just because it is written down. Important claims that guide current work must include at least:

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

For standalone memory items, use [memory-card](../templates/memory-card.md).

## Source, Evidence, Interpretation

- `source` answers where the claim came from.
- `evidence` answers what supports it.
- `interpretation` explains how the agent understood it.

If there is no direct quote, exact fragment, or verifiable basis, use low-strength evidence and do not include the claim as an unconditional fact in the current picture.

## Authority

A participant's opinion is not a decision unless a project owner or responsible person confirmed it. Client wishes, meeting comments, and confident wording without authority should be marked as `stated_by_other`, `hypothesis`, `preference`, or `risk`, not `decision`.

## Confidence Decay

For plans, deadlines, priorities, owners, task statuses, blockers, external constraints, architecture constraints, and client agreements, record:

```yaml
last_verified: YYYY-MM-DD
valid_until: YYYY-MM-DD
decay_policy: 30d | 60d | 90d | manual
needs_review: false
```

If `last_verified` is stale under `decay_policy`, lower confidence, set `needs_review: true`, and do not use the claim as strong evidence without checking.

## Conflicts

Do not hide contradictions. If two claims conflict, create or update a conflict:

- for vault-wide rules and memory: `meta/memory/conflicts/`;
- for project memory: near the data owner if a local decision or fact layer exists.

Use [memory-conflict](../templates/memory-conflict.md).

## Memory Ledger

Changes to confidence, status, claim type, current picture, strategic decisions, and conflicts must be recorded in [memory ledger](../memory/ledger.md).

## Anti-memory

Before extracting facts, compressing meetings, or rebuilding a current picture, check [anti-memory](../memory/anti-memory.md). Frequency, confident tone, client wishes, and polished agent summaries do not create facts by themselves.

## Rebuilding A Current Picture

When rebuilding a current picture, the agent:

1. Uses only active claims.
2. Does not treat `confidence: low` as fact.
3. Checks `claim_type`.
4. Checks `last_verified` and `valid_until`.
5. Checks unresolved conflicts.
6. Checks authority for decisions.
7. Does not turn `inferred`, `hypothesis`, `assumption`, or `plan` into fact.
8. Marks weak or disputed points as requiring verification.
9. Records the change in [memory ledger](../memory/ledger.md).

## Related Rules

- [Write protocol](./write-protocol.md)
- [Task routing](./task-routing.md)
- [Save and extract](./save-and-extract.md)
- [Memory ledger](../memory/ledger.md)
- [Anti-memory](../memory/anti-memory.md)
- [Agent rules](../../AGENTS.md)

## Next step

Use this rule on long-lived contours with large event streams. Add new memory files only where `context.md` is no longer enough.
