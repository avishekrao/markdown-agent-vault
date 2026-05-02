---
name: network-analytics
description: >
Building and Updating a Person-Org-Event-Topic Industry Link Graph for Navigation
AI outreach and prioritization outreach. Use this skill when you need to understand
Who is the bridge between clusters, which domains are formed, who are the key nodes,
And who to go to first to access the right people.
---

# Network Analytics


> Navigation: [Skill index](../README.md)
## Overview

Transform chaotic mentions and interactions into a working map of the network of influence.

Skill is responsible for the `normalize entities -> update graph -> compute metrics -> outreach plan` phase.

## Workflow

### 1) Normalize Entities

Use the circuit from
[graph-schema](./references/graph-schema.md).

Substances:
- `Person`
- `Organization`
- `Event`
- `Topic`

### 2) Update Edges

Maintain typed connections:
- `co-speaker`
- `co-organizer`
- `mentioned_with`
- `works_at`
- `introduced_by`
- `attended`

For each rib, fix:
- `source`
- `date`
- `confidence`

### 3) Compute Metrics

If you have graph analytics tools, consider:
- `degree centrality`
- `betweenness centrality`
- `eigenvector centrality`
- `communities` (Louvain/equivalent)

If tools are not available, use heuristics and explicitly mark
`method=heuristic`.

### 4) Interpret

Use the rules of
[metrics-and-prioritization](./references/metrics-and-prioritization.md):
- bridges between clusters,
- the core of each domain,
- New growing clusters.

### 5) Build Outreach Plan

Give me:
- 5 key bridges
- 3 clusters/domains
- 10 priority outreach steps (to whom, through whom, why)

## Output

1. Graph update summary
2. Top bridges (betweenness)
3. Community map
4. Outreach backlog (10 items)

Each outreach item:
- `target_person`
- `via`
- `reason`
- `suggested_message_angle`
- `expected_outcome`

## Quality Gates

- No rib without a source or date.
- There are no central conclusions without specifying the method of calculation.
- Outreach recommendations are tied to a specific goal, not a general “get to know.”

## Anti-Patterns

- Do not mix names without proof of identity.
- Do not confuse frequent mentions with real influence.
- Do not draw conclusions about the cluster based on 1-2 connections.

## References

- [graph-schema](./references/graph-schema.md)
- [metrics-and-prioritization](./references/metrics-and-prioritization.md)
