---
id: memory-readme
type: index
status: active
created: 2026-07-01
updated: 2026-07-13
aliases:
  - "Memory layer"
  - "Vault memory"
tags: [memory, trust, index]
source_path: "meta/memory/README.md"
knowledge_criticality: high
verification_status: unverified
curation_mode: llm_explicit_request
---

# Memory

## Essence

This directory holds the trust layer for long-lived vault memory: memory-change logs, anti-memory rules, conflict records, and review queues. It exists so an agent does not treat every old note, meeting comment, plan, or confident summary as current truth.

## Navigation

- [Memory ledger](./ledger.md) - append-only record of memory changes.
- [Anti-memory](./anti-memory.md) - what must not be turned into memory without evidence.
- [Conflicts](./conflicts/README.md) - unresolved contradictions between memory claims.
- Templates live under [meta/templates](../templates/README.md): memory card, conflict, audit, and working context.

## Operating rule

Current memory is a curated layer. Archive, logs, meetings, imports, and drafts remain evidence, but they are not current truth by themselves.

## Next step

Use [vault-memory](../rules/vault-memory.md) whenever a task changes current project or contour memory.
