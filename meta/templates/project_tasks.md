---
id: <yyyy-mm-dd>-<project-slug>-tasks
type: project
status: active
created: <YYYY-MM-DD>
updated: 2026-04-15
aliases:
  - "Project Task Template"
tags: [project, tasks]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: low
verification_status: unverified
verified_by_me: false
curation_mode: none
---

# Tasks

## The essence

**Execution-line project. Only the steps the agent is going to take in the current milestone. `tasks.md` does not store history (for this there is `log.md`), does not store a plan (for this there is `plan.md`), does not store delegation (for this there is `ops/<contour>/delegations/<slug>.md`), does not store personal obligations of the owner (for this there is `01_now/personal/tasks.md`).

Full methodology: [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md)]. Rules of ownership: [AGENTS.md Rules 10–12](../../AGENTS.md)]

## Prohibitions

- **Can't:** `Goal`, `Milestones`, `Contingency`, `Appetite` — all in `plan.md`.
- **Not:** `Blocked` section – blockers live in `plan.md §Blockers` as a first-class entity with `Bx` cards (see §5.4 methodology).
- **You can't:** lines like "understand what to do with X", "deal with Y" is a reflection, its place in `plan.md` under the corresponding milestone as an open question.
- **No:** Delegating to an employee ("Dima will do X") is in `ops/<contour>/delegations/<person-slug>.md`.
- **No:** The owner's personal obligation is in `01_now/personal/tasks.md`.

## Task Mode

Select one mode (it repeats `task_mode` from `plan.md`) and delete the second template below:
- `operational` – Normal tasks without changing the executable system
- `development` – code, scripts, tests, schema/data contracts, runtime, CI, build/release

Keep only one `Active`/`Active Step` at any given time.

---

## Template `operational`

### Active
- [ ] <one current step >>

### Next
- [ ] <2-5 next steps within the current milestone from plan.md >>

### Waiting
- [ ] <external dependencies / answers >>

### Backlog
- [ ] Not now, but not now. >>

### Done
- [x] <last 3-5 completed steps, no more - the old goes to log.md >>

---

## Template `development`

### Current Milestone
Reference to Millstone from `plan.md`: `M<N> - <name >>`. Don’t duplicate purpose and acceptance, they’re there.

### Active Step
- [ ] <one current step >>

### Why?
Why this step is now in the context of the milestone >>

### Exit Criteria
- <observable completion condition 1 >>
- <observable completion condition 2 >>

### Drift Guard (short)
- Where to go without re-planning in this step >>

### Next
- [ ] <2-5 next steps >>

### Backlog
- [ ] Later. >>

### Done
- [x] <last 3-5 steps >>

## Drift protocol

If you’re going to work outside of `Active`/`Next`, or if you realize that the current milestone is no longer leading to your goal, you’re going to:
1. `plan.md` (milestones, acceptance, drift guard, contingency)
2. One line in `log.md` is "drift: was X, became Y."
3. Only then update `tasks.md` and resume work.

## Next step.
Select `Task Mode`, remove the extra template and leave one `Active` step.
