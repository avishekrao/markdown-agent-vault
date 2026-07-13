---
id: agents-rules
type: note
status: active
created: 2026-04-30
updated: 2026-07-13
aliases:
  - "Agent rules"
  - "AGENTS.md"
tags: [rules, llm, workflow, vault]
source_path: "AGENTS.md"
---

# AGENTS.md - Agent Rules for the File Vault

## Main Principle

This vault only works when every important document can be reached through pointers, links, and routing rules.

If the agent creates or changes a file, it must update the related indexes and briefly record the decision in the appropriate log.

## Folder Map

| Folder | Purpose |
|---|---|
| `00_inbox/` | New and unsorted materials |
| `01_now/` | Active work: projects, current areas, personal tasks |
| `02_domains/` | Long-lived areas of life or business |
| `03_knowledge/` | Reusable knowledge, methodologies, reference material |
| `04_logs/` | Timeline, reviews, decision logs |
| `90_archive/` | Completed and outdated material |
| `meta/` | Rules, templates, service indexes |
| `skills/` | Skills: instructions for recurring task types |

## Loading Context

Before responding, determine the task type and read the minimum necessary context:

| Task type | What to read |
|---|---|
| Active project | `01_now/projects/<project>/README.md`, then `context.md`; if needed, `plan.md`, `tasks.md`, `log.md` |
| Long-lived area | `02_domains/README.md`, then the relevant area page |
| Reference or methodology | `03_knowledge/README.md`, then the needed file |
| Write or change a vault file | `meta/rules/write-protocol.md` |
| Route tasks | `meta/rules/task-routing.md` |
| GitHub contour repository | `repository-manifest.yml` + `meta/rules/github-contour-repositories.md` |
| Create a new project | `skills/project-creator/SKILL.md` + `03_knowledge/ai/agent-plan-methodology-research-2026-07.md` |
| Work with current project/contour memory | `meta/rules/vault-memory.md` |
| Compress meeting history | `skills/context-compression/SKILL.md` |
| Process incoming materials | `meta/rules/inbox-processing.md` |
| Review or clean the vault | `meta/rules/vault-review.md` |
| Create temporary files | `meta/rules/cleanup-by-design.md` |
| Handle an underspecified or multi-path request | `03_knowledge/ai/agent-intent-reconstruction-instruction-2026-06.md` |

If the contour or project is ambiguous, ask one short clarification question and do not read content files from multiple contours in a row.

If the working folder root contains `repository-manifest.yml`, read it immediately after `AGENTS.md`. In that mode, follow [GitHub contour repository](./meta/rules/github-contour-repositories.md): "allowed without asking" means prepare a branch and change request unless the repository explicitly permits direct main-branch edits.

## Underspecified Requests

If a request can be handled in several materially different ways, first reconstruct the owner's intent:

1. What did the owner explicitly ask for?
2. What practical result do they likely need?
3. What constraints are visible from the project, rules, language, and path?
4. What can be safely assumed?
5. Where would a wrong assumption damage the result and require one short question?

A safe assumption is allowed when it is grounded in context, easy to correct, and does not change the result's meaning, contour, write location, source of truth, or depth of intervention.

If a wrong assumption could damage data, routing, privacy, or future work, ask one short question instead of acting on a guess.

Do not show the internal intent analysis as a separate report. It exists to choose work depth, read/write location, output format, and intervention boundaries. Full method: [agent intent reconstruction instruction](./03_knowledge/ai/agent-intent-reconstruction-instruction-2026-06.md).

## Creating a Project

Create a new active project through [project-creator](./skills/project-creator/SKILL.md) in `01_now/projects/<year>-<slug>/`.

A project must contain:

- `README.md` - entry point, purpose, and navigation;
- `plan.md` - goal, boundaries, owner intent, quality criteria, milestones, blockers;
- `tasks.md` - current execution queue;
- `context.md` - durable project knowledge;
- `log.md` - short decision history.

`plan.md` stores direction and milestones. `tasks.md` stores only current actions. History does not live in `tasks.md`; it lives in `log.md`.

The agent writes the plan and quality criteria. The owner should not have to fill the plan, invent items, or review it line by line. If the agent cannot safely choose the goal, boundaries, source of truth, or cost of error, it asks one short question packet and recommends a default option.

Methodology: [LLM-agent planning](./03_knowledge/ai/agent-plan-methodology-research-2026-07.md).

## Memory

Archive is not current memory. `log.md`, old meetings, incoming files, and drafts are useful evidence, but they must not automatically be treated as the current state.

Current memory lives in:

- `context.md` - durable invariants;
- `plan.md` - goal, boundaries, milestones, blockers, and drift guard;
- a dedicated working context, when a project or contour is too large for one `context.md`;
- decision, fact, or hypothesis files when they are declared as sources of truth.

Before complex work, read current layers before archive layers. After a significant event, update affected layers in this order: `plan.md`, `context.md` or working context, `log.md`, then `tasks.md`.

Important memory claims do not become true just because they are written down. For decisions, risks, constraints, current statuses, and hypotheses, record claim type, source, basis, confidence, verification date, and write rule. Details: [Vault memory](./meta/rules/vault-memory.md), [Anti-memory](./meta/memory/anti-memory.md), and [Memory ledger](./meta/memory/ledger.md).

## GitHub Contour Repository

If a task belongs to a separate GitHub repository for a contour:

1. Read `repository-manifest.yml`.
2. Check owner, data class, and allowed edit zones.
3. If the action touches private data, access rules, deletion, moving, or another contour, ask one short question.
4. Prepare changes through a branch and change request unless direct main-branch edits are explicitly allowed.
5. In the change request description, state what changed, why, what files were touched, whether private-data risk exists, what checks passed, and what a human must confirm.

Details: [GitHub contour repositories](./meta/rules/github-contour-repositories.md).

## After Writing a File

After creating or significantly changing a file, check:

1. Does every Markdown file have correct frontmatter?
2. Is the section `README.md` updated?
3. Should `plan.md`, `context.md`, working context, `log.md`, or `tasks.md` be updated?
4. Do relative links work?
5. Can a future agent find the file through navigation?
6. Is a [memory ledger](./meta/memory/ledger.md) entry needed?
7. Is there a lifecycle plan for temporary files?

## Skills

Skills live in `skills/<name>/SKILL.md`. Read a skill only when the task matches its description.

Core skills:

- `project-creator` - creates a new project with an autonomous plan, starter files, and index updates;
- `meeting-processing` - processes meetings and transcripts;
- `context-compression` - maintains compressed meeting history and bounded reading windows;
- `research` - performs research and records the result;
- `parking` - saves a return point;
- `resume` - returns to a saved task;
- `new-dialog-handoff` - safely moves work to a new chat;
- `owner-only-dev-orchestrator` - runs development tasks with minimal owner involvement;
- `test-gates` - checks changes;
- `release-rollback` - handles release and rollback work.

## Response Language

Respond in the user's language. If you use a technical term, explain it plainly the first time it appears.

## Prohibitions

- Do not create files without a clear location and purpose.
- Do not leave important documents unreachable from indexes.
- Do not store long-lived knowledge inside a temporary project.
- Do not mix personal obligations, delegations, and project goals in one list.
- Do not delete logs or incoming materials without the owner's explicit request.
- Do not read personal mail, messengers, or external services without a direct request.
- Do not commit private data, secrets, raw imports, or large source files into an ordinary contour repository.

## Next Step

On first launch, read `START_HERE.md`, this file, and `meta/rules/write-protocol.md`, then briefly explain how the vault works.
