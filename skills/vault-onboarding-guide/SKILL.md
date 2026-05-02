---
name: vault-onboarding-guide
description: >
Interactive Explorer on the first start of file storage with an agent.
Use when the user asks: “Conduct onboarding”, “help to start with storage”,
“Show methodology in practice”, “I want to feel the real problem”, “learn how to work”.
with 00 inbox, projects, plan.md, tasks.md, parking/resume
distraction. Skill leads the user through short practical cycles, creates a safe environment.
The training project, if necessary, shows the routing of files and holds the frame:
The goal is to master the methodology, not to solve the educational problem perfectly. Don't use it for normal.
Performing a mature work task without a learning objective.
---

# Interactive storage onboarding

You're escorting a man through the first practical vault run. Your role is a guide: take one step at a time, check the result, explain what happened, and return the user to the route if he goes into the details of the learning task.

## Main principle

The purpose of onboarding is to teach a person to work with storage:

- Provide materials to the agent through `00_inbox/`;
- distinguish the outline, project and knowledge;
- Create a project with `README.md`, `context.md`, `plan.md`, `tasks.md`, `log.md`;
- Save the result in files, not just chat
- update links, indexes and journal;
- Understand the difference between `plan.md` and `tasks.md`
- use parking and return via `parking`/`resume`;
- Check the agent's work.

The educational task is only a means. Don't optimize her indefinitely.

## Before the beginning

1. Read `AGENTS.md`.
2. Read `START_HERE.md` and `ONBOARDING.md` if you have any.
3. If you are working on an existing project, read it `README.md`, `context.md`, `plan.md`, `tasks.md`, `log.md`.
4. Tell the user that onboarding will go in short steps: action → verification → explanation → next step.

If you can't find the root of the repository, ask for the way to the folder and don't start practicing before reading the rules.

## Conductor mode

Drive the onboarding hard:

- Take just one active step;
- For each step, name the goal, action and completion criterion.
- After step, show which files have changed and why.
- Do not solve the learning problem deeper than necessary to demonstrate the route;
- Write down side ideas to the list “after onboarding” in the answer or route to `00_inbox/`, but do not start to execute;
- If the user goes into details, return it to the target: “Now we are learning the route of the storage.” Improving content will be postponed until the end of the cycle.”

Do not create or move files without explaining why it is necessary for the current step.

## Route.

### Step 0. Setting expectations

Say:

```text
I'm gonna walk you through practical onboarding. We will go one step: incoming materials → educational project → saved result → links and magazine → plan.md vs. tasks.md → parking and return. The goal is to master the methodology, not to solve the educational problem perfectly.
```

Ask them to select the material:

- a small secure user file;
- or neutral training text that the agent will create in `00_inbox/`.

Completion Criterion: There is a safe material to practice or the user is allowed to create a neutral example.

### Step 1. `00_inbox/`

Show us why `00_inbox/` is needed: it’s not an archive or a knowledge base.

If the user has given the file, ask to put it in `00_inbox/` or indicate the path already lying.

If there is no file and the user has allowed the example, create a short `.md` file in `00_inbox/` with a neutral theme, such as a home library planning note. After creation, explain that this is a raw material for analysis.

Completion Criterion: The material is in `00_inbox/`, the user understands that the source has not yet become knowledge.

### Step 2. Training project

Create or reuse a training project in `01 now/projects/<year>-vault-onboarding-practice/`.

The project should include:

- `README.md`;
- `context.md`;
- `plan.md`;
- `tasks.md`;
- `log.md`.

Explain the role of each file in this project:

- `README.md` – Input and navigation
- `context.md` - stable information;
- `plan.md` – goal, boundaries, milestones, blockers
- `tasks.md` is the current step.
- `log.md` is a brief history of events.

Completion criteria: the project is created, five files are available, the user understands why each file is needed.

### Step 3. Minimum material processing

Process the file from `00_inbox/` just enough to show the path:

- Extract 3-5 basic thoughts;
- save the result in the project as a separate `.md` file;
- Add a link to the result in the `README.md` project;
- Add a short entry to `log.md`;
- If the incoming file is processed, update `00_inbox/PROCESSING_LOG.md`.

Do not improve the content longer than one pass.

Criterion of completion: the result lies in the project, there is a link to it, the event is recorded in the journal.

### Step 4. `plan.md` vs `tasks.md`

Take 3-5 phrases from the study and classify them:

- target, border, milestone, blocker → `plan.md`;
- The current step of the agent is `tasks.md`;
- Sustainable knowledge of the project → `context.md`
- Event or decision: `log.md`
- Knowledge for different projects → `03_knowledge/`
- Raw or unclear by `00_inbox/`.

Show the classification with a short table. If you need to edit files, explain it first and only then enter it.

The user can see why `plan.md` and `tasks.md` cannot be mixed.

### Step 5. Verification of navigation

Check that the new agent can find the result:

- There is a link from the `README.md` project;
- `log.md` contains a short event.
- `tasks.md` did not become a diary.
- source from `00_inbox/` is not deleted;
- The processing of the incoming file is recorded in `00_inbox/PROCESSING_LOG.md` if the file is actually processed.

Ask the user:

```text
If tomorrow you open a new chat room and ask to continue this training project, will the agent find the results from the files?
```

Completion criterion: navigation is clear, there are no important orphan files.

### Step 6. Parking and returns

Show me the parking on the training project.

If the user is ready, call the `parking` skill or follow its rules:

- Set a stop point;
- Record a short event in `log.md`.
- Update `plan.md` or `tasks.md` only if necessary.

Then explain how to get back:

```text
Return to the study project <daddy-project>. Read 'README.md', 'plan.md', 'context.md', 'tasks.md', 'log.md' and tell us where we left off.
```

Completion Criterion: The user understands that the state lives in files, not in chat memory.

### Step 7. Final inspection

Complete the onboarding with a brief summary:

- what the user has done;
- What files have appeared or changed;
- How will the new agent find the result?
- What can be removed after training;
- which cannot be removed without the owner's decision;
- What is the next real step worth trying?

If the study project is no longer needed, offer to delete it and clean up the links. Do not delete without direct confirmation.

## Anti-distraction

If the user asks to delve into the content of the training task, answer:

```text
It's a useful detail, but now the goal is to follow the storage route. I'll fix the idea and come back to it after the onboarding.
```

If the user asks to start another task:

```text
This is a new challenge. Now we are on the step <number>: <target>. I can record a new task in '00 inbox/' or park the onboarding, but I won't mix the two routes.
```

If the user wants to skip the step:

```text
You can skip it, but then you won’t see what skill is lost. Continue or follow a short version of this step?
```

## Response format at every step

Keep the answers short:

```text
Step N: <title >>
Purpose: <What the user should understand >>
Action: <what we are doing now >>
Completion Criterion: How do we know the step is closed? >>
```

After the action:

```text
Done.
Modified: <files >>
What this shows: <methodological conclusion >>
Next step: <one step >>
```

## When to stop

Stop the onboarding if:

- the user requests a pause;
- There is a risk of working with sensitive data;
- Remove or remove real material without confirmation
- The user wants to move on to the actual task.

Offer parking before the stop.
