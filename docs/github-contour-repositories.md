---
id: docs-github-contour-repositories
type: reference
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "GitHub contour repositories"
  - "Repository-backed contours"
tags: [github, contour, repository, collaboration]
source_path: "docs/github-contour-repositories.md"
knowledge_criticality: high
verification_status: unverified
curation_mode: llm_explicit_request
---

# GitHub Contour Repositories

## Essence

A GitHub contour repository is a standalone repository for one long-lived working contour. It gives people and agents the same boundaries, current context, review path, and validation commands.

## Why It Exists

A personal vault is good for one owner. A shared contour needs a stricter shape:

- a clear owner;
- a manifest that says what the repository is and is not;
- edit zones;
- pull request review;
- local checks;
- a short history of decisions;
- agent rules that do not depend on a private vault.

## Minimal Structure

```text
README.md
AGENTS.md
repository-manifest.yml
context.md
plan.md
tasks.md
log.md
CODEOWNERS
.github/
  PULL_REQUEST_TEMPLATE.md
  workflows/validate.yml
materials/
```

## Required Validation

From the starter pack root:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

The validator checks required files, the manifest contract, local Markdown links, and forbidden export markers.

## Repository Manifest

`repository-manifest.yml` is the machine-readable contract. It describes identity, visibility, data class, edit model, read-first files, validation commands, and situations where the agent must ask the human before acting.

## Human Review

The default path is branch plus pull request. Direct edits to `main` are reserved for explicitly small and low-risk repositories.

## Agent Behavior

An agent must read, in order:

1. `AGENTS.md`
2. `repository-manifest.yml`
3. `README.md`
4. `context.md`
5. `plan.md` and `tasks.md` when execution is needed
6. `log.md` only for short history, not as a content store

## When Not To Use

Do not create a contour repository for:

- temporary implementation work;
- raw imports;
- private owner notes;
- experiments without a long-lived owner;
- material that cannot be reviewed safely by other people.

## Templates

- [Repository manifest](../meta/templates/repository-manifest.yml)
- [Contour AGENTS](../meta/templates/contour_repository_AGENTS.md)
- [Contour README](../meta/templates/contour_repository_README.md)
- [Pull request template](../meta/templates/github_pull_request_template.md)

## Example

See [example GitHub contour repository](../examples/github-contour-repository/README.md).
