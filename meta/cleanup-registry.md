---
id: cleanup-registry
type: registry
status: active
created: 2026-04-30
updated: 2026-04-30
aliases:
  - "Cleanup registry"
tags: [cleanup, registry, vault]
source_path: "meta/cleanup-registry.md"
---

# Registry cleanup

## Essence

A registry of temporary files, caches and other materials created by the agent.

## Details

| Path | Class | Lifespan | Template | Owner | Cleanup Rule |
|---|---|---|---|---|---|
| `tmp/` | temp | 7 days | `**/*` | agent | Deleted during a scheduled storage check |

## Next step

Add new temporary folders and databases here as soon as you create them.