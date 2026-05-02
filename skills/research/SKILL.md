---
name: research
description: >
Conducting qualitative research with the help of an LLM with compensation for distortions and the mandatory preservation of the results in the knowledge base.
Be sure to use this skill when the user asks: to conduct a discussion, research the topic, collect best practices,
To study approaches, to review, to compare options, to find information about something, to understand the topic "what is known about X",
"How Y works", "What are the approaches to Z", "Get information", "learn the question". Also use it for any request,
It involves the collection and structuring of external information, even if the word "reference" is not pronounced.
Do not use simple factual questions with an unambiguous answer ("what is the capital of France").
---

# Research – Skill of Quality LLM Research

## Why is this skill?

LLM-speech without methodology produces beautiful but unreliable results: hallucinations look like facts, commercial content masquerades as best practices, vocal minority replaces the real picture. This skill applies a proven methodology so that the result is not only complete, but also reliable - and keeps it in the knowledge base so that the work does not disappear with the chat.

Full methodology with sources: `03_knowledge/llm-research-methodology.md`. Read it before you first use Skill to understand the theory. Below is the operational protocol.

---

## Phase 0. Classification of the request

Before starting, determine the type of study - it depends on the depth, stopping criteria and the format of the result.

**Research-Knowledge** (How is Personal CRM?)
Wide view, many points of view, maximum coverage. Stop criterion: saturation (new requests do not provide new information).

**Research solution** (“Which CRM should I choose?”)
→ A narrow focus on user limitations, clear criteria, quick action. Stop criterion: sufficient data to make a decision.

Set the type at the start of the job. A typical trap is to start with a solution, to slide into an endless accumulation of knowledge.

For research-solution immediately check with the user:
- What are the selection criteria?
- What are the constraints (budget, time, skills, ecosystem)?
- What is the acceptable level of uncertainty?

### Create a result file before collecting (required)

> This action is performed NOW, before moving to Phase 1.
> If the file is not created, do not move.

1. Identify the file name: `research-{topic-kebab-case}. md`
2. Determine the path by task-routing model (see [task-routing-methodology-2026-04.md §2](../../03_knowledge/task-routing-methodology-2026-04.md)):
   - **Standalone Restorch** (will survive any project, reused knowledge) → `03_knowledge/`
   - **Review in the context of the project, but reusable knowledge** → `03_knowledge/`, and from `<project>/context.md` link. Don't duplicate the project.
   - **Resource closely related to the project and not reused** (e.g., specific numbers per client) → `<project>/research/`
   - If knowledge changes the vector of the project (new solution, revision of the approach) – an open question or Contingency branch is added to `<project>/plan.md` with reference to the research file.
3. Set **resolved path** as a whole: `<directory>/<filename>. md`. This is the canonical path of the document for frontmatter, indexing and multi-session continuation.
4. Create a YAML-frontmatter file from the Phase 4 template (the body is still empty)
5. Add to TodoList the task: **Write the result in {resolved path}**
6. Inform the user: "I will write the result in {resolved path}"

Why: A file created before the start of work guarantees the preservation. It is impossible to “forget” what already exists. The results are added to this file in the course of work, and not copied there later.

**Rule:** Reference is NOT written in `<project>/tasks.md` (this is execution queue) and NOT written in `<project>/context.md` (this is project invariants, not methodology). `context.md` may only contain a link to a research file.

---

## Phase 1. Decomposition

Break the research question into 3-7 subquestions. Examine each sub-question separately – this reduces hallucinations, because the model focuses on a narrow context and less “fills the gaps” with fiction.

Show the user the decomposition before starting work: “Breaked the question into N subquestions: [list]. Did you miss something?

---

## Phase 2. Data collection

### For every sub-question

1. **Web search first move.** Start by searching, not generating from your head. This is the principle of source-first – from facts to conclusions, not vice versa. Look for a variety of sources: academic, practical, industry.

2. **Consider the distortion map when collecting:**

   | Distortion | How it manifests | What to do |
   |-----------|----------------|------------|
   | Vocal minority | SEO content and screamer opinions dominate | Ask: "What does a typical user who doesn't post?" |
   | Survivorship bias | Only success stories, no failures | Ask: "Who tried unsuccessfully?" Typical reasons for failure? |
   | Authority bias | FAANG/McKinsey preponderance, small business ignorant | Ask: "How is this solved in companies up to 50 people?" |
   | Commercial noise | Content marketing masquerades as best practice | Ask: "Which person has a commercial interest?" Ask for principles, not tools |
   | Language bias | Western default patterns | Explicitly indicate geography. Part of EN requests for access to another data layer |
   | Recency bias | Obsolete or hype information | Ask: “Is it relevant on [date]?” How has it changed in 3 years? |

3. Mark confidence. ** For each statement, evaluate:
   - Confirmed by multiple independent sources
   - x️ is in several sources, but controversial
   - Pattern-based assumption
   - failed to confirm

4. **Classify sources.** For everyone: academic/independent practical/commercial (content marketing). This helps the user to assess reliability.

---

## Phase 3. Verification

After collecting the data - a test for strength. Don't miss this phase, even if it seems obvious.

1. **Chain of Verification.** Listed key factual statements. For everyone: how sure? What source? Check through web search the most critical.

2. **Adversarial check.** Ask yourself:
   - What is the strongest argument against these conclusions?
   - What are the blind spots of this study?
   - If a skeptical expert read this, what would he say?

3. Check your own bias researcher.** Make sure:
   - The questions were neutral (not suggestive)
   - The first response was not the anchor for the entire study.
   - Different frames (plus and minus, not just one side) are considered.

---

## Phase 4. Synthesis → file

The result of the study is written **immediately into a file** created in Phase 0. NOT to chat, NOT to an existing working artifact - just to your file.

### The structure of the result

```markdown
---
id: <kebab-case-id>
type: note
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
aliases:
  - "Understandable name in Russian"
tags: [knowledge, research, <thematic tags>]
source_path: "<resolved_path_from_phase_0>"
freshness: seasonal
expires: <6 months from creation >>
research_type: knowledge | decision
confidence: low | medium | high
---

# <Title of study >>

## The essence
<1-3 sentences: what is researched, for what, the key conclusion >>

## Details.

### TL;DR
<5-7 points: the main findings >>

### <Section 1 >>
<Content with confidence markers: ✅ / ⚠️ / ❓ / 🔴>

### <Section N>

### Alternative perspectives
<Counterarguments, dissenting positions >>

### Blind spots and restrictions
What is not covered, where data is weak, what can change >>

## Sources

### Academic
- [Name](./URL) - brief description]

### Practical
- [Name](./URL) - brief description]

### Commercial (take into account bias)
- [Name](./URL) is a brief description of whose product promotes

## Next step.
What to do with the results: decision, additional research, specific action >>
```

### Rules of registration

- Russian language, unless the user requests otherwise
- Specific figures and facts, not general words
- Each statement with confidence marking
- Sources are divided by type (academic/practical/commercial)
- The Blind Spots section is mandatory - honesty about limitations is more important than the illusion of completeness

> **Stop before replying to the user.** Do not send the result to chat until Phase 5 is completed.
> Check: Is the Phase 0 file full? Are the indexes updated? Only after that - a response to the chat with a link to the file.

---

## Phase 5. Preservation and indexation (mandatory)

The result of the study is always saved in a separate file. This is not optional - the resorch by definition passes a triple filter (reusability + uniqueness + volume).

The file is already created in Phase 0 and completed in Phase 4. It remains to be linked to the rest of the base.

### Protocol of preservation

1. **Make sure the file is full.** The file from Phase 0 must contain the full template result. If you write the result in a chat or in another file, it is a mistake. Move it to the correct file right now.

2. **Update indexes** in order slow → fast layers (see [write-protocol.md §5](../../meta/rules/write-protocol.md)):
   - `03_knowledge/README.md` – Add a link if the file is in `03_knowledge/`
   - `<project>/plan.md` - if the spacing changes the vector of the project (new Contingency / open question / Drift Guard entry)
   - `<project>/context.md` – reference if the spacing is tied to the project and introduces a stable invariant
   - `<project>/log.md` – Record of the study with date and topic
   - `<project>/tasks.md` is NOT updated unless a new execution step appears.
   - If the recourse gives an open question requiring action from the employee, the entry is in `01_now/ops/<contour>/delegations/<slug>.md`, not in the project tasks.

3. **Take context. ** If there are related documents in the database, add cross references.

4. Don't ask "save?" - just save and tell the user where.

5. **In chat - only link + TL;DR (3-5 points).** Full result - in the file.

---

## Phase 6. Quality checklist (before finalization)

Go through each point before giving the result to the user:

- [ ] Are there links to primary sources (not just blogs)?
- [ ] Are alternative views presented?
- [ ] Are there any claims with low confidence?
- [ ] Are the key facts checked through web search?
- [ ] Are there potential commercial biases?
- [ ] Is there a voice minority vs silent majority?
- [ ] Checked for survivorship bias (are there examples of failures)?
- [ ] Is the result relevant to the user’s situation (not generic best practice)?
- [ ] Is the information relevant to the current date?
- [ ] Are there blind spots in the study?
- [ ] Neutral questioning (not confirmation bias)
- [ ] Is there a linguistic/cultural bias?
- [ ] Type (knowledge vs solution) and stopping criteria defined?
- [ ] The result is recorded in a separate file (created in Phase 0) and NOT in a chat/working artifact?
- [ ] Indices updated (README, context.md, log.md)?

---

## Anti-patterns (what NOT to do)

- **Generate from the head without web search.** Source-first - facts first, then conclusions.
- ** Give one long answer without structure.** Decomposition → collection → verification → synthesis.
- ** Skip adversarial check.** Even if the result looks convincing.
- **Forget to save.** A search without saving to the database = lost work.
- **Write the results of the essay into an existing working artifact. ** If you are conducting research for a task (taxonomy, architecture, stack selection), the result of the discourse is NOT written into the task artifact. The artifact is sent to the resist file. The study survives the task and has an independent value. Rule: ≥3 sources or ≥500 words of analytics = individual file, always.
- **Slip into over-researching.** Three sources say the same thing → saturation → stop.
- **Report the results of previous sessions in your own words. ** This introduces bias to the narrator. Refer to the saved document.
- **Recommend specific commercial products without reservations.** Describe selection criteria, not brands.

---

## Multi-session protocol

If the study continues from the previous session:

1. Read the saved document by its **resolved path** from Phase 0 / frontmatter `source_path` is context.
2. Don't do it again. Continue from the stopping point.
3. In the end, update (do not overwrite) the existing document with new findings.
4. If the study is completed, update `research_type`, `confidence` and `expires` to the frontmatter.
