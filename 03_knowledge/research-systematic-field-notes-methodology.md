---
id: research-systematic-field-notes-methodology
type: note
status: active
created: 2026-04-20
updated: 2026-04-20
aliases:
  - "Methodology for systematically collecting field notes from meetings with clients"
tags: [knowledge, research, methodology, field-notes, customer-insight, meetings]
source_path: "03_knowledge/research-systematic-field-notes-methodology.md"
freshness: seasonal
expires: 2026-10-20
research_type: knowledge
confidence: low
---

# Methodology for systematically collecting field notes from client meetings

## Essence
Research: how to systematically record insights from meetings with agencies/clients so that the data is not lost, but accumulated in all circuits where it can be useful. An important limitation: observations from one meeting should not be recorded as canon - a mechanism is needed for marking the level of confirmation and gradually increasing confidence when confirmation appears from other sources.

## Details

### TL;DR

- ✅ Basic storage unit - **atomic observation (nugget)**: one statement + source + tags + confirmation level. Not a report, not a summary, but a fact from a specific meeting.- ✅ Four-level hierarchy (adapted from Atomic Research Pidcock/Sharon): **Experiment → Fact → Insight → Recommendation**. Each level refers to the previous one, and does not exist on its own.
- ✅ **Confidence ladder** - a mechanism for increasing confirmation: `single-source` → `emerging` (2-3 sources) → `confirmed` (4+ or different types) → `canonical`. An observation from a single encounter is NEVER recorded as canon.
- ✅ **Grounded Theory saturation** - stopping criterion: when new meetings stop giving new categories, but only confirm those already identified.
- ⚠️ Practical tools (Dovetail, Condens, Notion) are secondary - the data structure and protocol are important, not the software.
- ❓ Optimal number of meetings until saturation: literature says 10-15 for customer discovery; for industry observations it may be more - it depends on the variety of types.

### 1. Theoretical foundation: Atomic Research

Daniel Pidcock and Tomer Sharon independently proposed the Atomic Research approach (similar to Brad Frost's Atomic Design): research knowledge is broken down into minimal independent units - **nuggets**.

**Pidcock hierarchy (four levels):**

| Level | Wording | Example (Klimchukovs) ||---------|------------|---------------------|
| **Experiment** | "We did it..." | Introductory meeting with a partner, 2026-04-16 |
| **Fact** | Observation without interpretation | “Ksenia tried AMO CRM - used it for a month, then quit. She's the only sales person." |
| **Insight** | Interpretation of one or more facts | “For agencies of the scale of 1-3 people, CRM is overhead without value if there is no one to coordinate.” |
| **Recommendation** | Insight-Based Action | “INF-15 does not work for this segment. An alternative client context entry point is needed." |

**Key Principle:** A fact does not contain the opinion of the researcher - only what was discovered or expressed by the participant. Interpretation lives on a separate level and makes explicit reference to facts.

**Sharon hierarchy (three levels):** observation + evidence + tags - simpler, but does not separate fact and interpretation.

For our vault, Pidcock's adaptation is preferable: it clearly separates "what they said" from "what we think it means" - which is critical when `confidence: single-source`.

### 2. Confidence Ladder: from observation to canon

Central problem: observation from one meeting is not the truth, but it is not garbage either. We need a scale.

**Suggested levels:**| Level | Criterion | How to label | What can you do |
|---------|----------|-----------------|-----------------|
| `single-source` | One meeting / one person | `confidence: single-source` in frontmatter | Record as field note. Do not refer to it as a fact in decisions. |
| `emerging` | 2-3 independent sources confirmed | `confidence: emerging` + links to sources | Formulate a hypothesis. You can refer to it with the “emerging pattern” clause. |
| `confirmed` | 4+ sources OR different types of confirmations (meeting + data + external resources) | `confidence: confirmed` | Use as a working invariant in context.md. |
| `canonical` | Confirmed, adversarial verified, not refuted for ≥3 months | `confidence: canonical` | Transfer to domain knowledge and build product solutions on this. |

**Boost Mechanism:**
When a new confirmation appears, update `confidence` in frontmatter, add a link to the confirmation source, write down the date and context of the promotion. Reduction is also possible (counterexample found).**Analogy from Grounded Theory:** theoretical saturation is the point at which new data stops generating new categories and only confirms existing ones. Glaser & Strauss: “no additional data are being found whereby the sociologist can develop properties of the category.” For customer discovery this is usually 10-15 interviews; for industry taxonomy - more, depending on the diversity of segments.

### 3. Storage structure: where to route what

Observations from the meeting concern different contours. The current vault already has the required structure; the task is to determine the route for each data type.

**Routing by surveillance type:**

| Data type | Where | Format | Example |
|-----------|------|--------|--------|
| Field notes (stack of observations from one meeting) | `03 knowledge/field-notes-{topic}-{date}. md` | Markdown with frontmatter `confidence: single-source` | `field-notes-agency-operations-klimchukovy-2026-04.md` |
| Fact about a specific person/organization | Card in `03_knowledge/contacts-network/persons/` or `orgs/` | Section "Profile" or "Notes" | “The partner compared two approaches to launching” → partner card |
| Design-Specific Implications | `01_now/projects/<project>/context.md` | Link to field note + summary | “INF-15 does not work for agencies without CRM” → context.md AI Hub || Cross-meeting pattern (when ≥2 meetings confirmed) | `03 knowledge/patterns-{domain}. md` or a separate file | Markdown with `confidence: emerging` | “CRM anti-pattern for small agencies” → separate pattern when confirmed by Fedoseeva |
| Open question for next meetings | `01_now/projects/<project>/plan.md` §Open Questions | Line with a link to field note | “The Depreciation of Deep Semantics—Will Others Confirm?” |
| Task (something needs to be done) | `tasks.md` related project | Task line | “Prepare a preread for the Klimchukovs’ live demo” |

### 4. Meeting processing protocol (operational checklist)

**Step 1. Summary of the meeting** (on the day of the meeting or the next one)
- Transcript → meeting-processing skill → summary in the project folder
- Update participant cards, interactions.csv, contacts-index

**Step 2: Retrieve Atomic Observations** (same session)
- Re-read the entire transcript with the focus “what new did I learn about the market / client / product”
- For each observation, record: (a) quote or paraphrase, (b) who said it, (c) context, (d) implication for the project
- Separate facts and interpretations (Pidcock levels)

**Step 3: Routing** (same session)
- Send each observation to the desired circuit according to the table from §3- Field notes - in `03_knowledge/`, consequences - in `context.md`, tasks - in `tasks.md`
- Put `confidence: single-source` on all new observations

**Step 4. Cross-check** (next meeting or research)
- Before each new meeting, run open questions from previous field notes
- If a new meeting confirms / denies - update confidence + add a link
- When reaching `emerging` - put it in a separate pattern file

**Step 5. Periodic synthesis** (once a month or with 5+ field notes)
- Scan all field notes for the period
- Identify recurring themes → design as patterns
- Update confidence for confirmed observations
- Close refuted hypotheses

### 5. Adaptation to the current vault

What already works:
- `meeting-processing` skill covers Step 1 (summary, cards, interactions)
- YAML frontmatter with `confidence: single-source` is already used in the Klimchukovs’ field notes
- Routing along circuits is described in AGENTS.md and task-routing

What to add:
- **Step 2 formalize as part of meeting-processing** - after the summary, automatically proceed to extracting atomic observations
- **Routing table** (§3) — add to the meeting-processing skill or to AGENTS.md as a subsection- **Confidence ladder** — add to write-protocol.md as a marking rule
- **Periodic synthesis** (Step 5) — add the protocol to the vault-review or as a separate scheduled task

### Alternative viewpoints

- **Minimalism:** some practitioners (NN/g, Teresa Torres) believe that it is enough to maintain an “opportunity solution tree” - a tree where observations are tied to opportunities. A separate nuggets repository is overhead for small teams.
- **Tooling-first:** Dovetail, Condens, Marvin - SaaS tools for insight repositories. Their advantage: AI-assisted tagging, automatic clustering. Disadvantage: vendor lock-in, data not in vault.
- **“Do not record, but act”:** lean approach - if observation does not lead to immediate action, it is not worth recording. Counterargument: in our case, one observation does not lead to action, but five similar ones do. Without accumulation, the pattern will not appear.

### Blind spots and restrictions

- The study is based on literature on UX Research and Customer Discovery. There are few direct analogues of “field notes from B2B sales meetings → product development” in the literature - it’s more of an adaptation.- Confidence ladder (§2) is an original design that has not been validated in practice. Thresholds (2-3 for emerging, 4+ for confirmed) are starting, subject to calibration.
- The issue of ownership has not been addressed: who is responsible for periodic synthesis when there are a lot of meetings.
- Grounded Theory in its pure form involves coding (open → axial → selective coding). In vault, this corresponds to tags → patterns → domain knowledge, but the formal coding protocol is not described.

## Sources

### Academic
- [Glaser & Strauss - Grounded Theory, theoretical saturation](http://www.scielo.br/j/reben/a/h6skK6tnvW4phBYzvxpWJ3Q/?lang=en) - methodology for achieving saturation in qualitative research
- [Data Saturation in Grounded Theory](https://nsuworks.nova.edu/cgi/viewcontent.cgi?article=2994&context=tqr) - “the mysterious step” - when to consider data sufficient
- [A Guide to Field Notes for Qualitative Research](https://www.researchgate.net/publication/315944152_A_Guide_to_Field_Notes_for_Qualitative_Research_Context_and_Conversation) - contextual and conversational field notes

### Practical
- [Daniel Pidcock — What is Atomic UX Research?](https://blog.prototypr.io/what-is-atomic-research-e5d9fbc1285c) — original article: experiments → facts → insights → recommendations
- [User Interviews - Atomic Research Nuggets](https://www.userinterviews.com/ux-research-field-guide-chapter/atomic-research-nuggets) - a practical guide to nugget-based repositories
- [Maze - What is Atomic Research?](https://maze.co/collections/user-research/atomic-research/) - overview of application in UX teams- [Dovetail - Atomic Research: From reports to consumable insights](https://dovetail.com/blog/atomic-research/) - adaptation for product teams
- [Teresa Torres — Customer Interviews](https://www.producttalk.org/2022/12/customer-interviews/) — interview + opportunity solution tree

### Commercial (take into account bias)
- [Neil Turner - Building a Customer Insights Repository](https://medium.com/ingeniouslysimple/building-a-customer-insights-repository-347d382e2ed7) - insight repository structure (the author is a UX consultant, does not sell software)
- [Insight7 - How to Build an Insights Repository](https://insight7.io/how-to-build-an-insights-repository-in-2024/) - review, but promotes its own product

## Next step

1. Add confidence ladder to `meta/rules/write-protocol.md` as a formal marking rule
2. Extend the meeting-processing skill with Step 2 (retrieving atomic observations)
3. Add monthly review field notes to the vault-review protocol
4. After 3-5 meetings with agencies, conduct the first synthesis and check whether the confidence ladder works in practice