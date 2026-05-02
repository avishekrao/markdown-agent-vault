---
id: vault-methodology-export-v0-start-here
type: guide
status: draft
created: 2026-04-30
updated: 2026-05-01
aliases:
  - "Where to start"
  - "First entry into the vault"
tags: [guide, onboarding, vault, methodology]
source_path: "START_HERE.md"
---

# Where to start

## Essence

This is not a file archive, but a work environment for a person and an agent.

## Details

The main idea: the agent should not only answer in the chat, but also maintain order in the files. For this you need:

- clear folder structure;
- recording and routing rules;
- indexes and links;
- templates;
- skills for repetitive tasks.

If this is your first time working with this methodology, first go through [onboarding](./ONBOARDING.md). This file is a short entry and the onboarding explains the entire first cycle of work. For a practical pass, ask the agent to use the skill [`vault-onboarding-guide`](./skills/vault-onboarding-guide/SKILL.md).

### How folders are organized

- `00_inbox/` - everything is new and unassembled.
- `01_now/` - active projects and current work.
- `02_domains/` - long-lived areas of life or business.
- `03_knowledge/` - reused knowledge.
- `04_logs/` - history of solutions, reviews, chronology.
- `90_archive/` - complete and outdated.- `meta/` - rules, templates, service indexes.
- `skills/` - instructions for repetitive task types.

### First request to agent

Tell the agent:

> Open this folder as a working storage. Read `AGENTS.md` first, then explain the folder structure to me and suggest where to put my first materials.

If this is the first launch, it is better to say:

> Open this folder as a working storage. First read `AGENTS.md`, `START_HERE.md` and `ONBOARDING.md`. Explain to me the folder structure, the main rules and suggest a safe first learning step.

If you want to go through onboarding interactively, say:

> Walk me through onboarding with the `vault-onboarding-guide` skill: one step at a time, on a safe learning task, checking files, links and log. Don't let me get into the details of the learning task.

### How to add materials

Place new documents in `00_inbox/` and ask the agent to sort them out. Do not move files by hand if you are not sure: the agent must transfer the file, update links and indexes.

### How to start a project

A new active project is created in `01 now/projects/<year>-<name>/`. Inside should be:

- `README.md` - login and navigation;
- `plan.md` - goal, boundaries, milestones and blockers;
- `tasks.md` — current execution queue;- `context.md` - stable knowledge of the project;
- `log.md` - ​​a short history of solutions.

## Next step

Ask the agent to carry out the initial setup for your tasks and not change files without explaining what exactly he is going to do. For the first practical launch, use [onboarding](./ONBOARDING.md), the “First training task” section, or the skill [`vault-onboarding-guide`](./skills/vault-onboarding-guide/SKILL.md).