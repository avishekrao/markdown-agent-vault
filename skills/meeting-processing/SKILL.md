---
name: meeting-processing
description: >
Processing meetings, transcripts and notes: extracting solutions, tasks, facts,
Risks and sustainable knowledge with routing by storage structure.
---

# Meeting Processing

## When to use

Use this skill when the owner asks:

- to sort out the meeting;
- process the decryption;
- identify solutions and tasks;
- make a brief sammari conversation;
- Put the meeting notes in the vault.

## Entrance

- Meeting text, transcript, notes or a link to the file.
- Contour or project, if known.
- If the outline is unclear, ask the owner a short question.

## Process

### 1. Identify a meeting place

Find out if the meeting relates to:

- active project in `01_now/projects/`;
- constant area in `02_domains/`;
- operating circuit in `01_now/ops/`;
- personal obligation of the owner;
- Incoming material with no clear place.

If the place is ambiguous, don't guess.

### 2. Extract layers

Divide the content into:

- decisions;
- agent's tasks;
- tasks of the owner;
- Delegating to other people;
- blockers;
- sustainable knowledge;
- episodic facts;
- unanswered questions.

### 3. File it up.

| Layer | Where to write |
|---|---|
| Solution | `log.md` project or contour |
| Sustainable knowledge | `context.md` or `03_knowledge/` |
| Agent's current move | `tasks.md` |
| Target, milestone, blocker | `plan.md` |
| Delegation | `01_now/ops/<contour>/delegations/<person>.md` |
| Personal obligation of the owner | `01_now/personal/tasks.md` |
| Episodic fact | meeting file, section `## Mentioned in passing` |

### 4. Create a meeting file

If the meeting is important, create a separate meeting file next to the project or outline:

```text
meetings/meeting-YYYY-MM-DD-topic.md
```

Structure:

```markdown
# Meeting YYYY-MM-DD: Theme

## The essence

## Participants

## Decisions

## Challenges

## Sustainable knowledge

## Questions

## Mentioned in passing

## References
```

### 5. Check the result.

Before finishing, check:

- Solutions are not lost in Sammari.
- tasks are not mixed with facts;
- `tasks.md` is not a store of thought.
- The blockers are in `plan.md`, not `tasks.md`.
- people not added without verification;
- A new meeting is reached through the `README.md` or another index.

## Exit

Give it back to the owner:

- created or modified;
- What decisions are recorded;
- What tasks have arisen;
- Which needs clarification.
