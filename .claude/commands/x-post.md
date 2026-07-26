---
description: Generate today's 2-3 X.com posts on trending AI topics via the X agent team
argument-hint: [optional topic override]
---

You are running Usama's X.com Content Engine. Produce 2-3 finished, scored, ready-to-approve
post drafts for today. Topic seed (optional): $ARGUMENTS

## Load context
- content/knowledge-base/x-playbook.md (register, formats, cadence)
- content/performance/x-performance-log.md (what the data says works)
- Last 3 days of content/drafts/x/ (no repeats)

## Run the X agent team in order
Model routing: run the pipeline agents with **sonnet**; any deep strategy/analysis step uses **opus**.
1. content/agents/x/x0-trend-scout.md — today's trending AI topics (generic AI news in scope), pick top 2-3.
2. content/agents/x/x1-post-writer.md — write each post (single or thread) in Usama's register.
3. content/agents/x/x2-media-brief.md — media brief per post (agents NEVER attach media).
4. content/agents/x/x3-qa.md — score /100; fix and re-score until every post passes ≥80, zero red flags.

## Output
Save each post to content/drafts/x/<today YYYY-MM-DD>/<n>-<slug>.md with frontmatter:
```
---
status: pending-approval
suggested_time: "<time ET>"
media: []            # Usama fills with file path(s) or leaves empty
first_reply: "<source link + any context>"
qa_score: <n>
---
```
Then show all posts + media briefs in chat and remind Usama: review, drop media paths into the
frontmatter (or reply with them), then run /x-publish. Nothing publishes without approval.
