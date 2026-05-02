---
id: vault-lifecycle-sop
type: note
status: active
created: 2026-03-01
updated: 2026-04-15
aliases:
  - Vault Life Cycle Regulations
tags: [meta, workflow, lifecycle, vault-hygiene]
source_path: "meta/vault-lifecycle-sop.md"
freshness: evergreen
---

# Vault Lifecycle SOP (now -> knowledge -> archive)

## The essence
Operating regulations that keep `01_now` only for current work, and stable knowledge transfers to `03_knowledge`/`02_domains`, with regular archiving and cleaning of temporary artifacts.

## Storage layers
- `00_inbox` is an incoming and unassembled stream.
- `01_now` is only active work and ongoing projects.
- `02_domains` is a permanent role/sphere context.
- `03_knowledge`: Knowledge that is reused outside of a specific project.
- `04_logs` is a weekly/monthly review.
- `90_archive` is complete and historical/legacy.

## Criteria for "Leave in 01 now"
A file remains in `01_now` if at least one is executed:
- It is necessary to complete tasks in the current horizon of 1-4 weeks.
- It has a direct connection with the active milestone in the `plan.md` or execution step in the `tasks.md` project.
- Describes operational decisions/state (plan/context/tasks/log of an active project).
- This is an open-line delegation file (`01_now/ops/<contour>/delegations/<person-slug>.md`).
- This is `01_now/personal/tasks.md` (the only personal commitment file).

## Transfer to 03 knowledge or 02 domains
Move from `01_now` to a stable base if you run 2 of 3:
- Reusability: Useful for more than one project.
- Uniqueness: contains new conclusions / data, does not duplicate what is already saved.
- Volume: The material is more meaningful than a brief note-answer.

## Requirements to archive in 90 archive
- The project is completed (`status: done`) or declared irrelevant.
- The material is no longer needed in operational work.
- There is a more recent/canonical version in `03_knowledge` or an active project.

## Closing procedure for the project
1. Extract reused knowledge in `03_knowledge`/`02_domains`.
2. Put `status: done` in `plan.md` and fix the result in `log.md`.
3. Update links to `context.md` and README active sections.
4. Check contour delegation files: open lines associated with the project, move to the `Archive` section or close in the tracker and mark `Done(7d)`.
5. Transfer the design outline to `90_archive/projects/`.
6. Delete or tag archive links in active indexes (`[archived]`).

## Clearing delegations

Separate hygiene cycle for `01_now/ops/<contour>/delegations/<person-slug>.md`:
- Lines in `Done(7d)` older than 7 days – transfer a section of the same file to `Archive`.
- Lines in `Active` with `due:` older than 30 days without updating - manually check in the tracker (live-first-audit), either close or update.
- Once a month - `forced rewrite` delegation files: remove everything that no longer rings, leave only alive.
- See [task-routing.md §delegations](./rules/task-routing.md).

## Cleanup of `01_now/personal/tasks.md`

- Once a month – forced rewrite (to remove everything that has lost meaning, to reformulate the rest).
- Update `last_rewrite` in frontmatter and file body.
- Do not write cleanup-registry records in it - the file rotates itself.

## Procedure for cleaning temporary files
- Temporary artifacts (`tmp`, `incoming`, `downloads`, test uploads) should not be referenced from stable notes.
- After knowledge integration, delete intermediate files unless there is an explicit request to save.
- Check that `README/context` has no time path references.

## Rhythm of implementation
- Weekly: short lifecycle review (10-15 minutes)
- Monthly (1st): Full `vault hygiene` in all sections.
- Upon completion of the project: separate closing procedure (see above).

## Review launch team
```bash
.venv/bin/python <workspace>/scripts/vault_lifecycle_review.py \
  --root <workspace> \
  --report-md <workspace>/04_logs/weekly/$(date +%G)-W$(date +%V)_vault-lifecycle-review.md \
  --report-json <workspace>/04_logs/weekly/$(date +%G)-W$(date +%V)_vault-lifecycle-review.json
```

## Next step.
After each review run, close at least 3 items from the report: (1) taxonomy/front matter, (2) transfers to `03_knowledge`, (3) archive/deletion of temporary files.
