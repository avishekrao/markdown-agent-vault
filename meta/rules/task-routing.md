---
id: task-routing
type: rule
status: active
created: 2026-04-15
updated: 2026-07-13
aliases:
  - "Task routing checklist"
  - "Where to put a task"
tags: [rules, tasks, routing, delegations, personal]
source_path: "meta/rules/task-routing.md"
knowledge_criticality: high
verification_status: active
---

# Task Routing - Tactical Checklist

## Essence

Before writing any task-level line, ask one question: **will this line outlive the current project?** Then pass the decision tree.

Full rationale: [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md).

## Decision Tree

```text
Will the line outlive this project?
├── NO
│   ├── Agent step in the current milestone? -> <project>/tasks.md, Active/Next
│   └── Episodic meeting fact? -> <meeting>.md, ## Mentioned in passing, #canonical-tag
└── YES
    ├── Performer is the vault owner?
    │   ├── Part of the project goal? -> <project>/plan.md, Milestones
    │   └── External obligation outside the project? -> 01_now/personal/tasks.md, Hard
    ├── Performer is a person in a contour? -> 01_now/ops/<contour>/delegations/<person-slug>.md, Active
    └── Durable invariant (term, metric, source of truth)? -> <project>/context.md
```

If the answer is ambiguous, stop and ask the owner.

## Routing Table

| Context layer | Destination | Guard rule |
|---|---|---|
| Agent execution step | `<project>/tasks.md`, Active/Next | tasks-only rule |
| Milestone, Goal, Intent Lock, Non-goal, Acceptance, Quality Criteria, Drift, Contingency | `<project>/plan.md` | plan contract |
| Milestone blocker | `<project>/plan.md §Blockers`, `Bx` card | blocker protocol |
| Durable invariant | `<project>/context.md` | durable memory |
| Decision, state change, blocker opened/closed | `<project>/log.md`, short entry | chronology |
| Delegation to a person in a contour | `01_now/ops/<contour>/delegations/<person-slug>.md`, Active | delegation index |
| Owner's personal external obligation | `01_now/personal/tasks.md`, Hard | personal tasks |
| Episodic meeting fact | `<meeting>.md`, `## Mentioned in passing` | episodic source |
| Fact about people or participation | contacts/people source declared by the vault | people-linking rule |

## Destination Rules

### `<project>/plan.md`

Required for every active project.

Contains: `Goal`, `Intent Lock`, `Owner Interaction Policy`, `Non-goals`, `Appetite`, `Source of truth`, `Milestones` with Acceptance and status, `Quality Criteria`, `Blockers`, `Blockers - Resolved`, `Drift Guard`, `Contingency`, and `Review Protocol`.

Slow file. Changes when goal, appetite, milestone order, quality criteria, owner-interaction policy, or blocker state changes.

When creating a project or substantially changing a plan, the agent writes `plan.md` itself. Do not ask the owner to formulate plan items, milestones, or quality criteria. Ask only a short question about a fork that changes goal, boundaries, source of truth, or cost of error.

Drift protocol: edit `plan.md`, then write one `log.md` line, then act.

Blocker protocol: new blocker -> `Bx` card in `§Blockers` + milestone status `blocked on Bx` + short `log.md` line. Resolution follows the reverse path. `tasks.md` is not the place to open or close blockers.

### `<project>/plan.md §Blockers`

Each blocker is a first-class plan entity with: Opened, Type, Waiting for, Blocks, My action, Return condition, Fallback, Stale check.

Types: `cross-project dependency | delegated-work | external-event | need-info`.

Links are double-sided: milestone says it is `blocked on Bx`; blocker states which milestones it blocks.

For `delegated-work`, the corresponding delegation line links back to the plan blocker.

Cross-project dependencies are one-sided: the waiting project records the blocker; the parent project does not have to know.

Stale check during startup scan: >30d warn, >60d stale, >90d requires a decision, unless a blocker-specific threshold is set.

### `<project>/tasks.md`

Contains execution only, not reflection.

Do not put `Goal`, `Milestones`, `Contingency`, `Quality Criteria`, or a `Blocked` section here. Keep one active step at a time.

A line like "understand what to do with X" belongs in `plan.md` as an open question under the relevant milestone, not in `tasks.md`.

### `01_now/ops/<contour>/delegations/<person-slug>.md`

One file per contour/person pair. If one person participates in two contours, use two files.

Sections: `Active`, `Done (7d)`, `Archive`. Waiting and overdue state are derived through fields such as `due:` and search.

Line shape:

```markdown
- [ ] 2026-04-12 -> task essence [TRACKER-123](url) - due: 2026-04-20 - [meeting](<relative meeting link>)
```

The external tracker is the source of truth. This file is a lean index.

### If a Team Contour Already Has a Live External Tracker

Do not turn shared `tasks.md` into a second working list. It should hold only steps for the contour shell itself.

Assignments, deadlines, locks, and statuses are read from the external tracker.

`delegations/` remains a short index with tracker links or becomes an archive transition layer.

### `01_now/personal/tasks.md`

The only file for the owner's personal external obligations.

Sections: `Hard` and `Maybe`.

Desires, curiosity, and project work do not belong here.

### `<project>/context.md`

Durable invariants only.

Meeting episodes do not go here. They remain in meeting summaries under a canonical tag. Transfer to `context.md` only when an actual opinion is formed: "we know X about Y".

### `<meeting>.md`, `## Mentioned in passing`

Use only canonical tags from the vault tag registry. Add a new tag to the registry before using it.

Line shape:

```markdown
- #canonical-tag: one-sentence mention.
```

## Legacy Migration at First Touch

When an agent opens a project without `plan.md`:

1. Read `tasks.md`.
2. Run the decision tree on each line.
3. Show the owner a proposed move list: what goes to `plan.md`, delegations, personal tasks, and what remains in `tasks.md`.
4. After confirmation, create `plan.md` from [project_plan.md](../templates/project_plan.md), move lines, and shorten `tasks.md`.
5. Write one `log.md` line: "migrated to task-routing-methodology-2026-04".

Mass migration without explicit owner request is prohibited.

## Anti-Patterns

- Put `Goal` in `tasks.md`.
- Put delegations in project `tasks.md` under "my task is to check X".
- Put a personal obligation into project `tasks.md` because it was mentioned in a project meeting.
- Move an episodic meeting fact into `context.md` as if it were a durable invariant.
- Use one delegation file for the same person across all contours.
- Use `tasks.md` as an event log.
- Move a topic into `context.md` by mention count instead of formulated opinion.
- Keep blockers in `tasks.md §Blocked`.
- Ask the owner to write the plan, milestones, or quality criteria.
- Write a blocker without linking it to milestones.
- Close a blocker in `tasks.md` first.
- Record the same delegated-work item in `plan.md §Blockers` and `delegations/` without two-way links.

## Related Rules

- [AGENTS.md](../../AGENTS.md) - root agent rules.
- [write-protocol.md](./write-protocol.md) - file-writing protocol.
- [live-first-audit.md](./live-first-audit.md) - live-source checks for external systems.

## Next Step

Keep this checklist synchronized with [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md). When the methodology changes, update the methodology first, then this checklist, then `AGENTS.md`.
