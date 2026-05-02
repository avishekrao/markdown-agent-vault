---
id: contour-isolation
type: rules
status: active
created: 2026-03-30
updated: 2026-04-03
aliases:
  - "Isolation of contours"
  - "Contour isolation rules"
tags: [rules, contours, isolation, projects]
source_path: "meta/rules/contour-isolation.md"
---

# Contour isolation

## Essence
Contours are independent areas of work. Data from one circuit **does not mix** with another. This rule protects against context leakage between businesses and projects.

## Terminology

| Term | What is this | Examples |
|--------|---------|---------|
| **Outline** | Holistic area of ​​working with your people, meetings and decisions | product, customer direction, personal area, book, trip |
| **Project** (vault folder) | A specific initiative within the circuit. Folder in `01_now/projects/` | `2026-click-ru-faq-modification`, `2026-click-ru-cjm` |
| **Main circuit design** | The storage folder is the entry point of the outline. Contains common `log.md`, `context.md`, `materials/`, `meetings/` | `01_now/ops/product/` for the product circuit |

A map of the contours and their main projects is in the skill `meeting-processing/SKILL.md`.

## Rules1. **One message = one circuit.** Do not mention data from one circuit in discussions about another. If the outline is unclear, stop and ask the owner to clarify the outline. You cannot list the found paths, projects or candidates.

2. **No implicit connections.** The agent does not build connections between circuits on its own. The data in `03_knowledge/` belongs to a specific loop and is not used as context for another.

3. **Cross-contour reference - only upon explicit request.** When using data from another contour - **sanitize**: replace references to the source contour with data from the target contour. The result should look like an independent artifact of the target contour.

4. **Search - with filter by contour.** Search by vault without filtering by contour is prohibited. Until the contour is refined, only top-level navigation search is allowed (`AGENTS.md`, `README.md`, rules, indexes). Reading the content files of specific contours until clarification is prohibited.

5. **People do not cross contours.** One person in several circuits is a separate entity in each. A mention in one circuit is not a reason to pull data from another.6. **Meetings belong to the same circuit.** If at a meeting on one circuit another is mentioned, this does not create a connection. Information is recorded within the current contour.

7. **Contact Network - Human Access.** `contacts-network/` refers to a separate contact circuit. In the work loop, you can pull up a story with a specific person by `person_id`, but not scan the entire magazine. A person’s affiliation with the circuit is determined through the `project_or_domain` field in the service markup of the card.

8. **Determination of file ownership in `03_knowledge/`.** Files with a path prefix in the name or in a named subfolder → belong to the path. Everything else (methodologies, general reference books) → general knowledge accessible from any circuit.