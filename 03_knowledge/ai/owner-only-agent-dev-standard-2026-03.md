---
id: owner-only-agent-dev-standard-2026-03
type: note
status: active
created: 2026-03-18
updated: 2026-03-22
aliases:
  - "Owner-only development standard with LLM agent"
  - "Minimal participation of the owner in AI development"
tags: [knowledge, ai, agents, software-development, scripts, quality, process]
source_path: "03_knowledge/ai/owner-only-agent-dev-standard-2026-03.md"
freshness: seasonal
expires: 2026-09-18
---

# Owner-only development standard with LLM agent

## Essence
Standard for a user without technical expertise: the agent does the implementation and full self-test, the user makes only minimal management decisions (target and release/rollback).

Associated section index: [Knowledge Index](../README.md).

## Details

### 1) Mandatory scope
Applies to all tasks where the agent writes or changes:
- scripts (`scripts/` and neighboring repositories),
- programs/applications (for example Swift/AppKit, Python, CLI),
- CI/CD and release configurations.

### 2) Roles and responsibilities
- User (Owner):
  - sets the goal and priority;
  - decides `Release` or `Rollback` for release changes;
  - does not participate in technical implementation.
- Agent:
  - performs decomposition, implementation, testing and assembly;
  - conducts a mandatory self-test before any “ready” status;
  - prepares a release packet with a risk assessment and a rollback plan.

### 3) Required process artifacts in a code project
Before significant changes to the project there must be:
- `AGENT_WORKFLOW.md`
- `TEST_PLAN.md`
- `RELEASE_CHECKLIST.md`
- `CHANGELOG.md`
- `INCIDENT_RUNBOOK.md`

If there are no artifacts, the agent must create them from templates:
- [Template AGENT_WORKFLOW](.../meta/templates/agent_workflow.md)
- [TEST_PLAN Template](.../meta/templates/test_plan.md)
- [Template RELEASE_CHECKLIST](.../meta/templates/release_checklist.md)
- [Template CHANGELOG](.../meta/templates/changelog.md)
- [Template INCIDENT_RUNBOOK](.../meta/templates/incident_runbook.md)
- [Template owner decision packet](.../meta/templates/owner_decision_packet.md)

### 4) Agent autonomy: what is allowed and what is prohibited
- The agent can autonomously:
  - write code within scope;
  - run lint/type/static checks;
  - run unit/integration/smoke;
  - update changelog and checklist.
- The agent is prohibited without explicit confirmation from the user:
  - destructive operations (`rm -rf`, history rewrite, force push);
  - changing secrets/accesses/permissions;
  - production deploy high-risk changes;
  - data migration without a confirmed rollback path.

### 5) Self-test circuit (mandatory)
Before the “ready” status, the agent must pass:
1. `Code gate`: lint/type/static/security checks.
2. `Test gate`: unit + integration for the affected scope.
3. `Release gate`: assembly of artifact + smoke in a clean environment.
4. `Rollback gate`: confirmed revert path (tag/revert/feature-flag).
5. `Adversarial self-check`: what could have broken and how it will be detected.

If at least one gate is not passed, `GREEN` is prohibited.

### 5.1) Additional gate for agentic development

If the change concerns:
- autonomous agents,
- scripts that the agent runs in a loop,
- self-healing / self-debugging scenarios,
- test-fix-retry circuits,

then **observability gate** is required.

Minimum:
- there are `agent-readable` runtime logs, not just human-readable output;
- the log contains `log-to-code correlation`;
- the log records `belief_state` of the agent, and not just the final error text;
- there is `anti-loop protection`;
- on a repeated fall, there is `forced context` or another mechanism for feeding memory of past failures.

If the agent is running in a loop and these mechanisms are not present, the `GREEN` status is disabled even if tests are passing.### 6) Format of communication with the owner (traffic light only)
The agent returns only one of the statuses:
- `GREEN`: everything has been checked, the risk is low/controlled, you can release it.
- `YELLOW`: there is a limitation, the owner needs to choose from 1-2 options.
- `RED`: release disabled, rollback/fix required.

For each status the agent adds:
- what has changed (1-2 lines in human language),
- what has been verified (short list),
- what step is needed from the owner (`Release`, `Hold`, `Rollback`).

### 7) Minimum entry from the owner
The owner gives the task in the format:
```text
Task: <what to change>
Goal: <what is the result for the user>
Deadline: <when needed>
Risk: low | medium | high (if not sure - medium)
Restrictions: <what cannot be touched>
```

### 8) Related documents
- The full study and rationale can be kept in a separate file next to the standard.
- [Protocol for creating and using scripts](.../meta/script-protocol.md)
- The logging case can be stored as a separate file next to the standard.

## Next step
In all active code projects, create a mandatory set of artifacts from templates and secure the gate policy in CI.