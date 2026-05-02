---
name: event-intelligence
description: >
Monitoring and prioritizing AI events and CFP for two funnels: Attend and Speak.
Use this skill when you need to take events by value, calculate scoring,
track application deadlines for speakers, and form a practical calendar
action for 30/60/90 days.
---

# Event Intelligence


> Navigation: [Skill index](../README.md)
## Overview

Convert the list of events into a managed funnel of participation and performances.

Skill is responsible for the `collect events -> normalize -> score -> rank -> calendar actions` phase.

## Workflow

### 1) Normalize Events

Bring all events to the scheme from
[event-schema-and-scoring](./references/event-schema-and-scoring.md).

Mandatory fields:
- `event_name`
- `date_start`
- `location`
- `format`
- `cfp_deadline` (if any)

### 2) Dedupe and Validate Dates

- Slice duplicates of one conference from different sources.
- Check the absolute dates (`YYYY-MM-DD`).
- Specify timezone if the data is over time.

### 3) Score Attend / Speak

Calculate:
- `AttendScore = 0.4*theme_fit + 0.4*network_value + 0.2*cost_efficiency`
- `SpeakScore = 0.4*theme_fit + 0.3*acceptance_probability + 0.3*strategic_value`

### 4) Rank

Back:
- `Top-5 Attend`
- `Top-5 Speak`
- `Watchlist`

### 5) Build Calendar

Gather deadlines in the horizons:
- 30 days
- 60 days
- 90 days

For `Speak`, attach a pitch draft to a template from
[cfp-pack-template](./references/cfp-pack-template.md).

## Output

Minimum exit:
1. Attend table (score + why)
2. Table Speak (score + deadline + pitch angle)
3. Calendar CFP 30/60/90
4. 3-5 next actions

## Quality Gates

- There are no events without an absolute date.
- There is no ranking without score breakdown.
- For each top event, there is a justification in 1-2 sentences.
- Speak has a realistic theme for the speech.

## Anti-Patterns

- Do not choose events only by the brand of the organizer.
- Do not ignore the cost of time (money + road + preparation).
- Do not submit to the CFP without matching the theme and format of the conference.

## References

- [event-schema-and-scoring](./references/event-schema-and-scoring.md)
- [cfp-pack-template](./references/cfp-pack-template.md)
