---
id: example-github-contour-repository-readme
type: index
status: active
created: 2026-07-13
updated: 2026-07-17
aliases:
  - "Example GitHub contour repository"
tags: [example, github, contour]
source_path: "examples/github-contour-repository/README.md"
---

# Example GitHub Contour Repository

## Essence

Minimal example of a repository-backed working contour. It shows the files, boundaries, validation, and review model expected from a shared contour repository.

## Scenario

A procurement team comparing CRM vendors and maintaining non-confidential shared materials, including research, evaluation criteria, project status, and decisions throughout the selection process.

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

### Safe to commit

- Public pricing, with the source and date verified.
- Publicly documented product features, rather than information obtained under an NDA or during a private demo.
- Publicly documented support offerings, rather than a negotiated service-level agreement.
- The team’s non-confidential evaluation process and criteria.

### Keep outside the repository

- Negotiated pricing and discounts.
- Account credentials, passwords, tokens, or API keys.
- Real CRM records containing customer information.

## Human Review

Before merging a proposed change, a human reviewer should check:

- **Privacy and scope:** Verify that no confidential pricing, credentials, customer data, or restricted vendor material is included in the change.
- **Factual accuracy:** Verify that pricing, features, and support information are correctly represented and sourced.
- **Judgment:** Verify that recommendations reflect the team’s evaluation criteria and are not presented as settled decisions merely because an agent generated them.

## Failure Case

An agent summarizes a vendor proposal and attempts to include confidential negotiated pricing in a comparison document. The agent should exclude the pricing, and a human reviewer should reject any proposed change that contains it.

## Validation

From the starter-pack root:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

## How To Use

Copy this structure when a long-lived contour needs GitHub review, shared context, and repeatable agent rules.
