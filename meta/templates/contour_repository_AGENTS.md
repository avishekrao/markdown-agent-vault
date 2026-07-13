---
id: contour-repository-agents-template
type: rules
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases:
  - "Contour repository AGENTS template"
tags: [template, agents, github, contour]
source_path: "meta/templates/contour_repository_AGENTS.md"
---

# AGENTS.md

## Repository Rule

This repository represents one working contour. Do not mix it with other contours and do not import private material unless the manifest explicitly allows it.

## Read First

Before doing any work, read in this order:

1. `AGENTS.md`
2. `repository-manifest.yml`
3. `README.md`
4. `context.md`
5. `plan.md` and `tasks.md` when execution is required
6. `log.md` only for short history

## Writing Rules

- Use Markdown files with frontmatter.
- Update navigation links after creating or moving files.
- Record decisions and important events in `log.md`.
- Keep detailed analysis in separate files, not in `log.md`.
- Use pull requests unless the manifest explicitly allows direct edits.

## Ask Before

Ask the human before:

- changing the contour boundary;
- editing protected files;
- moving or deleting files;
- adding private or sensitive material;
- treating a meeting comment as a decision;
- changing goals, review policy, or data ownership.

## Validation

Before a change request, run the commands listed in `repository-manifest.yml`.

## Response Rule

In responses, state what changed, what was checked, and what still needs human review.
