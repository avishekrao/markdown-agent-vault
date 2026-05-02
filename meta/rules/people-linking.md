---
id: people-linking
type: rules
status: active
created: 2026-04-30
updated: 2026-04-30
aliases:
  - "Human self-linking."
  - "Rules for Mentioning People"
tags: [rules, people, contacts, linking]
source_path: "meta/rules/people-linking.md"
---

# Autolinking people

## The essence

If an agent creates or edits a document that mentions people, it must link those mentions to people’s cards or record an unknown name in a mention log.

## Details.

### Data layers

| Layer | Path | Destination |
|---|---|---|
| External contacts | `03_knowledge/contacts-network/persons/` | People outside your organization |
| Employees or team members | `03_knowledge/people/persons/` | People within your organization or team
| Journal of Unknown Mentions | `03_knowledge/contacts-network/inbox/mention-log.md` | Names for which no card is yet available |
| Interaction log | `03_knowledge/contacts-network/registries/interactions.csv` | Meetings, calls, letters, messages |

If these folders don’t already exist, the agent first suggests creating a minimal structure, rather than putting people in random places.

### Rule of mention

When a person is mentioned, the agent:

1. Looks for a person's card in permitted indices.
2. If a person is found clearly, puts a link to the card.
3. If several candidates are found, ask the owner.
4. If the person is not found, ask: create a card or write in a journal of unknown mentions.

### What's wrong?

- You cannot guess a person by one name or last name.
- You can not store information about people only in the text of the meeting.
- You can’t mix facts, observations, and financial data in a single card without an explicit access rule.
- You cannot transfer sensitive data about people to a shared package or a shared section.

### Journal of Interactions

Meetings, calls and letters are recorded in `interactions.csv`:

```csv
date,person_id,company,interaction_type,summary,related_doc,project_or_domain
```

A person's card keeps a profile. The interaction log stores events.

## Next step.

At the first real use, create neutral templates of a person’s card, mention log, and interaction log.
