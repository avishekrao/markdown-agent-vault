---
id: scripts-readme
type: index
status: active
created: 2026-04-30
updated: 2026-07-13
aliases:
  - "Validation scripts"
tags: [index, scripts, validation]
source_path: "scripts/README.md"
---

# scripts

## Essence

Minimal executable layer for checking the portable vault.

## Details

Scripts do not depend on external services and do not contain owner-specific paths.

### Contents

- [check_links.py](./check_links.py) - checks relative links to `.md` files.
- [check_forbidden_markers.py](./check_forbidden_markers.py) - finds prohibited markers: local paths, private work contours, tokens, and other strings that should not enter the portable package.
- [check_repository_manifest.py](./check_repository_manifest.py) - checks the minimal `repository-manifest.yml` contract for a GitHub contour repository.
- [inventory.py](./inventory.py) - prints file count, size, and top-level composition.
- [validate_contour_repo.py](./validate_contour_repo.py) - runs a minimal contour repository check: required files, manifest, links, and forbidden markers.

### How to Run

From the package root:

```bash
python3 scripts/inventory.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
```

For the GitHub contour repository example:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

Or pass a path explicitly:

```bash
python3 scripts/check_links.py /path/to/vault
```

## Next Step

After any package change, run the base scripts. For contour-repository mode, also run `validate_contour_repo.py`.
