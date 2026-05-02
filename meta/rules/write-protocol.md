---
id: write-protocol
type: rules
status: active
created: 2026-03-30
updated: 2026-04-15
aliases:
  - "File Recording Protocol"
  - "Write protocol"
tags: [rules, write, files, vault-hygiene]
source_path: "meta/rules/write-protocol.md"
---

# Create and modify files in vault

## The essence
Unified set of rules when recording: frontmatter, structure, links, index updates, anti-fragmentation. Used when creating or editing any* vault file.

## 1.YAML frontmatter (mandatory)

Each markdown file must have:

```yaml
id: unique-slug
type: note | project | log | tasks | registry | reference | plan | index | rules
status: active | draft | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases:
  - "Short Russian Name" #1 Distinct at Vault Level
tags: [relevant, tags]
source path: "path/from/root/vault." md
```

Optional fields:
```yaml
freshness: evergreen | seasonal | ephemeral # by default seasonal
expired: YYYY-MM-DD #date review
knowledge_criticality: low | medium | high | critical
verification_status: unverified | in_review | verified_by_me | verified_by_team
curation_mode: none | manual_edit | llm_explicit_request | imported_not_curated
```

`verification_status: verified_by_me` is placed **only after manual user verification **. For imports by default: `unverified` + `imported_not_curated`.

### Confidence Ladder for Field Observations (MUST)

Observations from meetings, interviews and field studies are labeled with the `confidence` field in the frontmatter. This ***** editorial check (`verification_status`) is the degree to which an observation by independent sources is confirmed.

```yaml
confidence: single-source | emerging | confirmed | canonical
```

| Level | Criterion | What can be done |
|---------|----------|-----------------|
| `single-source` | One meeting/one person | Record as field note. Do not refer to it as fact in decisions. |
| `emerging` | 2-3 independent sources | Formulate a hypothesis. Refer to the “emerging pattern” clause. |
| `confirmed` | 4+ source OR different types (meeting + data + mirror) | Use as a working invariant in context.md. |
| `canonical` | Confirmed, not refuted ≥3 months | Domain knowledge. Building product solutions. |

**Increase:** When a new confirmation appears, update `confidence`, add a source link, record the date.
**Decrease:** When a counterexample is detected, lower `confidence` and record a counterexample.
**Default: * Any observation from a single meeting receives `single-source`. No exceptions.

Applied to: `field-notes-*.md`, observations in contact cards, hypotheses in research files.
It does not apply to: actual data (dates, figures, quotes), design decisions, vault rules.

Methodology: [research-systematic-field-notes-methodology.md](../../03_knowledge/research-systematic-field-notes-methodology.md)

## 2. Recommended body structure

- `## Essence` – one sentence: what it is and why (for LLM search)
- `## Details` – Main Content
- `## Next step` - if applicable

** Self-sufficiency test: ** If LLM reads only this file, will it understand what it is about and who is useful to? If not, the file is incomplete.

## 3. The reference standard in vault (Obsidian)

- Only clickable Markdown links: `[Comprehensible anchor](./relative-path.md)`
- Anchor is a human-readable description, not a file name
- Relative paths (`./`, `../`) with `.md` extension
- Prohibited: paths in backticks as links, file-name anchors (`[context.md](...)`), bare paths

### Verification of Relative Paths (Critical)

Before writing a link, calculate the depth:
1. Determine the source file level from the vault root (by `/`)
2. Each `../` raises one level
3. After all `../` should be the root vault, then the absolute path.

Example: file at depth 4 (`01_now/projects/foo/tasks/task.md`) → reference to `00_inbox/bar.md` requires **4** level of lift: `../../../../00_inbox/bar.md`.

**Rule:** After writing the link, mentally allow the path. If you use a script, turn on `os.path.exists()`.

## 4. Links in dialogue (Cowork/Claude Code)

Any file in the user's response is a clickable `computer://` link:
- `[Clear name](computer:///sessions/.../path/to/file.ext)]`
- Do not leave bare paths in bectics

## 5. Mandatory protocol after recording

Once a file has been created or substantially modified, follow **all applicable steps** in the specified order (slow layers → fast layers):

1. ** Update the `plan.md` project** (if Goal, Milestone, Appetite, Drift Guard, Contingency or Acceptance have changed). `plan.md` is a slow project contract; it is ruled before anything leaks into `context.md` or `tasks.md`. See [Rule 12 of AGENTS. md](../../AGENTS.md).
2. **Update the project `context.md`** - only when a stable invariant appears (term, metric, SoT, limitation). Episodic meeting content does not go here; it lives in `<meeting>.md` under `## Mentioned in passing` with a canonical tag. See [task-routing.md](./task-routing.md).
3. **Record in `log.md` project.** Short entry: date, what happened, what decision, link to artifact. Maximum 3-7 bullets. Detailed content is in a separate artifact, not log.md. See [AGENTS.md Rule 5](../../AGENTS.md).
4. **Update `tasks.md`** - Active/Next/Waiting only. The thinking (“to understand what to do with X”) goes not here, but in `plan.md` under the corresponding milestone. Goal, Milestone, Contingency in `tasks.md` are prohibited.
5. **Update delegation** – if the decision/step concerns the delegate, update the line to `01_now/ops/<contour>/delegations/<person-slug>.md` (one line + link to the external tracker as SoT). If the external tracker already operates in the circuit as a living working layer, do not start the second living layer in the general markdown loop: update the external tracker, and touch `delegations/` only if it is a short index or an archive transition layer. See [task-routing.md §delegations](./task-routing.md).
6. **Update personal `01_now/personal/tasks.md`* – if there is an external obligation of the owner, not related to the project. Ambient capture without MR-diff.
7. **Update the `README.md` section** where the file is located. Criterion: After reading README, LLM learns that the file exists.
8. **Cross-links** – Check backlinks in related documents.
9. **Update `01_now/README.md`* – only if the project is new or closed.
10. **Self-check routing:** If tomorrow a new LLM session asks about the subject of a document, will it find it through the README → plan.md → context.md → file? No, missed a step.
11. **Temporary artifact cleansing* – delete intermediate files after knowledge integration.

** Order critical:** `plan` → `context` → `log` → `tasks` → `delegations/personal` → `README`. The slow layers are always ahead of the fast ones. Disorder = drift of the plan over the old contract.

## 5.1. Mid-flight sync for project files

Don’t wait for the end of the task if you have a condition that will be difficult to recover from chat.

### When to update `log.md`

`log.md` is updated immediately upon event, not only upon finalization:
- a decision has been made;
- completed milestone;
- Blocker found;
- Changed plan/approach;
- An important artifact has been created or a noticeable risk has been closed.

`log.md` answers the question: What happened and why?

### When to update `context.md`

`context.md` is updated only when **persistent knowledge** is available for future sessions:
- new term, invariant, limitation;
- Metrics of success, quality criteria;
- source-of-truth document or mandatory dependency;
- New stable agreement on how the project works.

`context.md` answers the question: **What is now considered consistently true about the project**.

### What not to do

- Do not convert `log.md` to backlog.
- Do not write in `context.md` temporary turns and small chronology.
- Do not keep a few significant decisions/finds only in chat until the end of a long cycle.

### Mandatory Sync Trigger

If the next step cannot be reliably restored from the project files, or several unsaved solutions / finds have already accumulated in the chat, the agent must first update `log.md` and / or `context.md`, and then continue to work.

## `plan.md` + `tasks.md`: contract and execution queue

From April 2026, any active project must have two files:

- **`plan.md` is a slow contract. Goal, Non-goals, Appetite, Source of Truth, Milestones (with Acceptance), Drift Guard, Contingency. It changes when goals or boundaries change.
- **`tasks.md` is a fast execution queue. Only Active/Next/Waiting agent steps in the current milestone.

Full methodology: [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md)]. Tactical checklist: [task-routing.md](./task-routing.md)] Rules of ownership: [AGENTS.md Rules 11–14](../../AGENTS.md)]

### Regime of the project

Before deep work, the agent must select one mode (as specified in `plan.md`, not `tasks.md`):

- `operational`: Normal tasks without changing the executable system.
- `development` – code, scripts, tests, schema/data contracts, runtime, CI, build/release.

### Mandatory Rules for `tasks.md`

- In the file, clearly indicate `Task Mode: operational | development`.
- Keep only one `Active`/`Active Step`.
- If you are going to work outside of `Active` or `Next`, first update `plan.md` (if the vector changes) or `tasks.md` (if only the queue).
- Don’t dig up a long list of completed items: the story should live in `log.md`.
- **Prohibition:** `Goal`, `Milestones`, `Contingency`, `Appetite` — all in `plan.md`, not in `tasks.md`.
- ** Prohibition:** lines such as "understand what to do with X", "deal with Y" is not execution, it is reflection; its place in the corresponding milestone in `plan.md` as an open question.
- **Prohibition:** Delegating to an employee ("Dima will do X") is in `delegations/<person-slug>.md`. Personal obligations - in `01_now/personal/tasks.md`.

### Structure of `tasks.md` for `operational`

Minimum: `Active`, `Next`, `Waiting`, `Backlog`. Without `Goal`, it's in `plan.md`.

### Structure of `tasks.md` for `development`

Minimum: `Active Step`, `Exit Criteria`, `Drift Guard (short)`, `Next`, `Backlog`. `Current Milestone` refers to the corresponding clause in `plan.md` and does not duplicate it. Blockers – `plan.md §Blockers` as a first-class entity, the `Blocked` section does not exist in `tasks.md`.

### Drift protocol (mandatory)

If the agent changes the approach, scope, order of implementation, or finds that the current milestone no longer leads to the goal:
1. First, edit **`plan.md`** (changed Milestone, Acceptance, Drift Guard, Contingency or Non-goals).
2. One line in `log.md` is "drift: was X, became Y, cause Z."
3. Only then update `tasks.md` and resume work.

Disorder = the contract changes under the guise of execution, and the future agent will not find a trace of the solution.

## 6. Anti-fragmentation folders

- Use the existing folder first. New - only if the group is otherwise lost.
- Prohibited: Subfolder for 1-2 files.
- New Subfolder: Minimum 5+ files expected or long-lived outline.
- Depth: no deeper than 3-4 levels from the logical root.
- Serial files are the order in the name (`YYYY-MM-DD type number. md`), not in the folder structure.

## 7. File life cycle

- It's unclear where `00_inbox/`
- Analysis: active work → `01_now/`, area → `02_domains/`, help → `03_knowledge/`, diary → `04_logs/`, outdated → `90_archive/`
- `01_now` only stores the operating room (1-4 weeks). Extract it to `03_knowledge/`.
- Regulations [Vault Lifecycle SOP](../vault-lifecycle-sop.md)]

## 8. Lifecycle Artifacts (MUST)

When you create any new file, database, cache, dump – immediately answer:
- **TTL:** When can this be removed? (7d / 30d / 90d / manual / never)
- **Cleanup:** Who will delete and how? (script vault-hygiene / manual vault review / cron)
- **Register:** register it in [cleanup-registry.md](../cleanup-registry.md) if it is not a one-time file.

If the file from `00_inbox/` is written to `00_inbox/PROCESSING_LOG.md` after processing:
What is processed, where is transferred, status ( partial processed / ). partial).
Details: [Inbox](./inbox-processing.md) processing protocol]

Complete rules: [Cleanup by Design](./cleanup-by-design.md)]

## 9. Deletion and archiving

- When moving to `90_archive/`, delete/tag `[archived]` links in README and context.md.
- When you delete a file, clear all links to it.

## 10. Integrating knowledge from time sources

- References to temporary files cannot be left in the final documents.
- Temporary sources are disposable material for synthesis.
- After integration, delete intermediate files, check for no links to them.

## 11. Reverse synchronization after migration

After any migration or change of data format:
1. Find all the scripts, templates, regulations that generate the affected data.
2. Update each to create data in a new format.
3. Test: “A new agent launches imports from scratch – will it get a new format?” The migration is not complete.
