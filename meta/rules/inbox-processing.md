---
id: inbox-processing
type: rules
status: active
created: 2026-03-31
updated: 2026-03-31
aliases:
  - "Inbox processing protocol"
  - "Inbox processing protocol"
  - "Incoming processing log"
tags: [rules, inbox, processing, lifecycle, vault-hygiene]
source_path: "meta/rules/inbox-processing.md"
---

# Processing protocol 00 inbox/

## The essence

`00_inbox/` is a parsing zone, not garbage. Files come here from different sources (mail, messengers, manual import, scripts). The agent who processed the file from inbox ** is obliged to write the result of the processing to the log. Without logging, processing is considered incomplete.

This solves the main problem: the owner does not know which files in the inbox are already processed and safe to delete, and which are not yet touched.

---

## Log of processing

File: `00_inbox/PROCESSING_LOG.md`

### Recording format

```markdown
## 2026-03-31

- **source:** `00 inbox/task-export/` (234 files)
  **action:** Imported to '01 now/projects/example/tasks.md'
  **result:** All tasks moved, source safe to delete
  **status:** ✅ processed
  **agent:** Claude (Cowork session)

- **source:** `00_inbox/2026-03-05-project-meeting.md`
  **action:** Solutions extracted → `01 now/projects/example/log.md`, contacts → `03 knowledge/contacts-network/`
  **Result:** Completely disassembled
  **status:** ✅ processed
  **agent:** Claude (meeting-processing skill)
```

### Statuses

| Status | Value |
|--------|----------|
| Nick processed | Completely processed, source can be deleted |
| Partially processed, needs refinement |
| a reviewed | Viewed, decided to leave as is (no transfer) |
|   queued | Scheduled for processing, not yet touched |

---

## Mandatory actions of the agent

### When working with a file from 00 inbox/

1. Extract valuables, transfer them where you need them (01 now, 02 domains, 03 knowledge)
2. **Write to the log** - add the entry to `00_inbox/PROCESSING_LOG.md`
3. **Do not delete the source** - deletion only by the owner's decision

### During mass processing (dumps, imports)

1. Specify the total number of files and what was extracted.
2. If only part is processed, the `🔄 partial` status indicates what is left.

### At vault review

1. Read `00_inbox/PROCESSING_LOG.md`
2. Invite the owner to delete files with processed status
3. Files without log entry = unprocessed, do not offer for deletion

---

## What not to log

- Automatic dumps that overwrite (`messenger-dumps`, `web-dumps`) - they have their own TTL in [cleanup-registry.md](../cleanup-registry.md).
- Email-inbox is managed via SQLite in zimbra inbox fetcher. py
- Files that the agent only read but did not process (consultation   processing)

---

## Links

- [Cleanup by Design](./cleanup-by-design.md) — Artifact Life Cycle Rule]
- [Review protocol vault](./vault-review.md) — manual cleaning (using this log)]
- [Save Threshold ](./save-and-extract.md) - when to save when not
- [Register of artifacts ](../cleanup-registry.md) - TTL for automatic dumps]
