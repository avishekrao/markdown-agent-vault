---
id: <yyyy-mm-dd>-incident-runbook
type: process
status: active
created: <YYYY-MM-DD>
updated: 2026-03-18
aliases:
  - "INCIDENT RUNBOOK"
tags: [template, incident, rollback, operations]
source_path: "meta/templates/incident_runbook.md"
knowledge_criticality: high
verification_status: unverified
verified_by_me: false
curation_mode: none
---

# INCIDENT_RUNBOOK

Related index: [template index](./README.md).

## Trigger
- What signal/symptom triggers a runbook:

## First 10 Minutes
1. Freeze new deploys.
2. Identify last known good tag.
3. Select rollback path.

## Rollback Procedure
- Command/pipeline:

## Verification
- Smoke checks:
- Recovery metrics:

## Postmortem Inputs
- Root cause:
- Why the gate missed:
- What new test/gate are we adding:
