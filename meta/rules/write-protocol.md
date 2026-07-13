---
id: write-protocol
type: rules
status: active
created: 2026-03-30
updated: 2026-07-13
aliases:
  - "File write protocol"
  - "Write protocol"
tags: [rules, write, files, vault-hygiene]
source_path: "meta/rules/write-protocol.md"
---

# Creating and Changing Files in the Vault

## Essence

Unified write rules: frontmatter, structure, links, index updates, anti-fragmentation, memory updates, and lifecycle handling. Applies when creating or editing any vault file.

## 1. YAML Frontmatter

Every Markdown file must have:

```yaml
id: unique-slug
type: note | project | log | tasks | registry | reference | plan | index | rules
status: active | draft | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases:
  - "Short readable name"
tags: [relevant, tags]
source_path: "path/from/vault/root.md"
```

Optional fields:

```yaml
freshness: evergreen | seasonal | ephemeral
expires: YYYY-MM-DD
knowledge_criticality: low | medium | high | critical
verification_status: unverified | in_review | verified_by_me | verified_by_team
curation_mode: none | manual_edit | llm_explicit_request | imported_not_curated
```

Use `verification_status: verified_by_me` only after manual user verification. Imports default to `unverified` and `imported_not_curated`.

### 1.1. Pattern Confidence for Field Observations

Observations from meetings, interviews, and field studies can use `pattern_confidence`. This is not editorial verification; it is the maturity of an observation across independent sources.

```yaml
pattern_confidence: single-source | emerging | confirmed | canonical
```

| Level | Criterion | Allowed use |
|---|---|---|
| `single-source` | One meeting or one person | Record as a field note. Do not use as fact in decisions. |
| `emerging` | 2-3 independent sources | Formulate as a hypothesis or emerging pattern. |
| `confirmed` | 4+ sources or mixed evidence types | Use as a working invariant in `context.md`. |
| `canonical` | Confirmed and not refuted for 3+ months | Treat as domain knowledge. |

Raise confidence when new evidence appears. Lower it when a counterexample appears. A single-meeting observation defaults to `single-source`.

Older files may contain `confidence: single-source | emerging | confirmed | canonical`; do not mass-migrate them. On first meaningful touch, move that value to `pattern_confidence`.

### 1.2. Trust Fields for Important Claims

Important claims that shape current work, decisions, current picture, tasks, risks, constraints, or hypotheses get a minimal trust block:

```yaml
claim_type: observed | stated_by_user | stated_by_other | inferred | decision | assumption | hypothesis | preference | constraint | plan | risk | status | historical
source:
  - ""
evidence:
  kind: direct_user_statement | direct_quote | meeting_note | document_fact | agent_inference | repeated_pattern | external_source | unknown
  strength: high | medium | low
confidence: high | medium | low
last_verified: YYYY-MM-DD
write_policy: auto | suggest | human_review_required | locked
```

Rules:

- `confidence: high | medium | low` is trust in a specific claim.
- `pattern_confidence` is maturity of a repeated observation.
- `verification_status` is editorial or human file verification.
- `claim_type: inferred`, `assumption`, `hypothesis`, and `plan` must not be used as facts without additional basis.
- If there is no verifiable basis, use `evidence.kind: unknown` and `evidence.strength: low`.
- Strategic decisions, goals, memory rules, and decision-status changes use `write_policy: human_review_required` or `locked`.

## 2. Recommended Body Structure

- `## Essence` - one sentence explaining what this is and why it exists.
- `## Details` - main content.
- `## Next Step` - if useful.

Self-sufficiency test: if an agent reads only this file, can it understand what the file is about and when to use it? If not, the file is incomplete.

## 3. Link Standard

- Use clickable Markdown links: `[Readable anchor](./relative-path.md)`.
- Anchor text should be human-readable, not just a filename.
- Use relative paths with `.md` extension.
- Avoid bare paths and paths in backticks when a clickable link is expected.

Before writing a relative link, count directory depth. After writing, mentally resolve the path or use a script to confirm it exists.

## 4. Mandatory Protocol After Writing

After creating or substantially changing a file, perform all applicable steps in this order: slow layers first, fast layers last.

1. **Update project `plan.md`** if Goal, Intent Lock, Owner Interaction Policy, Milestone, Appetite, Drift Guard, Contingency, Acceptance, or Quality Criteria changed.
2. **Update project `context.md`** only when a durable invariant appears: term, metric, source of truth, or constraint.
3. **Update working context** if `README.md` or `context.md` declares one. This is the recomputed current-state layer: what matters now, what changed, what is stale, what was refuted.
4. **Write a short `log.md` entry.** Date, what happened, what decision changed, link to details. Keep it to 3-7 bullets. Detailed content belongs in a separate file.
5. **Update `tasks.md`** only for execution queue: active step, next step, waiting. Reflection belongs in `plan.md`, not in `tasks.md`.
6. **Update delegations** when the decision concerns another person in a contour: `01_now/ops/<contour>/delegations/<person-slug>.md`.
7. **Update personal tasks** when the owner gains an external personal obligation unrelated to the project: `01_now/personal/tasks.md`.
8. **Update the folder `README.md`** so a future agent can discover the file.
9. **Check cross-links** in related documents.
10. **Update `01_now/README.md`** only when a project is created or closed.
11. **Routing self-check:** if a future session asks about this document, can it find it through README -> plan -> context -> working context/file?
12. **Write to the memory ledger** if trust, freshness, status, claim type, conflict, working context, or a strategic decision changed: [ledger.md](../memory/ledger.md).
13. **Clean up temporary files** after knowledge integration.

Order matters: `plan` -> `context` -> working context -> `log` -> `tasks` -> delegations/personal -> `README` -> memory ledger. Slow layers must lead fast layers.

### 4.1. Writing in a GitHub Contour Repository

If the root contains `repository-manifest.yml`, read it first and apply [github-contour-repositories.md](./github-contour-repositories.md).

Special rules:

- `may_edit_without_asking` means the agent may prepare a branch and change request, not silently edit the main branch.
- Check `agent_policy.ask_before` and `agent_policy.never_commit` before writing.
- Stop and ask before private data, deletion, moving, access rules, `AGENTS.md`, `repository-manifest.yml`, or another contour is touched.
- After a meaningful change, add a short `log.md` entry if the manifest allows it.
- Before a change request, run checks from `validation.required_before_change_request`.
- The change request description must explain what changed, why, touched files, private-data risk, checks run, and what a human must confirm.

## 5. Mid-Flight Sync

Do not wait until the end of a long task if current state would be hard to reconstruct from chat.

Update `log.md` immediately when:

- a decision is made;
- a milestone is completed;
- a blocker appears;
- plan or approach changes;
- an important file is created or a visible risk is closed.

Update `context.md` only when durable knowledge appears:

- new term, invariant, or constraint;
- success metric or quality criterion;
- source-of-truth document or mandatory dependency;
- stable agreement about how the project works.

Update working context when it is declared and the event changes what currently matters. It is not chronology and does not replace `context.md`.

Do not turn `log.md` into a backlog. Do not write temporary turns into `context.md`. Do not keep several significant decisions only in chat.

Mandatory trigger: if the next step cannot be reliably restored from project files, or several unsaved decisions/finds have accumulated, update `log.md`, `context.md`, and working context as applicable before continuing.

## 6. `plan.md` and `tasks.md`

Every active project has two task-level files:

- `plan.md` - slow contract: Goal, Intent Lock, Owner Interaction Policy, Non-goals, Appetite, Source of truth, Milestones with Acceptance, Quality Criteria, Blockers, Drift Guard, Contingency, Review Protocol.
- `tasks.md` - fast execution queue: Current Milestone, Active/Next/Waiting steps, local Exit Criteria, short Drift Guard.

New projects are created through [project-creator](../../skills/project-creator/SKILL.md). The skill extracts context from the chat or command, checks data ownership, writes starter files, and updates indexes. Manual assembly is acceptable only when the skill is unavailable.

When creating a project or substantially changing `plan.md`, the agent writes the plan and quality criteria itself. The owner must not be asked to write plan items, invent criteria, or review the plan line by line. If the foundation cannot be chosen safely, ask one packet of up to three short questions about goal, boundary, priority, cost of error, or source of truth. Each question includes the agent's recommended option and asks the owner to confirm or correct it.

Project modes:

- `operational` - work that does not change an executable system.
- `development` - code, scripts, tests, schemas, data contracts, runtime, CI, build, or release work.

`tasks.md` rules:

- State `Task Mode: operational | development`.
- Keep exactly one `Active` / `Active Step`.
- Work outside `Active` or `Next` requires updating `plan.md` when the vector changes, or `tasks.md` when only the queue changes.
- Do not accumulate a long done list; history belongs in `log.md`.
- Do not put `Goal`, `Milestones`, `Contingency`, `Appetite`, or `Quality Criteria` in `tasks.md`.
- Do not put vague reflection such as "figure out X" in `tasks.md`.

Drift protocol:

1. Edit `plan.md` first.
2. Add one `log.md` line: "drift: was X, became Y, reason Z".
3. Then update `tasks.md` and resume work.

## 7. Anti-Fragmentation

- Use an existing folder first.
- Do not create a subfolder for 1-2 files.
- Create a new subfolder only when 5+ files are expected or the group is long-lived.
- Keep depth no deeper than 3-4 levels from the logical root.
- Serial files use order in filenames, not nested folders.

## 8. File Lifecycle

- Unknown destination -> `00_inbox/`.
- Active work -> `01_now/`.
- Long-lived area -> `02_domains/`.
- Reference knowledge -> `03_knowledge/`.
- Diary or chronology -> `04_logs/`.
- Outdated or completed -> `90_archive/`.

When creating any new file, database, cache, or dump, decide:

- **TTL:** when can it be deleted? 7d / 30d / 90d / manual / never.
- **Cleanup:** who deletes it and how? script / manual review / cron.
- **Registration:** register it in [cleanup-registry.md](../cleanup-registry.md) when it is not a one-off file.

When processing a file from `00_inbox/`, write to `00_inbox/PROCESSING_LOG.md`: what was processed, where it went, and whether status is processed or partial.

## 9. Deletion and Archiving

- When moving to `90_archive/`, remove or mark archived links in README and context files.
- When deleting a file, clear all links to it.

## 10. Temporary Sources

- Do not leave links to temporary files in final documents.
- Temporary sources are disposable material for synthesis.
- After integration, remove intermediate files and verify that links to them are gone.

## 11. Reverse Synchronization After Migration

After any migration or data-format change:

1. Find scripts, templates, and rules that generate the affected data.
2. Update each one to produce the new format.
3. Test the fresh-start path: if a new agent runs the process from scratch, will it get the new format? If not, migration is incomplete.
