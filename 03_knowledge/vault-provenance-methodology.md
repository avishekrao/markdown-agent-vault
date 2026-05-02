---
id: vault-provenance-methodology
type: reference
status: active
created: 2026-04-30
updated: 2026-04-30
aliases:
  - "Methodology of the origin of knowledge"
  - "Where did knowledge come from"
tags: [knowledge, methodology, provenance, trust]
source_path: "03_knowledge/vault-provenance-methodology.md"
knowledge_criticality: high
verification_status: unverified
curation_mode: manual_edit
---

# Methodology of knowledge origin

## Essence

Any important knowledge in the repository must answer the question: where did it come from, how much can it be trusted, and what source materials support the conclusion.

## Details

### Why is this necessary?

The agent can quickly process incoming materials: meetings, notes, research, tables, letters, documents. Without an explicit connection between the source and the output, over time it becomes unclear:

- the fact was said by a person or inferred by an agent;
- this is a single observation or a stable conclusion;
- can the conclusion be used to solve;
- what source material should be checked if in doubt;
- whether an important clause was lost during the retelling.

The methodology for the origin of knowledge is needed not for bureaucracy, but for trust in the base.

### Basic chainIn a simple case, knowledge goes through four layers:

| Layer | What is this | Where to store |
|---|---|---|
| Source | Raw material: recording, transcript, file, link, note | `00_inbox/` or external source |
| Extract | Brief analysis of the source: facts, solutions, questions | next to the project or in the meeting file |
| Sustainable output | Generalization that the source experiences | `context.md`, `03_knowledge/` or profile file |
| Usage | Solution, plan, task, skill, template | `plan.md`, `tasks.md`, `skills/`, `meta/templates/` |

The further the layer is from the source, the more important the link back is.

### Minimum fields for important knowledge

For files where verifiability is important, add to the service markup:

```yaml
source_type: meeting | file | research | manual_note | synthesis | imported
source_path: "path/or/link/to/source"
derived_from:
  - "path/to/source.md"
confidence: single-source | emerging | confirmed | canonical
verification_status: unverified | in_review | verified_by_me | verified_by_team
```

If the file already uses `source_path` as the path of the file itself in the repository, the sources can be stored in `derived_from`.

### Levels of trust

| Level | When to put | What can you do |
|---|---|---|| `single-source` | One source, one person, one meeting | Keep as an observation, do not build an important solution without checking |
| `emerging` | Several independent signals, but still little data | Use as a hypothesis |
| `confirmed` | Supported by multiple sources or data | Use as a working invariant |
| `canonical` | It was not refuted for a long time and became part of the system | Use as sustainable knowledge |

The level of trust can be raised or lowered. If a counterexample appears, it should be written down next to the conclusion.

### Agent Rule

When an agent transfers knowledge from a source to a stable layer, he must:

1. Save a link to the source.
2. Separate fact from interpretation.
3. Set a conservative level of trust.
4. Write down what exactly changed in `log.md` if the output affects the project.
5. Do not delete the source without the direct decision of the owner.

### Example of secure markup

```yaml
id: customer-support-patterns
type: reference
status: active
created: 2026-04-30
updated: 2026-04-30
aliases:
  - "Repeated support calls"
tags: [support, patterns]
source_path: "03_knowledge/customer-support-patterns.md"
source_type: synthesis
derived_from:- "01_now/projects/example/meetings/meeting-2026-04-20-support.md"
  - "00_inbox/support-export-2026-04.csv"
confidence: emerging
verification_status: in_review
```

### What not to do

- Do not write “it is known that...” without citing the source.
- Do not increase trust just because the text sounds convincing.
- Do not mix quotation, paraphrase and the agent’s conclusion without notes in one paragraph.
- Do not make the work project a long-term home for knowledge that will outlive the project.
- Do not store sensitive sources in a common package just for the sake of verifiability.

### Relationship to other rules

- Routing tasks and knowledge: [task-routing.md](../meta/rules/task-routing.md).
- Recording files and service markup: [write-protocol.md](../meta/rules/write-protocol.md).
- Processing of incoming materials: [inbox-processing.md](../meta/rules/inbox-processing.md).

## Next step

For each important file in `03_knowledge/`, check whether the source of knowledge is clear and whether it is possible to restore the chain from output to source tomorrow.