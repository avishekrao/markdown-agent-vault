---
id: vault-methodology-export-v0-start-here
type: guide
status: draft
created: 2026-04-30
updated: 2026-07-13
aliases:
  - "Where to start"
  - "First vault entry"
tags: [guide, onboarding, vault, methodology]
source_path: "START_HERE.md"
---

# Where to Start

## Essence

This is not a file archive. It is a working environment for a human and an agent.

## Details

The main idea: the agent should not only answer in chat, but also keep the files orderly. For that you need:

- a clear folder structure;
- write and routing rules;
- current memory instead of blind trust in archive;
- indexes and links;
- templates;
- skills for recurring task types.

If this is your first time using the methodology, start with [ONBOARDING.md](./ONBOARDING.md). This file is the short entry point; onboarding explains the full first work cycle. For a guided pass, ask the agent to use [`vault-onboarding-guide`](./skills/vault-onboarding-guide/SKILL.md).

### Folder Layout

- `00_inbox/` - new and unsorted materials.
- `01_now/` - active projects and current work.
- `02_domains/` - long-lived areas of life or business.
- `03_knowledge/` - reusable knowledge.
- `04_logs/` - decision history, reviews, timeline.
- `90_archive/` - completed and outdated material.
- `meta/` - rules, templates, service indexes.
- `skills/` - instructions for recurring task types.

### First Request to the Agent

Tell the agent:

> Open this folder as a working vault. First read `AGENTS.md`, then explain the folder structure and suggest where to put my first materials.

For the first launch, use a slightly fuller request:

> Open this folder as a working vault. First read `AGENTS.md`, `START_HERE.md`, and `ONBOARDING.md`. Explain the folder structure, the main rules, and suggest the first safe learning step.

If you want interactive onboarding, say:

> Walk me through onboarding with the `vault-onboarding-guide` skill: one step at a time, on a safe learning task, with checks for files, links, and log. Do not let me drift into the details of the learning task.

### Choose a Mode

If you are keeping a personal local vault, start with the ordinary first loop: file in `00_inbox/` -> training project -> links -> log.

If you want a separate GitHub repository for a product, team, client, or another long-lived area, use contour-repository mode:

- read the [guide](./docs/github-contour-repositories.md);
- copy [repository-manifest.yml](./meta/templates/repository-manifest.yml) and [contour_repository_AGENTS.md](./meta/templates/contour_repository_AGENTS.md);
- compare with the [example](./examples/github-contour-repository/README.md);
- run `python3 scripts/validate_contour_repo.py examples/github-contour-repository`.

### Adding Materials

Put new documents in `00_inbox/` and ask the agent to process them. Do not move files by hand if you are not sure: the agent should move the file, update links, and update indexes.

### Starting a Project

A new active project is created through [`project-creator`](./skills/project-creator/SKILL.md) in `01_now/projects/<year>-<slug>/`. The agent writes the plan, quality criteria, execution queue, context, log, and project README.

The project should contain:

- `README.md` - entry point and navigation;
- `plan.md` - goal, boundaries, owner intent, quality criteria, milestones, and blockers;
- `tasks.md` - current execution queue;
- `context.md` - durable project knowledge;
- `log.md` - short decision history.

## Next Step

Ask the agent to perform initial setup for your work and to explain any file changes before making them. For the first practical run, use [ONBOARDING.md](./ONBOARDING.md), the "First training task" section, or [`vault-onboarding-guide`](./skills/vault-onboarding-guide/SKILL.md).
