---
id: context-window-signaling-new-dialog-handoff-2026-04
type: note
status: active
created: 2026-04-06
updated: 2026-04-06
aliases:
  - "Signal for the remainder of the context and transition to a new dialogue"
  - "CTX rule and handoff to fresh chat"
tags: [knowledge, research, ai, agents, prompts, context-management, workflow]
source_path: "03_knowledge/ai/context-window-signaling-and-new-dialog-handoff-2026-04.md"
freshness: seasonal
expires: 2026-10-06
research_type: decision
confidence: medium
---

# Signal the rest of the context and move to a new dialog

## Essence
For a global rule, it is better to use not an exact token count, but a very short heuristic tail `CTX~N%`. When there is a critical remainder, the agent should not “press out” a long answer in a dying chat: it is safer to suggest `new-dialog-handoff`, rely on `parking`/`resume` and continue in a fresh context from a durable source of truth.

## Details

### TL;DR
- Best tail format: one line, no explanation, with a rough percentage estimate.
- The exact remainder of the window in the chat interface is usually not available; even Anthropic’s token counting API is described as an estimate, not as an absolute truth.
- It’s better to set the threshold not by a “hard number of tokens”, but by predicting the following answer: if the next meaningful step probably won’t fit, the agent offers a handoff.
- Handoff should not be a free retelling of the chat. The source of truth should be in the files: `log.md`, `tasks.md`, `context.md`, research-note, spec.
- For project work, you need to reuse `parking`, and in the next chat enter via `resume`.
- A long control review is better done in a fresh context, and not in the same overgrown chat.

### What to show at the end of each message
Recommended global tail:

```text
CTX~65%
```

Critical option:

```text
CTX~10% -> new-dialog-handoff
```

Why so:
- short;
- stable;
- almost does not consume tokens;
- understandable to a person without decoding;
- does not pretend that the agent knows the exact token balance.

### Why you shouldn’t demand an accurate meter
Official APIs can count tokens and manage compaction/state, but this does not mean that the agent in the chat product sees the exact remainder of the window on each turn. Anthropic token counting is directly described as estimate. Therefore, it is safer to specify in a global rule:
- rough estimate;
- rounding to 5-10%;
- explicit predictive trigger for handoff;
- prohibition of issuing a number as an exact remainder.

### When to offer new dialogue
Working threshold:
- `CTX~15%` and below;
- or the agent sees that the next answer will be long: code, review, research, multi-file edit, long explanation.

Solution:
- do not continue the long deployment;
- suggest `new-dialog-handoff`;
- first fix the state in the durable source of truth;
- only then transfer the work to a new chat.

This is better than trying to “squeeze one more big answer” into an almost exhausted window: the quality of the answer decreases, and the risk of losing the thread of the conversation increases.

### Which handoff is considered good
Good handoff:
- relies on existing artifacts;
- does not duplicate `parking` and `resume`;
- gives the next starting prompt in a maximum of 4 points;
- indicates 1-3 canonical file path as source of truth;
- fixes exactly one next step.

Bad handoff:
- a long retelling of the entire session;
- new parallel memory instead of `log.md`/`tasks.md`/research-note;
- an attempt to keep critical context only in chat.### Recommended operating model for this vault
1. In `AGENTS.md`, attach the required tail `CTX~N%`.
2. For a critical forecast, suggest `new-dialog-handoff`.
3. `new-dialog-handoff` should:
   - for project work, first call the `parking` protocol;
   - for the next chat, rely on `resume`;
   - if you have a ready-made durable artifact, do not create parallel memory;
   - return a short restart-packet rather than a long recap.

### Recommended global rule text
```text
At the end of each message, add one line: `CTX~N%`.
`N` - rough heuristic estimate of the window remaining after the current response, rounded to 5-10%.
If, according to the forecast, the next meaningful answer may hit the limit, write instead of the usual tail:
`CTX~N% -> new-dialog-handoff`
and offer to switch to a fresh dialogue through this skill. Don't give out `N` as the exact token count.
```

### Why this is consistent with local rules
- [AGENTS.md](../../AGENTS.md) requires keeping global rules short and stable.
- [parking](../../skills/parking/SKILL.md) already records the return point and directly recommends a new chat if the conversation has become long.
- [resume](../../skills/resume/SKILL.md) already sets the return path to the parked task.
- [General rules of agentic development for local storage](./general-rules-for-agentic-development-in-local-vault-2026-03.md) directly say not to keep the entire context only in the chat and to separate implementation/review by fresh context.

### Blind spots and restrictions
- Threshold `15%` is heuristic, not mathematical.
- The exact behavior of the window differs between products; local rule should be product-agnostic.
- If the platform later has a real visible token meter, the rule should be simplified and transferred from heuristics to a real counter.

## Sources

### Local
- [AGENTS.md](../../AGENTS.md)
- [parking](../../skills/parking/SKILL.md)
- [resume](../../skills/resume/SKILL.md)
- [General rules for agentic development for local storage](./general-rules-for-agentic-development-in-local-vault-2026-03.md)

### Official external
- [OpenAI: Conversation state](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses) - state, context window and compaction for long conversations
- [Anthropic: Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) — rolling/FIFO behavior and accumulation of tokens in long chats
- [Anthropic: Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting) — token count as an estimate, not an absolute guarantee
- [Anthropic: Be clear, direct, and detailed](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct) - the shorter and clearer the operational rule, the higher the chance of stable execution
- [Anthropic: Long context prompting tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips) - the quality of long context depends on the structure and placement of sources

## Next step
If the rule shows itself to be stable in several long sessions, you can leave only the short tail in `AGENTS.md`, and keep detailed justifications in this note.