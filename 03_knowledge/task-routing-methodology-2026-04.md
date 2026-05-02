---
id: task-routing-methodology-2026-04
type: note
status: draft
created: 2026-04-14
updated: 2026-04-15
aliases:
  - "Model of task routing and meeting context"
  - "Task routing model for vault"
  - "Separation plan/tasks/delegations/personal"
tags: [knowledge, methodology, vault-rules, tasks, meeting-processing, personal-ops, delegation]
source_path: "03_knowledge/task-routing-methodology-2026-04.md"
freshness: evergreen
knowledge_criticality: high
verification_status: draft
verified_by_me: false
curation_mode: owner-review
---

# Model of task routing and meeting context

## Essence

The document captures the target model for managing tasks, project plans, delegations, personal commitments, and the episodic context of meetings. The model replaced the previous approach, where `tasks.md` of the project accepted all four classes of entities at once and turned into a dump.

This file is **the source of truth of the methodology**. The rules in `meta/rules/` and the skill `meeting-processing` should be referenced here and not duplicate the reasoning.

---

## 1. The problem we are closing

The previous model stored four heterogeneous entities in one `tasks.md` project:
1. Execution steps of the agent according to the current milestone;2. Milestones and plan for achieving the goal;
3. Delegations to employees;
4. Personal external obligations of the owner mentioned at the meeting.

Consequences:
- A cross-section of “my tasks” and “delegate X’s tasks” is not possible without traversing all projects.
- The project plan is degrading: the strategic milestone is adjacent to the microtask, the vector is lost.
- `context.md` of the project becomes clogged with episodic facts from meetings - and ceases to be a stable invariant.
- Skill `meeting-processing` has a one-dimensional model “scatter across tasks.md” and does not distinguish between owner/layer/lifespan.

## 2. Basic principle

> Each task class lives where its owner and lifespan are, not where it was first mentioned.

Hence all the private rules.

## 3. Five classes of entities and their places

| Class | Description | Storage location |
|---|---|---|
| **Execution step of agent** | What is the agent doing in the current session within the project | `01_now/projects/<project>/tasks.md` |
| **Milestone project** | Sustainable plan step with acceptance criteria | `01_now/projects/<project>/plan.md` |
| **Delegation** | Task where the performer is not the owner | `01_now/ops/<contour>/delegations/<person-slug>.md` |
| **Personal External Commitment** | What the owner is obliged to do personally, without project reference | `01_now/personal/tasks.md` || **Anecdotal fact from the meeting** | Mentioned in passing, may come up later | `<project>/materials/<contour>/meetings/YYYY-MM-DD theme. md`, section `## Mentioned in passing`, under the topic hashtag |

Any stable invariant (term, metric, source of truth) is a separate class, it goes to `context.md` of the project and does not participate in this model.

## 4. Decision tree of the agent when routing a line from a meeting

The agent asks **one** question before recording each line: “will this line survive this project?”

```
Will the line survive this project?
├── No
│ ├── Is this the agent’s step at the current milestone? → <project>/tasks.md (Active/Next)
│ └── Is this an episodic fact? → meetings/YYYY-MM-DD.md, ## Mentioned in passing, #tag
└── Yes
    ├── Is the contractor the owner of the vault?
    │ ├── Part of the project goal? → <project>/plan.md as milestone
    │ └── External commitment (not a project)? → 01_now/personal/tasks.md, Hard
    ├── Is the performer an employee of the circuit? → 01_now/ops/<contour>/delegations/<person>.md
    └── Is this a stable invariant (term, metric, SoT)? → <project>/context.md
```

If the answer is ambiguous, the agent asks the owner and does not guess (Rule 6).

## 5. Project file structure (operational mode)

```
01_now/projects/<project>/├── README.md – navigation
├── context.md — STABLE invariants: terms, metrics, source of truth
├── plan.md - HARD skeleton: Goal, Non-goals, Appetite, Milestones, Blockers, Blockers - Resolved, Drift Guard, Contingency
├── tasks.md - SHORT: Active step, Exit criteria, Next. Only about execution, not about thinking.
├── log.md - chronology of events (Rule 5)
└── materials/<contour>/meetings/YYYY-MM-DD_topic.md - summary of meetings, episodes under hashtags
```

### 5.1. `plan.md` - project contract

```markdown
# Plan: <project>

##Goal
<one sentence, observable result>

## Non-goals
<what we do NOT do in this project - protection against scope creep>

## Appetite
<how much attention/time I am willing to invest, how long it will take to rethink>
Example: “an hour a day for 2 weeks, after that - the decision to continue or close.”

## Source of truth
- Context: ./context.md
- Chronology: ./log.md
- Current step: ./tasks.md

## Milestones

### M1. <name>
- What: <description>
- Acceptance: <observed completion criterion>
- Status: not-started | in-progress | done | blocked on Bx

### M2. ...

##BlockersEach active blocker is a separate record, which is referenced by milestones via `blocked on Bx`. An empty section is the normal state.

### B1 — <blocker short name>
- Opened: YYYY-MM-DD
- Type: cross-project dependency | delegated-work | external-event
- We are waiting: <what exactly needs to happen for the block to be removed>
- Blocks: M2, M3 (list of milestones, cascade)
- My action: passive | active-nudge | switch-to-fallback-at-YYYY-MM-DD
- Return condition: <how will I understand that the blocker has been removed>
- Fallback: <what we do if the blocker is not removed by the deadline>
- Stale check: <after how many days to consider the blocker obsolete and raise an issue>

## Blockers - Resolved

Log of removed blockers. Lives until review or forced rewrite, then collapses. Not a log.md chronicle, but a short summary of “what got in the way and how it went wrong” so as not to forget the pattern.

### B0 - <name> (resolved YYYY-MM-DD)
- Was: <one-line description>
- Divided via: <which made the block irrelevant>

## Drift Guard
If the agent wants to change the approach, scope or order of milestones:
1. Update this file (what changes and why).
2. Write the reason in log.md (one line).
3. Only then start working on a new plan.

##Contingency<plan B at the level of the entire project: what to do if the main path is blocked>
```

Borrowed from Shape Up (pitch): `Appetite` = appetite, `Non-goals` = no-gos, `Drift Guard` = rabbit holes, `Milestones` + `Goal` = solution. `Contingency` - ​​one section for the entire project, not under each milestone (validation 2026-04-15).

`plan.md` is a slow file. Changes when the goal, appetite or milestone changes.

### 5.2. `tasks.md` - short execution queue

```markdown
# Tasks: <project>

## Mode
operational | development

## Active step
<one sentence: what is the agent doing right now>

## Exit criteria
- <observed termination condition>

##Next
- <1-3 points, which is immediately after active>
```

**Content Rule:** `tasks.md` contains only lines about **execution**, not about thinking. If the line answers the question “what is not clear?”, “where to go?”, “which path to choose?” — its place in `plan.md` (as a milestone or as an open question under a milestone). If the line answers “what to do now?” - at `tasks.md`. There is no `## Blocked` section in `tasks.md` - blockers live in `plan.md §Blockers` as a first-class entity (see §5.4).A bloated `tasks.md` is always a symptom of thinking getting in there. This is easier to diagnose than counting lines.

### 5.3. Mode `development`

For code projects `tasks.md` is maintained in the `development` (`Current Milestone / Active Step / Exit Criteria / Drift Guard`) mode, `plan.md` is still required and contains a strategic skeleton. Rule 10 from AGENTS.md remains in force, but now the plans/tasks are physically separated.

### 5.4. Blockers as the first-class essence of the plan

A blocker is not a line in `tasks.md` or an entry in `log.md`. This is a **first-class plan entity** living in the `plan.md` section of the `## Blockers` section, referenced by milestones via the `blocked on Bx` status field. Until 2026-04, blockers lived in `tasks.md` as section `## Blocked` - this turned out to be a mistake: they lost contact with the milestone they were blocking and did not survive the rotation of the fast file.

**Why a separate section, and not Contingency.** Contingency is Plan B at the level of the entire project (“if the appetite is exhausted, we close”). A blocker is a specific blockage at a specific step, with a name, deadline, expected event and a cascade of influence on other milestones. These are different scales, they should not interfere.**Why not log.md.** `log.md` - chronology. It answers the question “what happened.” `plan.md §Blockers` answers the question “what is stopping you now and where is it in the project map.” The entry about the appearance of a blocker goes both ways, but the source of truth for the state is `plan.md`.

**Two-way links.** Each blocker knows what it is blocking (field `Block: M2, M3`). Each milestone knows that it is blocked (status `blocked on Bx`). This makes the cascades explicit: if B1 blocks M2, and M3 depends on the outputs of M2, M3 also receives `blocked on B1`, and this is immediately visible in plan.md.

**Cross-project dependencies - one-way only.** If project A is waiting for a result from project B, the blocker is written only to `plan.md` of project A (waiter). Project B (parent) does not know about waiters - otherwise the parent plan begins to bloat with service information. The agent detects cascade when touching the parent project via grep: `rg "B-contour.*cross-project" 01 now/projects/*/plan. md`.

#### 5.4.1. Types of blockers

| Type | When | Action Source |
|---|---|---|
| **cross-project dependency** | I'm waiting for the result from another vault project | Passive - will rise when you touch the parent project || **delegated-work** | Delegation on an employee, the result is needed for a milestone | In parallel - write to `delegations/<slug>.md`, to `plan.md §Blockers` - only if removing the block is critical for the milestone |
| **external-event** | Waiting for an external event (client response, date, government agency response) | Active nudge by `My action.` or passive until date |
The type is fixed in the blocker card, affects the nudge ritual and where else the line will be written.

`need-info` **is not a blocker type**. If the owner has an action that brings the result closer, this is not a wait-state:
- tactical `need-info` → `tasks.md`;
- strategic `need-info` → edit `plan.md` (`Milestones` / `Drift Guard`), but not card `Bx`.

#### 5.4.2. Blocker Resolution Ritual

The order of steps is rigid (slow layers are ahead of fast ones - [write-protocol.md §5](../meta/rules/write-protocol.md)):

1. Move the card from `## Blockers` to `## Blockers — Resolved` (in plan.md), reduce it to two lines: “Was / Sent through.”
2. Update the status of each milestone from the `Blocking.` field: `blocked on Bx` → `in-progress` or `not-started` (which is true based on the actual status).
3. If there was a linked `delegations/<slug>.md' item, move it to `Done (7d)' of the same file. 4. One line in `log.md': `YYYYY-MM-DD: I am RESOLVED Bx | <name> → <what unlocked >>'.
5. `tasks.md` **does not touch** - if the block has diverged, the agent will set the next execution step to Active with normal mid-flight sync.

The reverse order (tasks.md first) is not allowed: it leaves plan.md with outdated `blocked on Bx` and creates drift between the fast and slow layers.

#### 5.4.3. Stale check like bootstrap-scan

Instead of weekly review, blockers are checked each time a project is opened** (bootstrap) using the trigger “how many days has it been hanging”. This is not a separate ritual, but part of the normal `plan.md` reading at the beginning of the session.

Thresholds:
- **>30 days, type `external-event`:** is normal, but the agent shows the owner: “B1 has been hanging for 34 days, we are waiting for a client - should we kick or change the fallback?”
- **>30 days, type `delegated-work`:** the agent pulls up `delegations/<slug>.md` and shows the status of the associated line; if there is no movement in the tracker either, it suggests changing the fallback.
- **>60 days, any type:** shown as stale - the agent asks if it’s time to transfer to Resolved (via fallback) or close the milestone.
- **>90 days, any type:** requires a **decision** - either remove the block, or accept it as a permanent restriction and redo the plan (milestone goes to Contingency or Non-goals).The `Stale check` field in the blocker card overrides the default thresholds if they are not suitable for a particular blocker (for example, “check through 14d - fast cycle”).

#### 5.4.4. What is NOT a blocker

- **⏹️ STOPPED “the day has ended.”** Not a blocker, but a simple pause - only goes to `log.md`.
- **Step into `Next` with low priority.** Not a blocker, just not right now.
- **“We need to think.”** Not a blocker - this is an open question under milestone, edit `plan.md` to `Milestones` or `Drift Guard`.
- **💡 SPAWNED from the legacy model.** Category error: the emergence of a new idea is not a type of interruption, but a **routing event**. The idea goes to its target file (`plan.md` another project, `personal/tasks.md`, `00_inbox/`, `delegations/`), and the current task continues without parking.

## 6. Delegations

### 6.1. Place

```
01_now/ops/<contour>/delegations/<person-slug>.md
```

Contour separation: The delegate of one product and the delegate of another product do not mix. The person's card in `03_knowledge/contacts-network/persons/<person>/` remains a description of the person; The delegation file is a working registry and has a different life cycle.

### 6.2. PrincipleExternal contour task tracker - **source of truth** of the task. The file in vault is **lean index**: one line per task, only a link to the tracker, essence, dates, source.

### 6.3. String format

```markdown
- [ ] 2026-04-12 → update report template [TRACKER-1423](url) • due: 2026-04-20 • link to meeting file
```

Fields: status, date of delegation (= date of meeting), essence in one phrase, link to tracker, `due:` date of promise (optional), link to source meeting.

### 6.4. File Sections

```
## Active - in progress
## Done (7d) - closed in the last week
## Archive - everything older than 7 days done
```

Three sections, not five. `Waiting` and `Overdue` are expressed through the `due:` field and grep (`rg "due: 2026-0[1-3]"` - find overdue ones). Fewer sections means less chance that the structure will fall apart when the weekly review is inactive (validation 2026-04-15: the five-level structure is redundant).

`Archive` growing, but rarely read. ~100 lines per year is normal.

### 6.5. Live-first audit

The agent updates the task status only based on live observation in the tracker (live-first audit rule). The status is not stored outside the tracker, it is only duplicated for a quick snapshot.

### 6.6. Passive recall when a delegate is mentionedWeekly review is a ritual that the owner does not have (flow-worker profile). Instead - **passive recall**: when the delegate's name comes up in a fresh context (meeting, chat, debriefing), the agent automatically checks it `delegations/<slug>.md` and shows open lines.

Passive recall triggers:
- Skill `meeting-processing` sees the meeting participant → grep `delegations/` all circuits of this participant → show open.
- Any request containing the delegate name → the same grep.
- Opening a project in which a delegate is mentioned → agent with bootstrap shows its open delegations outline.

This replaces “I don’t remember what I delegated six months ago.” Not perfect, but it works without weekly reviews.

## 7. Personal tasks

### 7.1. Place

```
01_now/personal/tasks.md
```

One file. Two sections. No additional files for ideas/wants.

### 7.2. What hits

Only **external obligations to the world**: deadlines, documents, payments, bureaucracy, visits to specialists. Normal volume is 5–15 records.

### 7.3. What never hits

- Ideas and curiosity (“read about X”) → `00_inbox/` or `03_knowledge/`.
- Project work (“write draft letters”) → to the project.- Desires (“I want to do Y”) → are not recorded. If you want it, it will be done.

Principle: an entry in this file is defined through “have to”, and not through “want”.

### 7.4. Format

```markdown
---
mode: personal-hard-only
rule: only external obligations, no desires
last_rewrite: 2026-04-15
next_rewrite_hint: 2026-05-15
---

#PersonalTasks

Last rewritten: 2026-04-15

## Hard (external obligations)
- [ ] 2026-04-10 → extend the document until 2026-06-01
- [ ] 2026-04-14 → submit reports before 2026-04-30

## Maybe (reminders, can be deleted)
- [ ] 2026-04-08 → check new filters in mail

## Done (last 7 days)
- [x] 2026-04-09 → make an appointment with the dentist
```

The `last_rewrite` field is a visual marker that the file was recently “sieved” and not forgotten (borrowing from the Newport shutdown ritual, validation 2026-04-15). If `last_rewrite` is older than a month, the file is considered stale and the contents cannot be trusted without viewing.

### 7.5. Governance by forced rewrite

Instead of TTL timers - **forced rewrite once a month**. By trigger (`/personal rewrite` or the first ambient mention after the month has expired), the agent:
1. Reads the entire file out loud to the owner - section by section.2. For each line - one question: “relevant?” → keep / delete / move.
3. Writes a fresh file. `Done` is completely cleared. `Maybe`, which did not migrate to `Hard`, is deleted.
4. Updates `last_rewrite` in frontmatter and header.
5. One line in `04_logs/personal.log`.

Principle: the file does not accumulate dust, but is regularly rewritten from scratch based on what else is ringing. This is closer to the Newport practice of “small lists that are regularly erased” than rigid TTLs for each entry.

If the month has not passed, but the file has grown (>20 records in Hard), this is also a rewrite trigger.

### 7.6. Reading discipline

The file is **not read on a daily basis**. Only upon explicit request (“what’s hanging around me?”). If you start watching every morning, the file will turn into another TickTick and fail. This is a conscious design decision, not an oversight.

### 7.7. Ambient capture

When the owner casually mentions an obligation in the dialogue, the agent adds a line without MR-diff and without confirmation. The line is light, deleted by TTL, the risk of collisions is minimal. If the mention is ambiguous (“maybe we need X”), the agent clarifies with one question.

## 8. Anecdotal facts from meetings

### 8.1. ProblemAt meetings, facts are mentioned in passing that seem like noise at the time of the meeting, but become important a month later. You cannot put them in `context.md` of the project - it will cease to be invariant. You can't lose.

### 8.2. Solution: hashtag RAG in the meeting summary

The following section is added to the meeting summary file (`materials/<contour>/meetings/YYYY-MM-DD theme. md`):

```markdown
## Mentioned in passing
- #onboarding: Tanya said that they had a failure with video guides in 2025
- #pricing: Dima mentioned the desire to revise the scale tariff
- #hiring: there was a question about Casanova, it was hushed up
```

When bootstrapping a project, the agent, if the request contains the subject `X`, does:

```bash
grep -rh "#<X>" 01_now/projects/*/materials/**/meetings/
```

and pulls up the found fragments as additional context. Full-text search of ~100 summaries per year - milliseconds.

### 8.3. Canonical tag registry

Tag collisions (`#onboarding` vs `#activation`, `#hiring` vs `#recruiting`) are a known PKM pain point. Solution: **canonical registry in `meta/TAGS.md`**, section `## Task routing tags`.

Rules:
- Skill `meeting-processing` when writing `## Mentioned in passing` uses **only canonical tags** from the registry.
- If a new tag is needed, the skill adds it to the registry with one line of definition, then uses it.- Synonyms are not created - the first name assigned remains canonical.
- In case of a conflict (old file with `#activation`, registry knows only `#onboarding`) - the agent either asks or, when touching the old meeting, converts the tag to canonical.

### 8.4. When an episodic rises to invariance

The primary trigger is the **opinion statement**, not the counter. When an agent or owner formulates a conclusion on a topic (“we know about X that he is Y”), this is the moment when the fact is ready to move into `context.md` the project as a stable invariant.

Three mentions in different meetings is a heuristic so as not to miss the moment. When it is triggered, the agent **does not automatically transfer**, but says: “topic #X was mentioned in 3 meetings, are you ready to formulate an opinion about it?” If yes, go to `context.md`. If not, it remains episodic until the next accumulation.

Borrowing from Evergreen notes (Andy Matuschak): Evergreen lives where there is a strong opinion or strong fact, but not a simple unstated fact.

### 8.5. What it does NOT do

- Does not replace semantic search / embeddings - it is not needed for hundreds of files.
- Does not require infrastructure - only grep and convention for hashtags.- Does not store a copy of the fact in several places - the fact lives only in the summary.

## 9. Routing contract for skill `meeting-processing`

The skill replaces the current one-dimensional layout with this routing:

| Layer from meeting | Where does it go |
|---|---|
| Project solution | `log.md` project, 1 line |
| Stable invariant | `context.md` project, only if the self-check “survives 5 meetings” passes |
| Strategic fork/direction decision | `plan.md`, Milestones or Contingency |
| Action item of the agent for the current milestone | `tasks.md` project, Next |
| My non-project commitment | `01_now/personal/tasks.md`, Hard |
| Delegation | `01_now/ops/<contour>/delegations/<person>.md`, Active |
| Episodic fact | summary of the meeting, `## Mentioned in passing`, with the hashtag |
| Fact about people and participation | `interactions.csv` (as now) |

Before each line, the skill must launch the decision tree from §4.

## 10. Migration of existing projects

Previous `tasks.md` projects contain a mixture of all classes. Migration is not automatic, it is done the first time you touch the project:

1. The next time the agent opens the project, it reads the current `tasks.md`.
2. Runs decision tree §4 on each line.3. Shows the owner MR-diff: “this → plan.md”, “this → personal/tasks.md”, “this → delegations/<person>.md”, “this → remains in tasks.md”.
4. After confirmation, transfers and creates `plan.md`.
5. Writes one line to `log.md` of the project: “migration to a new routing model via `task-routing-methodology-2026-04.md`”.

Mass migration of all active projects in one fell swoop is prohibited - new models must be tested on 1-2 projects before rolling out.

## 11. What this document does NOT address

- Weekly review ritual. A separate question is how and when the owner looks at the summary of all four files.
- Integration with external task trackers. Now - a manual link in the delegation file, automation as a separate task.
- Governance for `backlog` project. For now, we believe that the backlog can remain in `plan.md` as a separate section.
- Migration of old meeting summaries to the new section `## Mentioned in passing` with hashtags. Applies only to new meetings from the moment the methodology is adopted.

## 12. Related documents

- [AGENTS.md](../AGENTS.md) - global rules, where Rules 11–14 are added.
- [write-protocol.md](../meta/rules/write-protocol.md) - file writing protocol.- [Rule 5: log.md - chronology, not storage](../AGENTS.md) - the same spirit of separating layers.
- [Rule 10: tasks.md - execution contract](../AGENTS.md) - extended by this methodology.
- [meeting-processing/SKILL.md](../skills/meeting-processing/SKILL.md) - the main consumer of the methodology, rewritten under §9.
- [owner-only-agent-dev-standard-2026-03.md](./ai/owner-only-agent-dev-standard-2026-03.md) - the basic ask/plan on which `plan.md` is based.
- [general-rules-for-agentic-development-in-local-vault-2026-03.md](./ai/general-rules-for-agentic-development-in-local-vault-2026-03.md) - the policy/memory/execution separation requirement on which the separation of `plan.md` and `tasks.md` is based.
- [meta/context.md](../meta/context.md) - owner profile (flow-worker, not driven-by-list), justifies §7 and §7.6.

## 13. Status

**Draft, post-validation.** The methodology passed external validation on 2026-04-15 (Shape Up, Newport, Ask a Manager/GTD, Obsidian PKM practice) and 8 inline edits were applied: Appetite in plan.md, Contingency moved to the top, quality rule for tasks.md instead of 20 lines, delegations sections collapsed to three, passive recall instead of weekly review, forced rewrite instead of TTL, last_rewrite ritual, canonical tag registry.The next step is storage rules and skills (Stage 1 of migration). Until Stage 2 is completed, the methodology is considered active for the rule-layer, but is not applied to live projects.

## Next step

1. Stage 1: AGENTS.md (Rules 11–14) + `meta/rules/task-routing.md` + patches of existing rules + README sections.
2. Stage 2: templates in `meta/templates/` + skill census `meeting-processing` + patches for 7 other skills.
3. Stage 3: pilot to `2026-click-ru-master-redesign`.
4. Stage 4: rolling out to other projects.