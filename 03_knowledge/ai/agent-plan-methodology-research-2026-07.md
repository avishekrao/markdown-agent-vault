---
id: agent-plan-methodology-research-2026-07
type: note
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Agent planning methodology"
  - "How to write a plan for an LLM agent"
  - "Plan against agent drift"
tags: [ai, agents, planning, methodology]
source_path: "03_knowledge/ai/agent-plan-methodology-research-2026-07.md"
freshness: evergreen
knowledge_criticality: high
verification_status: unverified
curation_mode: llm_explicit_request
---

# Agent Planning Methodology

## Essence

A good `plan.md` is not a long task list. It is a durable intent contract: what the owner wanted to change, what is outside the task, what counts as quality, where the agent must stop, and how the result will be reviewed.

The agent writes the plan. The owner should not be asked to invent milestones, quality criteria, or plan sections. The owner is only asked to confirm or correct fundamental forks when the agent cannot safely infer them.

## Why This Exists

In long work, agents drift. They help too broadly, mix research with execution, change completion criteria, or preserve an intent only in chat. Another failure mode is excessive confirmation: the agent keeps asking the owner to do planning work.

The solution is a slow, explicit `plan.md` layer paired with a fast `tasks.md` execution queue.

## Main Findings

- `plan.md` is an intent lock, not a micro-step script.
- Drift usually comes from weak boundaries, not from a missing task list.
- Quality criteria must exist before execution begins.
- Subagents are useful as independent reviewers, not as competing plan authors.
- Questions to the owner are allowed only when the answer changes goal, boundary, risk, or source of truth.
- After every milestone, the agent must compare actual state with goal, boundaries, quality criteria, blockers, and source of truth.

## Required Plan Sections

A project plan should include:

- `Goal` - a change in the world, not a list of actions;
- `Intent Lock` - what the agent must preserve;
- `Owner Interaction Policy` - when to ask, when to decide;
- `Non-goals` - what must not be done;
- `Appetite` - time, attention, and stopping point;
- `Source of truth` - where facts and decisions come from;
- `Milestones` - each with acceptance criteria and status;
- `Quality Criteria` - what passes and what fails;
- `Blockers`;
- `Blockers - Resolved`;
- `Drift Guard`;
- `Contingency`;
- `Review Protocol`.

## `plan.md` vs `tasks.md`

`plan.md` stores intent, boundaries, quality, milestones, blockers, and review. It changes only when the goal, boundary, milestone, or decision framework changes.

`tasks.md` stores the current execution queue derived from the current milestone. It must contain one active step, local exit criteria, a short drift guard, and next steps. It must not contain the full goal, milestones, contingency, or quality criteria.

## How The Agent Should Write A Plan

1. Reconstruct the owner's intent from the chat and local files.
2. Identify the likely contour and data owner.
3. Define goal as an outcome.
4. Define non-goals and dangerous interpretations.
5. Choose a small number of milestones.
6. Add acceptance criteria to every milestone.
7. Add quality criteria before execution.
8. Write the owner interaction policy.
9. Add drift guard and contingency.
10. Only then create `tasks.md`.

## When To Ask The Owner

Ask only when the answer changes:

- the target project or contour;
- the durable source of truth;
- the goal or non-goals;
- the acceptable risk;
- the public/private boundary;
- a costly irreversible action.

Question shape:

> I understand the goal as X. I propose Y because Z. Alternative A makes sense if B is more important. Confirm or correct.

## Review Questions

Before execution, the agent should verify:

- What interpretation of the request would be wrong?
- What action would cause drift?
- Which completion criterion is not observable?
- Which local rule could the plan violate?
- What data must not be stored in this project?
- What will be true when the project is done?

## Anti-patterns

- Asking the owner to write the plan.
- Putting strategic reflection into `tasks.md`.
- Treating a backlog as a plan.
- Making milestones that cannot be checked.
- Letting a subagent rewrite the final plan without main-agent synthesis.
- Changing criteria mid-work without updating `plan.md`.

## Vault Application

This methodology is implemented through:

- [project plan template](../../meta/templates/project_plan.md);
- [project tasks template](../../meta/templates/project_tasks.md);
- [project-creator skill](../../skills/project-creator/SKILL.md);
- [task routing](../../meta/rules/task-routing.md);
- [write protocol](../../meta/rules/write-protocol.md).

## Next step

Use this methodology whenever a new project is created or an existing `plan.md` is materially changed.
