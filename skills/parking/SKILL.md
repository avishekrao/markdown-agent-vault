---
name: parking
description: >
Parking the current work context to safely switch to another task.
The agent analyzes the course of the conversation, determines the project and task, classifies the type of interruption.
records the stop frame in the log.md of the project, updates plan.md (if a blocker appears or a vector changes),
and then fixes the state in the correct layer: plan.md §Blockers, tasks.md or
delegations/depending on the type of pause.
After that, you can safely switch or close the chat - the return point is saved.
Be sure to use this skill when the user says “park”, “park”, “park”, “park”.
“Stop-frame”, “park”, “parking”, “save the point of return”, “fix where we are”.
Use proactively if you see the user switching to another topic.
Without explicit parking, say, "Stop a frame before you switch?"
---

# Parking context

You execute the parking protocol – record the current state of work so that any future session (or return in the same chat) can restore the context from the stop point.

## Why should I?

Switching context costs ~23 minutes to restore focus (Ophir & Nass research). Without a clear point of return, the original task is lost — especially when the context box is clogged with new material. Parking solves this problem: it creates a formalized breadcrumb that survives both this chat and the next one.

## Task routing model

Parking works within the task-routing model (see [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md) and [Rules 10–14 AGENTS.md](../../AGENTS.md)]). Key invariants:

- `plan.md` (Goal, Milestones, **Blockers, Drift Guard, Contingency) Parking **required** changes `plan.md §Blockers` if the interrupt type is BLOCKED or DELEGATED with milestone-impact. Blockers are the first-class essence of the plan, not the `tasks.md` section. See [§5.4 of the methodology ](../../03_knowledge/task-routing-methodology-2026-04.md).
- `tasks.md` - **execution queue**. The `PAUSED` marker only comes here if it is the NEED INFO step of the current milestone. Thinking ("you have to deal with X") goes to `plan.md` as an open question under the milestone, not in `tasks.md`. Section `Blocked` in `tasks.md` **net** - she moved to `plan.md §Blockers`.
- `01_now/ops/<contour>/delegations/<slug>.md` – If the parking happened because the task was delegated to the employee, the marker goes here. If blocking a milestone, **parallel** recording in `plan.md §Blockers` with `Type: delegated-work`.
- `01_now/personal/tasks.md` is a personal external obligation of the owner. Parking doesn’t generate personal strings — it’s a routing event, not a type of interruption.
- `00_inbox/` is only for a “random idea” that has no design or home outline. Again, not parking, but routing.

** S SPAWNED is a categorical error.** The appearance of a new idea while working on the main task is not an interrupt type, but a routing event**: the idea goes to its target file (`plan.md` of another project, `personal/tasks.md`, `00_inbox/`, `delegations/`), and work continues without parking. In PAUSED types, this marker no longer exists.

## Protocol (strictly follow steps)

### Step 1. Define project and task from the context of the conversation

Analyze the current chat and determine:
- **Project: Which `01_now/projects/` project does the work relate to? If it does not apply to any of them, specify “outside the project” and select destination by type (see Step 4): personal → `01_now/personal/tasks.md`, curiosity → `00_inbox/`.
- **Task **: what exactly was done (not “working on the project”, but “completed 3 out of 5 points of unit economics analysis”).
- **Stop point: what exactly was interrupted - as specific as possible.
- Does the interruption affect the vector of the project? ** If yes, step 3 updates `plan.md`, not just `log.md`.

### Step 2. Classify type of interruption

Determine the type automatically from the context of the conversation. Do not ask the user if the type is obvious.

| Marker | Type | When to use | Return Trigger |
|--------|-----|-------------------|------------------|
| `⏸️ BLOCKED` | Waiting for an external event/result from another project/client response/delayline | The ball is not in the user's hands and **no action to approximate the result, he has**. It includes cross-project dependency and external-event. | Response received / deadline passed / fallback worked |
| `🔀 DELEGATED` | Handed over to an employee | The task in the work of the delegate, SoT is a tracker or `delegations/<slug>.md` | The result is ready, you need to check |
| `🔍 NEED_INFO` | You need to find/study | ** The owner has an action** that will approximate the result (read, ask, try) - this is a tactical execution step, not a blocker | Information found and structured |
| `⏹️ STOPPED` | Just stopped | End of session, no specific blocker | Next session on this project |

**BLOCKED vs NEED INFO disambiguation rule:** If the type is not obvious, ask one short question: “Do you have an action that will bring the result closer, or are you just waiting?” There's an action - NEED INFO. No action. BLOCKED.

The new idea/task is not parked, but routed to its target file without interrupting the main work (see § "Task Routing Model" above).

### Step 3. `plan.md` is the first-class layer

This is the first layer of the record. The order "slow-protocol.md §5](../../meta/rules/write-protocol.md)" means that `plan.md` always updates before `log.md`, `tasks.md`, `delegations/`.

By type of interruption:

| Type | What is written in `plan.md` |
|---|---|
| mi️ BLOCKED | **New card in `# Blockers`** (`Bx`, with fields: Open, Type, Wait, Lock, My Action, Return Condition, Fallback, Stale check + status of each affected milestone changes to `blocked on Bx` |)
|   DELEGATED without milestone-impact | `plan.md` does not change - it is recorded only in `delegations/<slug>.md` |
| DELEGATED with milestone-impact (blocks milestone) | **New card in `# Blockers`** with `Type: delegated-work`, parallel to entry in `delegations/<slug>.md` |
| NEED INFO tactical | `plan.md` does not change - line goes to `tasks.md §Next` |
| NEED INFO strategic (changes vector) | Editing in `§Milestones` or `§Drift Guard` is not a blocker, but a change in plan |
|  ️ STOPPED | `plan.md` is unchanged - entry only in `log.md` |

If the initial approach turned out to be a dead end, the scope changed, the milestone lost its meaning - it is always an edit of `plan.md` in `§Milestones` / `§Drift Guard` / `§Contingency`, not a blocker.

### Step 4. Record a stop frame in the `log.md` project

Open `01_now/projects/<project>/log.md` and add the entry in the format:

```
- YYYY-MM-DD: <MARKER> PAUSED | Task: <what did>.
  I stopped at: <specific point>.
  Reason: "Why do we switch?"
  Action: "What is done to unlock - to whom he wrote that he delegated, where he wrote the idea."
  Return when: "Return trigger".
```

A neutral example:
```
- 2026-03-07: BLOCKED PAUSED | Task: Recalculate the launch model.
  Stopped at: collected all the metrics except one input metric.
  The reason: there is no confirmed data from the responsible person.
  Action: Recorded delegation in the file responsible.
  Return when: I will receive the data or in 3 days.
```

For the `⏹️ STOPPED` type, the format is shorter:
```
- 2026-03-07: .️ STOPPED PAUSED | Task: <what was done>.
  I stopped at: <specific point>.
  The next step is “what to do when you return.”
```

### Step 5. Create/update the marker task in the target file

The choice of file depends on the type of interrupt:

| Type | Where is the marker going | Format |
|-----|------------------|--------|
| `⏸️ BLOCKED` | **`<project>/plan.md §Blockers`** — new Bx + `blocked on Bx` card on affected milestones | blocker card with all fields (see Step 3) |
| `🔀 DELEGATED` without milestone-impact | **Only** `01_now/ops/<contour>/delegations/<slug>.md` Active | `YYYY-MM-DD -> <essence> [tracker-link] - due: <date> - [context](rel-link)` |
| `🔀 DELEGATED` with milestone-impact | `delegations/<slug>.md` Active **+** `plan.md §Blockers` Bx (`Type: delegated-work`) with reference to the line in delegations | blocker card + lean-index string, bilaterally linked |
| `🔀 DELEGATED` without tracker | `delegations/<slug>.md` marked `tracker_sot: none` + `plan.md §Blockers` if blocks milestone | blocker card + lean-index without tracker-link |
| `🔍 NEED_INFO` tactical | `<project>/tasks.md §Next` | `- [] ► <collect X> → <what's after> (YYYY-MM-DD)` |
| `🔍 NEED_INFO` strategic | `<project>/plan.md §Milestones` or `§Drift Guard` | plan edit, not line marker |
| `⏹️ STOPPED` | `<project>/log.md` entry only (see Step 4). `tasks.md §Active` remains as it is | - |

**Convergence rule for delegated-work blockers:** if the employee stops blocking milestone (delegation is completed or no longer critical), the blocker is closed according to ritual §5.4.2 methodology - the card moves to `## Blockers — Resolved`, the milestone status is removed, the line in `delegations/<slug>.md` goes to `Done (7d)`.

A neutral example of a blocker card in `plan.md`:
```markdown
### B1 - Missing indicator from the responsible
- Open: 2026-03-07
- Type: delegated-work
- Waiting: a confirmed indicator to recalculate the model
- Block: M3
- My action: remind the person responsible in 3 days
- Condition of return: confirmed data received
- Fallback: Take a score from the latest report and mark as an approximation
- Stale check: 7 days
```

A neutral example of a parallel string in `delegations/responsible.md`:
```markdown
- [ ] 2026-03-07 → collect the missing indicator [TRACKER-123](url) • due: 2026-03-10 • link to `plan.md#b1`
```

### Step 6. Confirm the parking.

Respond to the user with one short message in the format:

> Parked. [Project X] — recorded a stop frame in log.md, a marker in [target file].
> (if applicable) plan.md is updated: [what has changed].
> Stopping point: [Short description].
> Return trigger: [condition].
> We can switch.

Example of delegation:
> Parked. 2026-example - log.md, delegation to ops/2026-example/delegations/responsible.md.
> Stopping point: collected all metrics except one metric.
> Return trigger: Responsible sends data or 2026-03-10.
> We can switch.

## Limiting the depth of switching

If the user is already in the first level of switching (moved from the main task A to service B) and wants to dive deeper (task C), block:

> “This is the second level of switching. Write the task [C] in tasks.md/inbox – let’s go back to it separately. Now we finish [B] or park and go back to [A].

Maximum permissible depth: 1 level.

## Long chat protocol

If the current chat has already had 2+ parking or the dialogue is clearly long and multi-theme – warn:

> “The chat became long. I recommend continuing in the new session - I will pick up the context from log.md when calling /resume.

## Proactive parking

If the user starts talking about another project / task without an explicit parking command, and there was meaningful work in the current chat - suggest:

> “I see we're switching. Do you want to make a stop frame of [the current task] so as not to lose the point of return?

Do not impose – if the user says “don’t” or switching trivial (a short question that does not require deep immersion) – skip.
