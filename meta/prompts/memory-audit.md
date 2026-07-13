---
id: memory-audit-prompt
type: note
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Memory audit prompt"
tags: [memory, audit, prompt]
source_path: "meta/prompts/memory-audit.md"
---

# Memory Audit Prompt

## Use When

Use this prompt when a project or contour may contain stale, contradicted, weak, or unverified memory claims.

## Task

Audit the selected project or contour without rewriting history. Separate current truth from archive and weak evidence.

## Required Reading

1. `README.md`
2. `context.md`
3. current picture, if any
4. recent `log.md`
5. relevant plans, meetings, or imported materials
6. [vault-memory](../rules/vault-memory.md)
7. [anti-memory](../memory/anti-memory.md)

## Output

Produce a short report using [memory-audit template](../templates/memory-audit.md):

- claims that remain active;
- stale claims;
- contradicted claims;
- claims that need review;
- conflicts created or updated;
- recommended memory-ledger entry.

## Rules

- Do not treat old logs as current truth.
- Do not turn a meeting comment into a decision without authority.
- Do not hide conflicts in a polished summary.
- Do not make strategic changes without human review when `write_policy` requires it.

## Next step

Apply low-risk updates only when the rule allows it. Put strategic or sensitive changes into human review.
