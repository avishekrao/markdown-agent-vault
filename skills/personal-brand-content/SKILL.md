---
id: skill-personal-brand-content
type: skill
status: active
created: 2026-03-25
updated: 2026-03-25
tags: [skill, personal-brand, content, social-media]
---

# Skill: Personal Brand Content

## Appointment

Creating and adapting expert content for a personal brand or expert channel. Skill helps: generate content from the queue, adapt the master version for a specific platform, maintain a single voice of the author.

## When to use

Triggers:
- Write a post about [theme] for [platform]
- Adapt [content] to [platform]
- “new idea: [text]”
- "to post what?"
- "handle backlog"
- «weekly review»
- "update metrics"

## Project context

**Must read before work:**
1. `<project>/context.md` – niche, audience, pillars, formats
2. `<project>/pipeline.md` is a content process methodology.
3. `<project>/platforms/{platform}.md` – target platform profile, if available

## Voice of the author (Author Voice)

**Expert, but accessible. Like talking to a smart colleague over coffee.

** Principles:**
- Specifics > abstraction. It was always “the result” and not “AI is the future.”
- Experience > Opinion. Tell me what you did, not what you think.
- Use > hype. Each post should give something useful: tool, approach, insight.
- Honesty > positivity. Do not hide failures and limitations
- Simplicity > smartness. Difficult things in simple language

** Forbidden:**
- Empty words, cliches, and bureaucratic phrasing
- "In the modern world ...", "It's no secret that ...", "We all know ..."
- Clickbait headlines without content
- General advice without specifics
- Self-praise without evidence

## Content creation process

### Step 1: Identify introductory

Read the idea from the backlog or the user request. Determine:
- Content pillar (pillar)
- Format
- Target platform(s)

### Step 2: Create a master version

Write the full version of the content without format limitations. Turn on:
- Title (3 options)
- Main text with specifics
- CTA (if appropriate)
- Sources/links

Save in: `content/YYYY-MM-DD-slug-master.md`

### Step 3: Adapt to the platform

Download the platform profile from `platforms/{platform}.md`. Adapt:
- Length (by platform limits)
- Formatting (markdown, HTML, plain text)
- Tone (more/less formal)
- Hashtags/tags
- CTA (subscription, comment, repost – by platform patterns)

Save in: `content/YYYY-MM-DD-slug-{platform}.md`

### Step 4: Final check

- Check the text for empty words, cliches, bureaucratic phrasing, and lack of specifics
- Verify compliance with the platform profile
- Check for specifics (digits, cases, tools)

## Working with a bank of ideas

### The command "new idea: [text]"

1. Read `ideas/ideas-backlog.csv`
2. Identify the next id
3. Add a line with: date added, source (user-input), title, the rest is empty.
4. Confirm to the user

### The "handle backlog" team

1. Read `ideas/ideas-backlog.csv`
2. Find records with status=draft and empty pillar/format
3. For each: offer pillar, format, platforms
4. Calculate the score using the ICE pipeline model.
5. Show the user to confirm
6. Update the CSV

### The post-what command?

1. Read `ideas/ideas-backlog.csv`
2. Filter status ) {draft, processed} (not published, not rejected)
3. Sort by priority score DESC
4. Show the top 5 with: title, pillar, format, platforms, score
5. Ask the user what they choose.

## Working with metrics

### The command "Update the metrics [post]"

1. Ask the user for current numbers (views, likes, comments, shares, new followers, link clicks)
2. Add a line to `analytics/metrics-log.csv` with snapshot time
3. Confirm.

### Weekly review team

1. Read `analytics/metrics-log.csv` in the last 7 days
2. Read `ideas/ideas-backlog.csv` in the last week.
3. Create a review from a template from `pipeline.md` (Weekly Review section)
4. Save it to `analytics/YYYY-Wnn-review.md`.
5. Propose adjustments to the strategy

## Related skills

- Signal Selection Skill or Separate List of Ideas – A Source of Topics for Expert Content, If It’s in Storage
- [translation-editorial](../translation-editorial/SKILL.md)] Translation-editorial signals into content
- [case-forensics](../case-forensics/SKILL.md) — extracting cases for content]

## References

Platform profiles (completed via Q&A with NotebookLM):
- `references/messenger-best-practices.md`
- `references/linkedin-best-practices.md`
- `references/facebook-best-practices.md`
- `references/vc-ru-best-practices.md`
- `references/habr-best-practices.md`
- `references/reddit-best-practices.md`
