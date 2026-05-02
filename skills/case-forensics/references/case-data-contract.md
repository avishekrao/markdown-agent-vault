# Case Data Contract

> Navigation: [SKILL](../SKILL.md)]

## Required Fields

- `case_id`
- `title`
- `objective`
- `context`
- `constraints`
- `steps[]`
- `artifacts[]`
- `metrics_before_after[]`
- `failures[]`
- `replication_120m`
- `transfer_limits`
- `gaps[]`

## Reproducibility Score (0-5)

### input_completeness
- 0: Entrance not described
- 3: Key input conditions described
- 5: inputs and limitations are fully reproducible

### method_specificity
- 0: common words
- 3: There are steps but no parameters
- 5: Steps with parameters and checks

### artifact_availability
- 0: Artifacts missing
- 3: there's a part
- 5: Full set of links/files

### metric_verifiability
- 0: no metrics
- 3: Metrics are available but untestable
- 5: Metrics with source and method of calculation
