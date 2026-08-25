# LinkedIn Performance Log
<!-- Appended each Sunday by Agent 6 using Zernio analytics. Newest entry on top.
     Post tables MUST carry the funnel columns: | DMs | Replies | Booked calls |
     Zernio does not report these. Usama supplies them from the LinkedIn inbox and the calendar. -->

## STANDING FUNNEL TRACKER (fill weekly, never overwrite a past row)

Impressions are the vanity number and this account already knows reach is not the constraint on
revenue. These three columns are the ones that decide whether the agency-owner re-point worked.
Attribute a DM or a call to the post it followed within 72 hours; if it cannot be attributed to a
post, log it under `(no post)` so the outbound lane gets credit separately.

| Week of | Posts live | DMs received | DMs replied to | Conversations opened | Booked calls | Source post(s) |
|---|---|---|---|---|---|---|
| 2026-08-03 | | | | | | |
| 2026-08-10 | 4 | | | | | (needs Usama: inbox + calendar) |
| 2026-08-17 | 3 (of 4 planned; post 3, fragrance-WhatsApp case study, still an unpublished Zernio draft) | | | | | (needs Usama: inbox + calendar) |

**Baseline, stated honestly:** as of 2026-08-03 all four numbers are zero and there is no DM lane
running (`../knowledge-base/frameworks/lakajev-linkedin-leadgen.md` 7.1). The first non-zero week is
the first real signal this positioning produces buyers, not reach.

## 2026-08-24 — Week of 2026-08-17 review: pass/fail bar FAILED, replication did not reproduce

Pulled live via `analytics_get_post_timeline` (cumulative through 2026-08-24) and
`accounts_get_follower_stats`. Only 3 of the 4 planned posts published; post 3 (fragrance-ecommerce
WhatsApp case study, drafted for the Wed 08-19 slot) is still sitting unpublished in Zernio.

| Post | Format/pillar | Impr | Reach | Likes | Comments | Saves | ER |
|---|---|---|---|---|---|---|---|
| 1 GHL missed-call teach (P3) | Teach, Welsh Trailer | 57 | 22 | 1 | 2 | 0 | 5.26% |
| 2 "Six weeks in" founder story (P4) | Hero, exact 07-28 time/register replication | 84 | 24 | 1 | 0 | 0 | 1.19% |
| 4 Medical-sales manager case study (P1) | Case study, skeleton A | 23 | 19 | 1 | 0 | 0 | 4.35% |

**Followers: 415 → 446, +31 (+7.47%)** over 08-16 to 08-24. Real growth, but this window also
includes the DM-queue system going live (08-20/08-21) and cold-email/community activity, so it
cannot be attributed to these 3 posts alone.

**The pre-committed pass/fail bar (set in current-strategy.md's WEEK OF 08-17 DIRECTIVES) FAILED
decisively.** Bar: "pass is a 4-post total above 800 or any single post above 500 ... fail is under
400 total." Actual: **164 total impressions across 3 posts**, no post cleared even 100, let alone
500. This is worse than the already-low week-of-08-10 baseline (280 total across 4 posts) despite
one post being a deliberate replication of the account's best-ever result.

**Best: post 1 (GHL teach), 5.26% ER, the only post with any comments (2, both from the same
commenter across the week — check if that's a real conversation or one person).** Lowest reach of
the three but the only one that earned a reply.

**Worst, and the most important finding: post 2, the exact-time/exact-register replication of
2026-07-28, did NOT reproduce anything close to that result.** 84 impressions / 24 reach / 1 like /
0 comments, against the corrected 07-28 baseline of 6,267 impressions / 4,613 reach / 75 likes / 19
comments, a **~75x shortfall**. This directly answers the open question flagged in the 2026-08-01
log entry ("does chapter two of the same story hold the reach, or was 07-28 a one-off novelty
spike?"). **Answer: one-off.** Same slot, same register, same "unresolved confession + real number"
structure, zero replication of the reach. Register and timing are not sufficient causes on their own;
07-28 likely also depended on something not yet identified (algorithmic novelty push, a specific
network moment, or distribution luck).

**Learnings:**
1. **Retire "replicate 07-28 exactly" as a strategy.** It was tested cleanly (same hour, same
   register, same weekday) and failed by 75x. Whatever made 07-28 travel, exact repetition of its
   surface features is not it. Stop spending hero-post slots trying to re-trigger it mechanically.
2. **All three posts are reach-capped in-network at a smaller scale than even the account's normal
   baseline** (23-84 impressions vs. the ~60-200 range most non-viral posts get). Something beyond
   register may be suppressing reach right now — check posting cadence, whether the account looks
   inactive to the algorithm between posts, or whether Zernio's publish path itself is scoring worse
   than native posting.
3. **Case study (post 4) beat founder story (post 2) on ER despite zero comments on both being close
   to true** (post 4 got 0 comments too) — proof-driven posts are not underperforming story right now;
   story specifically underperformed its own history.
4. **The account has now failed 2 of the last 2 pre-committed weekly pass/fail bars** (this week: 164
   vs 400 needed; prior weeks also flagged as reach-capped). Reach, not register, looks like the
   binding constraint again — worth re-testing the 2026-07-19 finding ("reach, not resonance, is the
   bottleneck") now that the register experiment has run its course.

## 2026-08-16 — Week of 2026-08-10 review: all 4 shipped, proof beat story

All 4 planned posts are live (Zernio, synced 2026-08-16). Followers 398 → 415, **+17 (+4.27%)**.

| Date (ET) | Post | Format | Impr | Reach | Likes | Comments | Saves | ER |
|---|---|---|---|---|---|---|---|---|
| 08-09 11:08pm | 1 Message I read at my desk (P4) | Story | 91 | 25 | 3 | 0 | 0 | 3.30% |
| 08-10 11:02pm | 2 Studio answering leads a day late (P1) | Case study | 60 | 30 | 1 | 2 | 0 | 5.00% |
| 08-11 11:46pm | 3 Answer every lead in 60s (P3) | Carousel | 64 | 34 | 3 | 2 | 0 | 7.81% |
| 08-13 12:25am | 4 He was the bottleneck (P1) | Before/after | 65 | 39 | 5 | 3 | 0 | 12.31% |

**Best: post 4, 12.31% ER, the highest in the account's history** (prior best 7.48%), with the week's best
reach and most comments. Plain text, before/after columns, one hard number (14 customers in 3 weeks), and a
question about work the reader still does by hand.
**Worst: post 1, 3.3% ER, zero comments.** The 07-28 breakout did not reproduce (91 impressions vs 1,500),
and 91 impressions over 25 reached means one small in-network set saw it 3-4 times. No out-of-network push.

**Learnings:**
1. **ER rose monotonically with proof density** (3.3 → 5.0 → 7.8 → 12.3); the story ranked last. Run 4
   proof/teach posts and zero hero next week; if ER holds above 7%, retire the 1-hero-in-3 ratio.
2. **The teach shipped without its teach.** The six steps moved from the body into a carousel PDF, so the
   body went out at ~180 chars vs the drafted 2,225, and the n8n gift sat in a comment. Still 0 saves this
   week (**3 in account history** after the 2026-08-16 correction to the 07-28 row: 1 from 07-07, 2 from
   07-28). Test one teach with every step IN the body, no PDF.
3. **Never in-slot.** All four published 11pm-12:30am ET (8-9am PKT), not the 7:30-10am ET slots in the
   titles. Three weeks of drafts remain untested in their intended window.
4. **Funnel columns need Usama.** DMs, replies and booked calls are not in Zernio; this week's tracker row
   stays blank until he fills it from the inbox and calendar.

## 2026-08-03 — Graph audit: how many automation-operator tribe members are actually in Usama's network (tribe.md open action 6)

Manually searched Usama's own LinkedIn connections (network filter = 1st degree, 371 total connections)
via the search bar for each keyword tribe.md flagged: n8n, automation, AI automation, workflow, GTM.

**Precise, high-confidence keywords:**
- `n8n` → 27 distinct 1st-degree connections, 3 pages. Near-zero noise: almost every hit self-describes
  as an AI Automation Specialist, AI Engineer building with n8n/Make/Zapier, Agentic AI Engineer, or
  GTM/RevOps person using Clay/Apollo/n8n.
- `"AI automation"` (phrase) → 4 pages (~35-40), heavy overlap with the n8n set. Small net-new add:
  a handful of adjacent titles (data/BI + agentic AI, full-stack + AI automation).
- **Deduplicated high-confidence tribe count: ~27-32 people, roughly 7-9% of the 371-connection network.**

**Noisy keywords, unreliable as a count:**
- `automation` alone → 10+ pages (100+ hits), majority false positives: HR process automation, ERP/BPM
  enterprise workflow roles, Amazon PPC/WordPress people who list "automation" as one skill among many.
- `GTM` alone → 10 pages, almost entirely false positives: generic digital marketing, SEO, content and
  personal-branding people. Genuine GTM-tribe hits (e.g. "AI GTM Architect for B2B Founders," "GTM Expert
  | Clay | AI Automation | Claude Code") were already captured in the n8n/AI-automation set above.
- `workflow` alone → 10 pages, almost entirely false positives: PMP/Scrum project managers, ERP/PeopleSoft
  and IBM BPM roles. Real hits already counted above.

**The finding that matters more than the count: composition, not size.** Of the ~27-32 high-confidence
tribe members, nearly all are based in Pakistan (Lahore/Karachi), and by title the large majority are
BUILDERS and PEERS, not BUYERS: other AI Automation Specialists, agency founders selling similar
automation/voice-AI services, and at least one person explicitly labeled a "GTM & RevOps Learner." Under
tribe.md 8.4's own Hormozi lens ("can they pay: solo learner with no client, no"), most of this slice
fails the paying-buyer test. Segment B (built it, breaks Thursday) and Segment C (an inventory, no idea
what runs) are underrepresented in the CURRENT graph; the network is dense with fellow builders in the
same Pakistani AI/automation scene Usama already belongs to, thin on the US/EU agency-owner buyer with a
client or revenue process depending on the build.

**What this does and does not mean.** It does not invalidate the tribe: the vocabulary and recognition
markers are confirmed real (27+ people in the existing graph already self-describe exactly the way
tribe.md predicted). It does mean organic reach WITHIN the existing graph will skew toward Segment A
discourse (fellow builders, reach not revenue) unless a post breaks out-of-network the way the 2026-07-28
founder story did (95% out-of-network). The buyer segments (B, C) are more likely to be reached by the
algorithm pushing a post past this account's own graph than by the graph itself.

**Action implied:** the connection-request/DM lane (`tribe.md` 1A.2) should target OUTSIDE this existing
graph, specifically US/EU agency owners and consultants, not more of the same Pakistani builder community
already well represented here. Posting into the existing graph will not itself find Segment B/C buyers.

## 2026-08-01 — Founder story (2026-07-28) broke every record on the account

Logged from the post's own LinkedIn analytics panel (screenshot supplied by Usama), not a Zernio sync.

| Date | Day | Post (angle) | Impressions | Reached | Reactions | Comments | Profile views | Followers |
|---|---|---|---|---|---|---|---|---|
| 07-28 | Tue | Founder story, "that is not a success story, it is a receipt" (P4) | 1,500 | 1,056 | 18 | 5 | 12 | 3 |

**Correction, 2026-08-16 (CEO weekly review):** the row above was read off Usama's screenshot of the
LinkedIn analytics panel taken shortly after posting. Zernio's synced platform timeline for this same
post (`urn:li:share:7487810498852294657`, verified live via `analytics_get_post_timeline` on
2026-08-16) shows the post kept growing for a week and the true total is **6,267 impressions, 4,613
reach, 75 likes, 19 comments, 2 saves.** That is roughly **4x the impressions the account has been
reasoning from for two weeks.** The profile-views (12) and followers (3) columns above have no
Zernio equivalent and are unverified, not confirmed. Every content decision made between 2026-08-01
and 2026-08-16 that cited "1,500 impressions" as the account's best post was working from a number
about a quarter of the true one.

**This is the single biggest result the account has produced.** Prior best impressions: 196. Corrected,
that is roughly **32x the impressions and 15x the reactions of anything before it** (against the old
196 baseline), and the first post to move profile views and followers in a measurable way.

Distribution split matters: **95% out-of-network, 5% in-network.** Every previous post was
reach-capped near 100 impressions and stayed inside the follower graph. This one got pushed out. That
is the algorithm rewarding dwell time and comment depth, which a story earns and a framework post does not.

**What changed vs. the ~100-impression posts:**
1. **Register.** Level 1 hero story, no CTA, no offer, no client, no framework. Pure first-person.
2. **Unfinished stakes.** It refused to resolve into a win ("$850, still 9 to 6, no predictable
   pipeline"). The previous register always closed on a result or a takeaway.
3. **Question that asks for a confession**, not an opinion. 5 comments off ~1,000 reached.

**Correction to the 2026-07-19 learnings:** "reach, not resonance, is the bottleneck" was right about the
symptom and wrong about the cause. Timing was not the cap. **Register was.** Cost-delta hooks + named-steps
frameworks max out around 100-200 impressions on this account because they stay in-network. Story breaks out.

**Learnings for the next drafts:**
1. **Raise founder-story frequency.** The framework says 1 hero post per 4-5. On this evidence, run
   **1 per 3** until the reach advantage decays. Do not convert the whole feed to story: authority still
   has to come from the P1/P2/P3 posts, and hero-only means entertainment with nobody buying.
2. **The honesty is the mechanism, not the topic.** A polished founder-journey post is still a polished
   post. What travelled was the admission with a number attached to it.
3. **Zero-CTA is not costing us anything yet.** The no-CTA post out-earned every CTA post on profile
   views. Inbound interest is coming from recognition, not from asks.
4. **Next test (this post, 2026-08-01):** does chapter two of the same story hold the reach, or was
   07-28 a one-off novelty spike? Check impressions + out-of-network split against 1,500 / 95%.

## 2026-07-19 — Week of 2026-07-13 review

**Follower growth:** 302 → 308 (+6, +1.99%) over 2026-07-15 to 2026-07-19. Slower than last
week's +25, but only 5 days of data and only 2 posts live.

**Posts with synced analytics (2, both published 2026-07-17):**

| Date | Day | Post (angle) | Impressions | Reach | Likes | Comments | Saves | Eng. rate |
|---|---|---|---|---|---|---|---|---|
| 07-17 | Fri | Sonnet 5 stack swap, cost-delta sequel (P1) | 100 | 46 | 5 | 2 | 0 | 7.0% |
| 07-17 | Fri | Multi-channel outbound carousel (P3) | 107 | 37 | 4 | 4 | 0 | 7.48% |

Both were drafted for week-of-2026-07-20 (Tue/Wed slots) but published early by Usama on Friday.

**Best: the multi-channel carousel (7.48% ER, 4 comments).** Highest engagement rate of ANY post
to date (previous best 5.8%), and double the comments of the text post. Carousel format + a full
named-steps framework + the reply-cancels-everything stop condition gave people something concrete
to react to.

**Runner-up, not worst: the Sonnet 5 swap (7.0% ER).** Also beat every pre-07-17 post. The
cost-delta hook keeps winning.

**Caveat:** both went live around 11:30pm-12:15am ET (Thu night/Fri early AM), far off the
recommended Tue-Thu morning ET windows. Impressions stayed near 100 despite record engagement
rates, so reach, not resonance, is the current bottleneck.

**Learnings for this week's drafts:**
1. **The register is working, keep it.** Cost-delta hooks + named-steps frameworks lifted ER from
   a 2-5.8% range to 7-7.5%. Do not change the formula this week; change the variables.
2. **Carousels earn comments.** 2x the comments of the text post at similar impressions. Keep one
   carousel per week and keep the comment-trigger close on the final slide.
3. **Test the actual slots.** Both record posts went out near midnight ET. If the same register
   posts in the Tue-Thu 7:30-10am ET windows this week, we get a clean read on whether timing
   moves impressions. Ask Usama to publish in-slot this week rather than batching late-night.



**Follower growth:** 277 → 302 (+25, +9.03%) over 2026-07-02 to 2026-07-15. Healthy trajectory for a cold account.

**Posts with synced analytics (3):**

| Date | Day | Post (angle) | Impressions | Reach | Likes | Comments | Saves | Eng. rate |
|---|---|---|---|---|---|---|---|---|
| 07-02 | Thu | "429 retry bug" silent-failure story (P1) | 196 | 93 | 3 | 1 | 0 | 2.04% |
| 07-06 | Mon | "Your LLM is not a sales agent" contrarian (P2) | 119 | 44 | 3 | 2 | 0 | 4.2% |
| 07-07 | Tue | "$1,500/mo → $45/mo n8n stack" (P3, STACK CTA) | 138 | 92 | 5 | 2 | 1 | 5.8% |

**Best: the $1,500→$45 stack post (07-07).** Highest engagement rate and the only post with a save.
Real dollar-delta hook in line 1, named tools + real prices, a live vendor-risk peg (Artisan's
LinkedIn ban), and a comment-to-DM CTA (STACK) gave people a concrete reason to comment vs. just react.

**Worst: the 429 retry bug story (07-02).** Highest impressions/reach of the three but the lowest
engagement rate (2.04%) and only 1 comment. It's a strong story but ended on a generic reflection
question ("what's the quietest failure...") with no CTA structure and no stat/number to pull people
into the comments the way the cost-comparison and contrarian-stat posts did.

**Note:** 2 of last week's planned 4 drafts (the follow-up-automation build story for Wed and the
5-boring-automations carousel for Thu) do not show as published — likely still pending Usama's image
step or a scheduling gap. Worth flagging in this week's summary.

**Learnings for this week's drafts:**
1. **Cost/number-delta hooks outperform pure story hooks in engagement rate** — lead with a real
   dollar or percentage delta in line 1 where the angle allows it, even on build-in-public posts.
2. **A concrete CTA (comment-to-DM keyword tied to a real magnet) beats a generic reflection
   question** for driving comments — reserve the generic "what's your experience" close for posts
   that truly have no natural magnet fit, and sharpen it to reference something specific in the post.
3. **Saves are still rare (1 of 3 posts, 0 elsewhere)** — this week, lean harder into save-worthy
   structure (numbered lists, frameworks, before/after tables) per `winning-post-patterns.md`, since
   the account isn't earning saves yet on story-only formats.
