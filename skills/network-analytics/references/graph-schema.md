# Graph Schema

> Navigation: [SKILL](../SKILL.md)]

## Nodes

```yaml
node_id: "person:ext-001"
node_type: "Person|Organization|Event|Topic"
label: "..."
attributes:
  role: "..."
  company: "..."
  region: "..."
```

## Edges

```yaml
edge_id: "edge-..."
from_node: "person:..."
to_node: "event:..."
edge_type: "co-speaker|co-organizer|mentioned_with|works_at|introduced_by|attended"
weight: 0..1
confidence: 0..1
date: "YYYY-MM-DD"
source_url: "https://..."
```

## Identity Rules

- Canonize a person with a sustainable `person_id`.
- Do not combine profiles with ambiguity.
- When in doubt, create a `review_needed` flag.
