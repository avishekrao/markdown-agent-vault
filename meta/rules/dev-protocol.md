---
id: dev-protocol
type: rules
status: active
created: 2026-03-30
updated: 2026-03-30
aliases:
  - “Protocol of development”
  - "Dev protocol"
tags: [rules, dev, scripts, code, owner-only]
source_path: "meta/rules/dev-protocol.md"
---

# Development protocol and scripts

## The essence
Rules for any task where an agent creates or alters code, scripts, or programs. Minimum user participation, mandatory self-checking, final status of GREEN/YELLOW/RED.

## 1. script protocol

When creating any script:
1. **First explain the logic, limitations and implementation options
2. *Write the code only after confirmation**
3. **After launch** – record the result and the rollback command in `scripts/runs.log`

Details: [Protocol of creation and application of scripts ](../script-protocol.md)]

## 2. Owner-only development

For any code change task:

1. Work according to the standard: [Owner-only development standard ](../../03_knowledge/ai/owner-only-agent-dev-standard-2026-03.md)]
2. Minimize user involvement: the user sets a goal and only accepts a release decision; the agent performs implementation and complete self-checking
3. Before changes, ensure the process-artifacts:
   - `AGENT_WORKFLOW.md`, `TEST_PLAN.md`, `RELEASE_CHECKLIST.md`, `CHANGELOG.md`, `INCIDENT_RUNBOOK.md`
   - If not, create from `meta/templates/` templates.
4. Quality gates: lint/type/static, unit/integration, smoke, rollback plan
5. Report in format only:
   - `GREEN` - all checks passed, release is safe
   - `YELLOW` – there are risks or incomplete checks
   - `RED` – Prohibited release, further development required

## 3. General Standard for Agentic Development

- Global rules are short, project specifics are next to code
- Before the code - mandatory `ask/plan`
- Breaking the job down into milestones
- `tasks.md` for code tasks to run only in `development` mode: one `Active Step`, mandatory `Exit Criteria` and `Drift Guard`
- Avoid Silent Fallback on the Critical Path
- Ambiguous automatic solutions → review queue

Full reference: [General rules of agentic development ](../../03_knowledge/ai/general-rules-for-agentic-development-in-local-vault-2026-03.md)]

## 4. Rules for issuing terminal commands

- Before **any* terminal command, check the paths: user working folder Indicate complete absolute paths
- Before `rm`, `mv`, `sed -i`, `git reset`, `DROP` - show what will be deleted/moved/modified and receive confirmation
- All scripts are via `python3`, not `python`. For pip: `--break-system-packages`
- If the `Permission denied` error does not do `chmod 777`, offer an alternative

## 5. Lifecycle Code Artifacts (MUST)

Any script that **creates files, databases, caches, or dumps** must:
1. Have a built-in cleaning mechanism (`--clean` parameter, TTL logic, rotation)
2. Document what creates and where - in the code comment + in [cleanup-registry.md](../cleanup-registry.md).
3. For SQLite: mandatory date field (`created_at`/`fetched_at`) for TTL filtering

If a script creates data but does not provide how to delete it, it is a bug, not a feature.

Complete rules: [Cleanup by Design](./cleanup-by-design.md)]

## 6. Upgrade instead of crutches

If a bug or incompatibility is detected, fix the **cause** (update the format, fix the generator, fix the circuit) rather than bypass the symptom. A workaround is permissible only as a temporary measure with a TODO marker and a correction task.
