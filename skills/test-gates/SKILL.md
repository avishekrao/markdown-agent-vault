---
name: test-gates
description: >
Run and verify quality gates for development tasks (scripts/programs).
Use when you need to check for a change before status is ready or release:
lint/type/static checks, unit/integration, smoke, flaky-policy and GREEN/YELLOW/RED status.
Triggers: “run the check”, “check the quality”, “validation”, “smoke”, “quality gates”.
---

# Test Gates

## Appointment
Check the change with machine-verified checks. Do not trust a textual explanation without commands executed.

Related context: [LLM Rules](.../meta/LLM_RULES.md)].

## Entrance
- Target repository/folder.
- A list of modified files.
- Risk class change.
- Local teams from `TEST_PLAN.md` and `README.md`.

## Workflow
1. Gather teams of checks from:
- `TEST_PLAN.md`
- `AGENT_WORKFLOW.md`
- `README.md`
2. First, run the code gate:
- lint
- type/static/security checks (if configured)
3. Perform test gate:
- unit tests
- integration tests
4. Run the release/smoke gate:
- Smoke teams from the project
5. Process flaky:
- flag
- Do not count flaky-pass as a full-fledged green without project policy.
6. Create a single gate report.

## Tough rules.
- Do not declare `GREEN` unless the mandatory command is triggered.
- If the command is not available in the environment, mark as `INCOMPLETE`, not `PASS`.
- If the check drops, add the short root of the problem and the nearest corrective step.

## Exit (gate report)
- `Code gate: PASS|FAIL|INCOMPLETE`
- `Test gate: PASS|FAIL|INCOMPLETE`
- `Smoke gate: PASS|FAIL|INCOMPLETE`
- `Flaky notes:` if any
- `Overall status: GREEN|YELLOW|RED`

## Status criteria
- `GREEN`: All required gates = PASS.
- `YELLOW`: There is no FAIL, but there is INCOMPLETE/residual risk.
- `RED`: There is a FAIL in the mandatory gates.
