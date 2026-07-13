---
id: vault-methodology-onboarding
type: guide
status: active
created: 2026-05-01
updated: 2026-07-13
aliases:
  - "Vault methodology onboarding"
  - "How to start working with the vault"
tags: [guide, onboarding, vault, methodology, agents]
source_path: "ONBOARDING.md"
freshness: evergreen
knowledge_criticality: high
verification_status: unverified
curation_mode: manual_edit
---

# Onboarding to the Vault Methodology

## Essence

This guide helps you launch the vault for the first time: open the folder in a file-capable agent, run a safe training task, save the result in the right place, check navigation, and understand when repeated work becomes a rule or a skill.

## How to Read This

Do not try to learn the whole system before using it.

1. Read sections 1-3 and complete the first-hour route.
2. Return to sections 4-7 when you need routing rules.
3. Use sections 8-10 for the first real project.
4. Use sections 11-13 when the work becomes long, repetitive, or team-facing.

If you want guided onboarding, ask the agent to use [`vault-onboarding-guide`](./skills/vault-onboarding-guide/SKILL.md).

## 1. Main Idea

This is not a folder of notes. It is a working environment where:

- the human sets direction and checks sensitive decisions;
- the agent reads rules, files, indexes, and logs;
- project state is stored in files rather than in chat memory;
- decisions, tasks, context, and sources have different places.

A normal chat loses state easily. This vault gives the next agent session a path back into the work: indexes -> project README -> plan/context/tasks/log -> detailed files.

## 2. Before the First Launch

1. Put the vault in a stable folder, not in downloads.
2. If you want sync, place it in a cloud drive or Git repository intentionally.
3. Open the root folder in an agent that can read and change files.
4. Open the same folder in a Markdown editor such as Obsidian if you want human-friendly browsing.
5. Keep the full folder path visible so you can point tools to it.

First request:

```text
Open this folder as a working vault. Read AGENTS.md first, then START_HERE.md and ONBOARDING.md. Explain the folder structure, main operating rules, and the first safe test step.
```

If the agent starts changing files before reading rules, stop it:

```text
First read AGENTS.md and reconsider your actions according to the vault rules.
```

## 3. First-Hour Route

Start with a small training task.

1. Open the vault in the agent.
2. Send the first request from section 2.
3. Put a small Markdown note in `00_inbox/`.
4. Ask the agent to create a training project through `project-creator`.
5. Check the created project files and updated indexes.
6. Open a new chat and ask the agent to continue from files.

Minimum request:

```text
This is my first time working with this vault. Walk me through the tutorial: read the rules, explain the structure, create a training project for the file from 00_inbox/ through project-creator, save the result, update indexes, and show the log entry.
```

The goal is to see the loop: incoming material -> project -> saved result -> links -> log -> continuation in a new session.

## 4. Root-Level Map

- `AGENTS.md` - rules the agent reads at the beginning of work.
- `START_HERE.md` - short entry for first launch.
- `ONBOARDING.md` - this guide.
- `00_inbox/` - new materials before processing.
- `01_now/` - active work: projects, operations, personal tasks.
- `02_domains/` - long-lived areas of life or business.
- `03_knowledge/` - reusable knowledge and methodologies.
- `04_logs/` - timeline, reviews, decision logs.
- `90_archive/` - completed and outdated material.
- `meta/` - rules, templates, service indexes, memory support.
- `skills/` - reusable task instructions.
- `scripts/` - local validation checks.

## 5. Navigation Rule

A document is not useful if the agent cannot reach it.

The vault has three navigation layers:

- folder `README.md` files explain what each area contains;
- links connect documents with each other;
- project state files (`README.md`, `plan.md`, `tasks.md`, `context.md`, `log.md`) let a future session recover status.

After creating an important file, the agent should:

- add a link from the relevant README or neighboring document;
- add backlinks when useful;
- record the event in `log.md` if it changes project state;
- check that the file is reachable through navigation.

Test question:

```text
If I open a new chat tomorrow and ask about this file, will the agent find it through README files and links?
```

If the answer is no, the work is unfinished.

## 6. Where Things Go

Basic routing:

- new and unsorted -> `00_inbox/`;
- active project with a bounded result -> `01_now/projects/`;
- long-lived operating area -> `01_now/ops/` when the vault has that convention;
- long-lived domain -> `02_domains/`;
- reusable knowledge -> `03_knowledge/`;
- decision/event history -> `04_logs/` or project `log.md`;
- completed/outdated -> `90_archive/`;
- agent rule -> `meta/rules/` or `AGENTS.md`;
- reusable technique -> `skills/<name>/SKILL.md`.

Do not route data by convenience. Ask who owns the data and where it must live after the current project closes.

## 7. Projects

A project is bounded work with a result and a closing point. New projects are created through [`project-creator`](./skills/project-creator/SKILL.md).

A project must contain:

- `README.md` - entry point and navigation;
- `plan.md` - slow contract: goal, boundaries, intent, quality criteria, milestones, blockers;
- `tasks.md` - current execution queue;
- `context.md` - durable project invariants;
- `log.md` - short chronology of decisions and state changes.

The agent writes the plan and quality criteria. The owner should not have to fill an empty plan or invent milestones. If a foundational fork is unclear, the agent asks one short question and recommends a default option.

## 8. Current Memory

Archive is not current truth.

Old logs, meeting notes, drafts, and inbox files are evidence. They are not automatically the current state. Before complex work, the agent should read current layers first:

- `plan.md` for goal, boundaries, milestones, blockers, and drift guard;
- `context.md` for durable invariants;
- working context if the project declares one;
- memory ledger, anti-memory, and conflicts when memory status matters.

Important claims should carry type, source, basis, confidence, verification date, and write policy. See [vault-memory.md](./meta/rules/vault-memory.md).

## 9. Meetings

Meeting processing separates decisions, tasks, delegations, durable knowledge, episodic facts, and open questions.

For recurring meetings or folders with more than a few summaries, use [`context-compression`](./skills/context-compression/SKILL.md). It maintains `meetings/README.md` as a compressed historical layer: recent meetings, decision chains, stale decisions, open questions, and anchor sources.

This keeps the agent from rereading every old meeting and from treating outdated decisions as current.

## 10. Incoming Materials

`00_inbox/` is not an archive. It is a staging area.

Workflow:

1. Human places material in `00_inbox/`.
2. Agent processes it for a specific task.
3. Valuable output moves to a project, contour, domain, or knowledge file.
4. Agent records processing in `00_inbox/PROCESSING_LOG.md`.
5. Source material stays until the owner decides what to delete.

Do not search `00_inbox/` as if it were a knowledge base. If material matters later, process it and link it from the right place.

## 11. GitHub Contour Repositories

For a team, product, client, or other long-lived work contour, use a separate GitHub contour repository.

Core pieces:

- `repository-manifest.yml` - machine-readable boundaries, ownership, data classes, edit zones, and checks;
- `AGENTS.md` - repository-specific agent rules;
- `plan.md`, `tasks.md`, `context.md`, `log.md` - contour working state;
- pull request template - human review surface;
- validation script - local checks before a change request.

Start with [docs/github-contour-repositories.md](./docs/github-contour-repositories.md) and [examples/github-contour-repository](./examples/github-contour-repository/README.md).

## 12. Checks

Run from the repository root:

```bash
python3 scripts/inventory.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
```

For the contour repository example:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

A change is not ready if links are broken, forbidden markers appear, or the new file cannot be reached through indexes.

## 13. When to Create a Rule or Skill

Create a rule when the same routing or safety decision repeats.

Create a skill when the same task type repeats and needs a stable procedure: meeting processing, research, project creation, parking/resume, release work, or validation.

Keep rules and skills small enough for an agent to read and follow. After changing a skill, update related indexes and run checks.

## Next Step

Run the first-hour route in a safe copy. Then open a new chat and verify that the agent can continue from files alone.
