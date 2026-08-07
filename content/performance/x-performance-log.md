# X.com Performance Log
<!-- Handle: @UsamaAutomates (resolved via Composio 2026-07-07, account connected 2026-07-05) -->
<!-- Appended daily by Agent 6. Newest entry on top. Format per entry:
## YYYY-MM-DD
| post (hook, truncated) | topic type | format | time ET | views | likes | replies | RTs |
Learnings:
- ...
-->

## 2026-08-07
No per-post metrics this run: Apify is not connected in this session at all (ToolSearch for "apify"/scraper tools returned zero matches, not even an auth-blocked entry), so the scrape step is skipped rather than retried — consistent with the 07-24 learning not to re-probe a blocker that hasn't changed. Composio TWITTER_USER_LOOKUP_ME (cheap authenticated read) confirms account-level deltas vs the 07-24 entry: tweet_count 41 → 53 (+12 over 14 days), media_count 3 → 4 (+1), following 100 → 105 (+5), most_recent_tweet_id changed (2079983472408658384 → 2083087977257877751, so new posts did go out). followers_count is UNCHANGED at 8 — same as every entry back to 07-15 (three-plus weeks flat).
Learnings:
- +12 posts in 14 days is ~0.9/day, well under the 2-3/day cadence target and roughly half of what even the 07-22→07-24 catch-up pace implied. The backlog (22 pending-approval drafts spanning 07-07 through 07-24, confirmed via file grep this run) is not shrinking fast enough relative to daily generation — publishing throughput is still the binding constraint, not content supply.
- Followers flat at 8 through 53 total posts is now a 3+ week pattern, not a blip. At this follower count X is giving standalone posts effectively zero organic distribution. Reiterating the 07-22 recommendation with more weeks of evidence behind it: shift a meaningful share of posts toward replies/quote-tweets on larger AI accounts rather than more standalone takes, since standalone-post volume alone has not moved followers once in a month.
- Do not spend a cycle re-attempting the Apify connection each run; this session had zero Apify-related tools discoverable at all (a step below prior sessions' 402/noResults, which at least reached the tool). Flag to Usama once, then rely on the free Composio account-level read for state-change detection only.

## 2026-07-24
Publishing freeze BROKE. Composio TWITTER_USER_LOOKUP_ME: tweet_count 41 (was 39 on 07-22, +2), most_recent_tweet_id 2079983472408658384 (changed from 2079223785585324171), media_count 3 (was 2, +1), following 100 (was 97). followers_count still 8 (unchanged), so the 2 new posts haven't moved the needle yet. Per-post metrics still unreachable (same Apify/X-API-credit blockers as every prior entry; not re-tested today since the tooling diagnosis hasn't changed since 07-22 and re-running it would just reproduce the same 402/noResults). CEO weekly review (07-24) confirmed the backlog independently: 12 drafts sitting pending-approval across 07-19/07-20/07-21/07-22, none marked posted.
Learnings:
- The "nothing ships" theory is now half-wrong: 2 posts went live between 07-22 and 07-24, so Usama is posting manually, just slower than the daily draft output (12 unposted drafts still queued). The bottleneck is review/posting throughput, not a dead pipeline.
- With followers flat at 8 despite 41 posts, standalone posts still aren't getting discovery. Recommend Usama's CEO-review idea (cut X draft generation to 3x/week) gets adopted at the next review — the queue is 4x today's output and growing daily.
- Do not re-run the Apify/X-credit metrics probe every day once it has failed 6+ consecutive times for the same documented reason; the cheap Composio public_metrics check is enough to detect state changes (like today's) without wasting a scrape.

## 2026-07-22
No per-post metrics this run (metrics blocker still open). Confirmed real facts via Composio TWITTER_USER_LOOKUP_ME (authenticated, public_metrics): tweet_count 39, followers 8, following 97, likes given 273, media 2, protected false. Deltas vs 07-21: tweet_count 0, followers 0. `most_recent_tweet_id` is 2079223785585324171 — IDENTICAL to 07-21, so no new post shipped in the interval despite drafts being generated daily. Scraping still dark: apidojo/tweet-scraper returned `noResults` 10/10 (seventh straight, free plan), and the alternate scrape.badger/twitter-tweets-scraper FAILED on start (exitCode 1, needs a paid Apify plan). Per-post views/likes/replies/reposts remain unreachable.
Learnings:
- Publishing has stalled, not just metrics: tweet_count AND most_recent_tweet_id are frozen since 07-21. Drafts are being written but not pushed live. Nothing new to measure because nothing new is posting — fix the publish step first.
- The account is pre-traction: 39 posts have netted 8 followers, and it has given 273 likes while receiving near-zero pickup. At <10 followers X gives standalone posts almost no reach. X1 should weight toward replies/quote-tweets under larger trending AI accounts over standalone takes until the follower base grows (testable: track follower delta after a reply-heavy week vs a post-only week).
- Blocker to re-litigate no further: real engagement numbers need EITHER an Apify paid token (apidojo/badger both gate on it) OR an X API credit top-up (TWITTER_RECENT_SEARCH/GET_POST_ANALYTICS return 402). Composio public_metrics is the only free read and it gives account totals only, never per-post.

## 2026-07-21
Resolved the open question definitively. Apify apidojo/tweet-scraper returned `noResults` again (10/10, sixth straight empty run). But the account is NOT empty: Composio TWITTER_USER_LOOKUP_ME (authenticated, cheap read, succeeded) reports `tweet_count: 39`, a live `most_recent_tweet_id` (2079223785585324171), `protected: false`, 8 followers, media_count 2. So @UsamaAutomates HAS 39 published posts. The prior five entries' zero-posts theory was wrong; the dark metrics loop is a TOOLING problem, not an empty account. Per-post metrics stay unreachable two ways: apidojo scraper returns noResults for this low-follower profile (free Apify plan, nudged to paid), and TWITTER_RECENT_SEARCH returns 402 "API credits depleted" (matches the known depleted X-API-credits state).
Learnings:
- Definitive: the account has 39 live posts. Stop asking Usama to confirm posts exist; they do. The blocker is metric retrieval, not publishing.
- To unblock real numbers: either (a) top up X API credits so TWITTER_RECENT_SEARCH/GET_POST_ANALYTICS work, or (b) put an Apify paid token behind the scraper and test a higher-profile handle to confirm apidojo works at all. Until one is fixed, this loop cannot report engagement.

## 2026-07-20
No data this run. Apify apidojo/tweet-scraper ran clean against @UsamaAutomates (10/10 requested), returned `noResults` again. Fifth consecutive empty run (2026-07-07, 07-16, 07-19, 07-20; 07-15 was a separate Apify-auth blocker). Drafts have been produced daily since 07-07 (3-3-3-3 posts across 07-07/07-15/07-16/07-19) but the metrics loop has never once returned a real number.
Learnings:
- This is no longer a tooling question. Four batches of drafts exist on disk; if none were ever run through `/x-publish`, the account has zero live posts and `noResults` is the scraper reporting the truth, not failing. Recommend Usama confirm in the X app whether @UsamaAutomates has any posts at all before the next run.

## 2026-07-19
No data this run. Apify apidojo/tweet-scraper ran clean (no auth errors) but returned `noResults` for both query forms: profile scrape of @UsamaAutomates (10/10 empty) and search `from:UsamaAutomates` (10/10 empty). Fourth consecutive empty run. Either the account still has zero published posts, or the handle differs from the cached one.
Learnings:
- Action for Usama: confirm the live handle by opening the profile in a browser. If posts exist under a different handle, update the cached handle in this log's header. If the drafts from 07-15/07-16 were never posted, the metrics loop stays dark by definition; posting is the unblock, not tooling.

## 2026-07-16
No data this run. Apify MCP tool worked this time (no auth error), ran apidojo/tweet-scraper against @UsamaAutomates (10 items requested) but got `noResults: true` for all items, zero tweets returned. Third straight run with no metrics (2026-07-07: cold account; 2026-07-15: Apify auth blocked entirely). The auth issue from 07-15 is now fixed but the handle itself returns nothing scrapable.
Learnings:
- Verify @UsamaAutomates is the correct, public, non-suspended handle and has actually published posts (via Composio or manual check) before the next run. Three consecutive empty scrapes points at the account/handle, not the tool.

## 2026-07-15
No data this run. Apify access unavailable: no APIFY_TOKEN in env/config, the Apify MCP server is not loaded this session, and a direct apidojo/tweet-scraper run returns HTTP 402 (token/payment required). Could not scrape @UsamaAutomates metrics, and therefore cannot confirm whether the 2026-07-07 drafts (3 posts) were ever published.
Learnings:
- Blocker, not signal: wire up an Apify token (env or MCP) before the next run so this loop has real data. Until then the metrics side of the loop is dark.

## 2026-07-07
No data this run. Account has zero posts (Apify apidojo/tweet-scraper returned noResults for @UsamaAutomates, 10/10 items). This is the account's first content batch.
Learnings:
- N/A, cold start. Next run will have real data to compare against.
