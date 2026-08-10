# DM Lane Targeting Spec (LinkedIn)
> The operational companion to `../strategy/2026-08-09-dm-lane-decision-brief.md`. Open this, work
> down it, stop. Every target number below either traces to research (source noted) or is marked as an
> assumption to be replaced by Usama's own data after two weeks.
> **This spec replaces `linkedin-connect-todo.md`.** That queue is deleted, see section 0.

---

## 0. BEFORE THE FIRST REQUEST

**Delete the 24-name queue. Do not send it, do not withdraw anything already sent.**

Those names are C-suite at established agencies. ReachIQ's 2026 seniority data puts C-suite reply rate
at 1.9% against 5.5% for managers and 6.1% for individual contributors, and Belkins' 7.5M-email dataset
puts 11-50 employee firms at 0.49% against 0.22% for 10,000+. More importantly, LinkedIn's own help
documentation names invitations "ignored, left pending, or marked as spam" as a trigger for restricting
the account, escalating from hours to a month to suspension. One account, no backup. Bad targeting is
not a cheap test.

**Withdrawal is not the fix.** Withdrawing locks out re-inviting that person for up to three weeks,
there is no bulk withdraw, and the recipient is never notified. Leave what is sent, fix what is next.

**Three profile changes first, they gate everything downstream:**
1. Remove "speed to lead" and any variant from the headline. It is vendor vocabulary that no owner
   uses, and among marketers it is now openly contested as a metric.
2. Put the three anonymized proof numbers in the banner and the top of About, where they are visible
   **before** the accept decision: reply time 24 hours to seconds, consults 7-8/month to 27/month, 14
   customers in 3 weeks.
3. State a US-hours overlap commitment explicitly in About. Do not wait for it to become a call
   objection. Named Pakistan-based operators serving US clients converge on this: never hide the
   location, answer it structurally before it is asked.

**Do not buy Premium or Sales Navigator for a higher invite cap.** LinkedIn's docs state the limits
apply to "all LinkedIn members, including those with Basic and Premium accounts." There is no higher
cap to buy.

---

## 1. THE TARGET PROFILE

| Attribute | Value | Why |
|---|---|---|
| **Headcount** | **1-10 employees.** Hard ceiling 20 | Sapience 2026: 1-10 person companies reply 75% more often than 5,000+. Belkins: 11-50 at 0.49% vs 10,000+ at 0.22% |
| **Title** | Founder, Owner, Co-founder, Principal, Managing Director of that company. **Never** a C-suite title at a company big enough for the title to mean a layer | ReachIQ: C-suite 1.9% reply, Director 4.6%, Manager 5.5%. At 4 people the founder IS the operator; at 40 the CEO is a layer |
| **Business type** | B2B service firms that sell an outcome they only partly control: creative studios, performance/media buying shops, recruiting firms, fractional teams, boutique consultancies with a non-technical service | Professional services ranks 2nd of all buyer industries at 5.1% median reply, explicitly because the buyer also does outbound |
| **Geography** | US, UK, CA, AU, Western Europe | Existing target market. Note: US is the hardest reply market measured (6.0% in Belkins' 17-country breakdown), so do not read low US numbers as a targeting failure |
| **Activity** | **Posted in the last 30 days.** Non-negotiable | A live account sees the request and can be warmed first. A dormant one produces a pending invite, which is a documented restriction trigger |

### The one disqualifier that does the most work

> **If the prospect's own product is software, marketing automation, data, or technical consulting,
> they are a peer, not a buyer.**

This is simpler than headcount and catches every failure mode at once. It kills web/dev shops (they
employ the engineers), IT and management consultancies (they sell the same thing), other n8n and
AI-automation operators (tribe version 2's error, do not repeat it), and SaaS startups (they have a
product team).

### The second disqualifier, and it is new

> **If they run GoHighLevel, skip them, or change the pitch entirely.**

GHL ships missed-call text-back as a native toggle on every plan ($97 / $297 / $497 per month, verified
on the pricing page 2026-08-09). Most small marketing and performance agencies already pay for it.
Selling a $1,500 build of a feature already in their stack is a dead sale, not a hard one. If a
GHL-running agency is otherwise a great fit, the only pitch that survives is what GHL does not do
without a builder: unifying WhatsApp, Instagram DM, web form and phone under one qualification brain
with CRM write-back.

### Also skip

Freelancers with no team (different economics, cannot pay), pre-revenue and course-stage (no accounts
to lose), enterprise (procurement, not a person), and anyone whose problem is that they have no leads at
all (we do not do demand generation, and saying so early is what earns the referral later).

---

## 2. SEARCH RECIPES

Apollo is paywalled on this account. These are the routes that work without it.

### Recipe 1: LinkedIn people search, the core engine
```
Search: "founder" OR "owner" OR "co-founder"
Filters: Company headcount = 1-10, 11-50  |  Locations = United States, United Kingdom, Canada, Australia
Then filter by hand on headline keyword: agency, studio, recruiting, consulting, creative, media
```
Sort the results by who has posted recently. Expect roughly 40% to fail the peer disqualifier on sight.
**Volume: ~30 qualified names per 20 minutes. Quality: highest of any recipe.**

### Recipe 2: The engagers on somebody else's post
Find a post from an agency-owner account arguing about retainers, capacity, churn or client management.
Open the reaction list. Everyone who reacted is a live account that just self-identified on the topic.
**Volume: 10-30 per post. Quality: highest per name, lowest volume.** These are the ones to warm first.

### Recipe 3: Comment sections of the "leads are garbage" genre
Search LinkedIn for the phrase, not the person: `"the leads are garbage"`, `"they went with someone
else"`, `"we are at capacity"`. Work the commenters, not the poster (the poster is usually a vendor).
**Volume: low. Quality: they used the words themselves, which is the single best signal available.**

### Recipe 4: Apify Google Maps, for the cold-email lane only
This does **not** feed LinkedIn. Google Maps returns a business, not a named person with a profile, and
no cheap bridge exists now that Apollo is paywalled. Keep the two funnels separate rather than
pretending they join.
```
Query: <segment noun> + <metro>, rotating: Austin, Denver, Charlotte, Phoenix,
       Manchester, Leeds, Calgary, Ottawa, Brisbane, Perth   (avoid NYC/London/LA)
Keep rows where: 15-250 reviews, rating 4.2+, website present, phone present, not a chain
```
**Highest-intent free filter available:** Google reviews mentioning "never called back," "no response,"
or "hard to reach." That is the prospect telling you the problem in public.

### Recipe 5: Community answering, the primary lane
Not a search recipe, a standing habit. r/n8n, r/automation, r/smallbusiness, r/nocode, and the n8n
community forum. Search for people describing the problem: "manual process," "wasting time on," "follow
up," "leads." **Answer completely, give the whole solution away, never pitch.** Let them DM.

This ranks first on evidence because it is the only channel found where competence is demonstrated
**before** identity is evaluated, which matters given the measured offshore penalty (Upwork's own
commissioned economist report: US freelancers earn 82% more from the same clients and are 51% more
likely to be hired, controlling for the rate bid). Caveat honestly: every first-client account
supporting this lane is an unverified self-report. The mechanic is well corroborated across independent
accounts; the specific numbers are not.

---

## 3. QUALIFY BEFORE YOU CONNECT (30 seconds per profile)

Run in this order. Any FAIL, skip and move on. Do not "give it a try."

1. **Headcount 1-20 on the company page?** Not 1-20 in your impression of them, on the page. FAIL if bigger.
2. **Is their product software, marketing automation, data, or technical consulting?** FAIL if yes.
3. **The build-it-themselves test:** would this person, or someone visibly on their team, plausibly wire
   this in a weekend? Look for any engineer, any developer, any "technical co-founder," any n8n or
   Zapier or Make mention anywhere on the profile. FAIL if yes.
4. **Posted in the last 30 days?** FAIL if no. Dormant accounts produce pending invites, and pending
   invites are a documented account-restriction trigger.
5. **Do they have inbound at all?** Any sign of clients, ads, a real website, reviews. We do not do
   demand generation. FAIL if there is nothing arriving.
6. **Open Profile?** If the button says "Free Message" rather than "InMail," they can be messaged
   directly with no connection request and no credit. **Route these around the invite cap entirely.**
   Measured Open InMail reply rate is 7.5%, roughly level with cold connector campaigns at 7.9%.

---

## 4. THE DAILY RUN SHEET (45 minutes)

The order matters. Warming first, requests second, because the request lands on a name that has already
seen you.

| Block | Minutes | What |
|---|---|---|
| **1. Community answering** | 25 | 2-3 complete answers in r/n8n, r/automation, r/smallbusiness, or the n8n forum. Whole solution, no pitch, no link, no "happy to help if you want to chat" |
| **2. Warm** | 8 | Follow 5 targets (free, unlimited, notifies them, costs zero invite budget). Leave 3-5 substantive comments on target posts. Not "great post" |
| **3. Source and request** | 7 | Qualify 8-10 profiles against section 3, send **4-5 blank connection requests**. No note: free accounts get only 5 notes a month, so the debate is moot |
| **4. Converse** | 5 | Reply to anyone who accepted or replied. First message after acceptance is where all the personalization goes. **No offer, no price, no calendar link in message one.** One question. Mirror their length |

**Weekly volume: 20-25 connection requests, not 50, and nowhere near the platform ceiling.** A
PhantomBuster survey (fielded Q4 2025) found reps sending under 25 requests a week are nearly twice as
likely to hit 40%+ acceptance as those sending 26 or more. That is self-reported vendor data, so soft,
but it converges from a completely different direction with LinkedIn's own documented trigger, "many
invitations within a short amount of time." Two independent reasons pointing the same way is enough.

**Never automate any of it.** LinkedIn's Prohibited Software policy explicitly bans tools that scrape or
automate activity, consequence being restriction or shutdown. Manual only, which 20-25 a week makes
easy.

---

## 5. THE TRACKING TABLE

One row per day. The first four columns produce a readable number inside a week, which is the entire
point of tracking them.

| Date | Answers posted | Follows | Comments | Requests sent | Accepts | First messages | Replies | Live threads | Inbound DMs |
|---|---|---|---|---|---|---|---|---|---|

### Target values and what they mean

| Metric | Benchmark | Source | Read it at |
|---|---|---|---|
| Connection acceptance | **28.5%** platform-wide | Expandi, 13.2M requests, May 2025-Apr 2026 | Day 7. 88% of accepts land within a week, 63% within 24 hours |
| Post-connection reply | **10.4%** | Same dataset | Week 4 |
| Conversations per month | **~3** at 20-25 requests/week | Derived from the two rates above | Week 8 |
| Community answers to first inbound DM | No reliable benchmark exists | Self-reports only, all unverified | 40 answers over 6 weeks |
| Cold email replies | Median 3.43-4.8% | Instantly, ReachIQ 2026 | **120 sends**, not before |

### The stop-and-change triggers, set in advance

1. **Acceptance rate materially below 15%** against the 28.5% benchmark, measured over the first 100
   requests → the blocker is the profile or the location being read off it. Content must precede DMs
   rather than accompany them. Fix the profile before sending more.
2. **40+ genuinely useful community answers over 6 weeks producing zero inbound DMs** → the community
   lane is wrong for this niche. Promote LinkedIn DMs to primary.
3. **120 well-targeted cold emails to 1-10 person prospects still yielding zero replies** → the defect
   is the offer or the ICP, not the channel and not the volume. Rework the offer before any channel
   gets more time.
4. **Nothing at all by day 90-120 across all three lanes** → that is the real review point. Multiple
   independent operator accounts put first client at month 2 to month 5. Day 19 at zero is normal, and
   rewriting the strategy at day 19 has already cost more than it produced.

### Two matched batches, run once, this week

Twenty minutes, settles an argument that no public dataset can answer:

- **Batch A:** 25 no-note requests to founders and owners at 2-20 headcount.
- **Batch B:** 25 no-note requests to CEOs at 50-200 headcount.

Read both at day 7. No study anywhere breaks acceptance rate down by recipient seniority or recipient
company size with disclosed methodology; the one source claiming a gradient publishes no sample size,
no method, no date, and sells LinkedIn outreach services. Usama's own 50 requests will be better
evidence than anything currently published.

---

## 0b. OPEN ACTIONS (next session starts here)

In this order, because each one gates the next. Status updated 2026-08-10. The live log for actions
2 to 5 is `dm-lane-tracker.md`.

1. **Rewrite the profile.** ✅ Copy written 2026-08-10: `profile-rewrite-2026-08-10.md`. Two fill-ins
   left for Usama (the US overlap window, the Axios line) and then it has to be pasted into LinkedIn by
   hand. **Nothing in action 2 goes out until it is live.** Original brief below. Headline, banner line, and About section. Every connection
   request lands on this, so it gates the whole lane. Drop "speed to lead" and the generic
   "AI automation for Founders & agency owners" framing (a named buyer with 31 agreeing commenters
   said he now auto-rejects anyone whose profile says AI automation). Put the three anonymized numbers
   above the fold, and state the US-hours overlap commitment in About.
2. **Run the two matched batches of 25** from section 5. Twenty minutes. Read at day 7. Tables, search
   method and the day-7 read are set up in `dm-lane-tracker.md`. Manual sending only, blocked on 1.
3. **Start the community habit** from Recipe 5. Two complete answers a day, no pitch. Logged daily in
   `dm-lane-tracker.md`.
4. **Cold email: CONTINUES. Keep sourcing.** *(Corrected by CEO ruling 2026-08-10. This item previously
   read "107 of 120 sends are done, finish in flight only" and told the Mon/Thu scheduled tasks to be
   stopped or emptied. That was a unit error: the 120 threshold counts independent contact attempts, not
   individual emails, and three emails to one uninterested person is one decision. **The tasks stay ON.**
   Rationale in `../strategy/current-strategy.md`, COLD EMAIL RULING.)*
   **Real position: 31 of 120 prospects contacted, about 26% of the way.** No owed follow-ups remain,
   batches 01-04 are all fully sequenced. **Citation fix (found 2026-08-10 during the batch-05 run):**
   the cold-email lane's actual sourcing criteria live in **section 2, Recipe 4** ("Apify Google Maps,
   for the cold-email lane only" — review count/rating/chain filters, metro rotation) plus the peer
   disqualifier and the "already has a bot" check pulled from section 1. Section 1's target profile
   itself (headcount, B2B service-firm business type, GoHighLevel check) is written for Lane 2 LinkedIn
   DM and does not map onto interior-design/home-design studios; reading it literally for Lane 1 sourcing
   would incorrectly disqualify the entire niche. Batch-05 (Denver, 10 sourced) was sourced correctly
   under this reading. `current-strategy.md`'s COLD EMAIL RULING still says "section 1" and should be
   updated to point here the next time that file is touched. Sourcing continues to 120 unique prospects,
   then the close decision is taken on reply count. Deliverability discipline still applies in full:
   Reply rates fell from 8.5% in 2019 to ~3.4% in 2026,
   and since May 2025 Google and Microsoft require SPF/DKIM/DMARC, a 14-day domain age, a 200/day ramp
   on new domains, and spam complaints under 0.10%. Compliant senders reach the inbox ~89% of the time,
   non-compliant senders get 22-34% routed to spam. The setup cost no longer justifies scaling this lane
   at 10-15 hours a week. Decision to close it properly comes at 120 sends, not before.
5. **Then** work the daily run sheet in section 4.

## 6. THE SCRIPTS

**The rules these obey, all from the research. Do not break them to save a message.**

- **No pitch, no price, no calendar link in message one.** A Pakistan-based CPA wrote publicly that US
  professionals now hesitate to accept requests from offshore senders because of the volume of immediate
  pitches, and that the damage is cumulative across the cohort. The bar is higher than neutral.
- **No "speed to lead," no "lead response time," no "AI automation."** Owner vocabulary: missed calls,
  goes to voicemail, call them back, after-hours, they went with someone else, already booked someone
  else. The unit of loss is a **job** or a **customer**, never a lead. And a named UK buyer with 31
  agreeing commenters said he now auto-rejects anyone selling "AI automation" by name.
- **One question. Mirror their message length.** A long reply to a one-liner reads as waiting to be asked.
- **Split into 2-3 short consecutive messages,** never one block.
- **Never claim customers do not mind whether a human or an AI answers.** That exact claim drew the most
  hostile replies of anything in the voice-of-customer research. The defensible version: AI answers
  first, a human is one step away, and the comparison is not AI versus a great receptionist, it is AI
  versus the call that was missed.
- **Pick shape A or shape B. Never both in one thread.** A message that says "your leads, or your
  clients' leads" has picked neither.

### Script 1: accepted connection, shape A (their client's inbox). Lead with this one.

Send within 24 hours of the accept. Two messages, sent back to back.

> Thanks for connecting [Name]. Saw you run [company] and you're doing [the specific thing: paid social
> for home services, retained search, whatever their profile actually says].

> Genuine question, no pitch attached. When you hand a client a month of leads and the booked-calls
> number comes back low, how often does it turn out they just did not call them back?

**Why that question.** It is the whole filter. An agency owner who has lived it answers immediately and
usually with heat, because it is the exact unfairness in section 6 of `../strategy/tribe.md`: being
judged on a number that runs through somebody else's inbox. Someone who has not lived it gives a flat
answer and you have learned that cheaply.

### Script 2: accepted connection, shape B (their own inbox). The easier first yes.

> Thanks for connecting [Name]. [One specific line about their work.]

> Quick one since you run a small shop: when an inquiry comes in on a Friday afternoon while you're
> heads-down delivering, what actually happens to it?

### Script 3: intent signal (they viewed, liked, commented, followed)

Ask about the exact thing they engaged with, then stop. Being wrong about which post does not matter.

> Hey [Name], saw you came across the post about [topic]. Has that one hit you, where the work was fine
> and the account still went sideways?

**Profile viewers are worth more than post engagers.** Senior buyers avoid public engagement because
their team sees it, so they view the profile instead.

### Branch on what comes back

| They say | Do |
|---|---|
| A real story, with heat | You are in. Ask what it cost them: the account, the retainer, the month. Do not pitch yet. That number is the whole sale later |
| "Yeah it happens, it's the client's problem" | Ask whether the client saw it that way. That is the wedge |
| "Our clients are fine on follow-up" | Believe them and move to shape B, their own inbox. If that is also clean, say so and leave. That is what earns the referral |
| "What is it you do?" | Now you can answer. One sentence, outcome not mechanism, no price. Then ask if they want to see the numbers from a build |
| Nothing | One follow-up after 4-6 days, on something they posted, not on your question. Then stop |

### The follow-up

React to something they posted before you message again. Two messages in a row from you, with nothing
from them in between, assumes a yes they never gave.

> [Name], your post on [thing] reminded me of this. [One useful sentence, no ask.]

Follow-up is permitted indefinitely **as long as each one gives something.** The 26-touch arc is real:
roughly 13 messages each way over one to four months. A thread is not dead until they say so.

### When they ask what it costs

Not in message one, not in message two. When it comes:

> $500 for the first two, then $1,500. 50% up front. Live in 7 days or you don't pay, and you own the
> build with no retainer.

**Frame the $500 correctly, every time.** It is two founding slots bought in exchange for a named
reference and a testimonial with a number in it. It is **not** "I'm cheaper." Discounting does not buy
past the geography gap (Upwork's commissioned economist report: US freelancers earn 82% more from the
same clients, controlling for the rate bid; NBER substitution elasticity 0.039). A lower price only
reduces what you collect from buyers who were going to hire you anyway.

### The three artifacts that kill the real objection

The strongest objection in this market is abandonment, not price. Buyers describe paying $2,000-$5,000
and ending up three months later with six subscriptions, an automation that breaks weekly, and no
documentation. Name all three, unprompted, before they ask:

1. Written documentation, handed over.
2. A named point of contact. You.
3. A defined answer to what happens when it breaks: 30 days of fixes included, then a monthly option if
   they want you watching it.

"You own it, no retainer" is currently framed as a pricing feature. It is the best objection-killer
available and it is buried. Lead with it.
