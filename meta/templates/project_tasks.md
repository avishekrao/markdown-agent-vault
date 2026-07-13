---
id: <yyyy-mm-dd>-<project-slug>-tasks
type: tasks
status: active
created: <YYYY-MM-DD>
updated: 2026-07-10
aliases:
  - "Project tasks template"
tags: [project, tasks]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: low
verification_status: unverified
verified_by_me: false
curation_mode: none
---

# Tasks

## Essence

Execution queue for the project. This file is derived from `plan.md`: current milestone, one active step, local exit criteria, short drift guard, and next step.

`tasks.md` does not store history (`log.md` does), does not store the plan (`plan.md` does), does not store delegations (`ops/<contour>/delegations/<slug>.md` does), and does not store the owner's personal obligations (`01_now/personal/tasks.md` does).

Methodology: [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md).

## Prohibitions

- Do not put `Goal`, `Milestones`, `Contingency`, `Appetite`, or `Quality Criteria` here; they belong in `plan.md`.
- Do not create a `Blocked` section; blockers live in `plan.md §Blockers` as first-class `Bx` cards.
- Do not write vague lines such as "understand what to do with X" or "figure out Y"; that is reflection and belongs in `plan.md` under the relevant milestone.
- Do not write "ask the owner to make the plan", "ask for criteria", or "approve the items". If a question changes goal, boundaries, source of truth, or cost of error, handle it in `plan.md`; otherwise the agent records a safe assumption.
- Do not put employee delegations here.
- Do not put the owner's personal external obligations here.

## Task Mode

Choose one mode (matching `task_mode` in `plan.md`) and delete the other template:

- `operational` - work that does not change an executable system.
- `development` - code, scripts, tests, schemas, data contracts, runtime, CI, build, or release work.

Keep exactly one `Active` / `Active Step` at any moment.

`Current Milestone` is required in both modes and must reference `M<N>` from `plan.md`. If the current step does not follow from that milestone, update `plan.md` first.

---

## Template: `operational`

### Current Milestone

Reference to milestone from `plan.md`: `M<N> - <name>`. Do not duplicate purpose or acceptance here.

### Active

- [ ] <one current step>

### Exit Criteria

- <local observable completion condition>

### Drift Guard (short)

- <short excerpt from Drift Guard / Non-goals / Quality Criteria in plan.md>

### Next

- [ ] <1-3 next steps within the current milestone>

### Backlog

- [ ] <not now, but still within the current milestone>

### Done

- [x] <last 3-5 completed steps only; older history goes to log.md>

---

## Template: `development`

### Current Milestone

Reference to milestone from `plan.md`: `M<N> - <name>`. Do not duplicate purpose or acceptance here.

### Active Step

- [ ] <one current step>

### Why

<why this step matters now within the current milestone>

### Exit Criteria

- <observable completion condition 1>
- <observable completion condition 2>

### Drift Guard (short)

- <short excerpt from Drift Guard / Non-goals / Quality Criteria in plan.md>

### Next

- [ ] <1-3 next steps within the current milestone>

### Backlog

- [ ] <later, but still within the current milestone>

### Done

- [x] <last 3-5 steps>

## Drift Protocol

If work moves outside `Active`/`Next`, or the current milestone no longer leads to the goal:

1. Edit `plan.md` first: milestones, acceptance, quality criteria, owner-interaction policy, drift guard, or contingency.
2. Add one line in `log.md`: "drift: was X, became Y".
3. Only then update `tasks.md` and resume work.

## Next Step

Select `Task Mode`, delete the extra template, name `Current Milestone` from `plan.md`, and leave one active step.
