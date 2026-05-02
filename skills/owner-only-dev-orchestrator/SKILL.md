---
name: owner-only-dev-orchestrator
description: >
Orchestrating a full development cycle with minimal ownership and maximum agent self-testing.
Use when the user asks: “turnkey”, “minimum of my participation”, “check it yourself”,
Implement/fix the script or program completely. Skill is required for code tasks where necessary.
pass quality gates, prepare owner decision packet and issue the result only in GREEN/YELLOW/RED format.
---

# Owner-Only Dev Orchestrator

## Appointment
Perform end-to-end contour for development tasks: contract task -> implementation -> self-test -> solution for the owner.

Related context: [LLM Rules](.../meta/LLM_RULES.md)].

## Mandatory sources of rules
Read before work:
- [LLM Rules](.../meta/LLM_RULES.md)
- [Owner-only development standard with LLM agent ](.../03_knowledge/ai/owner-only-agent-dev-standard-2026-03.md)]
- [Protocol of creation and application of scripts ](.../meta/script-protocol.md)]

## Workflow
1. Identify the target repository/code folder.
2. Check for mandatory process artifacts in the repository:
- `AGENT_WORKFLOW.md`
- `TEST_PLAN.md`
- `RELEASE_CHECKLIST.md`
- `CHANGELOG.md`
- `INCIDENT_RUNBOOK.md`
3. If there are no artifacts, create them from `meta/templates/` before risky changes.
4. Set the task contract:
- Goal
- Scope
- Out of scope
- Risk class (`low|medium|high`)
- Required validations
5. Follow through with small, logical steps.
6. Call `$test-gates` to run quality gates.
7. If there is a release part, high-risk change or incident, call `$release-rollback`.
8. Create an owner decision packet and return only the management decision.

## Limitations on autonomy
- Do not perform destructive/history-rewrite actions without explicit confirmation.
- Do not change secrets/access/production configurations without confirmation.
- Do not declare `GREEN` unless you have passed mandatory checks.

## Format of response to the owner
Always complete the answer with a block:
- `STATUS: GREEN | YELLOW | RED`
- `What's changed:` 1-2 lines without techjargon
- `What's verified:` short list of gate results
- `We need from the owner:` `Release | Hold | Rollback`

## Status criteria
- `GREEN`: All mandatory gates passed, rollback path confirmed.
- `YELLOW`: Some of the checks are incomplete or there are manageable risks.
- `RED`: Mandatory gates fail or risk unacceptable; release prohibited.
