---
id: skill-orchestration-owner-only
type: process
status: active
created: 2026-03-19
updated: 2026-03-19
aliases:
  - "Owner-only Skill Orchestra"
  - Owner-only-dev-orchestrator / test-gates / release-rollback
tags: [process, skills, orchestration, owner-only, development]
source_path: "meta/skill-orchestration-owner-only.md"
---

# Owner-only Skill Orchestra Protocol

## The essence
Uniform rules for launching and bundling three skills for development tasks with minimal participation of the owner: `owner-only-dev-orchestrator`, `test-gates`, `release-rollback`.

Related index: [README meta](./README.md)]

## Details.

## What skills and what are responsible for
- `owner-only-dev-orchestrator` is the main full-cycle orchestrator (contract -> implementation -> self-check -> owner's decision).
- `test-gates` is a code/test/smoke gate.
- `release-rollback` - release readiness, rollback-ready, actions in case of an incident.

## How to launch
- Explicit user launch (preferably):
  - `$owner-only-dev-orchestrator`
  - `$test-gates`
  - `$release-rollback`
- Auto-launch on intent:
  - “Turnkey,” “minimum of my participation,” “check and release” –> `owner-only-dev-orchestrator`.
  - Requests for "Run Verification", "Validation", "Smoke" -> `test-gates`.
  - Requests "release", "tag", "rollback", "incident" -> `release-rollback`.

## Mandatory sequence of orchestration
1. Launch `owner-only-dev-orchestrator`.
2. The orchestrator checks for process artifacts in the target project:
- `AGENT_WORKFLOW.md`
- `TEST_PLAN.md`
- `RELEASE_CHECKLIST.md`
- `CHANGELOG.md`
- `INCIDENT_RUNBOOK.md`
3. If there are no artifacts, create from `meta/templates/`.
4. After implementation, you must run `test-gates`.
5. If the change is release, high-risk or involves rollbacks/incidents, run `release-rollback`.
6. Return only the final decision packet (`GREEN/YELLOW/RED` + 1 owner action).

## Rules of acceptance
- `GREEN`:
  - All required quality gates `PASS`.
  - Rollback path confirmed.
  - No blocking risks.
- `YELLOW`:
  - There is no `FAIL`, but there is a `INCOMPLETE` check or managed residual risk.
- `RED`:
  - There is `FAIL` in the mandatory gates.
  - The real risk is unacceptable.
  - Rollback path missing.

## When you can't go on
- `test-gates = RED` -> Release prohibited, first remediation.
- `release-rollback = NOT_READY` -> release is prohibited until the rollback-ready state is restored.

## Mandatory limitations of autonomy
- Without explicit confirmation of the owner it is impossible:
  - destructive/history rewrite actions;
  - Change secrets/access/prod-permissions
  - Implement high-risk changes;
  - Run migrations without a verified rollback.

## Unified response format to the owner
- `STATUS: GREEN | YELLOW | RED`
- `What's changed:`
- `What's verified:`
- `Needed from the owner: Release | Hold | Rollback`

## Related documents
- [AGENTS.md](../AGENTS.md)
- [Protocol of creation and application of scripts ](./script-protocol.md)]
- [Owner-only development standard with LLM agent ](../03_knowledge/ai/owner-only-agent-dev-standard-2026-03.md)]
- [Owner-only Skill Launch Cheat Sheet ](./owner-only-skills-cheatsheet.md)]

## Next step.
Support this protocol synchronously with the skills `skills/owner-only-dev-orchestrator`, `skills/test-gates`, `skills/release-rollback`.
