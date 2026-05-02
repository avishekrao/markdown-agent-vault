---
name: case-forensics
description: >
Extracting reproducible AI cases from long threads, comments and chat discussions.
Use this skill when you need to turn disparate messages into methodology.
repeatable: context, steps, artifacts, metrics, limitations, and list
Gaps (GAP) that need clarification.
---

# Case Forensics


> Navigation: [Skill index](../README.md)
## Overview

Convert the unstructured discussion into a reproducible instruction-level case.

Skill is responsible for the `thread -> evidence map -> method extraction -> reproducibility report` phase.

## Workflow

### 1) Parse Timeline

Restore the chronology:
- who acted,
- What decisions were made,
- What changes have been made,
- That was the result.

### 2) Build Evidence Map

Mark each thesis:
- `EVIDENCE` – Confirmed by message/artifact
- `ASSUMPTION` – conclusion without direct proof
- `GAP` - critically lacking data

### 3) Extract Method

Collect the method in consecutive steps:
- entry
- action
- toolkits
- quality control
- completion

### 4) Quantify Outcome

Record:
- `before/after` metrics
- Type of effect (time/money/quality/risk)
- failed

### 5) Reproducibility Score

Evaluate the reproducibility of the contract
[case-data-contract](./references/case-data-contract.md):
- `input_completeness`
- `method_specificity`
- `artifact_availability`
- `metric_verifiability`

### 6) Prepare Final Case

Give me:
- case-case
- How to Repeat in 120 Minutes
- `GAP` block + questions to clarify from
[gap-interview-questions](./references/gap-interview-questions.md)

## Output

Return the sections:
1. Context and purpose
2. Baseline conditions
3. Method(s)
4. Materials/industry/tools
5. Outcome and metrics
6. That didn't work.
7. Replication in 120 minutes
8. Limits of portability
9. GAP and issues

## Quality Gates

- No steps without entry/exit.
- Every numerical metric has a source in a thread.
- Any hypothesis without confirmation is labeled `ASSUMPTION`.
- There are obvious limitations to the applicability of the case.

## Anti-Patterns

- Do not give out a “success story” as a methodology.
- Do not hide failures/limitations.
- Do not replace `GAP` with guesswork.

## References

- [case-data-contract](./references/case-data-contract.md)
- [gap-interview-questions](./references/gap-interview-questions.md)
