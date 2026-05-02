# Quickstart

This file helps you test the vault methodology in 5-10 minutes.

## 1. Make a safe copy

Use this repository as a GitHub template or clone it into a test folder.

Do not start with your real vault. First test the workflow on a small copy.

## 2. Open the folder in the agent

Open the repository root in an agent that can work with files.

Send a request:

```text
Open this folder as your working storage. First read AGENTS.md, START_HERE.md, QUICKSTART.md and ONBOARDING.md. Explain the folder structure in simple words. Then help us carry out one safe test: parse a small note from 00_inbox/, create a training project, update links and log the event.
```

The agent must read the rules before changing files.

## 3. Add one test file

Create a small Markdown file in `00_inbox/`, for example:

```markdown
# Test note

I want to see if an AI agent can turn an unparsed note into a small project with state files.
```

Then ask:

```textParse the test note from 00_inbox/ into a new study project. Before making changes, tell me what files you will create or update. After the changes, show the README, plan, tasks, context and project log.
```

## 4. Check the result

A good first result usually creates or updates:

- project folder in `01_now/projects/`;
- `README.md` for navigation;
- `plan.md` for goals, boundaries, milestones and blockers;
- `tasks.md` for the current execution queue;
- `context.md` for sustainable knowledge of the project;
- `log.md` for a short history of events;
- required folder indexes.

Compare the result with [examples/first-session/](./examples/first-session/README.md).

## 5. Check the links

From the repository root:

```bash
python3 scripts/check_links.py
python3 scripts/inventory.py
```

If the public files of the kit have changed, also run:

```bash
python3 scripts/check_forbidden_markers.py
```

## 6. Continue in a new session

Open a new chat and ask:

```text
Continue the project through the storage files. First read AGENTS.md, then find the active project through 01_now/README.md. Explain the current state before any changes.
```

The test is successful if the agent can continue working from the files rather than from the old chat history.
