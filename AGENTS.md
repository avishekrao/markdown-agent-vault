---
id: agents-rules
type: note
status: active
created: 2026-05-02
updated: 2026-05-02
aliases:
  - "Agent rules"
  - "AGENTS.md"
tags: [rules, llm, workflow, vault]
source_path: "AGENTS.md"
---

# AGENTS.md - Agent Rules For A File-Based Vault

## Core Principle

This vault works only when important documents are reachable through indexes, links, and routing rules.

When an agent creates or changes a file, it must update the relevant indexes and record important decisions in the right log.

## Folder Map

| Folder | Purpose |
|---|---|
| `00_inbox/` | New, unsorted material |
| `01_now/` | Active work: projects and current tasks |
| `02_domains/` | Long-lived areas of life or work |
| `03_knowledge/` | Reusable knowledge, methods, and references |
| `04_logs/` | Timeline, reviews, and decision logs |
| `90_archive/` | Completed or obsolete material |
| `meta/` | Rules, templates, and indexes |
| `skills/` | Reusable instructions for recurring task types |

## Loading Context

Before answering, the agent identifies the task type and reads the smallest useful context.

| Task type | Read first |
|---|---|
| Active project | `01_now/projects/<project>/README.md`, then `context.md`, and when needed `plan.md`, `tasks.md`, `log.md` |
| Long-lived area | `02_domains/README.md`, then the relevant section |
| Reference or method | `03_knowledge/README.md`, then the relevant file |
| Creating or editing a file | `meta/README.md`, then the relevant template or rule |
| Processing inbox material | `00_inbox/README.md` |
| Reviewing or cleaning the vault | `scripts/README.md` and relevant indexes |

If the project or area is ambiguous, ask one short clarifying question and do not read multiple unrelated work areas to guess.

## Creating A Project

New active projects live in `01_now/projects/<year>-<slug>/`.

Each project should have:

- `README.md` - entry point, purpose, and navigation;
- `plan.md` - goal, boundaries, milestones, and blockers;
- `tasks.md` - current execution queue;
- `context.md` - stable project knowledge;
- `log.md` - short event and decision history.

`plan.md` keeps direction. `tasks.md` keeps only the current execution queue. History lives in `log.md`, not in `tasks.md`.

## After Writing Files

After creating or substantially changing a file, the agent checks:

1. Does the Markdown file have suitable front matter when the vault expects it?
2. Is the folder `README.md` updated?
3. Should project `plan.md`, `context.md`, `log.md`, or `tasks.md` be updated?
4. Do relative links work?
5. Can a future agent find the file through navigation?
6. Is there a lifecycle plan for temporary files?

## Do Not

- Do not create files without a clear place and purpose.
- Do not leave important files without links from indexes.
- Do not store long-lived knowledge inside a temporary project.
- Do not mix personal obligations, delegated work, and project goals in one list.
- Do not delete logs or inbox material without an explicit owner request.
- Do not read personal mail, messengers, or external services without an explicit owner request.

## First Step

On first launch, read `START_HERE.md`, this file, and `QUICKSTART.md`, then briefly explain how the vault is organized.
