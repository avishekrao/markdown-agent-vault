---
id: agent-intent-reconstruction-instruction-2026-06
type: note
status: active
created: 2026-06-09
updated: 2026-06-09
aliases:
  - "Agent intent reconstruction"
  - "Underspecified request handling"
tags: [ai, agents, intent, methodology]
source_path: "03_knowledge/ai/agent-intent-reconstruction-instruction-2026-06.md"
freshness: evergreen
knowledge_criticality: high
verification_status: unverified
curation_mode: llm_explicit_request
---

# Agent Intent Reconstruction

## Essence

This instruction prevents an agent from executing an underspecified request too literally. The agent must reconstruct likely intent, identify the risky ambiguity, and ask only when a wrong assumption would materially damage the result.

## Problem

Users often write short commands such as:

- "move this to current";
- "update the project";
- "prepare it for publication";
- "fix the repository";
- "save this".

A literal agent can choose the wrong project, write to the wrong folder, treat old notes as current truth, or perform a deep rewrite when the user wanted a small change.

## Five Ambiguity Checks

Before acting, check whether the request is ambiguous in any of these dimensions:

1. **Project or contour** - which working area owns the task?
2. **Read or write location** - where should the agent read from and where should it write?
3. **Output format** - answer, file, patch, plan, commit, issue, article, table?
4. **Current state vs history** - is the user asking for the latest state or an old record?
5. **Depth of intervention** - light edit, rewrite, new document, rule change, or structural change?

If a wrong assumption would be hard to repair, ask one concise question. If it is easy to repair, choose the most likely path using `README.md`, `plan.md`, `tasks.md`, `context.md`, and `log.md`, then state the assumption in the final answer.

## How To Reconstruct Intent

Use this order:

1. Parse the literal request.
2. Identify the practical outcome the user likely wants.
3. Load only the routing context needed to identify the project or contour.
4. Check whether local rules constrain the action.
5. Identify the cheapest safe assumption.
6. Ask only if the remaining ambiguity changes ownership, write location, format, current status, or intervention depth.

## Allowed Question Shape

Ask a question only when needed. It should be short and framed as confirmation:

> I understand the target as X and would do Y. This is safer because Z. Confirm or correct.

Do not ask the owner to write the plan, criteria, milestones, or checklist for the agent.

## Examples

### "Move this to current"

Risk: `current` may mean `01_now/`, a specific project, a current picture, or the current task queue.

Action: if the contour is known from context, move within that contour. If not, ask which contour owns it.

### "Update the repository"

Risk: could mean pull from remote, apply local methodology changes, update README, or publish a release.

Action: inspect repository status and project plan before writing. Ask only if multiple repositories are plausible.

### "Prepare this for publication"

Risk: format, platform, privacy level, and depth of rewrite may differ.

Action: identify platform if available. If not, ask for the target platform or prepare a platform-neutral draft and state the assumption.

## Prohibitions

- Do not execute a complex underspecified request purely literally.
- Do not read several unrelated contours to guess.
- Do not expose an internal checklist to the user.
- Do not change global rules, `AGENTS.md`, or skills when the user asked only for analysis or a working document.

## Relationship To Project Planning

When the request creates or materially changes a project, the reconstructed intent must be written into `plan.md`: goal, boundaries, non-goals, milestones, quality criteria, drift guard, and review protocol. The result must not stay only in chat.

## Next step

Use this instruction from `AGENTS.md` Rule 0 and from `project-creator` before creating or materially changing a project.
