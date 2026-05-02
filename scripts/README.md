---
id: scripts-readme
type: index
status: active
created: 2026-04-30
updated: 2026-04-30
aliases:
  - Scripts of verification
tags: [index, scripts, validation]
source_path: "scripts/README.md"
---

# scripts

## The essence

Minimum executable layer for checking the portable storage.

## Details.

Scripts do not depend on external services and do not contain the ways of the owner.

### Composition

- [check links] py](./check_links.py) checks relative links to `.md` files.
- [check forbidden markers. py](./check_forbidden_markers.py) is looking for prohibited tokens: local paths, working circuits, tokens and other strings that should not fall into the alienated packet.
- [inventory] py](./inventory.py) shows the number of files, size and composition of the upper level.

### How to launch

From the root of the package:

```bash
python3 scripts/inventory.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
```

Or point the way clearly:

```bash
python3 scripts/check_links.py /path/to/vault
```

## Next step.

After any changes to the package, run all three scripts.
