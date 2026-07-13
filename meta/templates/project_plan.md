---
id: <yyyy-mm-dd>-<project-slug>-plan
type: plan
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
aliases:
  - "Project plan template"
tags: [project, plan, contract]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: medium
verification_status: unverified
verified_by_me: false
curation_mode: none
task_mode: operational | development
---

# Plan

## Essence

`plan.md` is the project's slow contract. It answers: where are we going, what are the boundaries, how do we check quality, and when must the agent stop and ask? It changes only when the goal, appetite, milestone order, quality criteria, or owner-interaction policy changes.

Methodology:

- [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md)
- [agent-plan-methodology-research-2026-07.md](../../03_knowledge/ai/agent-plan-methodology-research-2026-07.md)

This is not a backlog. Execution steps live in `tasks.md`. Delegations live in `ops/<contour>/delegations/<person-slug>.md`. Invariants live in `context.md`. History lives in `log.md`.

The agent writes the plan. The owner does not draft plan items, quality criteria, or milestone order. If clarification is needed, the agent asks one short packet only about foundational forks and recommends a default option.

## Goal

<1-3 sentences: what problem is solved and what final state should exist. Phrase it as a changed state, not as a list of actions.>

Changing the project goal uses `write_policy: human_review_required`. The agent may propose a new formulation, but must not silently change strategic direction without owner confirmation.

## Intent Lock

The agent fills this after reading context and, if needed, asking one short clarifying packet.

- **What the owner actually wants:** <practical result and why it matters>
- **Wrong interpretation:** <literal or agent-convenient execution that would fail>
- **Allowed agent assumptions:** <what can be accepted without another question>
- **Stop and ask if:** <fork that changes goal, boundaries, cost of error, or source of truth>

## Owner Interaction Policy

- The agent writes and updates `plan.md`.
- The owner does not write plan items, invent quality criteria, or review the plan line by line.
- Before creating or substantially changing the plan, one packet of up to three short questions is allowed only for intent forks.
- Each question must include the agent's recommended option: "I understand it as A; B makes sense if X matters more; confirm or correct."
- Reconfirmation is required only when goal, boundaries, source of truth, cost of error, or a sensitive action changes.

## Non-goals

Explicit list of what is not in scope. Protects against creeping expansion.

- <what exactly we do not do and why>
- <second explicit non-goal>

## Appetite / Budget

How much time and attention the owner is willing to invest. When exhausted, rethink rather than automatically extend.

- **Time appetite:** <for example, "2 hours/week for 6 weeks" / "one focused 3-day block" / "background project for about a quarter">
- **Attention:** <high / medium / low relative to other active projects>
- **Exit condition:** <conditions under which the project closes early as not viable>

## Source of Truth

Where the authoritative state lives: file, tracker, data, external system, or another contour. If the source of truth is external, link to it.

- <SoT 1: e.g. Asana board / Google Doc / project file folder>
- <SoT 2, if any>

## Trust Policy

Strategic claims in this plan require explicit basis:

```yaml
claim_type: decision | constraint | plan | risk | status | assumption | hypothesis
source:
  - ""
evidence:
  kind: direct_user_statement | direct_quote | meeting_note | document_fact | agent_inference | repeated_pattern | external_source | unknown
  strength: high | medium | low
confidence: high | medium | low
last_verified: YYYY-MM-DD
write_policy: human_review_required
```

Rule: do not change goal, boundaries, milestone order, architecture decisions, key constraints, or blocker resolution as a simple editorial edit. If the agent proposes a change, record the basis and write a short `log.md` entry. If current memory or memory status changes, also write to the [memory ledger](../memory/ledger.md).

## Milestones

Major project boundaries. Each milestone is an observable state, not a task list. Order is usually sequential but may be either/or.

### M1 - <short name>

**Purpose:** <what becomes true after completion>
**Acceptance:** <how we know it is complete: concrete observable conditions>
**Current status:** not-started | in-progress | done | blocked on Bx

### M2 - <short name>

**Purpose:** <...>
**Acceptance:** <...>
**Current status:** not-started | in-progress | done | blocked on Bx

### M3 - <short name>

**Purpose:** <...>
**Acceptance:** <...>
**Current status:** not-started | in-progress | done | blocked on Bx

## Quality Criteria

The agent defines quality criteria before execution. The owner may confirm or correct foundational intent, but is not responsible for inventing criteria.

| Criterion | Passes | Fails | Check |
|---|---|---|---|
| Intent fit | <what must be true> | <what would be drift> | <how the agent checks> |
| Boundaries | <what remains respected> | <what forbidden expansion happened> | <how the agent checks> |
| Result verifiability | <how readiness is observable> | <formal but weak completion> | <how the agent checks> |

## Blockers

First-class records of what prevents milestone progress. Milestones reference blockers through `blocked on Bx`. An empty section is normal.

Full blocker model: [task-routing-methodology-2026-04.md §5.4](../../03_knowledge/task-routing-methodology-2026-04.md).

### B1 - <short blocker name>

- **Opened:** YYYY-MM-DD
- **Type:** cross-project dependency | delegated-work | external-event | need-info
- **Waiting for:** <what must happen for the blocker to be removed>
- **Blocks:** M2, M3
- **My action:** passive | active-nudge | switch-to-fallback-at-YYYY-MM-DD
- **Return condition:** <how I know the blocker is gone>
- **Fallback:** <what happens if the blocker is not removed by the deadline>
- **Stale check:** <days until stale; defaults: 30/60/90 if empty>
- **Last verified:** YYYY-MM-DD
- **Trust:** `claim_type: status`, `confidence: high | medium | low`, `write_policy: suggest | human_review_required`

## Blockers - Resolved

Short log of removed blockers so the pattern is not forgotten. Collapse during forced rewrite or project review.

### B0 - <blocker name> (resolved YYYY-MM-DD)

- **Was:** <one-line description of the problem>
- **Resolved through:** <what made the block irrelevant>

## Drift Guard

Where the project must not go without explicit plan revision. These are anti-drift patterns for this project.

- <example: "do not start coding before the brief is accepted">
- <example: "do not expand to a neighboring product without a separate milestone">

**Drift protocol:** if the current milestone no longer leads to the goal, first edit `plan.md` (Milestone / Acceptance / Drift Guard), then add one `log.md` line, then update `tasks.md` and continue.

## Contingency

One overall fallback for the project. Not one fallback per milestone.

- **If blocker X:** <action>
- **If appetite is exhausted:** <pause / archive / handoff>

## Review Protocol

How the plan is checked before execution and after milestones.

- **Before execution:** the agent checks `Intent Lock`, `Owner Interaction Policy`, `Non-goals`, `Milestones`, `Quality Criteria`, and `Drift Guard`.
- **Reviewers:** <not needed / roles needed: intent reconstructor, rule checker, drift skeptic, quality evaluator>
- **Owner check-in:** <not needed / needed only for fork: ...>
- **After each milestone:** compare result with `Quality Criteria` and `Drift Guard`; when goal or boundaries change, update `plan.md`, then `log.md`, then `tasks.md`.

## Related Files

- [tasks.md](./tasks.md) - project execution queue
- [context.md](./context.md) - durable project invariants
- [log.md](./log.md) - event and decision chronology
- [README.md](./README.md) - entry point

## Next Step

The agent fills Goal, Intent Lock, Owner Interaction Policy, Non-goals, the first milestone, Quality Criteria, and Drift Guard. Add the rest as clarity appears. A rough milestone is better than an empty one. `Blockers` and `Blockers - Resolved` remain empty in a new project until a real blocker appears.
