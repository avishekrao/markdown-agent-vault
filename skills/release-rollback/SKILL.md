---
name: release-rollback
description: >
Release verification, release and rollback for secure code/script changes.
Use when the user asks: “release”, “prepare the release”, “rollback”,
"What to do in case of an incident", "check release checklist". Skill checks release readiness,
A safe rollback point forms the GREEN/YELLOW/RED solution for the owner.
---

# Release Rollback

## Appointment
Make the release manageable and reversible: validate -> release decision -> rollback readiness.

Related context: [LLM Rules](.../meta/LLM_RULES.md)].

## Entrance
- `RELEASE_CHECKLIST.md`
- `CHANGELOG.md`
- Current commit/branch/tag
- `$test-gates`

## Mode A: Release Readiness
1. Check the `RELEASE_CHECKLIST.md` item by item.
2. Make sure there is a release version (`vMAJOR.MINOR.PATCH`) and a recording in `CHANGELOG.md`.
3. Confirm the safe rollback point (last stable tag/commit).
4. Prepare a short release decision packet for the owner.

## Mode B: Incident Rollback
1. Freeze's new rollouts.
2. Find the last known good version.
3. Choose the path of return (in descending cost):
- feature flag/config toggle off
- `git revert` Problem Change
- rollback to the previous stable tag
4. Perform post-rollback smoke.
5. Decide what new gate/test you need so it doesn’t happen again.

## Tough rules.
- Do not issue a high-risk change without an explicit owner solution.
- Do not consider the release ready without rollback-path.
- In the conflict between speed and safety, choose reversibility.

## Exit
- `Release status: GREEN|YELLOW|RED`
- `Rollback readiness: READY|NOT_READY`
- `Owner action:` `Release | Hold | Rollback`
- `Next safest step:` 1 Specific Step
