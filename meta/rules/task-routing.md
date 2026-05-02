---
id: task-routing
type: rule
status: active
created: 2026-04-15
updated: 2026-04-15
aliases:
  - Task Routing is a tactical checklist
  - "Where to put the task."
tags: [rules, tasks, routing, delegations, personal]
source_path: "meta/rules/task-routing.md"
knowledge_criticality: high
verification_status: active
---

# Task Routing - tactical checklist

## The essence

Before you write down any task-level string, the agent answers one question**: “Will this line survive the current project?” and passes the decision tree. Full justification - in [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md)]. Here's a working checklist.

## Decision tree (before each line)

```
Will the line survive this project?
No.
Agent's step in the current milestone? → <project>/tasks.md, Next
Episodic fact from the meeting? → <meeting>.md, ## Mentioned in passing, #canonical-tag
─Yes.
    ── The performer is the owner of the vault?
    Part of the purpose of the project? → <project>/plan.md, Milestones
    ♥  ─ External commitment, not by project? → 01 now/personal/tasks.md, Hard
    ── Acting as an employee of the circuit? → 01 now/ops/<contour>/delegations/<person-slug>.md, Active
    Sustainable invariant (term, metric, SoT)? → <project>/context. md
```

If the answer is ambiguous, stop and ask the owner (Rule 6).

## Routing table

| Layer from context | Where is it going | Guardian Rule |
|---|---|---|
| Execution step of agent | `<project>/tasks.md`, Active/Next | Rule 10 |
| Milestone, Goal, Non-goal, Acceptance, Drift, Contingency | `<project>/plan.md` | Rule 12 |
| **Blocker milestone (first-class)** | **`<project>/plan.md §Blockers`, card Bx** | **Rule 12 blocker protocol** |
| Stable invariant | `<project>/context.md` | Rule 14 |
| Solution, change of status, opening/closing of the blocker | `<project>/log.md`, line 1 | Rule 5 + Rule 8 |
| Contour delegation | `01_now/ops/<contour>/delegations/<person-slug>.md`, Active | Rule 11 |
| Personal external obligation of the owner | `01_now/personal/tasks.md`, Hard | Rule 13 |
| Episodic fact from the meeting | `<meeting>.md`, ## Mentioned in passing, #tag | Rule 14 |
| Fact About People, Participation | `03_knowledge/contacts-network/interactions.csv` | People-linking Rule |

## Rules for each destination

### `<project>/plan.md`
- Required for every active project.
- Contains: `Goal`, `Non-goals`, `Appetite`, `Source of truth`, `Milestones` (each with `Acceptance` and `not-started | in-progress | done | blocked on Bx` status), **`Blockers`**, **`Blockers — Resolved`**, `Drift Guard`, `Contingency`.
- Slow file. Changes when the goal, appetite, order of milestones, or state of the blockers changes.
- Drift protocol: first edit `plan.md`, then one line in `log.md`, then act.
- Blocker protocol: new blocker → `Bx` card in `§Blockers` + milestone status `blocked on Bx` + string `⏸️ NEW BLOCKER Bx` in log.md. Resolution → reverse order, ritual §5.4.2 methodology. `tasks.md` is not affected when the blocker is opened/closed.

### `<project>/plan.md §Blockers`
- First-class essence of the plan. Each card is a separate `Bx` entry with fields: Open, Type, Wait, Block, My Action, Return Condition, Fallback, Stale check.
- Types: `cross-project dependency | delegated-work | external-event | need-info`.
- Double-sided links: milestone knows it's `blocked on Bx`; blocker knows it's `Block: M2, M3`.
- For `delegated-work`, the parallel line in `delegations/<slug>.md` is backlinked to `[plan](rel-link)`.
- Cross-project dependency is one-sided: waiter writes a blocker at home, parent knows nothing. Cascades are detected via grep by `cross-project` in all `plan.md`.
- Stale check at bootstrap-scan: >30d warn, >60d stale, >90d requires decision. The individual threshold is the `Stale check` field of the card.

### `<project>/tasks.md`
- Content: only **performance**, not reflection.
- The line like "understand what to do with X" is not here, it's in `plan.md` under the corresponding milestone.
- Prohibition: `Goal`, `Milestones`, `Contingency`, **`Blocked` sections (blockers - in `plan.md §Blockers` as first-class)**
- One `ACTIVE` step at a time.

### `01_now/ops/<contour>/delegations/<person-slug>.md`
- One file per pair (contour, delegate). If one delegate in two circuits, two files.
- Sections: `Active`, `Done (7d)`, `Archive`. `Waiting` and `Overdue` via the `due:` and grep field.
- Line format:
  ```
  - [ ] 2026-04-12 → the essence of the problem [TRACKER-123](url) • due: 2026-04-20 • [meeting](rel-link)]
  ```
- The external tracker is the source of truth. The file is lean index.
- Passive recall: When a delegate’s name is mentioned in a fresh context, the agent shows the open lines.

### If the command circuit already has a live external tracker
- The common `tasks.md` does not turn into a second working list; it holds only steps along the contour shell itself.
- Appointments, deadlines, locks and statuses are read from an external tracker.
- `delegations/` either remain a short index with links to the tracker or are translated into an archive transition layer.
- The owner’s personal review is stored only outside the general repository as a derivative summary and not as a second source of truth.

### `01_now/personal/tasks.md`
- The only file for the owner's personal obligations.
- Two sections: `Hard` (external commitments to the world) and `Maybe` (short reminders).
- Desire, curiosity, project work - not here.
- Frontmatter: `last_rewrite: YYYY-MM-DD`, plus the same string in the body.
- Forced rewrite once a month. No weekly review.
- Ambient capture: A string is added without MR-diff.
- It is not read on a daily basis.

### `<project>/context.md`
- Only stable invariants.
- The episode from the meetings ** doesn't get** - it's in a sammari meeting under the hashtag.
- Episodic transfer trigger: formulated opinion (“we know X is Y”).

### `<meeting>.md`, section `## Mentioned in passing`
- Tags - only from the canonical registry [meta/TAGS.md](../TAGS.md#task-routing-tags).
- Add a new tag to the registry first, then use it.
- Format: `#canonical-tag: what was mentioned in one sentence`.

## Legacy migration `tasks.md` at the first touch of the project

When an agent opens a project without `plan.md`:
1. Reading `tasks.md`.
2. It runs the decision tree on each line.
3. Shows the owner of MR-diff: what → `plan.md`, what → `delegations/<person>.md`, what → `personal/tasks.md`, what remains in `tasks.md`.
4. After confirmation, create `plan.md` from the [project plan template](../templates/project_plan.md), transfer the lines, and shorten `tasks.md`.
5. He writes one line in `log.md`: "Migration into task-routing-methodology-2026-04."

Mass migration without the express request of the owner is prohibited.

## Antipatterns (not allowed to do so)

- Put `Goal` in `tasks.md` - it's in `plan.md`.
- Add the delegation to the `tasks.md` project under the guise of "my job is to check what Dima did to X."
- Write a personal commitment (“extend your visa”) to project `tasks.md` just because it was mentioned at the project meeting.
- Writing an episodic fact from a meeting in the `context.md` project is an invariant with a future half-life.
- Make `delegations/<person>.md` uniform across all contours.
- To use `tasks.md` as an event log is `log.md`.
- Automatically transfer the theme from an episodic to `context.md` over the counter, without formulating a opinion.
- **Keep the blockers in `tasks.md §Blocked`** - no longer the section, the blockers live in `plan.md §Blockers` as a first-class entity with cascade via `Block: Mx`.
- **Write a blocker without connection with milestones** - the `Blocking.` field is mandatory, otherwise the blocker loses its targeting.
- **Close the blocker first in `tasks.md`** - ritual permissions go from top to bottom: plan.md → log.md → delegations/, not vice versa.
- **Record the same delegated-work task in plan.md §Blockers and in delegations/ without a two-way link** - links are required, otherwise the files diverge.

## Related rules

- [Rule 5: log.md — chronology, not storage ](../../AGENTS.md) — adjacent layer separation pattern.]
- [Rule 6: clarify, don't guess ](../../AGENTS.md) - in ambiguous routing.
- [Rule 8: Mid-flight sync](../../AGENTS.md) - when to write in log.md and context.md]
- [Rules 10–14](../../AGENTS.md) are the source of this checklist.
- [write-protocol.md](./write-protocol.md) is the file-writing protocol for the vault.
- [live-first-audit.md](./live-first-audit.md) — Tracker-only delegation status.]

## Next step.

Support this file synchronously with [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md)]. When changing the methodology, first edit the methodology, then this checklist, then AGENTS.md.
