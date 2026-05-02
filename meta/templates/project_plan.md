---
id: <yyyy-mm-dd>-<project-slug>-plan
type: plan
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
aliases:
  - "Plan.md project template"
tags: [project, plan, contract]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: medium
verification_status: unverified
verified_by_me: false
curation_mode: none
task_mode: operational | development
---

# Plan

## The essence

`plan.md` is a slow contract. The question is “Where are we going and where are the borders?” It only changes when the goal, appetite, or order of milestones changes. Full methodology: [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md)].

**This is not backlog.** Execution steps are in `tasks.md`. Delegations to `ops/<contour>/delegations/<person-slug>.md`. Invariants are in `context.md`. The story is in `log.md`.

## Goal

<1-3 sentences: what problem we solve and what the final result is. Formulation through changing the state of the world, not through a list of actions. >>

## Non-goals

A clear list of what ***** is not in scope. Protects against creeping expansion.

- What we do not do and why >>
- <second explicit non-goal >>

## Appetite / Budget

How much time and attention the owner is willing to put into the project. After exhaustion, rethinking, not automatic renewal.

- **Time appetite:** <e.g. "2 hours a week for 6 weeks" / "one concentrated block in 3 days" / "background project per ~quarter" >>
- **Attention:** <high/medium/low — priority level over other active projects >>
- **Exit condition:** <under what conditions the project is closed early as "not taken off">

## Source of truth

Where the main thing lies - artifact, tracker, data. If the SoT in an external system is a reference to it.

- <SoT 1: For example, Asana Board / Google Doc / folder of artifacts >>
- <SoT 2, if available >>

## Milestones

List of major frontiers. Each milestone is an observable state, not a task list. The order is usually sequential, but can be either/or.

### M1 - <short name >>

**Purpose:** What becomes true after passing >>
**Acceptance:** <when we know what's happened - specific observable conditions >>
**Current status:** not-started | in-progress | done | blocked on Bx

### M2 - <short name >>

** Goal:** <... >>
**Acceptance:** <…>
**Current status:** not-started | in-progress | done | blocked on Bx

### M3 - <short name >>

** Goal:** <... >>
**Acceptance:** <…>
**Current status:** not-started | in-progress | done | blocked on Bx

## Blockers

First-class records of what prevents you from moving along the milestones. Each entry is referenced by milestones through the status of `blocked on Bx`. An empty section is normal.

Full blocker model: [§5.4 task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md)]

### B1 - <short name of the blocker >>

- **Open:** YYYY-MM-DD
- **Type:** cross-project dependency | delegated-work | external-event
- **We're waiting for the block to be removed. >>
- **Blocks:** M2, M3 (list of milestones)
- **My action:** passive | active-nudge | switch-to-fallback-at-YYYY-MM-DD
- **Return condition: ** How do I know the blocker is off >>
- **Fallback:** What do we do if the blocker is not removed by the deadline? >>
- **Stale check:** <how many days to consider a blocker obsolete; if empty, defaults: 30/60/90 days >>

## Blockers — Resolved

A log of removed blockers. Short entries "what got in the way/how broke up" to not forget the pattern. Crack down on forced rewrite/project review.

### B0 – <blocker name> (resolved YYYY-MM-DD)

- ** Was:** <one-line description of the problem >>
- **Distributed through:** What made the block irrelevant >>

## Drift Guard

Where not to go without an explicit revision of the plan. Anti-drift patterns for this particular project.

- <example: "Do not start writing code before you sign brief" >>
- <example: "do not expand scope to a neighboring product without a separate milestone" >>

**Drift protocol:** If during operation it turns out that the current milestone no longer leads to the goal, first edit `plan.md` (changes Milestone / Acceptance / Drift Guard), then one line in `log.md`, only then update `tasks.md` and continue.

## Contingency

One overall plan B for the entire project (not for every milestone). What to do if a project is blocked or a non-negotiable condition is violated.

- **If blocker X:** <action >>
- **If appetite is exhausted:** <pause/archive/handoff >>

## Related files

- [tasks.md](./tasks.md) — execution-queue of the project]
- [context.md](./context.md) — stable invariants of the project]
- [log.md](./log.md) — chronology of events and decisions]
- [README.md](./README.md) — entry point]

## Next step.

Fill in Goal and the first milestone. The rest is written as clarity becomes apparent – a poorly formulated milestone is better than an empty one. The `Blockers` and `Blockers — Resolved` sections in the new plan.md remain empty – they fill up when the first real block appears.
