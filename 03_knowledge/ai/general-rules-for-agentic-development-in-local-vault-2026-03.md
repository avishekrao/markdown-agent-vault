---
id: general-rules-agentic-development-local-vault-2026-03
type: note
status: active
created: 2026-03-30
updated: 2026-03-30
aliases:
  - "General rules for agent-based development for local storage"
  - "How to assign development to an LLM agent in any project"
tags: [knowledge, research, ai, agents, codex, development, process, vault-rules]
source_path: "03_knowledge/ai/general-rules-for-agentic-development-in-local-vault-2026-03.md"
freshness: seasonal
expires: 2026-09-30
research_type: decision
confidence: medium
---

# General rules for agentic development for local storage

## Essence
In the global storage rules, you need to write not project specifics, but a stable operating model for any development with an agent. The best general standard for your regime is this: short global rules as a policy layer, repo-local docs as a system of record, mandatory ask/plan before code, work with small milestones, strict quality gates, explicit `review queues` for ambiguous decisions and a ban on silent fallback on the critical path.

## Details

## What should live in global storage rules

### 1. Global rules should be short and stable
Global rules should only include things that do not depend on a specific project:
- where active projects, knowledge and logs are located;
- mandatory bootstrap for a new thread;
- owner-only mode and autonomy matrix;
- mandatory quality gates;
- rules for working with indexes, logs and design outline;
- general policy on Git, secrets, destructive operations and releases.

No need to put it into global rules:
- details of the architecture of a specific product;
- long research notes;
- the specifics of a separate stack or one team;
- large prompt fish for one project.

### 2. Each code project must have its own system of record
Global rules should require that in any new project live next to the code:
- `AGENTS.md` as a project map;
- `ARCHITECTURE.md`;
- `docs/design-docs/`;
- `docs/data-contracts/`;
- `docs/exec-plans/active/`;
- process artifacts `AGENT_WORKFLOW.md`, `TEST_PLAN.md`, `RELEASE_CHECKLIST.md`, `CHANGELOG.md`, `INCIDENT_RUNBOOK.md`.

The principle is simple: the agent should not pull out critical context from the chat memory. The source of truth must lie in the project.

### 3. Ask/plan phase is required before the code
General rule for any development:
- first the agent reads local rules and repo-local docs;
- then forms a self-contained execution plan;
- only after this the code starts.

The plan should record:
- goal and user result;
- scope and non-goals;
- input documents and source codes;
- milestones;
- acceptance criteria through observed behavior;
- test strategy;
- risks and rollback path.

If there is no plan, the agent almost always starts patching up local symptoms instead of a design solution.

### 4. Tasks should be given in small, complete milestones
The global policy should prohibit vague tasks of the format:
- “remake the system”;
- “make a new architecture”;
- “fix everything.”

Normal unit of work for an agent:
- one milestone;
- about an hour of engineering work or several hundred lines;
- clear artifact at the output;
- locally verifiable result.

### 5. Global rules must separate policy, memory and implementation docs
Good three-layer model:
- `global policy` — general storage rules;
- `project memory` - stable project-specific instructions and known quirks;
- `execution plan` - what we are doing in the current cycle;
- `code/docs` is the actual implementation.

This reduces drift and prevents the agent from dragging random context into a new project.### 6. Any agentic development should be observability-first
If the agent or script is running in a loop, `stdout` alone is not enough.

Global rule:
- agentic scripts are required to write structured logs;
- the log must contain `run_id`, `step_id`, `belief_state`, `observed_result`, `next_action`;
- there must be `anti-loop protection` and forced context on the second fall;
- without this, the `GREEN` status is prohibited.

### 7. Silent fallback and hidden degradation are prohibited on the critical path
This is worth writing down as a general principle, not just for AI Digest.

If critical step depends on:
- models;
- external API;
- structured output schemes;
- mandatory data field,

then in case of failure the system must:
- either clearly fall;
- either create a review queue / degraded mode with explicit markings,

but don’t silently replace “simpler” logic.

### 8. Ambiguous decisions should go to the review queue
In all tasks where the agent:
- matches by entities;
- records fade;
- normalizes directories;
- chooses from several interpretations,

I need a general pattern:
- `confident` -> apply;
- `uncertain` -> send to review queue;
- `unsafe` -> stop.

This is especially important for graphs, CRM, deduplication, migrations and data normalization.

### 9. Review and implementation need to be separated by context
General rule: do not do coding, debugging and final review in one long context.

Normal pattern:
- ask/plan;
- implementation;
- fresh-context review;
- test gate;
- release decision.

Otherwise, the agent begins to defend its own previous decisions instead of independent verification.

### 10. Global rules should require evals, not just "seems ok"
For any complex agentic logic you need to require an eval harness.

Minimum:
- golden examples;
- regression set;
- obvious failure classes;
- success metrics for critical behavior.

If logic relies on LLM, the system cannot be considered controllable without evals.

## What is better to keep not in global rules, but in the project

In the project, and not in the vault policy, you need to store:
- specific product architecture;
- data contracts;
- naming conventions and business terms;
- reuse boundaries for legacy;
- anti-patterns of this particular project;
- prompt templates for a specific domain;
- eval datasets and scoring rubrics.

Rule: the closer the knowledge is to one repository, the closer to the code it should be.

## Basic workflow that should be made mandatory for any development

### Step 1. Bootstrap
The agent is obliged:
- read the global rules;
- check the indices and outline of the project;
- collect only relevant context pack;
- do not scan the entire vault unless necessary.

### Step 2. Ask-mode plan
The agent does not write code until it builds:
- goal;
- restrictions;
- acceptance criteria;
- milestones;
- test plan;
- rollback idea.

### Step 3. Repo bootstrap
If the project is new or poorly instrumented, the agent first creates:
- process artifacts;
- repo-local docs;
- execution plan;
- runbook.

### Step 4. Implementation of a short milestone
One cycle = one milestone with a clear output.

### Step 5: Independent Verification
A separate review pass in a fresh context:
- correctness;
- regressions;
- edge cases;
- tests quality;
- observability.

### Step 6. Release decision packet
The user receives only:
- `GREEN / YELLOW / RED`;
- what has changed;
- what has been verified;
- what the owner needs to decide.

## Which prompt standard makes sense to fix globally

For any development tasks, one general formulation template is sufficient:```text
Task: <what to change>
Goal: <what custom result is needed>
Context: <which files and documents are considered source of truth>
Restrictions: <what cannot be broken/touched>
Scope: <what's included>
Non-goals: <what is not included>
Output artifacts: <what files/docs/tests should appear>
Acceptance criteria: <what observable behavior is considered success>
Work order: first ask/plan, then implement milestone-by-milestone
```

This is enough if the global rules already include:
- owner-only mode;
- mandatory tests;
- release gate;
- updating of indexes and design contour.

## Antipatterns that should be banned outright
- Start code without ask/plan.
- Try to repair legacy locally if greenfield-redesign is needed.
- Giving the agent too broad a scope at once.
- Mix global policy and project specifics in one file.
- Leave critical decisions without evals.
- Silently degrade into heuristic/manual fallback.
- Complete the task without tests, smoke and rollback paths.
- Try to keep all the context in the chat only.

## What I would recommend adding to your local rules as a permanent standard
1. For any development, first `ask/plan`, then the code.
2. Global rules are short; design specifics live next to the code.
3. Each code project must have a repo-local system of record and process artifacts.
4. Any LLM-critical logic requires evals and a ban on silent fallback.
5. Agentic scripts without structured logs and anti-loop protection cannot receive `GREEN`.
6. Ambiguous automatic decisions must go into the review queue.
7. Implementation and review should take place in different phases and, if possible, in different contexts.
8. By default, launch a new major product as a separate track, and not as an endless refactor legacy.

## Sources
- [OpenAI: How OpenAI uses Codex](https://openai.com/business/guides-and-resources/how-openai-uses-codex/)
- [OpenAI: A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Anthropic: Manage Claude's memory](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude blog: Using CLAUDE.md files](https://claude.com/blog/using-claude-md-files)

## Next step
If necessary, turn this note into a short block that can be safely embedded in `meta/LLM_RULES.md` without expanding the global rules into an encyclopedia.