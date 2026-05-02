---
name: resume
description: >
Restoring the context of a parked task to continue working.
The agent scans plan.md §Blockers, log.md and delegations/files of active projects.
finds active blockers, PAUSED records and open delegation, shows the user
a list of parked tasks with types and triggers, and after selection loads the full context
Project (plan → context → tasks → log)
Be sure to use this skill when the user says “resume”, “continue”.
"Go back to," "what I parked," "where I stayed," "what hung,"
"Parking list," "show me the parking lot," "what I forgot."
Also use at the beginning of a new session if the user asks “what did we do?”
or "what I worked on."
---

# Restoring Parked Context

You execute the return protocol – find all the tasks parked, show the user, and after choosing, upload the full context of the project to continue working.

## Why should I?

Each task parked is an incomplete work context that has been worked on. Without an explicit recovery protocol, these points are lost: the user forgets what was parked, or spends time re-immersing. Resume makes returns cheap – the agent pulls up the context and reminds you where you left off.

## Task routing model

Resume works within the task-routing model (see [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md) and [Rules 10–14 AGENTS.md](../../AGENTS.md)]). It means:

- The parked state of the project may lie in **five different locations**, in order of priority reading:
  1. **`<project>/plan.md §Blockers`* are first-class blockers of the project (BLOCKED, DELEGATED-with-milestone-impact). The main source is “what does not allow you to move”. Reading first.
  2. `<project>/tasks.md` – Project steps with interrupt markers (NEED INFO, STOPPPED Active-step)
  3. `<project>/log.md` – PAUSED/RESUMED recordings without active blockers (STOPPED)
  4. `01_now/ops/<contour>/delegations/<person-slug>.md` - open delegation to employees, you can pull the status from the `due:` field
  5. `01_now/personal/tasks.md` - personal obligations of the owner (not through the parking lot, but can surface by passive recall)
- When restoring the context of the project, the order of reading service files: **README → plan (including §Blockers) → context → tasks → log** (slow layers outpace the fast ones, as in [write-protocol.md §5](../../meta/rules/write-protocol.md)).
- For each employee mentioned in the parking lot - **passive recall** according to the corresponding `delegations/<slug>.md`: what else hangs on it, whether there are related blockers.
- **Marker and SPAWNED no longer search** - the new idea is not parked, it is immediately routed to its target file without interruption (see [§5.4.4 of the methodology](../../03_knowledge/task-routing-methodology-2026-04.md)].

## Protocol (strictly follow steps)

### Step 1. Find all the parked tasks

Read `01_now/README.md` for a list of active projects. Then, for each project, collect four classes of parked state in order of priority:

Class A – Active blockers (main source) ** For each project, read `<project>/plan.md §Blockers`. Each `Bx` card is an active blocker. Calculate the age from the `Open:` field to the current date - it will be useful in Step 4 for stale check. These blockers are the main reason why the work on the project is worth it, and the first thing to show the owner.

**Class B - PAUSED in log.md.** Read `<project>/log.md` and find the notes with the markers:
- `⏸️ BLOCKED PAUSED`
- `🔀 DELEGATED PAUSED`
- `🔍 NEED_INFO PAUSED`
- `⏹️ STOPPED PAUSED`

A record is considered **active** if there is no corresponding `▶️ RESUMED` or `✅ RESOLVED Bx` in the same log.md (for BLOCKED/DELEGATED). **Not looking for the `💡 SPAWNED PAUSED`* – this marker is not in the new model.

**Class C - NEED INFO in tasks.md.** Read `<project>/tasks.md §Next` and find tasks with the `🔍` marker - these are the tactical steps of collecting information that the owner left behind (not a blocker, but a delayed action).

**Class D - Open delegation.** Read `01_now/ops/<contour>/delegations/*.md` section `## Active`. Special attention: the lines with the past `due:` is a parking lot that is rotten.

In addition, when bootstrap project automatically check `01_now/personal/tasks.md §Hard` for the obligations mentioned in the context of parking - this is a passive recall, not a separate class.

All four classes give one summary picture of the parked condition.

### Step 2. Show the list to the user

Find the parking lots in a compact table:

```
Parked tasks:

1. ⏸️ [2026-03-07] example-project - model of new tariffs
   We are waiting: the answer from @Ivanov at cost

2. - [2026-03-05] Personal-content - content plan for the channel
   Delegated: @Petrova, expect draft

3. ⏹️ [2026-03-06] travel-planning - accommodation booking
   Next Next post: Compare 3 Options by Price

What's going on?
```

If there's no parking, say, "No active parking." All PAUSED log entries have the corresponding RESUMED.

If the user has already specified a specific project or task in his query (for example, “resume click-ru” or “continue with the unit economy”) – do not show the full list, but immediately proceed to step 3 for this task.

### Step 3. Download the project context

Once the user has selected the task (or you have identified it from the query), upload the context in the order of **slow layers → fast** (as in [write-protocol.md §5](../../meta/rules/write-protocol.md)):

1. `01_now/projects/<project>/README.md` - what/why/borders
2. `01_now/projects/<project>/plan.md` is a slow project contract: Goal, Non-goals, Milestones, **Blockers** (the first pass is to perform a stale check of each Bx card on the `Open:` field and default thresholds from §5.4.3 of the methodology), **Blockers – Resolved**, Drift Guard, Contingency. This is the first thing to read after README: without understanding the plan and current blockers, you can’t make out steps in tasks. md
3. `01_now/projects/<project>/context.md` - stable invariants: terms, metrics, SoT, stakeholders
4. `01_now/projects/<project>/tasks.md` - Execution queue with interrupt markers
5. `01_now/projects/<project>/log.md`: The last 5-10 entries to understand chronology
6. For each employee mentioned in the parking lot, **passive recall** `01_now/ops/<contour>/delegations/<person-slug>.md` section `## Active`. Show the user what else hangs on this person, so as not to lose adjacent blockers. For each blocker in `plan.md §Blockers` type `delegated-work` – make sure that the parallel line in delegations is still relevant.
7. If parking is a personal obligation - `01_now/personal/tasks.md` § Hard

If the active project does not have `plan.md` (legacy, not yet migrated), first create `plan.md` from the [project plan template](../../meta/templates/project_plan.md), transfer the goal and the current milestone from `README.md` / `tasks.md`, and only then continue resume. After the migration, add one line to `log.md`: "Created plan.md during resume modernization of the legacy project."

### Step 4. Restore context to the user

Briefly report:

> Uploaded the context of [project X].
> You stopped at: [a specific point from the PAUSED recording].
> The trigger for the return was: [condition]. [Status: Completed/Unfulfilled/Unknown—Clarify].
> Current milestone according to plan.md: [name + acceptance criteria].
> Related tasks in tasks.md: [if any].
> Open delegation to the persons mentioned: [if any, from delegations/].
> Keep going?

If the return trigger involved an external event (response from a person, delegation result) ask if it happened: “Response from @Ivanov received?”

If you read plan.md and find that the active milestone no longer corresponds to reality (drift) - highlight it separately: "plan.md says that we are in milestone M1, but log.md work is already in M2 - you need to update plan.md before continuing."

### Step 5. Write the return to log. md

After confirming the user, add a record:

```
- YYYY-MM-DD: ← RESUMED | Task: <original task>.
  The result of the pause: "what was received during the pause - the answer, the result of delegation, the information found; or "no changes">.
  Continue with: <specific point of renewal>.
```

## Review mode (without selecting a specific task)

If the user asks “what’s hanging” / “show all the parking lots” / “what I’ve forgotten” – only follow steps 1–2 (scan and show the list). Do not download the context of the project until the user has selected a specific task.

In the review mode **required** illumination (not optional):
- **Stale blockers in `plan.md §Blockers`** – if the card age exceeds `Stale check` or default thresholds (§5.4.3 of the methodology): >30d warn, >60d stale, >90d requires decision. For >90d: "B1 hangs for 94 days - do you need a solution: drop back, transfer to Contingency or close milestone?"
- PAUSED parking in log.md is older than 7 days - "This parking has been hanging for N days, it is worth checking or closing."
- Delegations with past `due:` - "In delegations/ivanov.md, the line from 2026-03-07 has due: 2026-03-10 - a delay of 35 days, you need to kick or remove."
- Parking with overdue return trigger - "The "kick in 3 days" trigger expired 2 days ago."

## Quick resume in the same chat

If `/resume` is called in the same chat where `/parking` was previously, you do not need to scan all projects. The agent remembers the context from this chat and can restore the point directly:

> Back to [task]. You stopped at [dot]. Keep going?
