---
id: contour-repository-readme-template
type: index
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases:
  - "Contour repository README template"
tags: [template, github, contour]
source_path: "meta/templates/contour_repository_README.md"
---

# <Contour Name>

## Essence

This repository holds the durable working context for one contour: current context, plan, tasks, log, materials, and agent rules.

## Navigation

- [Agent rules](./AGENTS.md)
- [Repository manifest](./repository-manifest.yml)
- [Context](./context.md)
- [Plan](./plan.md)
- [Tasks](./tasks.md)
- [Log](./log.md)
- [Materials](./materials/)

## Boundaries

This repository contains:

- current contour context;
- decisions and short logs;
- project plans and current tasks;
- materials that should be shared with this contour.

This repository does not contain:

- unrelated contours;
- private owner notes;
- raw imports that have not been reviewed;
- secrets, credentials, or API keys.

## Change Model

Use a branch and pull request for meaningful changes. Direct edits to `main` are allowed only when the manifest says so.

## Validation

```bash
python3 scripts/validate_contour_repo.py .
```
