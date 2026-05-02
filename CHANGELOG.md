# Changelog

All notable public changes are tracked here.

This project uses early semantic versions. Until `v1.0.0`, breaking changes to structure or rules may happen when they make the starter pack clearer or safer.

## [v0.2.0] - 2026-05-02

Full English mirror of the Russian methodology.

### Added

- Full translated methodology layer from the Russian repository: `meta/`, `meta/rules/`, `meta/templates/`, `03_knowledge/`, and the complete `skills/` library.
- Additional release notes for prior Russian-version releases now represented in the English repository.
- Sync policy describing the current `mirror while solo-maintained` mode.

### Changed

- `README.md` now states that this repository is the English mirror/adaptation while the project is solo-maintained.
- Local checks now allow the Russian repository link only in `docs/sync-policy.md`.
- Code comments, docstrings, and user-facing messages remain English without changing script logic.

## [v0.1.2] - 2026-05-02

### Changed

- Restored the repository split notes after creating a separate English-first package.
- Restored the root README and quickstart for the package audience.

### Removed

- Removed transitional English entry files from this repository: `AGENTS.en.md`, `START_HERE.en.md`, `ONBOARDING.en.md`.

## [v0.1.1] - 2026-05-02

### Added

- English versions of the core first-run documents: `AGENTS.en.md`, `START_HERE.en.md`, and `ONBOARDING.en.md`.
- Language navigation in `README.md`.

### Changed

- `QUICKSTART.md` now points English-speaking users to the English first-run files while preserving the Russian originals.

## [v0.1.0] - 2026-05-02

First public starter-pack release.

### Added

- Public README with positioning, first 10-minute flow, comparison table, maturity status, topics, and validation commands.
- `QUICKSTART.md` for a safe 5-10 minute test.
- MIT license.
- Contribution, support, roadmap, and pull request guidance.
- GitHub issue templates for bugs, documentation fixes, examples, and method changes.
- Minimal `examples/first-session/` workflow showing an inbox note routed into a project.
- Release notes under `docs/releases/v0.1.0.md`.

### Notes

- This release is intentionally small.
- Tool-specific compatibility claims are not included yet.
- The repository should be tested as a copy before being used on a real vault.
