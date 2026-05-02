---
id: skill-sync-cowork
type: rules
status: active
created: 2026-04-22
updated: 2026-04-22
aliases:
  - "Cowork Skill Synchronization"
  - "Skill synchronization rule"
tags: [rules, skills, cowork, sync]
source_path: "meta/rules/skill-sync-cowork.md"
globs: "skills/**"
---

# Rule: synchronization of skills vault → Cowork

## When it works.

If you change files in `skills/` - create a new skill, edit SKILL.md, delete the skill.

## The essence

Vault (`skills/`) is the only source of truth for custom skills. Cowork can hold two copies: the personal skills in `~/.claude/skills/` and the active cache Claude Desktop `~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/.../skills/`. After editing the skill in vault, you need to make sure that `~/.claude/skills/` points to vault through symlinks, and `skills-plugin` contains fresh physical copies through `rsync`.

## What to do with an agent

### After editing the existing skill

1. If the skill is included in the Cowork include-list (see below) - ** be sure to run `./skills/sync-cowork-skills.sh` after editing**. `skills-plugin` is a physical `rsync` copy, not live-link; without running the script, Cowork will remain on the old version.
2. After launch, check `./skills/sync-cowork-skills.sh --status`: `~/.claude/skills/` should show `symlink ✓` and `skills-plugin` should show `copy ✓`. Absolute symlinks of the host in `skills-plugin` are prohibited: inside Cowork VM they are broken.
3. Inform the owner: Skill `<name>` updated and synchronized. Cowork will pick up changes at the next session (or after `/reload-plugins`).

### After creating a new skill

1. Ask the owner, “Do you need this skill in Cowork?” If yes, I will add to the include-list and create a symlink.
2. If yes:
   - Add the name of the skill to the `INCLUDE_SKILLS` array in `skills/sync-cowork-skills.sh`
   - Execute: `./skills/sync-cowork-skills.sh` (or ask the owner to run if there is no access to the host terminal). The script creates a symlink in `~/.claude/skills/` and copies the skill to an active `skills-plugin` Cowork cache via `rsync`.
3. If not, the skill remains vault-only (available in Claude Code CLI, but not in Cowork).

### After squill removal

1. If the skill was included-list, remove it from `INCLUDE_SKILLS` to `skills/sync-cowork-skills.sh`.
2. Run `./skills/sync-cowork-skills.sh` - the script will remove the orphaned symlink

## Include-list (relevant)

Skills synchronized in Cowork via `rsync` copies in `skills-plugin`:

meeting-processing, research, parking, resume, landing-copywriter, meta-ads-bulk, meta-ads-campaign-builder, meta-ads-campaign-structure, meta-ads-creative, meta-ads-creative-factory, meta-ads-optimizer, meta-ads-preflight, meta-ads-reporter, meta-ads-transport-api, meta-ads-transport-human, meta-ads-transport-ui.

Full list and logic of exceptions: `03_knowledge/cowork-skill-sync-research.md`.

## What not to do

- Do not edit Skills in `~/.claude/skills/` or `skills-plugin` directly – all edits via vault
- Do not copy skills manually - only `rsync` through the script
- Do not add skills that require CLI-only tools (git, make) to the include-list - they are useless in Cowork.
