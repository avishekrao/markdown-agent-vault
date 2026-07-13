# Writing `plan.md` Autonomously

This reference explains how the agent writes the project contract itself, using the [LLM-agent planning methodology](../../../03_knowledge/ai/agent-plan-methodology-research-2026-07.md). The owner is not the plan's co-author. The owner confirms or corrects only foundational intent decisions.

The full section template lives in [project_plan.md](../../../meta/templates/project_plan.md).

## Planning Depth

Choose planning depth by drift risk and cost of error. Do not write a heavy plan for a small, low-risk task.

| Level | When | Enough output |
|---|---|---|
| Normal new project | Contour and near-term goal are clear | Full `plan.md`, with concise milestones and criteria |
| High drift risk | Underspecified request, many contours, costly execution, autonomous work beyond one session | Full `plan.md`, independent review if available, explicit stop conditions |

For high-risk plans, a separate reviewer or subagent can check intent, vault rules, drift risk, and quality. The main agent still assembles the final plan; reviewers do not write competing plans.

## Section Guidance

### Goal

Write one to three sentences describing a changed state, not a list of agent actions.

Bad:

> Analyze competitors, make a table, write conclusions.

Good:

> The owner has a justified positioning decision for the product: one core formulation that survives competitor substitution, with reasons for rejecting two alternatives.

### Intent Lock

Intent Lock is the main anti-drift section. Fill it after reconstructing intent:

- **What the owner actually wants:** the practical result and why it matters now.
- **Wrong interpretation:** the literal or agent-convenient version that would be a failure.
- **Allowed agent assumptions:** what the agent accepted without asking; record these explicitly.
- **Stop and ask if:** a decision appears that changes the goal, boundaries, cost of error, or source of truth.

### Owner Interaction Policy

Adapt this invariant to the project:

- The agent writes and maintains the plan and quality criteria.
- The owner does not draft plan items or criteria.
- Before execution, one packet of up to three clarifying questions is allowed only for foundational forks.
- Reconfirmation is required only when the goal, boundaries, source of truth, cost of error, or a sensitive action changes.

### Non-goals

List what the project will not do, even if it looks useful. Use exclusions from the chat and obvious neighboring temptations.

### Appetite / Budget

State how much attention is acceptable: time appetite, priority, and exit condition. The exit condition also defines when the project should be paused or closed rather than expanded.

### Source of Truth

Name where current truth lives: project files, external tracker, dataset, repository, or another contour. If data belongs to another contour, link to the owner contour instead of copying it into the project.

### Milestones

Each milestone is an observable state with an acceptance check, not a vague phase such as "research", "build", or "review".

For each milestone include:

- **Purpose:** what becomes true after it is completed.
- **Acceptance:** concrete observable conditions.
- **Status:** `not-started`, `in-progress`, `done`, or `blocked on Bx`.

The agent writes the milestones. A rough but useful milestone is better than an empty plan; it can be refined when evidence changes.

### Quality Criteria

Define quality before execution. Use a table with these columns: `Criterion`, `Passes`, `Fails`, `Check`.

At minimum include:

- intent fit;
- boundary discipline;
- verifiability of the result.

Without this section, review tends to reward volume and confidence instead of fit to the goal.

### Blockers / Blockers - Resolved

In a new plan both sections are empty. Add blocker cards only when a real blocker appears. Blockers live in `plan.md`, not in `tasks.md`.

### Drift Guard

State where the project must not drift without a plan revision. Include the drift protocol:

1. update `plan.md`;
2. add a short `log.md` entry;
3. update `tasks.md` only after the plan changes.

Examples:

- Do not start coding before the first-version shape is accepted.
- Do not expand to a neighboring product without a new milestone or project.

### Contingency

Write one fallback plan: what to do if the main path is blocked or the appetite is exhausted. Usually this is pause, archive, hand off, or close with an explicit negative finding.

### Review Protocol

Define how the plan is reviewed before execution and after milestones. Include whether a separate reviewer is needed and what change requires owner confirmation.

## When to Ask the Owner

Ask only if all three conditions are true:

1. The answer cannot be inferred from indexes, `README.md`, `plan.md`, `tasks.md`, `context.md`, `log.md`, local rules, or the current request.
2. Different answers materially change the goal, boundaries, source of truth, depth of intervention, cost of error, or major milestone order.
3. There is no safe conservative assumption, or the cost of a wrong assumption is higher than the cost of asking.

Good question:

> I understand the goal as T. I recommend A because P. B makes sense if X matters more. Confirm or correct.

Bad questions:

> What plan items should I write? What criteria should I add? Please review the plan line by line. What should I do next?

## Short Worked Plan Example

Project: `YYYY-demo-product-positioning-strategy`, task mode `operational`. It emerged from a chat where the owner said the demo product sounded like every competitor.

```markdown
---
id: YYYY-demo-product-positioning-strategy-plan
type: plan
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Plan - demo product positioning"
tags: [project, plan, contract, demo-product, positioning]
source_path: "01_now/projects/YYYY-demo-product-positioning-strategy/plan.md"
task_mode: operational
---

# Plan

## Goal
The owner has a justified positioning decision for the demo product: one core formulation that survives competitor substitution, with reasons for rejecting two alternatives.

## Intent Lock
- What the owner actually wants: stop sounding interchangeable and get a positioning core that can guide the site and sales.
- Wrong interpretation: produce a competitor overview and call it strategy without choosing.
- Allowed agent assumptions: the initial horizon is the local market; compare against direct competitors mentioned in the chat.
- Stop and ask if: it becomes clear that positioning is needed for a specific segment rather than the product as a whole.

## Owner Interaction Policy
- The agent writes and maintains the plan and criteria.
- The owner does not draft plan items or quality criteria.
- Before execution, one packet of up to three clarifying questions is allowed only for foundational forks.
- Reconfirmation is required only if the goal, boundaries, source of truth, or cost of error changes.

## Non-goals
- Do not rewrite the landing page in this project; only define the positioning core.
- Do not launch ads or build a media plan.

## Appetite / Budget
- Time appetite: one focused block of about three days.
- Attention: high.
- Exit condition: if no defensible differentiation exists, record that finding and close the project.

## Source of Truth
- Project files in this folder.
- Materials from the source chat and the competitor overview linked from `context.md`.

## Milestones
### M1 - Competitive Field Map
**Purpose:** direct competitors and occupied language are visible.
**Acceptance:** a table of 5+ competitors with their positioning core and occupied terms exists.
**Status:** not-started

### M2 - Positioning Candidates
**Purpose:** there are three candidate cores, each tested against competitor substitution.
**Acceptance:** for each candidate, the project shows why a direct competitor cannot say the same thing.
**Status:** not-started

### M3 - Decision and Rationale
**Purpose:** one option is chosen and two alternatives are rejected with reasons.
**Acceptance:** the decision is recorded; rejected alternatives have explicit reasons.
**Status:** not-started

## Quality Criteria
| Criterion | Passes | Fails | Check |
|---|---|---|---|
| Intent fit | A chosen core and rationale exist | Only an overview exists | Check M3 output |
| Boundaries | Work stayed on positioning core | The project started rewriting the site | Compare with Non-goals |
| Verifiability | The core survives competitor substitution | The wording fits any competitor | Run the substitution test |

## Blockers
_Empty._

## Blockers - Resolved
_Empty._

## Drift Guard
- Do not drift into a competitor overview instead of choosing the core.
- Do not expand into landing-page redesign.
- Drift protocol: update `plan.md`, then `log.md`, then `tasks.md`.

## Contingency
If product-level differentiation is not defensible, record that finding and close the project instead of inventing a weak core.

## Review Protocol
- Before execution: check Intent Lock, Non-goals, Milestones, Quality Criteria, and Drift Guard.
- Separate reviewers: not required for normal risk.
- Owner confirmation: only if a product-wide vs segment-specific fork appears.

## Related Files
- `tasks.md` - execution queue
- `context.md` - durable invariants
- `log.md` - chronology
- `README.md` - entry point

## Next Step
Start M1: build the competitive field map.
```
