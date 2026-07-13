---
name: project-creator
description: >
  Creates a new vault project and the full starter documentation set: plan.md,
  tasks.md, context.md, log.md, README.md, plus index updates. The agent writes
  the plan itself using the autonomous LLM-agent planning methodology: Intent
  Lock, Owner Interaction Policy, milestones with acceptance conditions, Quality
  Criteria, and Drift Guard. Use when the owner says: "create a project", "start
  a project", "turn this into a project", "capture this as a project", "set up a
  project for X", or equivalent wording. Works in two scenarios: the project is
  extracted from the current conversation, or the owner asks for a new project
  from scratch. Do not use for meeting processing, parking/resume flows, or
  ordinary continuation of an existing project.
---

# Vault Project Creation

You create a new project in `01_now/projects/` and write its starter documentation: `plan.md`, `tasks.md`, `context.md`, `log.md`, and `README.md`. You also update the relevant indexes so a future agent can find the project without reading the chat.

The central guarantee of this skill: **the agent writes the plan and starter documentation itself**. The owner receives a usable project frame, not an empty brief to fill in.

## Core Rule

The agent writes the project documentation. Do **not** ask the owner to draft the plan, list milestones, invent quality criteria, or review the plan line by line.

Clarifying questions are allowed only when the answer is necessary to choose the foundation of the project safely: goal, contour, boundaries, cost of error, or source of truth. Everything else is inferred from the conversation, the command, and local rules, then recorded as an assumption.

Supporting sources:

- [LLM-agent planning methodology](../../03_knowledge/ai/agent-plan-methodology-research-2026-07.md)
- [intent reconstruction instruction](../../03_knowledge/ai/agent-intent-reconstruction-instruction-2026-06.md)
- [project plan template](../../meta/templates/project_plan.md)

## Read Before Acting

Use durable local sources, not model memory:

- [LLM-agent planning methodology](../../03_knowledge/ai/agent-plan-methodology-research-2026-07.md) - how to write a plan that resists drift.
- [project_plan.md](../../meta/templates/project_plan.md) - canonical plan sections.
- [agent-intent-reconstruction-instruction-2026-06.md](../../03_knowledge/ai/agent-intent-reconstruction-instruction-2026-06.md) - how to handle underspecified requests.
- [write-protocol.md](../../meta/rules/write-protocol.md) - frontmatter, links, and index updates.
- [task-routing.md](../../meta/rules/task-routing.md) - what belongs in `plan.md`, `tasks.md`, and other files.

## File Access Requirement

This skill requires write access to the vault. If the agent does not have file access, do not pretend to create the project. Ask the owner to connect the vault folder or provide a writable workspace.

## Two Entry Scenarios

Determine the scenario from the owner's wording and the current conversation state.

### A. The Project Emerges From the Current Conversation

Typical triggers: "capture this as a project", "turn this into a project", "let's create a project for this", "make this a project".

Before asking any question, extract the brief from the conversation that already happened:

- **Goal** - what result was discussed and what should change.
- **Idea and reason** - what the initiative is and why it appeared.
- **Decisions already made** - conclusions reached in the chat.
- **Boundaries and non-goals** - what was excluded or should be avoided.
- **Open questions** - unresolved decisions.
- **Discussed materials** - links, files, data, or examples mentioned in the chat.
- **Likely contour** - the area the project belongs to, based on names, products, or domains in the conversation.
- **Reason for a separate project** - why this is not just a task in an existing project.

Do not start with a blank brief. Do not ask the owner to retell what is already in the chat. The extracted brief becomes input for `Goal`, `Intent Lock`, `context.md`, and the first `log.md` entry.

### B. The Project Starts From a Fresh Command

Typical triggers: "create project X", "start a project about Y", "new project for Z".

Reconstruct intent from the command, local rules, and nearby vault context such as relevant indexes and sibling projects. If there is enough information to choose the project foundation safely, write the documentation immediately. If not, ask one short question packet using the budget below.

## Question Budget

Ask the owner only when all of these are true:

- the answer cannot be inferred from the conversation, command, and rules;
- different answers materially change the goal, contour, boundaries, cost of error, or source of truth;
- there is no conservative assumption that is safe enough to record and revise later.

Rules:

- Ask one packet at a time, maximum three short questions.
- Each question includes the agent's recommended option and asks the owner to confirm or correct it.
- Use this shape: "I understand the goal as ... . I recommend A because ... . B makes sense if ... . Confirm or correct."
- Never ask the owner to write the plan, list milestones, define quality criteria, or approve a checklist line by line.

If multiple contours are genuinely possible and choosing the wrong one would damage the result, stop and ask for the contour instead of guessing.

## Procedure

### 1. Verify That This Is a New Project

A project is an initiative with a clear result, bounded horizon, and eventual closing point.

Check the owner/source-of-truth rule:

- raw imports belong in `00_inbox/`;
- long-lived operating datasets belong in `01_now/ops/<contour>/`;
- reusable methodology belongs in `03_knowledge/`;
- a temporary implementation layer may belong in a project.

Do not create a project to host data whose durable home is elsewhere.

### 2. Choose Year, Contour, and Slug

Use the current year from the environment or `date +%Y`; do not rely on memory.

The slug is kebab-case Latin text, describes the intended outcome, and does not repeat the year. Include a contour prefix only when the vault convention uses one.

Path pattern:

```text
01_now/projects/<year>-<slug>/
```

Examples:

```text
01_now/projects/YYYY-demo-product-positioning-strategy/
01_now/projects/YYYY-sample-trip/
```

### 3. Choose Task Mode

Use one mode for the project start:

- `operational` - research, analysis, content, coordination, and other knowledge work.
- `development` - code, scripts, tests, schemas, data contracts, runtime, build, or release work.

Write the mode in `plan.md` frontmatter and in `tasks.md`.

For `development`, also create the development-protocol files from `meta/templates/` when the vault contains them: `AGENT_WORKFLOW.md`, `TEST_PLAN.md`, `RELEASE_CHECKLIST.md`, `CHANGELOG.md`, and `INCIDENT_RUNBOOK.md`. These files supplement the five required starter files; they do not replace them.

### 4. Reconstruct Intent Silently

Before writing, answer these internally:

- What did the owner explicitly ask for?
- What practical outcome do they likely need?
- What constraints are visible from the conversation and vault rules?
- What can be handled by a safe recorded assumption?
- Where would a wrong assumption break the result and require a question?

Do not show this internal checklist to the owner.

### 5. Ask Only If Needed

If the question-budget test is met, ask one short packet and wait. Otherwise proceed.

### 6. Write `plan.md`

Use [references/plan-authoring.md](./references/plan-authoring.md).

Required sections:

- `Goal`
- `Intent Lock`
- `Owner Interaction Policy`
- `Non-goals`
- `Appetite / Budget`
- `Source of truth`
- `Milestones` with `Acceptance`
- `Quality Criteria`
- `Blockers`
- `Blockers - Resolved`
- `Drift Guard`
- `Contingency`
- `Review Protocol`

The goal describes a changed state, not a list of agent actions. The agent defines milestones and quality criteria.

### 7. Write the Starter Files

Use [references/starter-files.md](./references/starter-files.md).

- `context.md` - durable invariants only.
- `tasks.md` - execution queue derived from the current milestone in `plan.md`; one active step; local exit criteria; short drift guard; next step.
- `log.md` - first event entry: date, short title, 3-7 bullets, links to details when needed.
- `README.md` - entry point with links to service files.

### 8. Update Indexes

Register the project in `01_now/README.md`. If the vault has a dedicated `01_now/projects/README.md`, update it too or make sure it will be regenerated by the local index mechanism.

The test: a new agent session must be able to reach the project through indexes, then `README.md`, then `plan.md` and `context.md`.

### 9. Verify and Report

Run the checklist below, then report briefly: project path, plan essence, first active step, and any assumptions you recorded.

## Required Files

| File | Purpose | Required |
|---|---|---|
| `plan.md` | Slow project contract: goal, boundaries, milestones, criteria, drift guard | yes |
| `tasks.md` | Execution queue for the current milestone | yes |
| `context.md` | Durable project invariants | yes |
| `log.md` | Chronology; first entry records project creation | yes |
| `README.md` | Entry point and navigation | yes |
| development files | `AGENT_WORKFLOW.md` and related templates | only for `development` |

Also update `01_now/README.md` and any existing project index.

## Final Checklist

- [ ] Each Markdown file has frontmatter required by [write-protocol.md](../../meta/rules/write-protocol.md): `id`, `type`, `status`, `created`, `updated`, `aliases`, `tags`, `source_path`.
- [ ] `created` and `updated` use today's date.
- [ ] `plan.md` includes all required sections, including filled `Intent Lock`, `Owner Interaction Policy`, and `Quality Criteria`; `Blockers` and `Blockers - Resolved` are empty in a new project.
- [ ] `Goal` describes a changed state, not "do N actions".
- [ ] `tasks.md` declares `Task Mode`, names the current milestone from `plan.md`, has exactly one active step, local exit criteria, and `Drift Guard (short)`.
- [ ] `tasks.md` does not contain `Goal`, `Milestones`, `Quality Criteria`, `Contingency`, or a `Blocked` section.
- [ ] `context.md` contains durable invariants, not meeting episodes or chronology.
- [ ] The first `log.md` entry is short and does not store full research or meeting content.
- [ ] Internal links are relative Markdown links and point to existing files.
- [ ] The project is registered in indexes so a future session can find it.
- [ ] No prohibited question was asked: the owner was not asked to write the plan, milestones, or criteria.

## Anti-Patterns

- Creating an empty brief and asking the owner to fill it.
- Asking the owner to restate information that is already in the chat.
- Showing an internal checklist as if it were the work product.
- Putting `Goal`, `Milestones`, `Contingency`, or `Quality Criteria` in `tasks.md`.
- Putting blockers in `tasks.md`; blockers belong in `plan.md`.
- Guessing the contour when the choice is materially ambiguous.
- Creating a project as the durable home for data that belongs in `ops/`, `00_inbox/`, or `03_knowledge/`.

## References

- [references/plan-authoring.md](./references/plan-authoring.md) - how to write `plan.md` autonomously.
- [references/starter-files.md](./references/starter-files.md) - templates for `README.md`, `context.md`, `tasks.md`, and `log.md`.
- [references/worked-examples.md](./references/worked-examples.md) - two end-to-end examples.
