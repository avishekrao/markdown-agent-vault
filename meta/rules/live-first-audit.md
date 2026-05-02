---
id: live-first-audit
type: rule
status: active
created: 2026-04-11
updated: 2026-04-15
aliases:
  - "Live audit rule"
  - "Live-first audit"
tags: [rules, audit, ops, ads, campaigns]
source_path: "meta/rules/live-first-audit.md"
---

# Rule: Live-first audit

## The essence
The current status of any external object (advertising campaign, CRM funnel, website, automation, integration) must be confirmed by observation on a live source. Log is an action history, not a current state.

## Details.

### Why?
They work with objects with their hands. Settings change between sessions, the marketer/owner/operator can fix anything, and `log.md` may not get this edit. Relying on the log as the source of the current status = audit error and false conclusions.

### Rule.
1. **Audit = observation.** Before you say “campaign in such-and-such state”, “URL such-and-such”, “such-and-such announcement is active/suspended”, the agent must obtain this value from a live source: API, UI in the browser, the site itself, CRM admin, dashboard analytics.
2. **Log for history only.** `log.md`, `tasks.md`, past entries in `context.md` are permissible only as a source:
   - Action history (what was done and when)
   - known blockers (so as not to attack again);
   - hypotheses about the cause of the discrepancies.
   They are the source of the current status.
3. **Comparison is required.** After observation, the agent compares the real state with what is recorded in the log:
   - What coincided is confirmed;
   - that did not coincide with a separate block of “disparity”, with the date of observation;
   - What could not be recorded (new edits by hand) → a separate block "new changes", write in `log.md` the same session.
4. ** If a living source is not available, let it be clear.** The phrases “by log on such and such date” and “observed live such and such date” are not interchangeable. If the API/browser/live access is blocked (rate limit, no token, communication), the agent is obliged to say: “Live audit is not available due to X.” Below is the last known log state from DATE, accuracy is not guaranteed. And don't pass it off as current status.
5. **The procedure for requesting "check X". **
   1. Try to remove the condition from a living source.
   2. If possible, check with the log, update the log/context in case of discrepancy.
   3. If it did not work, ask the owner to either fix the access or allow him to answer the log as a story.
   It is forbidden: silently answer the log, passing it off as current status.

### Applicability
- Ad campaigns (Meta, Google, TikTok, Yandex): API → Ads Manager UI.
- CRM: API → interface.
- Sites and landing pages: Direct HTTP request, not a description from TK.
- Integration (Pixel, CAPI, webhook, scheduler): Endpoint verification, not README configuration.
- Analytics (GA4, Metabase): fresh upload, not past CSV.
- **Delegation to employees: external tracker = source of truth. The `01_now/ops/<contour>/delegations/<person-slug>.md` file is a short index, not a problem status source. If the owner asks “what’s in charge?” – first observe the links from the file in the tracker, only then the answer. If the tracker is unavailable – clearly mark “by file, without live verification”. See [task-routing.md §delegations](./task-routing.md).

### What to do about the discrepancies
If the living state diverges from the log:
1. Record the discrepancy in `log.md` of the same session with a separate entry: `Observation → waiting by log → delta → hypothesis of cause`.
2. Update `context.md` only if the discrepancy reflects a steady state change (not a one-time hand edit in the UI).
3. Never edit the story in `log.md` retroactively - add a new entry.

### Exceptions
Only one thing: if the owner explicitly says "answer the log, don't walk alive" - then answer the log, but clearly mark the answer as `I mean, no-live.`.

## Related rules
- [write-protocol.md](./write-protocol.md) defines the format of new `log.md` entries.
- [AGENTS.md, Rule 8](../../AGENTS.md) — mid-flight sync for `log.md` and `context.md`.]
- [task-routing.md](./task-routing.md) - where the delegation task state lives and why the file is not the status source.
- [AGENTS.md, Rule 11](../../AGENTS.md) - division of task ownership (external tracker = SoT for delegation).

## Next step.
A reference to the rule is added to `AGENTS.md`. When adding new types of external objects, expand the “Applicability” section.
