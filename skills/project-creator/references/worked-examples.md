# Worked Examples

Two end-to-end runs: one where the project emerges from the current conversation, and one where the owner asks for a project from scratch. The examples show the agent's decisions, not full file contents. Templates are in [starter-files.md](./starter-files.md); the plan example is in [plan-authoring.md](./plan-authoring.md).

## Example A. Project Extracted From the Current Conversation

**Situation.** The conversation discussed a demo product that sounds interchangeable with competitors. The owner considered several formulations, rejected "cheapest" as a weak differentiator, and mentioned an existing competitor overview. Then the owner says: "okay, let's capture this as a project".

**Step 1 - Extract context from the conversation without asking the owner:**

- Goal: get a positioning core that is distinguishable from competitors.
- Idea: the product currently sounds generic and needs meaningful differentiation.
- Decisions already made: "cheapest" was rejected as a positioning core.
- Boundaries: work on the core, not the landing page; initial market is local.
- Open question: product-wide positioning vs a specific segment was not explicit.
- Materials: previously collected competitor overview mentioned in the chat.
- Contour: demo-product, based on the product name.
- Reason for a separate project: this is a strategic decision, not a single task inside ongoing execution.

**Step 2 - Source-of-truth check:** this is an analysis and decision project, not a long-lived dataset or raw import. A project folder is appropriate.

**Step 3 - Is a question needed?** The only uncertainty is product-wide vs segment-specific positioning. Product-wide is a conservative assumption with low reversal cost. The agent does not ask. It records the assumption in `Intent Lock` and adds "stop and ask if a segment-specific fork appears".

**Step 4 - Year, slug, mode:** current year from `date +%Y`; slug `demo-product-positioning-strategy`; path `01_now/projects/YYYY-demo-product-positioning-strategy/`; task mode `operational`.

**Step 5 - Documentation:** the agent writes `plan.md` with a changed-state goal, Intent Lock, three milestones, and quality criteria. Then it writes `context.md`, `tasks.md`, `log.md`, and `README.md`.

**Step 6 - Indexes and report:** register the project in `01_now/README.md` and answer briefly:

> Created `YYYY-demo-product-positioning-strategy` (contour demo-product, mode `operational`). Goal: choose a positioning core that is distinguishable from competitors. I wrote a three-milestone plan: field map, candidate cores, final decision with rationale. Assumption recorded in Intent Lock: product-wide positioning first, not segment-specific. First step: build the competitive field map.

Key point: the owner did not retell the chat and did not write the plan. The agent extracted the brief and authored the starter files.

## Example B. Project Created From Scratch

**Situation.** The owner writes: "create a project - I want to build a personal CRM from my notes about people within a month".

**Step 1 - Reconstruct intent from the command and rules:**

- Explicit request: personal CRM from notes about people, roughly one-month horizon.
- Practical result: a system where each person has visible history and a next action.
- Constraints from vault rules: personal contour; people data is sensitive; long-lived person records may belong outside the project.
- Safe assumptions: the initiative can be a project, but durable data ownership is unclear.

**Step 2 - Source-of-truth fork:** "CRM" can mean an implementation project or a long-lived people register. A wrong choice could strand sensitive people records in a project that later gets archived. There is no safe assumption, so one question is justified.

**Step 3 - One recommended question:**

> I understand the goal as building a working personal CRM within about a month. I recommend A: the project defines the process and setup, while durable person records live in the contacts area and the project links to them. That way the data survives project closure. B would keep everything inside the project, which is faster but makes the project the data home. Confirm A or correct it. Also confirm whether this is `operational` setup or `development` work for a tool.

**Step 4 - After the answer** (assume the owner chose A and `operational`): the agent writes the full documentation. The Goal becomes "a working personal CRM exists: each person has history and next action". Non-goals state that person cards are not duplicated into the project. Source of truth points to the contacts area. Milestones and quality criteria are authored by the agent.

**Step 5 - Slug and path:** `YYYY-personal-crm`, path `01_now/projects/YYYY-personal-crm/`. Files, indexes, and a short report follow.

## What the Examples Show

- A question is asked only when no safe assumption exists and the cost of error is real.
- In both scenarios, the agent writes `plan.md`, milestones, and quality criteria.
- In the conversation-derived scenario, the agent extracts the brief and does not ask for a retelling.
- Source-of-truth ownership is a common reason to ask the one justified question.
