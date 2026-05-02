---
id: vault-methodology-onboarding
type: guide
status: active
created: 2026-05-01
updated: 2026-05-01
aliases:
  - "Onboarding into the repository methodology"
  - "How to start working with storage"
tags: [guide, onboarding, vault, methodology, agents]
source_path: "ONBOARDING.md"
freshness: evergreen
knowledge_criticality: high
verification_status: unverified
curation_mode: manual_edit
---

# Onboarding to the repository methodology

## Essence

This document helps you launch the repository for the first time: open a folder in the agent, give the first task, save the result in the right place, check the work and gradually turn repeated actions into rules and skills.

## Details

### How to read this document

Don't try to learn everything in advance. Take it one step at a time. If you want to do an internship with an agent, ask him to use the skill [`vault-onboarding-guide`](./skills/vault-onboarding-guide/SKILL.md): he will guide you one step at a time, check the result and not let you get lost in the details of the training task.

1. Read sections 1-3 and do the first hour quick route.
2. Return to sections 4-7 when you need to understand where to store files and how projects are organized.
3. Use sections 8-9 for the first real problem.4. Use sections 10-12 when the work has become long, repetitive actions have appeared, or the rules need to be corrected.
5. Use sections 13-16 as a checklist.

If a term is unclear, don't stop. Ask the agent to explain it using an example from this folder.

### 1. Main idea

A repository is not a folder of notes. This is a work environment: a human sets the direction and checks the result, and an agent reads files, creates documents, updates links, maintains a log and maintains order.

Regular chat works differently:

- each time you need to bring the context anew;
- downloaded files are lost in a long conversation;
- the result often has to be carried by hand;
- knowledge is difficult to maintain and improve.

The agent works with the folder on the computer:

- reads the rules from `AGENTS.md`;
- searches for documents via `README.md` and links;
- creates and changes files in the storage;
- records important actions in `log.md`;
- continues to work in a new chat if the state is saved in files.

Don't just ask an agent to "write the text." Ask to do work in the repository: find sources, create a project, save the result, update navigation and check links.

### 2. What to do before the first launch1. Put the storage in a permanent folder, not in downloads.
2. If you need synchronization, put the folder in a cloud drive.
3. Open the repository in the agent as a working folder.
4. Open the same folder in Obsidian or another Markdown editor to read files, tables and links.
5. Include the full path in the file manager and add the folder to quick access. This makes it easier to give the agent the path to the files.

First request to the agent:

```text
Open this folder as your working storage. Read `AGENTS.md` first, then `START_HERE.md` and `ONBOARDING.md`. Explain to me in your own words the folder structure, the main operating rules and suggest the first safe test step.
```

If the agent started acting before reading the rules, stop it:

```text
First read `AGENTS.md` and reconsider your actions according to the storage rules.
```

### 3. Fast route of the first hour

If you haven't worked with agents before, don't start with a big task. Go through the training cycle first.

1. Open the repository in the agent.
2. Submit the first request from section 2.
3. Ask to explain the folder structure in simple words.
4. Place a small test document in `00_inbox/`.
5. Ask to create a training project and process the document.6. Check which files the agent created and which links it updated.
7. Ask to explain why the result is there.
8. If the educational project is not needed, ask to remove it and clean up the navigation.

Minimum request:

```text
This is my first time working with this repository. Walk me through the tutorial: read the rules, explain the structure, create a tutorial project for the file from `00_inbox/`, save the result in the project and show which indexes and logs are updated.
```

Interactive option:

```text
Walk me through onboarding with the `vault-onboarding-guide` skill: one step at a time, on a safe learning task, checking files, links and log. If I get lost in the details of the task, bring me back to the onboarding route.
```

The goal of the first hour is to see the work cycle: incoming materials → project → saved result → links → journal → review.

### 4. What lies at the root

- `AGENTS.md` - rules for the agent. He reads them at the beginning of work.
- `START_HERE.md` - short input for the first launch.
- `ONBOARDING.md` - this detailed route.
- `00_inbox/` - new materials before analysis.
- `01_now/` - active work: projects, operational areas, personal current tasks.
- `02_domains/` - long-lived areas of life or business.- `03_knowledge/` - knowledge and methodologies for reuse.
- `04_logs/` - magazines, reviews, chronology.
- `90_archive/` - complete and outdated.
- `meta/` - ​​rules, templates and service indexes.
- `skills/` - skills for repetitive tasks.
- `scripts/` - package portability checks.
- `skills/vault-onboarding-guide/` - a guide for practical onboarding step by step.

### 5. Navigation rule

A document is useless if the agent can't get to it.

The repository has three navigation layers:

- `README.md` in the folders explains what is here;
- links connect documents with each other;
- `log.md`, `plan.md`, `tasks.md` and `context.md` help restore the status of the project.

If an agent created a file but did not add a link from the index or neighboring document, the next agent may not find it. After creating the file, you need to update the navigation.

Test question:

```text
If tomorrow I open a new chat and ask about this file, will the agent find it through `README.md` and links?
```

If the answer is no, the work is not finished.

#### Why do we need `README.md`

`README.md` is the folder index. From it the agent understands:

- why does the folder exist;
- which files are important;
- where to start reading;- what documents are linked;
- which files can not be read.

Without `README.md` the agent only sees a list of files and guesses what is important. In a live repository, this leads to errors: the agent reads the wrong files, skips the right ones, creates duplicates and puts knowledge in the wrong place.

#### Why there shouldn't be "orphans"

An "orphan" is a file that is not referenced from `README.md`, a linked document, project, or index.

Such a file is not physically lost, but lost for use. The new agent doesn't know that the file exists or when to read it. For an agent, it is almost equal to being absent.

After creating an important file, the agent must:

- add a link to the `README.md` folder;
- if necessary, add a backlink from the linked document;
- record the event in `log.md` if this is a project result;
- check that the file is located through the navigation chain.

Request for verification:

```text
Check to see if the affected folders contain important orphan files: files that are not referenced from `README.md` or neighboring documents. Don't move anything without my approval.
```

### 6. Where to put what?

Basic rule:

- new and unassembled → `00_inbox/`;
- an active task with a clear result → `01_now/projects/`;- long-lived workspace with projects, meetings, tasks, delegations and operational data → `01_now/ops/`;
- permanent area of ​​life or business → `02_domains/`;
- knowledge for different projects → `03_knowledge/`;
- history of decisions and events → `04_logs/` or `log.md` of the project;
- completed → `90_archive/`;
- agent operation rule → `meta/rules/` or `AGENTS.md`;
- repeatable technique → `skills/<name>/SKILL.md`.

Do not transfer files by hand between work folders. If in doubt, put the file in `00_inbox/` and ask the agent to sort it out.

Request:

```text
I put new materials in `00_inbox/`. Sort them out, suggest routing, move them only after explaining where and why, then update the indexes and the incoming processing log.
```

#### Outline, project and knowledge

The circuit is a long-lived area of work. It doesn't end with one result. The loop is home to regular meetings, people, external systems, operational rules, recurring tasks, delegations, registries, and multiple projects.

A project is a limited work with a goal and completion. The project must end: the result is done, the decision is made, the research is carried out, the version is released, the document is prepared.Knowledge is materials that can be used beyond one project and often beyond one circuit: methodologies, reference books, principles, generalizations and proven approaches.

Test questions:

- "will this live after the current task is completed?" → outline or knowledge;
- “Is this only necessary for the current result?” → project;
- “will this be useful in several projects or people in the future?” → knowledge;
- "is it related to a persistent area, people, meetings, operations or external systems?" → contour.

What to store in the circuit:

- stable working context of the area;
- regular meetings and their summary;
- operational rules of the region;
- delegation and expectations for people;
- links to external sources of truth;
- registries that will survive individual projects;
- materials for managing an area, not just one result.

What to store in the project:

- goal and boundaries;
- plan, milestones and blockers;
- current actions of the agent;
- project context;
- the results created for the sake of this project;
- journal of project decisions.

What to store in knowledge:

- methodology;
- reference books;
- terms and definitions;
- generalizations from several sources;
- sustainable conclusions for reuse;- instructions that are not tied to one active project.

A common mistake is to put contour data into a project because the project is currently using it. If the project is archived before the data is no longer valuable, the data has no place in the project.

Request for routing:

```text
Determine whether it is a project, a circuit or knowledge. First explain the selection criteria, then suggest a storage location and only after my confirmation create or move files.
```

#### Life cycle `00_inbox/`

`00_inbox/` is not an archive or a knowledge base. This is the place for analysis.

This includes:

- transcripts of meetings;
- unloading from external systems;
- documents to read;
- tables and files without a clear place;
- materials to be given to the agent.

Work cycle:

1. The person places the file in `00_inbox/`.
2. The agent reads the file on a task basis, and not as a permanent source of knowledge.
3. The agent extracts what is valuable and transfers the result to a project, circuit or knowledge.
4. The agent writes the processing to `00_inbox/PROCESSING_LOG.md`.
5. The source remains in `00_inbox/` until the owner decides.
6. In the review, you can only delete what is marked as processed.Don't look for answers in `00_inbox/` as in the knowledge base. If the material is needed further, it must be processed and transferred to the correct location.

#### Why it's better not to upload files to chat

The chat file is suitable for a one-time question, but does not work well with storage:

- takes the context of the conversation;
- gets lost in long work;
- does not receive a place in the structure;
- does not receive a link from `README.md`;
- the next chat may not know about it;
- the agent can process it without logging the source and result.

Working way:

1. Place the file in `00_inbox/`.
2. Give the agent the path to the file or folder.
3. Ask to process, transfer the result and update the log.

Upload the file directly to the chat only for a one-time question, if the result does not need to be saved and continued.

#### Why should the work files for the agent be `.md` and `.csv`

Markdown (`.md`) is the main format for text documents. It is read by the person, the agent, and the note editor. It contains headers, lists, tables, links and service markup at the beginning of the file.

CSV (`.csv`) is a simple table format. It is easy to read, compare, check and script.

Why is this convenient:- the agent reads `.md` and `.csv` without complex import;
- changes are easier to check;
- links and indexes remain plain text;
- the format does not hide important data;
- such files are convenient to compare when changing.

Files `.docx`, `.xlsx`, `.pdf` and presentations can be placed in your inbox, but consider them raw materials. If the knowledge is to live on, the agent must retrieve the work content at `.md` or `.csv`.

### 7. How the project works

A new active project lives in `01 now/projects/<year>-<slug>/`.

Inside should be:

- `README.md` — project entry and navigation;
- `context.md` - stable knowledge of the project: terms, limitations, sources of truth;
- `plan.md` - goal, boundaries, milestones, blockers and rules for maintaining direction;
- `tasks.md` — current step and next actions;
- `log.md` - a brief history of decisions and changes.

Difference between files:

- `context.md`: which is consistently true;
- `plan.md`: where are we going and what do we consider success;
- `tasks.md`: what are we doing now;
- `log.md`: what happened and why.

If the work lasts more than one short session, create a project. Chat-only work is quickly lost.

#### Project life cycle

The project goes through seven states:1. **Creation.** The agent creates a project folder and five required files.
2. **Planning.** `plan.md` records the goal, boundaries, milestones, readiness criteria and blockers.
3. **Execution.** The current step and the nearest queue live in `tasks.md`.
4. **Recording decisions.** Events and links to results are briefly recorded in `log.md`.
5. **Knowledge Extraction.** Everything that survives the project is transferred to the circuit or `03_knowledge/`.
6. **Closing.** The project receives a summary, active tasks are closed, links are updated.
7. **Archive.** The completed project goes to `90_archive/`, and active indexes no longer point to it as an ongoing work.

The project should not become an eternal warehouse. If work lives for months as a constant area with meetings, people, rules and delegations, it already looks like an outline.

#### Why you need to follow `plan.md`

`plan.md` keeps the project going. He answers the questions:

- why the project was started;
- what is not included in the work;
- what milestones need to be passed;
- on what grounds will the result be accepted;
- what blocks the movement;
- what rules prevent the project from unraveling?If the goal, milestone order, readiness criterion changes, or a blocker appears, first update `plan.md`, then `log.md`, and only then change the current queue in `tasks.md`.

#### How is `plan.md` different from `tasks.md`

`tasks.md` is not a project plan or a diary. This is the execution queue.

`tasks.md` should contain:

- one current active step;
- exit criteria for this step;
- immediate actions;
- waiting if work is stopped.

The following should not live in `tasks.md`:

- the purpose of the project;
- strategy;
- a long history of what was done;
- project blockers;
- delegation to people;
- personal obligations of the owner;
- thinking like “understand what to do.”

Test question:

```text
Does this line help complete the next step or describe the direction of the project?
```

If it is a direction, goal, blocker or success criterion - place in `plan.md`. If this is the agent's action now, the place is `tasks.md`.

Request:

```text
Create a project in `01_now/projects/` for the task: <what I want to receive>. Name the project `<year>-<short-name >>`. First create `README.md`, `context.md`, `plan.md`, `tasks.md`, `log.md`, then suggest the first step.
```

### 8. First learning taskFor the first hour, take a small document that you don’t mind reworking.

1. Place the document in `00_inbox/`.
2. Open a new chat with the agent in the root of the repository.
3. Ask the agent to read the rules.
4. Ask to create a teaching project.
5. Ask to process the document and save the result.
6. Check the created files.
7. Ask to see which indexes and logs have been updated.
8. If the result is not needed, ask to delete the educational project and clean up the links.

Example request:

```text
I put a small document in `00_inbox/` for educational processing. Create a learning project, extract the main ideas from the document, save the result in the project, update `README.md` of the project and `log.md`. After that, show what files you created or changed.
```

Check with your eyes:

- the project was created in `01_now/projects/`;
- the project has five required files;
- the result lies in the project, and not just in the chat response;
- there is a link to the source;
- `README.md` of the project leads to results;
- `log.md` briefly records the action;
- the agent did not change unnecessary folders.

### 9. How to assign tasks to an agent

A good request tells the agent:

- what you need to get;
- where the source materials are located;
- where to save the result;- what rules or skills to apply;
- what to check before completion;
- what you can’t touch.

Template:

```text
Task: <what to do>.
Source: <path or description>.
Save the result: <folder or project>.
Before starting, read: <rule or skill, if I know>.
Don't touch: <restrictions>.
At the end, show what you changed, what checks passed, what remains open.
```

If you don’t know where to put the result, just say so:

```text
I don't know where to put it correctly. First, suggest routing according to the storage rules, explain the options and wait for my decision.
```

### 10. What to do in a new chat

Each chat has a context limit. In a long chat, the agent remembers details worse.

New task - new chat. To continue an old task, open a new chat and say:

```text
Continue working on the project `<daddy-project >>`. Read `README.md`, `context.md`, `plan.md`, `tasks.md` and `log.md`, then tell me where we left off and what the next safe step is.
```

If you need to move without loss:

```text
Prepare a short continuation package for a new chat: where is the project, what has already been done, what decisions have been made, what to do next.
```To pause, use the skill `parking`, to return - `resume`.

#### Why do you need parking?

Parking saves a return point before switching, pausing, or closing the chat.

It is needed when the work has begun, but it is impossible or not necessary to continue now:

- need to switch to another task;
- you are waiting for an answer, data or an external event;
- the task has been transferred to another person;
- the chat has become long and it’s time to move to a new one;
- there is a risk of forgetting where you stopped;
- you need to fix the state before the break.

Without parking, the task remains in the chat memory. Then you will have to remember what has been done, what decisions have been made, where the files are and what the next step is. Parking transfers this state into the project files, so the future agent will restore the work without retelling the whole story.

#### What the agent should keep when parking

When parking, the agent determines:

- what project the work belongs to;
- what did they do;
- where we stayed;
- why did you stop;
- what must happen for a return;
- is there a blocker, delegation or pause;
- which files need to be updated.

In a simple case, the agent writes a short entry to `log.md` of the project.If work is stopped due to a blocker, the agent updates `plan.md` because the blocker is changing the state of the project.

If you need to gather information, the next step might fall into `tasks.md`.

If the work is delegated to a person, the entry may end up in the circuit delegation file.

The parking lot doesn't just say "we're stopping." It places the return point in the correct storage layer.

#### How to use the parking lot

When you want to stop, say:

```text
Park the current task.
```

Or more details:

```text
Park this work: record what has already been done, where you stopped, what is blocking continuation, and under what condition you need to return.
```

If you switch to another topic:

```text
First, take a snapshot of the current project, then we’ll move on to a new task.
```

After parking, the agent should respond something like this:

```text
I parked. Recorded a still image in `log.md`, updated `plan.md`/`tasks.md` if necessary.
Breaking point: <what exactly has been done>.
Return trigger: <when ​​to return>.
You can switch.
```

#### How to return to a parked task

In a new or old chat, say:

```text
Show me what's parked.
```

Or:

Return to the parked task for project.
```

The agent must find the parking records, read `README.md`, `plan.md`, `context.md`, `tasks.md`, `log.md`, restore the stopping point, and suggest the next step.

If you don't remember the project:

```text
Find all parked tasks and show the list: project, reason for pause, return trigger and what to do next.
```

#### When parking is not needed

Parking is not needed for a short question that does not change files or interrupt ongoing work.

A new idea doesn’t always require parking during work either. If the idea belongs to another project or area, it should be put in the correct place: `tasks.md`, `plan.md`, `00_inbox/`, `03_knowledge/` or delegation file. The current task is parked only during a real stop.

#### What to do after context compression

Sometimes an agent compresses the conversation history: leaving a summary instead of the full chat. This way you can work longer, but at this stage the agent often loses some of the instructions, nuances and restrictions.

After compression, do not continue difficult work immediately. First, return the agent to the storage files:

```textIt looks like the context has been compressed. Before continuing, read `AGENTS.md` again, then the current project files: `README.md`, `context.md`, `plan.md`, `tasks.md`, `log.md`. After that, briefly say what rules and next step you restored.
```

If the work is not in the project, but in the circuit:

```text
It looks like the context has been compressed. Re-read `AGENTS.md`, `README.md` of the desired circuit and the associated rules. Don't continue working until you tell me what context you've restored.
```

Storage rules live in files, not in chat memory. After compression, you need to again rely on the sources of truth: `AGENTS.md`, indexes, plan, log and current tasks.

### 11. Skills

Skill - instructions for repetitive work. It is needed when an agent must do the same thing every time: conduct research, process a meeting, edit text, create content for a presentation, review changes.

Difference:

- `AGENTS.md` - rules that are almost always needed;
- `meta/rules/` - detailed rules for individual classes of tasks;
- `skills/` - techniques that are included for a specific task.

Don't put all the rules in `AGENTS.md`. If instructions are needed only sometimes, make a skill.For your first practice pass, use `vault-onboarding-guide`. It does not replace this document, but guides you through it: it gives you one step, waits for the action, checks the files and returns you to the route if the learning task begins to drag on.

#### `AGENTS.md` and `SKILL.md`: what's the difference

`AGENTS.md` answers the question: "How should an agent behave in this repository in general?"

`SKILL.md` answers the question: "How should an agent perform a specific repetitive type of work?"

`AGENTS.md` should contain rules that are needed before selecting a task:

- how folders are arranged;
- how the agent loads the context;
- what to do in case of ambiguity;
- how to create and modify files;
- which indexes to update;
- what cannot be read or deleted without asking;
- where to go for detailed rules.

`SKILL.md` contains techniques that are needed only sometimes:

- processing appointments;
- research of the topic;
- text editing;
- creating content for the presentation;
- development with checks;
- creation of new skills;
- a repeatable analytical or creative procedure.

Simple test:

```text
This rule should apply in almost every session until the task is understood?
```

If yes, this is a candidate for `AGENTS.md` or `meta/rules/`.

```textIs this a detailed methodology for one type of work?
```

If yes, this is a candidate for `SKILL.md`.

Examples:

- "After creating the file, update the folder index" → `AGENTS.md` or `meta/rules/write-protocol.md`.
- “When processing a meeting, extract decisions, promises, tasks and anecdotal facts” → `skills/meeting-processing/SKILL.md`.
- “Before web research, check the sources and save the result to the knowledge base” → `skills/research/SKILL.md`.
- “If the project is ambiguous, clarify the outline” → `AGENTS.md`.
- “How to write a Hero-block of a landing page” → skill for text, not `AGENTS.md`.

Principle: `AGENTS.md` routes and protects order, `SKILL.md` describes specialized work.

Requests:

```text
Conduct research using skill `research` and save the result in the knowledge base.
```

```text
Process this encounter with the skill `meeting-processing`.
```

```text
Create a skill for a recurring task: <description>. First use `skill-creator`, check if there is a similar skill, then suggest a structure.
```

### 12. How to develop rules

Rules emerge from repeated problems.

When I noticed the repetition:

1. Describe the problem to the agent.
2. Ask for a rule.
3. Decide where it should live:
   - always necessary → `AGENTS.md` or `meta/rules/`;- needed only in one project → `context.md` or `plan.md` project;
   - needed for a repetitive type of work → `skills/`;
   - needed as a document template → `meta/templates/`.
4. Ask the agent to add a rule and update the links.
5. Check the result.

Request:

```text
We have already encountered the problem: <description> several times. Suggest a rule, but first determine where it belongs: `AGENTS.md`, `meta/rules/`, project file or skill.
```

#### How to modify `AGENTS.md`

`AGENTS.md` - the top layer of rules. It is read frequently and influences almost any agent's work. Don't turn it into a textbook, a journal of decisions, or a collection of all the exceptions.

A good rule for `AGENTS.md`:

- short;
- unambiguous;
- verifiable;
- written as an agent's action;
- contains the conditions of application;
- leads to a detailed rule if details are needed;
- does not require guesswork.

Bad rule:

```text
Try to work with files carefully and do not forget about order.
```

It is difficult for an agent to execute such a phrase: it is not clear what “carefully” means, what order is needed and how to check the result.

A good rule of thumb:

```textAfter creating the `.md` file, update `README.md` its folder and check that the new file is reachable via the link from the index.
```

There is an action, a condition and a check.

#### The rule must be machine executable

Write the rule as an instruction to the performer, and not as a reminder to the person.

Test questions:

- will the agent understand when to apply the rule?
- will the agent understand what action to perform?
- will the agent understand where to write the result?
- will the agent be able to check that the rule is satisfied?
- will two different agents read the rule the same way?

If the answer is no, simplify the wording.

Instead of:

```text
Don't forget to run the project properly.
```

Better:

```text
If you are creating an active project, create `README.md`, `context.md`, `plan.md`, `tasks.md`, `log.md` before starting any meaningful work.
```

Instead of:

```text
Record important things.
```

Better:

```text
If a decision is made, a plan is changed, or an important file is created, add a short entry to `log.md` of the project: date, event, decision, link to the file.
```

#### Keep root `AGENTS.md` small

The root `AGENTS.md` should contain only what is needed almost always:

- folder map;
- loading context;
- basic recording rules;
- routing rules;- prohibitions and safety restrictions;
- links to detailed rules.

Take everything specific below:

- rules for processing meetings → `skills/meeting-processing/SKILL.md`;
- research rules → `skills/research/SKILL.md`;
- development rules → `meta/rules/dev-protocol.md` or development skill;
- rules for a specific project → `plan.md` or `context.md` project;
- rules for a specific circuit → `01_now/ops/<contour>/AGENTS.md`, if the environment supports local rules, or a separate rules file within the circuit with a link from `README.md`;
- rare details → `meta/rules/<topic>.md`.

If you put everything into one big `AGENTS.md`, problems will appear:

- the agent will waste context on rules that are not needed by the current task;
- important rules will drown among rare exceptions;
- the agent will skip details more often;
- it will become difficult for a person to maintain the file;
- any change to the top file will affect all types of work.

The root `AGENTS.md` should be a router: it tells which rules to read for which type of task. Details live in separate files.

#### When to add a rule to the top

Add a rule to the root `AGENTS.md` only if it:

- used in almost every session;
- protects data from loss or leakage;
- determines the structure of the entire repository;- helps you choose the right context before answering;
- Prevents a common, expensive mistake.

If a rule is only needed for one activity, don't move it up. Make a separate rule, local `AGENTS.md` or skill.

Request for safe modification:

```text
You need to add a rule for agents: <situation>. First, suggest where it should live: root `AGENTS.md`, local `AGENTS.md`, `meta/rules/`, project file or skill. Then formulate the rule briefly, unambiguously, and in such a way that the agent can execute and check it.
```

### 13. How to check the agent’s performance

The agent speeds up the work, but the person remains responsible for the result.

After every significant change, ask:

```text
Show me a list of changed files, explain why each one was changed, check the links and tell me what I need to check with my eyes.
```

Minimum check list:

- the result is saved in a file, and not just in the chat;
- the storage location is chosen according to its meaning;
- there are links from `README.md` or related files;
- the project log has been updated;
- `tasks.md` has not accumulated history instead of current steps;
- temporary files are not left without a reason;
- sources from `00_inbox/` were not removed without a direct request;- there is no personal data in files that are planned to be transferred to other people.

For this package, after making changes, run:

```bash
python3 scripts/inventory.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
```

### 14. What not to do with your hands

- Do not transfer files between working folders without an agent.
- Do not create a project without `README.md`, `context.md`, `plan.md`, `tasks.md`, `log.md`.
- Do not put long-lived knowledge inside a temporary project.
- Do not delete `log.md` and incoming materials without an obvious reason.
- Do not turn `tasks.md` into a diary or warehouse of thoughts.
- Don't ask the agent to "just do it" on an important task without a place to save and check.
- Do not add long instructions to `AGENTS.md` that are only needed sometimes.

### 15. Useful first queries

Inventory:

```text
Take an inventory of the storage: what sections are there, what rules have you read, what skills are available, what should I open first.
```

Inbox parsing:

```text
Look `00_inbox/`, group materials by type and suggest processing order. Don't move anything until I confirm.
```

Creating a project:

```textCreate a project for <task>. First create a project structure and plan, then stop and show me what you've created.
```

Continuation of the project:

```text
Continue the project `<daddy >>`. Restore the state from the project files, then suggest one next step.
```

Knowledge Update:

```text
The repository contains outdated knowledge: <what has changed>. Find where it is reflected, suggest changes, then update the associated files and log.
```

Create a rule:

```text
We encountered a recurring error: <error>. Suggest a rule or skill that will prevent it in the future.
```

Go to new chat:

```text
Prepare a continuation package: what has been done, where the files are, what decisions have been made, what to do next.
```

### 16. Correct start criterion

You are working according to the methodology correctly if:

- new materials first go to `00_inbox/`;
- important work is formalized as a project;
- the agent updates navigation and logs;
- you check the result with your eyes;
- repeating actions turn into rules, patterns or skills;
- the new chat can restore the state from files without retelling the entire story.If this is done, the repository acts as a second brain: it doesn’t just store files, but helps you continue working, maintain context, and improve rules.

## Next step

Open a new chat in the root of the repository and follow the quick route from section 3.