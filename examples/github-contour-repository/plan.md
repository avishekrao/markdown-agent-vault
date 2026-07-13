---
id: example-contour-plan
type: plan
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Example contour plan"
tags: [example, plan, contour]
source_path: "examples/github-contour-repository/plan.md"
---

# Plan

## Goal

Show the minimal file contract for a GitHub-backed contour repository that agents and humans can use safely.

## Intent Lock

This example demonstrates structure and validation only. It must not become a real data store.

## Owner Interaction Policy

The agent may update example wording and links. It must ask before adding private or real-world data.

## Non-goals

- Do not model a full business process.
- Do not add private data.
- Do not replace the root starter pack.

## Appetite

Small example, kept compact.

## Source of Truth

- `repository-manifest.yml`
- `AGENTS.md`
- `README.md`

## Milestones

### M1 - Minimal contour repository

Acceptance: required files exist, manifest validates, links pass.
Status: active.

## Quality Criteria

- All required files exist.
- Manifest validation passes.
- Links resolve.
- The example remains public-safe.

## Blockers

None.

## Blockers - Resolved

None.

## Drift Guard

Keep the example minimal and generic.

## Contingency

If the example grows too large, move optional material to separate documentation.

## Review Protocol

Validate before changes are merged.
