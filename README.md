---
id: markdown-agent-vault-readme
type: index
status: active
created: 2026-04-30
updated: 2026-07-13
aliases:
  - "Markdown Agent Vault"
tags: [vault, methodology, starter-pack]
source_path: "README.md"
---

# Markdown Agent Vault

## Essence

Markdown Agent Vault is a file-based starter pack for organizing projects, notes, decisions, and reusable knowledge with an AI agent that can read and edit local files. It provides a ready-made folder structure, Markdown templates, agent rules, logs, and local checks. It is not a plugin, application, or hosted memory service.

Use it when you want an AI agent to continue work across sessions by reading project state from files instead of relying only on chat history.

## What It Solves

A typical AI session often ends with:

- context remains in the chat;
- files are uploaded, summarized, and forgotten;
- the next session has to be reintroduced to the work;
- decisions, tasks, knowledge, and sources drift into different places.

This starter pack keeps project state in ordinary files that both you and the agent can read:

- `AGENTS.md` explains the vault rules to the agent;
- `00_inbox/` accepts new and unsorted materials;
- `01_now/` stores active projects and current work;
- `03_knowledge/` stores reusable knowledge;
- `log.md`, `plan.md`, `tasks.md`, and `context.md` help the next session continue without guessing;
- `project-creator` creates a complete project: the agent writes the plan, execution queue, context, log, and entry README;
- `vault-memory` separates current memory from archive: old meetings and logs remain evidence, but do not replace the current picture;
- the trust layer for memory makes important claims carry type, source, basis, confidence, and verification date;
- `context-compression` compresses recurring meeting history so the agent does not reread the entire archive or treat outdated decisions as current.

An additional mode is the [GitHub contour repository](./docs/github-contour-repositories.md): a separate repository for a long-lived work contour, where the agent prepares changes through a branch and change request, and the human gets a clear risk/result summary.

## Who It Is For

This kit is useful if you:

- work with agents that can read and change local files;
- keep notes in Markdown or Obsidian;
- want project state to survive individual chats;
- want a clear order for incoming materials, tasks, decisions, and knowledge;
- prefer regular files over closed service-side memory.

This is not:

- a SaaS application;
- an Obsidian plugin;
- magic memory;
- a task tracker replacement;
- a universal methodology for all people and cultures.

## Usage Modes

### Personal Local Vault

The default mode: one owner works with an agent inside a local folder. Project state lives in files, and the agent follows `AGENTS.md`, routing rules, indexes, and logs.

### GitHub Contour Repository

A mode for a team, product, client, or another long-lived area of work. One contour lives in one repository. Boundaries are described by `repository-manifest.yml`; changes go through change requests; private data is not mixed into the ordinary repository layer.

See [GitHub contour repositories](./docs/github-contour-repositories.md) and the [example contour repository](./examples/github-contour-repository/README.md).

## Installation

This repository is not installed as an app. It is a starter folder for a Markdown vault used with an AI agent.

### Option 1: Git

```bash
git clone https://github.com/dzhokhov/markdown-agent-vault.git my-vault
cd my-vault
```

### Option 2: ZIP

Download the repository as a ZIP from GitHub and unpack it into a separate folder, for example `my-vault`.

## First Launch

1. Clone the repository or use it as a template in a safe test folder.
2. Open the folder in an agent that can work with files.
3. Tell the agent:

   ```text
   Open this folder as a working vault. First read AGENTS.md, START_HERE.md, QUICKSTART.md, and ONBOARDING.md. Explain the folder structure and main rules, then walk me through one safe test project with a small file in 00_inbox/.
   ```

4. Put a small test file in `00_inbox/`.
5. Ask the agent to create a training project through `project-creator`, update links, and record the event in the log.
6. Compare the result with [examples/first-session](./examples/first-session/README.md).

A plain chatbot without local file access cannot fully use this methodology. You need an agent that can see the folder, read rules, and propose or make file changes.

## Compatible Agents

Any agent that can work with a local folder can use this methodology: read Markdown files, create new files, modify existing ones, and run simple checks.

| Agent | When to choose it |
|---|---|
| [OpenAI Codex](https://github.com/openai/codex) | When you need an agent in a terminal, editor, or desktop app; it works well with local folders and `AGENTS.md` rules. |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) | When you prefer a terminal/editor agent that reads a project, changes files, and runs commands. |
| Claude Cowork | When you work in Claude Desktop and want to give an agent access to the vault folder. Limitation: Cowork does not automatically read `skills/` as a live skill library. Use [skills/sync-cowork-skills.sh](./skills/sync-cowork-skills.sh) as a workaround. |
| [Cursor](https://cursor.com/) | When you want to work inside a VS Code-like editor with an AI assistant over the whole folder. |
| [Windsurf](https://windsurf.com/) | Another editor with agentic mode and project understanding. |
| [Cline](https://cline.bot/) | Editor extension for running different models while keeping actions under explicit control. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google's terminal agent; useful when you want an open tool with file and command access. |
| [Google Antigravity](https://antigravity.google/) | Useful when you want to manage and monitor several agents over different working folders. |
| [GitHub Copilot coding agent](https://docs.github.com/copilot/concepts/coding-agent/about-copilot-coding-agent) | Useful when the vault is on GitHub and you want changes through issues and pull requests. |

The methodology is not tied to one provider. The key requirement is that the agent reads `AGENTS.md` first and follows routing rules for files, logs, tasks, and knowledge.

### Note on Claude Cowork

Claude Cowork can work with this vault, but skills from `skills/` are not picked up automatically as a single live source.

The starter pack includes a sync script:

```bash
./skills/sync-cowork-skills.sh
```

After changing a skill, rerun synchronization or check status:

```bash
./skills/sync-cowork-skills.sh --status
./skills/sync-cowork-skills.sh
```

By default, the script syncs all skills that contain `SKILL.md`. You can restrict the list through an environment variable:

```bash
COWORK_SKILLS="research parking resume" ./skills/sync-cowork-skills.sh
```

## Navigation

| Path | Purpose |
|---|---|
| [AGENTS.md](./AGENTS.md) | Rules for agent operation inside the vault |
| [START_HERE.md](./START_HERE.md) | Short entry for the first session |
| [ONBOARDING.md](./ONBOARDING.md) | Detailed onboarding |
| [QUICKSTART.md](./QUICKSTART.md) | Quick practical start |
| [00_inbox/](./00_inbox/README.md) | New and unsorted materials |
| [01_now/](./01_now/README.md) | Active projects and current work |
| [02_domains/](./02_domains/README.md) | Long-lived areas of life or work |
| [03_knowledge/](./03_knowledge/README.md) | Reusable knowledge and methodologies |
| [04_logs/](./04_logs/README.md) | Timeline, reviews, and decision logs |
| [90_archive/](./90_archive/README.md) | Completed and outdated material |
| [meta/](./meta/README.md) | Rules, templates, and service indexes |
| [meta/memory/](./meta/memory/README.md) | Memory ledger, anti-memory, and conflicts |
| [skills/](./skills/README.md) | Skills for recurring task types |
| [scripts/](./scripts/README.md) | Local checks |
| [examples/first-session/](./examples/first-session/README.md) | Minimal first-loop example |
| [docs/github-contour-repositories.md](./docs/github-contour-repositories.md) | Guide for separate GitHub repositories by contour |
| [examples/github-contour-repository/](./examples/github-contour-repository/README.md) | Minimal GitHub contour repository example |

## How Is It Different?

| Alternative | What it gives | What this kit adds |
|---|---|---|
| One `AGENTS.md` | Agent behavior rules | A full file architecture: inbox, projects, knowledge, logs, templates, skills, and routing |
| Basic Memory and similar tools | Memory layer and note search | File-based state for projects, decisions, tasks, and sources |
| Cline Memory Bank | Project memory files for development | A broader method: not only code, but also research, meetings, knowledge, incoming materials, and logs |
| Obsidian plugins | Interface features and automation inside Obsidian | This is a file convention and agent operating procedure, not a plugin |
| Ordinary Obsidian vault | Notes and links for a human | Agent rules, project state files, lifecycle rules, and checks |

## Maturity

Status: early public starter pack.

Done:

- portable folder structure;
- agent rules;
- project templates;
- autonomous project creation through `project-creator`;
- material routing;
- current-memory rule and trust layer for claims;
- compressed history for recurring meetings;
- onboarding;
- skills;
- local checks;
- minimal first-loop example;
- minimal GitHub contour repository mode with manifest, templates, example, and validation.

Not ready yet:

- broad instructions for every agent tool;
- external user examples;
- stable compatibility with any agent;
- mature public contribution model.

## Checks

From the repository root:

```bash
python3 scripts/inventory.py
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
```

To validate the GitHub contour repository example:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

## License

MIT. See [LICENSE](./LICENSE).

<!-- AUTOGEN-NAV START -->
## Autogenerated links
### Directory files
- [CHANGELOG.md](./CHANGELOG.md)
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [PULL_REQUEST_TEMPLATE.md](./PULL_REQUEST_TEMPLATE.md)
- [ROADMAP.md](./ROADMAP.md)
- [SUPPORT.md](./SUPPORT.md)
### Subdirectories
- [.github](.github/README.md)
- [03_knowledge](./03_knowledge/README.md)
- [docs](./docs/README.md)
- [meta](./meta/README.md)
- [skills](./skills/README.md)
<!-- AUTOGEN-NAV END -->
