---
id: example-contour-agents
type: rules
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Example contour agent rules"
tags: [example, agents, contour]
source_path: "examples/github-contour-repository/AGENTS.md"
---

# AGENTS.md

## Read First

Before work, read:

1. `AGENTS.md`
2. `repository-manifest.yml`
3. `README.md`
4. `context.md`
5. `plan.md` and `tasks.md` when execution is needed

## Scope

This repository is an example contour only. Do not add real private data, credentials, or client materials.

## Write Rules

- Keep changes small and reviewable.
- Update links after adding or moving files.
- Use `log.md` for short events and decisions only.
- Keep detailed material in `materials/`.

## Ask Before

Ask before changing the manifest, deleting files, changing the contour boundary, or adding sensitive data.

## Validation

Run:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```
