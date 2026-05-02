---
id: personal-tasks
type: tasks
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
last_rewrite: <YYYY-MM-DD>
next_rewrite_hint: <YYYY-MM-DD — +30 days>
aliases:
  - "Personal tasks of the owner"
  - "Personal tasks"
tags: [personal, tasks, obligations]
source_path: "01_now/personal/tasks.md"
knowledge_criticality: low
verification_status: verified_by_me
curation_mode: manual_edit
---

# Personal Tasks

Last rewrite: <YYYY-MM-DD>

## The essence

A single file of personal external obligations of the owner. **No backlog, no wish list, no working inbox. If something is a desire or a curiosity, it doesn’t get there. If something is working, it goes to `<project>/tasks.md` or `<contour>/delegations/<slug>.md`.

The owner is a flow-worker. This file is not read on a daily basis. Reading - only by external trigger: "I remembered about Y - what was written there?" or after monthly forced rewrite.

Methodology: [task-routing-methodology-2026-04.md §7](../../03_knowledge/task-routing-methodology-2026-04.md)] Rules of ownership: [AGENTS.md Rule 13](../../AGENTS.md)]

## Rules

- **Ambient capture:** strings are added without MR-diff, without coordination, without explanation. The task of fixation is not to forget at the time of mention.
- Recording is a reminder, not a performance contract.
- **Forced rewrite once a month.** Rewrite the file, discard anything that no longer rings. Update `last_rewrite` in frontmatter and in the row above.
- **No weekly review.** If something gets into a file and forced rewrite deletes it a month later, it's a normal system operation, not a loss.
- **Two sections, no more.** Hard (real external commitments to the world) and Maybe (short reminders that may come in handy).
- **Do not write off project or delegated tasks here.** Even if mentioned at a project meeting, if it is an external obligation of the owner, it is here; if the performer does something, it is not here.

## Hard

Real external obligations to the world: money, dates, documents, promises to specific people. Violation = real-world consequence.

- [ ] <obligation - specific action, deadline if any, counterparty if applicable >>
- [ ] <second obligation >>

## Maybe

Short reminders, curiosity, ideas. No obligation to comply. Most of that will be removed in the next forced rewrite - and that's OK.

- <reminder >>
- <idea> >>
- <curiosity>

## Next step.

Nothing. This file does not require follow-up. If a real task appears, it migrates to `<project>/tasks.md` or `delegations/<slug>.md`. If there is a commitment, stays in Hard. Everything else is ephemeral.
