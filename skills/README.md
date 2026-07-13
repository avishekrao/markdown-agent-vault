---
id: skills-index
type: note
status: active
created: 2026-03-20
updated: 2026-07-13
aliases:
  - "Skills index"
  - "Custom skills vault"
tags: [skills, index, workflows]
source_path: "skills/README.md"
---

# Skills

## Essence

Index of vault skills: reusable instructions for recurring task types.

## Operating Skills

- [project-creator](./project-creator/SKILL.md) - create a complete project with agent-written plan, tasks, context, log, README, and index updates.
- [vault-onboarding-guide](./vault-onboarding-guide/SKILL.md) - guided first-start onboarding.
- [meeting-processing](./meeting-processing/SKILL.md) - process meetings, decisions, tasks, and routing.
- [context-compression](./context-compression/SKILL.md) - maintain compact meeting history in `meetings/README.md`.
- [research](./research/SKILL.md) - source-first research with saved results.
- [parking](./parking/SKILL.md) - save a return point.
- [resume](./resume/SKILL.md) - restore parked context.
- [new-dialog-handoff](./new-dialog-handoff/SKILL.md) - safely move work to a new chat.

## Development and Release

- [owner-only-dev-orchestrator](./owner-only-dev-orchestrator/SKILL.md) - full development-cycle orchestration for owner-only mode.
- [test-gates](./test-gates/SKILL.md) - run quality gates and produce final status.
- [release-rollback](./release-rollback/SKILL.md) - release readiness and rollback.

## Content and Analytics

- [landing-copywriter](./landing-copywriter/SKILL.md) - landing-page hero and first-screen copy.
- [slide-copywriter](./slide-copywriter/SKILL.md) - slide and presentation content.
- [translation-editorial](./translation-editorial/SKILL.md) - translate technical signals into editorial output.
- [case-forensics](./case-forensics/SKILL.md) - extract reproducible cases from threads and chats.
- [event-intelligence](./event-intelligence/SKILL.md) - monitor and rank AI-related events.
- [network-analytics](./network-analytics/SKILL.md) - update a relationship graph and prioritize outreach.

## Cowork Sync

Use [sync-cowork-skills.sh](./sync-cowork-skills.sh) when an environment needs skills copied or linked outside this repository.

```bash
./skills/sync-cowork-skills.sh --status
./skills/sync-cowork-skills.sh
```

## Next Step

Invoke skills explicitly with `$skill-name` when deterministic workflow selection matters.
