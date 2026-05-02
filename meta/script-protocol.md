---
id: script-protocol
type: process
status: active
created: 2026-03-10
updated: 2026-03-22
tags: [process, scripts, mandatory-rule]
priority: critical
---

# Protocol for Creating and Using Scripts

## Status: Effective from 2026-03-10

## BEFORE coding

1. ** Explain what the script does - 3-5 sentences, no code. Entrance, output, what files read / write.
2. *Name the limitations when the method can give the wrong result. Example: “YAML regex parsing will break on multiline values.”
3. ** Offer options** – if there is more than one approach, briefly describe each with pros/cons.
4. **Wait for confirmation.** The code is only after yes.

## Before launch

1. `--dry-run` (if supported) - show what will change.
2. Backup of affected files.

## Additional for Agentic Scripts

If the script:
- starts in the `plan -> run -> test -> retry` cycle,
- used by an AI agent for autonomous operation,
- Or manage a multi-step agent scenario,

The usual `stdout/stderr` is not enough. It must have an **agent-readable logging contract.

### Minimum logging contract

The log shall, where possible, contain:
- `run_id`
- `step_id`
- `file_or_module`
- `function_id`
- `block_id`
- `belief_state` - which hypothesis the agent now believes is correct
- `observed_result` – What really happened
- `next_action` – What the Agent Is Going to Do Next

### Mandatory properties of agent-readable logs

1. **Log-to-code correlation**  
   The same function/block identifiers must be repeated in logs and code so that the agent can glue the code and log into a single context.

2. **Structured format over prose**  
   Structural fields, tags, or repeatable anchor tokens are preferred over free text without markup.

3. **Belief-state logging**  
   The agent must record not only the error, but also its current hypothesis about the cause and mechanics of the failure.

4. **Anti-loop protection**  
   For repeated failures, there should be a retry limit, an explicit stop or change of strategy. Infinite retry without stop protocol is prohibited.

5. **Forced context on repeated failure**  
   If the script falls again, the agent should be given a summary of past failed attempts or a known-fix context, not just the bare error of the current run.

## After launch

1. Show the result: how many files are created / modified / deleted, errors.
2. Write to `scripts/runs.log`:

```
YYYY-MM-DD HH:MM | script name.py | parameters
  Result: N created, M modified, K errors
  Beckup: the way
  Pushback: team for pullback
```

## Log of application

The `scripts/runs.log` file is a mandatory log of all launches. Without logging, running a script that changes data is prohibited.

For agentic scripts, `runs.log` does not replace runtime logs, but only supplements them as a startup fact log.
