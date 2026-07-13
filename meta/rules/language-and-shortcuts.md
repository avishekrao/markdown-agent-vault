---
id: language-and-shortcuts
type: rules
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Response language and shortcuts"
tags: [rules, language, communication]
source_path: "meta/rules/language-and-shortcuts.md"
---

# Response Language and Shortcut Rules

## Essence

The agent answers in the user's language, expands cryptic identifiers, and avoids unexplained professional jargon.

## User Language

Respond in the same language the user used in the current message unless they explicitly request another language.

Allowed exceptions:

- exact product names, file names, API names, class names, command names, or system entities;
- original terms where translation would distort meaning, with a short plain-language explanation;
- industry-standard abbreviations such as CPC, CPL, CPM, CPA, CTR, ROAS, ROMI, LTV, UTM, URL, API, MCP, KPI, and A/B test.

If an idea can be expressed naturally in the user's language without losing meaning, prefer that.

## Shortcut Expansion

When first mentioning letter-number identifiers such as `K3`, `R4`, `P2`, `T7`, `M1`, `B2`, or `A5`, expand them once:

```text
T6 (task to materialize the shared contract for stage K6a)
R4 (rule about separating campaigns by lead economics)
M8 (milestone: first connected channel)
```

After expansion, the short form may be used in the same message. In a new session or after a long gap, expand again.

## Jargon Rule

Do not use professional jargon without explanation when writing to the owner. Prefer plain words.

If a precise technical term is necessary, introduce it with a short explanation the first time it appears.

Examples:

- Instead of "pipeline", write "sequence of processing steps" unless the project itself uses the exact term.
- Instead of "fallback", write "backup path" or explain the term.
- Instead of "source annotation", write "note showing where the claim came from".

File and path names remain in their original form because they are technical identifiers.

## Before Sending

Before sending a user-facing answer, check for:

1. unexpanded letter-number identifiers;
2. unexplained jargon;
3. mixed-language phrasing where a clear single-language phrase would work;
4. claims whose source or confidence should be stated.

## Next Step

Use this file together with [write-protocol.md](./write-protocol.md) when writing user-facing summaries or public documentation.
