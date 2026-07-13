---
id: example-github-contour-repository-readme
type: index
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Example GitHub contour repository"
tags: [example, github, contour]
source_path: "examples/github-contour-repository/README.md"
---

# Example GitHub Contour Repository

## Essence

Minimal example of a repository-backed working contour. It shows the files, boundaries, validation, and review model expected from a shared contour repository.

## Navigation

- [Agent rules](./AGENTS.md)
- [Repository manifest](./repository-manifest.yml)
- [Context](./context.md)
- [Plan](./plan.md)
- [Tasks](./tasks.md)
- [Log](./log.md)
- [Example note](./materials/example-note.md)

## Boundaries

This example is intentionally ordinary and public-safe. It contains no private data, credentials, people records, client materials, or raw exports.

## Validation

From the starter-pack root:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

## How To Use

Copy this structure when a long-lived contour needs GitHub review, shared context, and repeatable agent rules.
