---
id: markdown-agent-vault-readme
type: index
status: active
created: 2026-04-30
updated: 2026-05-02
aliases:
  - "Markdown Agent Vault"
tags: [vault, methodology, starter-pack]
source_path: "README.md"
---

# Markdown Agent Vault

## Essence

This is the English mirror/adaptation of `markdown-agent-vault-ru` while the project is solo-maintained. It keeps the same structure and methodology in English: rules, folder structure, templates, skills, logs, and checks for maintaining a file workspace together with an AI agent.

The sync policy may change after external contributions or an independent English-language audience appear. For the current policy, see [Sync Policy](./docs/sync-policy.md).

## What It Solves

A typical AI session often ends with:

- the context remains in the chat;
- files are downloaded, retold and forgotten;
- the next session has to be introduced into the course again;
- solutions, tasks, knowledge and sources diverge in different places.

This kit makes the file system a persistent state layer:

- `AGENTS.md` explains the workspace rules to the agent;
- `00_inbox/` accepts new and unprocessed materials;
- `01_now/` stores active projects and current work;
- `03_knowledge/` stores reused knowledge;
- `log.md`, `plan.md`, `tasks.md` and `context.md` help the new session continue without guesswork.

## For whom it is useful

The kit is useful if you:

- you work with agents who can read and change local files;
- take notes in Markdown or Obsidian;
- you want the project state to survive individual chats;
- want a clear order for incoming materials, tasks, solutions and knowledge;
- you prefer regular files rather than closed “memory” inside the service.

This is not:

- SaaS application;
- Obsidian plugin;
- magical memory;
- replacement of the task tracker;
- a universal methodology for all people and cultures.

## First launch

1. Clone the repository or use it as a template in a safe test folder.
2. Open the folder in an agent that can work with files.
3. Tell the agent:

   ```text
   Open this folder as your working storage. First read AGENTS.md, START_HERE.md, QUICKSTART.md and ONBOARDING.md. Explain the folder structure, the main rules and walk me through one safe test project with a small file in 00_inbox/.
   ```
4. Place a small test file in `00_inbox/`.
5. Ask the agent to create a training project, update links and log the event.
6. Compare the result with the example [examples/first-session](./examples/first-session/README.md).

## Navigation

| Path | Destination |
|---|---|
| [AGENTS.md](./AGENTS.md) | Rules for agent operation inside the storage |
| [START_HERE.md](./START_HERE.md) | Short entry for the first session |
| [ONBOARDING.md](./ONBOARDING.md) | Detailed onboarding |
| [QUICKSTART.md](./QUICKSTART.md) | Quick practical start |
| [00_inbox/](./00_inbox/README.md) | New and unassembled materials |
| [01_now/](./01_now/README.md) | Active projects and current work |
| [02_domains/](./02_domains/README.md) | Long lasting areas of life or work |
| [03_knowledge/](./03_knowledge/README.md) | Reused knowledge and methodologies |
| [04_logs/](./04_logs/README.md) | Timeline, Reviews and Solution Logs |
| [90_archive/](./90_archive/README.md) | Completed and outdated |
| [meta/](./meta/README.md) | Rules, templates and service indexes |
| [skills/](./skills/README.md) | Skills for repetitive types of tasks |
| [scripts/](./scripts/README.md) | Local checks |
| [examples/first-session/](./examples/first-session/README.md) | Minimal example of the first loop |

## How is it different?

| Alternative | What it gives | What makes this kit different |
|---|---|---|
| One `AGENTS.md` | Agent Rules of Conduct | The entire file architecture is here: inboxes, projects, knowledge, logs, templates, skills and routing |
| Basic Memory and similar tools | Layer of memory and search by notes | Here the focus is on the file status of projects, solutions, tasks and sources |
| Cline Memory Bank | Design Memory Files for Development | Here the approach is broader: not only code, but also research, meetings, knowledge, input and journals |
| Obsidian plugins | Interface features and automation inside Obsidian | This is not a plugin, but a file convention and operating procedure for the agent |
| Regular Obsidian Storage | Notes and links for a person | Rules for the agent, project state files, life cycle and checks are added here |

## Maturity

Status: early English mirror/adaptation of the Russian methodology.

Done:

- portable folder structure;
- agent rules;
- project templates;
- routing of materials;
- onboarding;
- skills;
- local checks;
- a minimal example of the first loop.

Not ready yet:

- broad instructions for all agent tools;
- external user examples;- stable compatibility with any agent;
- mature public contribution model.

## Check

From the repository root:

```bash
python3 scripts/inventory.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
```

## License

MIT. See [LICENSE](./LICENSE).
