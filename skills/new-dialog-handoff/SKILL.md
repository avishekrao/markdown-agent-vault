---
name: new-dialog-handoff
description: >
Safe transition to a new dialog when the chat has become long or the agent predicts the context window will soon run out.
Skill reuses `parking` and `resume`, captures durable source of truth and prepares a short restart-packet for fresh chat.
Be sure to use when the user says: “new dialogue”, “transfer to a new chat”, “make a handoff”, “continue in a new chat”,
And also when the agent itself outputs the critical tail of the species `CTX~N% -> new-dialog-handoff`.
---

# Transition to a new dialogue

You run a secure handoff protocol in a fresh chat. The goal is not to lose working condition, not to duplicate memory and not to drag critical context only into the story of the conversation.

## Principle

First save the state in durable source of truth, then transfer the work to a new chat. Don’t do a long retelling of the conversation if you already have `log.md`, `tasks.md`, `context.md`, research-note, spec or other canonical artifact.

## When to apply

- The chat has become long, and the quality of the following answers may subside.
- The agent shows the critical tail of `CTX`.
- The user clearly asks to continue in the new chat.
- There's a long next step: review, big diff, big crack, multifile editing, long explanation.

## Protocol

### Step 1. Determine where the state should live

Ask yourself:
- This is project work.
- This is standalone research/knowledge.
- Or there is already a ready-made canonical artifact that you can lean on.

Priority source of truth (in order **slow layers → fast**, as in [write-protocol.md §5](../../meta/rules/write-protocol.md)):
1. Existing design contour – `README.md` → `plan.md` → `context.md` → `tasks.md` → `log.md`;
2. `01_now/ops/<contour>/delegations/<person-slug>.md` – if the state is an open delegation
3. `01_now/personal/tasks.md` - if the state is a personal obligation of the owner;
4. already created standalone note in `03_knowledge/`;
5. `00_inbox/` – if it is a curiosity without a project
6. a new checkpoint only if the condition is really lost without it.

If the handoff concerns an active project, and `plan.md` does not yet exist (legacy), first create `plan.md` from the template, then fix the state already in the new slow-layer contract. Handoff should not rely solely on `log.md` if the project is already active.

### Step 2: Reuse `parking`, not replace it

If the work relates to the project:
- First, execute the protocol from `skills/parking/SKILL.md` – it will dilute the state by the correct files (plan / log / tasks / delegations / personal) according to the task-routing decision tree (see [task-routing-methodology-2026-04.md §4](../../03_knowledge/task-routing-methodology-2026-04.md));
- Do not invent a parallel fixation system.
- In the next chat, recommend entering via `resume` - he will reread README → plan → context → tasks → log and make a passive recall by delegation.

If the task is outside the project, but in the current cycle, a durable artifact has already been created:
- Use it as a source of truth.
- Do not create a separate handoff memory.

If durable artifact is not yet available and the loss of context is real:
- Create a minimum checkpoint in the right place.
- Only then offer a new chat.

### Step 3. Squeeze the handoff to restart-packet

Give the user a short package, maximum 5 items:

```text
New dialogue:
- What we continue: <1 line >>
- Source of truth: <1-3 files – plan → context → tasks → log >>
- Open delegation: <if available, the path to delegations/*.md >>
- Next step: <1 specific action >>
- Start in a new chat: <short command or prompt >>
```

Don't retell the whole session. Don't copy the long analysis. Do not duplicate the contents of files in chat.

### Step 4. Rule for launching a new chat

If the project handoff:
- recommended start: `resume <project or task >>`

If it's a standalone job,
- give paste-read prompt:

```text
Continue <task>. Source of Truth: "Paths to Files" Do not repeat again, continue with the next step.
```

### Step 5. With a critical residue, do not try to "press"

If the tail is already critical:
- Don't start another long analysis.
- Do not go into additional searches;
- Checkpoint/handoff first;
- Then a new chat.

## Limitations

- Don’t keep an important state in the history of the conversation.
- Do not create a new handoff artifact if `parking` + existing files is enough.
- Do not replace `resume`; the new chat must either be logged in via `resume` or rely on explicitly named source-of-truth files.
- Do not stretch the restart-packet: it should be shorter than the usual recap.
