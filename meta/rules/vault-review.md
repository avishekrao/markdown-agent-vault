---
id: vault-review
type: rules
status: active
created: 2026-03-30
updated: 2026-03-30
aliases:
  - Review vault.
  - "Vault hygiene"
tags: [rules, vault-hygiene, review]
source_path: "meta/rules/vault-review.md"
---

# Review protocol vault

## The essence
Regular cleaning of the vault. Performed on request (“vault review”, “vault hygiene”) or on the 1st of each month.

## Steps.

1. **Inbox:** read '00 inbox/PROCESSING LOG.md' → suggest removing about processed → disassemble the rest ([Protocol](./inbox-processing.md)]
2. **Expires:** find files with `expires < today` - update, archive or delete
3. **Completed projects:** Check `01_now/projects/` - offer to archive completed projects
4. **Knowledge extraction:** suggest transferring reusable data from projects to `03_knowledge/`
5. **README:** Check the relevance of README
6. **Field notes synthesis:** Scan all `03_knowledge/field-notes-*.md`:
   - Find repetitive observations from multiple sources → upgrade `confidence` to `emerging` or `confirmed` (see [write-protocol.md §1.1](./write-protocol.md)])
   - Close or mark disproved hypotheses (counterexample found)
   - If 3+ field notes on a single topic – suggest synthesis into a separate `03 knowledge/patterns-{domain}. md` pattern file
   - Check open questions from field notes – which are still relevant, which are closed by subsequent meetings
   - Update taxonomy organization profiles (`contacts-network/companies/`) with data from new meetings
