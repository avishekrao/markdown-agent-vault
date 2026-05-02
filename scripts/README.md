---
id: scripts-readme
type: index
status: active
created: 2026-05-02
updated: 2026-05-02
aliases:
  - "Validation scripts"
tags: [index, scripts, validation]
source_path: "scripts/README.md"
---

# scripts

## Summary

This folder contains small local validation scripts for the portable starter kit.

## Scripts

- [check_links.py](./check_links.py) - checks relative links to Markdown files.
- [check_forbidden_markers.py](./check_forbidden_markers.py) - scans for local paths, private markers, tokens, and other strings that should not appear in a public starter kit.
- [inventory.py](./inventory.py) - prints file count, size, and top-level structure.

## How To Run

From the repository root:

```bash
python3 scripts/inventory.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
```

Or pass the root path explicitly:

```bash
python3 scripts/check_links.py /path/to/vault
```

## Next Step

Run all three scripts after meaningful package changes.
