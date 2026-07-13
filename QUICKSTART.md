# Quickstart

This file helps you test the vault methodology in 5-10 minutes.

## 1. Make a Safe Copy

Use this repository as a GitHub template or clone it into a test folder.

Do not start with your real vault. First test the workflow on a small copy.

## 2. Open the Folder in an Agent

Open the repository root in an agent that can work with files.

Send this request:

```text
Open this folder as a working vault. First read AGENTS.md, START_HERE.md, QUICKSTART.md, and ONBOARDING.md. Explain the folder structure in simple words. Then help me run one safe test: process a small note from 00_inbox/, create a training project through project-creator, update links, and record the event in the log.
```

The agent must read the rules before changing files.

## 3. Add One Test File

Create a small Markdown file in `00_inbox/`, for example:

```markdown
# Test note

I want to see whether an AI agent can turn an unsorted note into a small project with state files.
```

Then ask:

```text
Process the test note from 00_inbox/ into a new training project through project-creator. Before making changes, tell me which files you will create or update. After the changes, show the project's README, plan, tasks, context, and log.
```

## 4. Check the Result

A good first result creates or updates:

- a project folder in `01_now/projects/`;
- `README.md` for navigation;
- `plan.md` for goal, boundaries, owner intent, quality criteria, milestones, and blockers;
- `tasks.md` for the current execution queue;
- `context.md` for durable project knowledge;
- `log.md` for short event history;
- required folder indexes.

If the agent asks you to write the plan or quality criteria yourself, the test failed. In this methodology, that is the agent's responsibility.

Compare the result with [examples/first-session/](./examples/first-session/README.md).

## 5. Check Links

From the repository root:

```bash
python3 scripts/check_links.py
python3 scripts/inventory.py
```

If public starter-pack files changed, also run:

```bash
python3 scripts/check_forbidden_markers.py
```

## Separate Quick Test: GitHub Contour Repository

If you are testing a separate repository for a contour rather than a personal local vault, start here:

- [docs/github-contour-repositories.md](./docs/github-contour-repositories.md)
- [examples/github-contour-repository](./examples/github-contour-repository/README.md)

Then run:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

The test passes if validation sees `repository-manifest.yml`, required root files, valid links, and no forbidden markers.

## 6. Continue in a New Session

Open a new chat and ask:

```text
Continue the project from the vault files. First read AGENTS.md, then find the active project through 01_now/README.md. Explain the current state before making any changes.
```

The test succeeds if the agent can continue from files rather than old chat history.
