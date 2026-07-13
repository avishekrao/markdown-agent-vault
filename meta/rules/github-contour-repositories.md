---
id: github-contour-repositories
type: rules
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "GitHub contour repositories"
  - "Contour repository rules"
tags: [rules, github, contour, repository]
source_path: "meta/rules/github-contour-repositories.md"
knowledge_criticality: high
verification_status: unverified
curation_mode: llm_explicit_request
---

# GitHub Contour Repositories

## Essence

A long-lived working contour can be moved into its own GitHub repository when it must be shared with other people, reviewed through pull requests, and protected from accidental cross-contour edits.

## When To Use

Use a separate contour repository when:

- multiple people need the same durable context;
- the contour should survive individual implementation projects;
- changes require human review;
- boundaries, edit zones, and private data rules must be explicit;
- GitHub history and pull requests are useful for coordination.

Do not use it for a short project, temporary research, raw imports, or private material that should stay in the owner's vault.

## Required Files

A contour repository must include:

- `README.md` - human entry point;
- `AGENTS.md` - agent operating rules for this repository;
- `repository-manifest.yml` - machine-readable boundary and policy;
- `context.md` - stable contour context;
- `plan.md` - slow contract;
- `tasks.md` - current execution queue;
- `log.md` - short event and decision history;
- `CODEOWNERS` - review ownership;
- pull request template;
- validation workflow when GitHub Actions is enabled.

## Manifest

Use [repository-manifest.yml template](../templates/repository-manifest.yml). The manifest states:

- repository identity and contour;
- visibility and data class;
- human operating model;
- write model;
- files the agent must read first;
- what can be edited without asking;
- what requires human review;
- validation commands;
- mandatory user questions.

## Agent Rules

Use [contour repository AGENTS template](../templates/contour_repository_AGENTS.md). Agents must read `AGENTS.md`, `repository-manifest.yml`, `README.md`, and `context.md` before work.

## Validation

Before a change request, run at least:

```bash
python3 scripts/validate_contour_repo.py <repo-root>
```

The validator checks required files, manifest contract, local links, and forbidden export markers.

## Example

See [example contour repository](../../examples/github-contour-repository/README.md).

## Related Documentation

- [GitHub contour repositories](../../docs/github-contour-repositories.md)
- [Write protocol](./write-protocol.md)
- [Task routing](./task-routing.md)

## Next step

Use this rule only when a contour needs shared GitHub-based work, not just because a folder exists.
