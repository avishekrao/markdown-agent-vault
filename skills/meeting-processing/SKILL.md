---
name: meeting-processing
description: >
  Processes meetings, transcripts, and notes: extracts decisions, tasks, facts,
  risks, and durable knowledge, then routes them through the vault structure.
  For recurring meetings with history, use context-compression first so the
  agent does not read the whole meeting archive.
---

# Meeting Processing

## When to Use

Use this skill when the owner asks to:

- process a meeting;
- process a transcript;
- extract decisions and tasks;
- make a short meeting summary;
- route meeting notes into the vault.

## Input

- Meeting text, transcript, notes, or a link to the file.
- Contour or project, if known.
- If the contour is unclear, ask one short question.

## Process

### 1. Identify the Meeting Location

Determine whether the meeting belongs to:

- an active project in `01_now/projects/`;
- a long-lived area in `02_domains/`;
- an operating contour in `01_now/ops/`;
- a personal obligation of the owner;
- incoming material with no clear destination.

If the place is ambiguous, do not guess.

If the meeting is recurring, refers to prior discussions, or the meetings folder already has more than three old summaries, use [context-compression](../context-compression/SKILL.md) first. The output should identify which old meetings to read fully, which decisions are stale, which questions are open, and which old files are covered by compressed history.

### 2. Extract Layers

Separate content into:

- decisions;
- agent tasks;
- owner tasks;
- delegations to other people;
- blockers;
- durable knowledge;
- episodic facts;
- unanswered questions.

For important claims, distinguish fact, decision, hypothesis, assumption, and plan. A participant's statement does not become a decision without authority and explicit basis. An old plan does not become current reality without verification. If an old source conflicts with the current picture, do not smooth it into a neat summary; record a conflict or open question according to [vault-memory.md](../../meta/rules/vault-memory.md).

### 3. Route to Files

| Layer | Destination |
|---|---|
| Decision | project or contour `log.md` |
| Durable knowledge | `context.md` or `03_knowledge/` |
| Current agent step | `tasks.md` |
| Goal, milestone, blocker | `plan.md` |
| Delegation | `01_now/ops/<contour>/delegations/<person>.md` |
| Owner personal obligation | `01_now/personal/tasks.md` |
| Episodic fact | meeting file, `## Mentioned in passing` |

### 4. Create a Meeting File

If the meeting is important, create a separate meeting file near the project or contour:

```text
meetings/meeting-YYYY-MM-DD-topic.md
```

Structure:

```markdown
# Meeting YYYY-MM-DD: Topic

## Essence

## Participants

## Decisions

## Tasks

## Durable Knowledge

## Questions

## Mentioned in Passing

## Links
```

### 5. Check the Result

Before finishing, check:

- decisions were not lost inside a summary;
- tasks are not mixed with facts;
- `tasks.md` did not become a place for reflection;
- blockers are in `plan.md`, not `tasks.md`;
- people were not added without verification;
- the new meeting is reachable through `README.md` or another index;
- if current picture, claim trust, or a memory conflict changed, [ledger.md](../../meta/memory/ledger.md) has an entry.

## Output

Report to the owner:

- what was created or changed;
- which decisions were recorded;
- which tasks appeared;
- what needs clarification.
