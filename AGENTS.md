---
id: agents-rules
type: note
status: active
created: 2026-04-30
updated: 2026-04-30
aliases:
  - "Agent Rules"
  - "AGENTS.md"
tags: [rules, llm, workflow, vault]
source_path: "AGENTS.md"
---

# AGENTS.md - agent rules for file storage

## Main principle

This repository only works when every important document can be reached through pointers, links, and routing rules.

If the agent creates or changes a file, it must update the associated indexes and briefly record the decision in the appropriate log.

## Folder map

| Folder | Destination |
|---|---|
| `00_inbox/` | New and unsorted materials |
| `01_now/` | Active work: projects, current areas, personal tasks |
| `02_domains/` | Permanent areas of life or business |
| `03_knowledge/` | Reused knowledge, methodologies, help |
| `04_logs/` | Timeline, Reviews, Solution Logs |
| `90_archive/` | Completed and outdated |
| `meta/` | Rules, templates, service indexes |
| `skills/` | Skills: instructions for repetitive task types |

## Loading context

Before responding, the agent determines the task type and reads the minimum required context:

| Task type | What to read |
|---|---|| Active project | `01_now/projects/<project>/README.md`, then `context.md`, if necessary `plan.md`, `tasks.md`, `log.md` |
| Permanent area | `02_domains/README.md`, then the profile section |
| Help or Methodology | `03_knowledge/README.md`, then the desired file |
| Write or change a file | `meta/rules/write-protocol.md` |
| Task Routing | `meta/rules/task-routing.md` |
| Processing of incoming materials | `meta/rules/inbox-processing.md` |
| Checking and cleaning storage | `meta/rules/vault-review.md` |
| Creating temporary files | `meta/rules/cleanup-by-design.md` |

If a circuit or project is ambiguous, the agent asks one short question for clarification and does not read the content files of different circuits in a row.

## Creating a project

A new active project is created in `01 now/projects/<year>-<slug>/`.

The project should have:

- `README.md` - input, meaning and navigation;
- `plan.md` - goal, boundaries, milestones, blockers;
- `tasks.md` — current execution queue;
- `context.md` - stable knowledge of the project;
- `log.md` - a short history of solutions.

`plan.md` stores direction and milestones. `tasks.md` stores only current actions. History does not live in `tasks.md`; she lives in `log.md`.

## After writing the file

After a file is created or significantly modified, the agent checks:1. Is there correct service markup at the beginning of the `.md` file.
2. Is the `README.md` section updated?
3. Should I update `plan.md`, `context.md`, `log.md` or `tasks.md`.
4. Do relative links work?
5. Will the new agent find this file through navigation.
6. Is there a lifecycle plan for temporary files.

## Skills

The skills are located in `skills/<name>/SKILL.md`. The agent reads the skill only when the task matches its description.

Basic skills:

- `meeting-processing` - processing of meetings and transcripts;
- `research` - research and recording of the result;
- `parking` — saving the return point;
- `resume` — return to the saved task;
- `new-dialog-handoff` - safe transition to a new chat;
- `owner-only-dev-orchestrator` - managing development tasks with minimal involvement of the owner;
- `test-gates` — checking changes;
- `release-rollback` - release and rollback.

## Response language

The agent responds in the user's language. If he uses a technical term, he explains it in simple terms the first time it is mentioned.

## Prohibitions

- Do not create files without a clear location and purpose.
- Do not leave important documents without a reference from the indexes.- Do not store long-lived knowledge inside a temporary project.
- Do not put personal obligations, delegations and project goals into one list.
- Do not delete logs and incoming materials without an explicit request from the owner.
- Do not read personal mail, instant messengers or external services without a direct request.

## Next step

If this is the first run, the agent should read `START_HERE.md`, this file, and `meta/rules/write-protocol.md`, then briefly explain to the owner how the storage works.
