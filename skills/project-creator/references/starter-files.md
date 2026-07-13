# Project Starter Files: Templates and Examples

This reference shows filled examples for `README.md`, `context.md`, `tasks.md`, `log.md`, and index updates. The sample project is `YYYY-demo-product-positioning-strategy` in `operational` mode.

Frontmatter follows [write-protocol.md](../../../meta/rules/write-protocol.md): `id`, `type`, `status`, `created`, `updated`, `aliases`, `tags`, and `source_path`. Use today's date for `created` and `updated`.

## `README.md` - Entry Point

A short navigator: what the project is, where service files live, and what comes next. Use `type: project`.

```markdown
---
id: YYYY-demo-product-positioning-strategy-readme
type: project
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Demo product positioning"
tags: [project, demo-product, positioning, strategy]
source_path: "01_now/projects/YYYY-demo-product-positioning-strategy/README.md"
freshness: seasonal
expires: 2027-01-10
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Demo Product Positioning

## Essence

Project for choosing the demo product's positioning core: one formulation that survives competitor substitution, with reasons for rejecting alternatives.

## Details

- Contour: demo-product.
- Task Mode: `operational`.
- Service files:
  - `plan.md` - project contract: goal, boundaries, milestones, criteria.
  - `tasks.md` - execution queue for the current milestone.
  - `context.md` - durable project invariants.
  - `log.md` - decision chronology.

## Next Step

Start M1: competitive field map.
```

## `context.md` - Durable Invariants

Store only what should survive sessions: terms, metrics, sources of truth, constraints, and dependencies. Do not store meeting episodes or chronology here.

```markdown
---
id: YYYY-demo-product-positioning-strategy-context
type: project
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Context - demo product positioning"
tags: [project, context, demo-product, positioning]
source_path: "01_now/projects/YYYY-demo-product-positioning-strategy/context.md"
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Context

## Essence

Durable decisions and invariants for the demo product positioning project.

## Details

- Terms:
  - Positioning core: one formulation a direct competitor cannot credibly reuse.
  - Competitor substitution test: if a direct competitor can say the same thing, the wording does not differentiate.
- Constraints:
  - Work on the positioning core, not landing-page copy or advertising.
  - Initial horizon: the local market and direct competitors.
- Success measures:
  - One core is chosen with reasons for rejecting two alternatives.
  - The core survives competitor substitution.
- Source of truth:
  - `plan.md`.
  - Competitor overview linked when connected.
- Dependencies:
  - Materials from the source conversation.

## Next Step

Add invariants as milestones produce stable decisions.
```

## `tasks.md` - Execution Queue

`tasks.md` is derived from `plan.md`. It contains only execution: `Task Mode`, `Current Milestone`, one active step, local exit criteria, short drift guard, and next step.

It must not contain `Goal`, `Milestones`, `Contingency`, `Quality Criteria`, or a `Blocked` section. Blockers live in `plan.md`.

### Operational Variant

```markdown
---
id: YYYY-demo-product-positioning-strategy-tasks
type: tasks
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Tasks - demo product positioning"
tags: [project, tasks, demo-product, positioning]
source_path: "01_now/projects/YYYY-demo-product-positioning-strategy/tasks.md"
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Tasks

Task Mode: `operational`

## Current Milestone

`M1 - Competitive Field Map` from `plan.md`

## Active

- [ ] Build the competitive field map: 5+ direct competitors, their positioning core, and occupied terms.

## Exit Criteria

- Competitor table is filled enough to show occupied language.

## Drift Guard (short)

- Do not choose the positioning core before the field map is complete.
- Do not move into landing-page or ad work; those are non-goals.

## Next

- [ ] Draft three positioning candidates and run the competitor substitution test.

## Backlog

- Empty.
```

### Development Variant

For `development`, keep the same minimal structure: current milestone from `plan.md`, active step, exit criteria, short drift guard, next step. Blockers still belong in `plan.md`.

```markdown
# Tasks

Task Mode: `development`

## Current Milestone

`M1 - Skeleton` from `plan.md`

## Active Step

- [ ] Initialize the repository and build an empty skeleton.

## Exit Criteria

- The project builds and the self-check passes.

## Drift Guard (short)

- Do not add features outside the first-version shape.

## Next

- [ ] Implement the core behavior from the technical brief.

## Backlog

- Empty.
```

## `log.md` - Chronology

The first entry records project creation. Format: date, title, 3-7 bullets. Store detailed research, meeting summaries, and analysis in separate files, not in `log.md`.

```markdown
---
id: YYYY-demo-product-positioning-strategy-log
type: log
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Log - demo product positioning"
tags: [project, log, demo-product, positioning]
source_path: "01_now/projects/YYYY-demo-product-positioning-strategy/log.md"
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Project Log

## Essence

Key decisions and state changes for the demo product positioning project.

## Details

### 2026-07-10 - Project Created

- The project was extracted from a conversation about the demo product sounding interchangeable.
- The goal, boundaries, and `operational` task mode were recorded.
- The agent wrote the plan: three milestones from field map to candidates to decision, with quality criteria.
- Recorded assumption: product-wide positioning first; ask if a segment-specific decision appears.
- Source materials from the conversation will be connected in `context.md` as needed.

## Next Step

Start M1: competitive field map.
```

## Index Updates

### `01_now/README.md`

Add the project under the relevant contour. Match the surrounding file's style before editing.

```markdown
- `Demo Product Positioning` -> `./projects/YYYY-demo-product-positioning-strategy/README.md` - choose a defensible positioning core. `operational`, active.
```

### Optional Project Index

If the vault has `01_now/projects/README.md`, it may be autogenerated. If so, do not hand-edit generated blocks unless the local workflow expects it. Make sure the project folder contains `README.md` so the generator can discover it.

## Note for Development Projects

For `development` projects, also create the development-protocol files from `meta/templates/` when available: `AGENT_WORKFLOW.md`, `TEST_PLAN.md`, `RELEASE_CHECKLIST.md`, `CHANGELOG.md`, and `INCIDENT_RUNBOOK.md`. They supplement the five starter files.
