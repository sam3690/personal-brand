---
description: Publish approved X drafts for today via Composio (human gate - confirms each post)
argument-hint: [optional date YYYY-MM-DD, defaults to today]
---

You are publishing Usama's approved X.com posts through Composio. Date: $ARGUMENTS (default today).

## Process
1. Read content/drafts/x/<date>/. List every draft with its status, QA score, and media field.
2. Only posts Usama explicitly confirms in this session get published (status frontmatter alone
   is not enough; confirm the list with him before sending anything).
3. Use COMPOSIO_SEARCH_TOOLS (use_case: "create a post on twitter", and "upload media to twitter"
   if any draft has media) then COMPOSIO_MULTI_EXECUTE_TOOL to publish. For threads, post the
   parts in reply-chain order (each replies to the previous; these are dependent calls, do NOT
   batch them in parallel). Post the first_reply (source link) as a reply to each published post.
4. If media upload is not supported on the free tier, publish text-only and tell Usama to add
   media natively; never silently drop a post.
5. Update each published draft's frontmatter to status: published + the tweet URL.
6. Summarize: what went live, links, and the suggested golden-hour action (reply to comments).

Hard rules: never publish a pending or unconfirmed draft; no em dashes; 500 posts/month Composio
cap means max 3/day, warn if the month's count is trending over.
