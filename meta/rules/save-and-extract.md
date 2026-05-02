---
id: save-and-extract
type: rules
status: active
created: 2026-03-30
updated: 2026-03-30
aliases:
  - Conservation Threshold
  - "When to maintain results"
tags: [rules, save, knowledge, extraction]
source_path: "meta/rules/save-and-extract.md"
---

# Conservation Threshold and Knowledge Extraction

## The essence
When to save results in vault, when not. How to Extract Reused Knowledge from Projects

## The Triple Filter: Do You Keep the Results?

After completing the task, evaluate according to three criteria:

1. **Reusability.** Useful in future sessions? (Dictionary, yes. "What the weather is" No.
2. **Unique.** Does it contain data that is not in the database? (Budget analysis, yes. Retelling the document - No.
3. ** Volume.** More than 1 paragraph? (2 lines to not create a file.)

**Although 2 out of 3** → offer a specific action: "Save to `03_knowledge/adtech-market-2026.md`?"
Don't save, don't ask.

## Best Practices and Resources – Always

When the user asks to conduct a discussion, collect best practices, study the approaches:

1. Save the result in `03_knowledge/`. If there is no suitable domain, create (with anti-fragmentation in mind).
2. Format: full note from YAML, `## Essence`, **links to sources** (URL, authors). Without sources, the discourse loses credibility.
3. Link to the project: if the spacing in the context of the project is a link from `context.md`.
4. Do not ask "save?" - always save. The mirror, by definition, passes a triple filter.
5. Without an explicit project, offer to create a project or standalone note.

**Motivation: * The information collected is the most valuable by-product of LLM. Losing the recess due to the end of the chat is inexcusable.

## Extraction of knowledge from projects

When a project creates a document that is useful outside of the project:
- Main file in `03_knowledge/` or `02_domains/`
- In the project → link from the context. md

Examples: dictionary of terms → `03_knowledge/`, procedure → `03_knowledge/`, contacts and roles → `02_domains/work/`.
