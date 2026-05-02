---
id: language-and-shortcuts
type: rules
status: active
created: 2026-04-24
updated: 2026-04-24
aliases:
  - "Response language and decoding of abbreviations"
  - "Language and shortcuts rules"
  - "Rules against a mixture of languages and ciphers"
tags: [rules, llm, language, shortcuts, communication]
source_path: "meta/rules/language-and-shortcuts.md"
---

# Language of response and decoding of abbreviations

## The essence

The owner reads the answers as a person, not as an agent. Letter-number identifiers (K6a, T5, R4, M8) without explanation and English-language professional jargon (shell, pipeline, stage) turn the answer into a cipher. This rule details and tightens [AGENTS.md Rule 6a](../../AGENTS.md).

## Part 1 – Decoding index abbreviations

### Where applicable

To all contour identifiers with an index:

| Prefix | What is | Source File |
|---|---|---|
| `K` | Canonical process steps, if they are set up in the project | process profile file within the project |
| `R` | Subject area rules if the project uses indexed rules | profile rule file within the project |
| `P` | Discovery Priority Level (P0 - blocks next step, P2 - postponed) | Files with run finds |
| `T` | Task (task) in the `tasks.md` active project or circuit | `<project>/tasks.md` |
| `M` | Milestone at `plan.md` | `<project>/plan.md` |
| `B` | Blocker card in `plan.md §Blockers` ([AGENTS.md Rule 12](../../AGENTS.md)) | `<project>/plan.md` | |
| `A` | Canonical document or result inside the process card | profile file of the process card |

### Decoding format

`<index> (name or summary)` - ** at the first mention in the message**.

The example is correct:

> Generalization R4 (VK rule on division of campaigns on the economics of the lead) was included in invariant 5 of the general contract of the K6a stage (the campaign concept).

Example incorrect (cipher):

> The generalization R4 is included in the invariant 5 shell K6a.

### When the decryption is repeated

- at the first mention in each new message;
- After a long omission in the dialogue (new chat, return after compression of the context);
- if the reduction receives a new meaning (reassembly of milestones, redefinition of tasks).

Within one message, after decryption, you can refer briefly: “further to R4...”, “the remaining points T6...”

## Part 2 – Prohibition of professional jargon without translation

### Terms prohibited in answers to the owner without a Russian translation

| English term | Russian analogue |
|---|---|
| shell | Universal shell / General stage contract |
| pipeline | work chain/stage conveyor |
| stage | stage / stage |
| handoff | Transmission between stages |
| gate | checkpoint/transition condition |
| entry gate / exit gate | entry condition / exit condition |
| registry | registry |
| manifest| channel capability map / channel description |
| fallback | spare way |
| trigger (non-domestic) | trigger condition |
| adapter | channel/channel implementation |
| scope | workload/task boundaries |
| inventory (in the sense of state registry) | inventory/audit matrix |
| audit (in the sense of file verification) | check/review |
| milestone | milestone plan |
| deliverable | result / issue |
| artifact (in the sense of "file") | document/file (the word "artifact" is permissible, but better specific) |
| contract (in the sense of “document-contract”) | contract (permissible, but at the first mention to explain the role) |
| generalization | synthesis |
| upstream/downstream | previous step/next step; top/bottom chain |
| source annotation | source tag |
| pending | pending/deferred to |
| partial / materialized / declared-only | partially collected / materialized / only declared |
| coverage | coverage |
| rehearsal | rehearsal run |
| bounded | limited in scope |
| evergreen | permanent (in the context of document lifetime) |
| seasonal | seasonal (in the same context)

The list is open. When a new term appears in the answer, the agent checks whether there is a Russian analogue, and if there is one, uses it.

### Names of files and paths - exception

The file and path names remain in the original because they are technical tags: `universal-routing-contract.md`, `campaign-concept-shell.md`, `shell-materialization-inventory.md`. But the **meaning** file in the chat is explained in Russian:

Right:

> In the `campaign-concept-shell.md` file (the general contract of the K6a stage is the campaign concept), six unchanged rules are recorded.

Wrong:

> The `campaign-concept-shell.md` has 6 invariants for the K6a shell.

## Part 3 – Industrial minimum (allowed without translation)

Only terms widely used in the Russian-language advertising industry are such that their translation would be artificial:

- `CPC` - Click Price
- `CPL` - the price of the lead
- `CPM` – price per thousand impressions
- `CPA` – Price of Action
- `CTR` – Clickability
- `ROAS` – refund on advertising costs
- `ROMI` – Return on Marketing Investments
- `LTV` – Customer Lifetime Value
- `UTM` – parameters of link markup
- `URL` - Page address
- `API` - System Interaction Interface (universally common)
- `MCP` - protocol for connecting external systems to agents (internal term vault, the owner uses it)
- `KPI` is a key indicator
- `A/B test` - split test

** Not included in the minimum** (translated mandatory): SDK, IDE, CI/CD, workflow, payload, schema, endpoint, stakeholder, use-case, pain point, value proposition, follow-up, check-in, sync, stand-up, retro and the like.

## Part 4: Testing Step Before Sending a Response

Before sending, the agent must re-read his response and remove:

1. Undeployed index abbreviations at the first mention in the message.
2. English-language terms from the prohibited list without Russian translation nearby.
3. A mixture of Russian and English in one word (`shell`, `gate`, `blueprint`, `handoff`).
4. Calcs, where the Russian analogue sounds natural (`generalization` → “generalization”, `orphanage` → “objects without a parent”).

Paragraph 3 is a particular problem: the agent tends to glue the Russian suffix to the English root (`pipeline`, `shell`). This is forbidden most severely - such a text is unreadable and simultaneously violates both rules.

## Part 5 – Working with Knowledge Base Files

Most of the files in the knowledge base have historically been written in a mixture of languages – that’s a fact, not a license.

**Required:**
- In chat rooms, the rule applies regardless of how the original file is written.
- citations from the file, if necessary, are given in the original, but the explanation is in Russian.

**Not necessarily (soft rule):**
- When you first touch a file on another task, if possible, translate jargon into new and changing sections.
- The retrospective translation of all knowledge base files is automatically started.
- If the owner asks to translate a specific file, it is a separate task with its own cycle.

## Links

- Parental rule: [AGENTS.md Rule 6a](../../AGENTS.md)].
- Tag directory for contour identifiers: [TAGS.md](../TAGS.md).
- Source files of index prefixes – see the table in Part 1.

## Next step.

The rule applies from the moment the file is created. Agents reading it for the first time begin to observe it in the same message where the rule is mentioned.
