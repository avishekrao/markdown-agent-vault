---
name: context-compression
description: >
  Maintains a compressed meetings/README.md for recurring meetings and long-lived contours. Use when a project has 3+ meeting summaries, when a decision is reversed, when a new meeting should update the rolling context, or when the agent would otherwise need to read the full meetings folder.
---

# Context Compression

## Purpose

Keep long meeting history usable without reading every meeting file. The skill builds and updates a compressed `meetings/README.md` that separates recent meetings, active decision chains, stale agreements, open questions, and anchor sources.

## When To Use

Use this skill:

- before processing a regular meeting when the folder has three or more summaries;
- after adding a new meeting summary to a recurring project or contour;
- when a decision is reversed or superseded;
- when the owner asks for a catch-up across many meetings;
- when a future agent needs a short current history instead of a full archive scan.

Do not use it for one-off meetings with no ongoing thread.

## Required Inputs

- Target project or contour.
- Meetings folder path.
- Existing `meetings/README.md`, if present.
- New meeting summary, if the task follows a meeting.
- Project `README.md`, `context.md`, and current picture if available.

## Output File

Default output:

```text
<project-or-contour>/meetings/README.md
```

Use [meetings README template](../../meta/templates/meetings_readme.md).

## Compression Model

The compressed index must include:

1. **Latest meetings** - most recent entries with links and why they matter.
2. **Active decision chains** - current decisions and the meetings that led to them.
3. **Stale or superseded agreements** - old decisions that should not guide current work.
4. **Open questions** - unresolved issues, owner questions, or missing sources.
5. **Anchor sources** - meetings that remain important even if old.
6. **Update rule** - when the file should be rebuilt again.

## Rules

- Do not treat frequency as truth.
- Do not turn a participant's comment into a decision without authority.
- Preserve disagreement and reversals.
- Prefer links to source meetings over long copied summaries.
- Keep the compressed file compact enough to be read before future meetings.
- If a claim is important and uncertain, mark it as such instead of smoothing it.

## Update Procedure

1. Read project or contour entry files.
2. Read the existing compressed meetings index if present.
3. Read only the meeting summaries needed for the update.
4. Identify new decisions, reversed decisions, stale agreements, and open questions.
5. Update `meetings/README.md`.
6. If the current project or contour picture changed, update it according to [vault-memory](../../meta/rules/vault-memory.md).
7. Record a short event in `log.md` if the update changes project state.

## Quality Check

Before finishing, verify:

- all meeting links resolve;
- old agreements are not presented as current;
- new decisions have source links;
- open questions are explicit;
- the file is shorter than reading the full meeting archive.

## Next step

After updating the compressed index, continue the meeting-processing or project task that triggered the compression.
