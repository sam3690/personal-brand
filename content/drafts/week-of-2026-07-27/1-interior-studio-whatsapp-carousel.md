# Post 1 — "An interior design studio's WhatsApp enquiries: 24-hour wait → instant reply" (Carousel)

- **Skeleton:** C (Build-in-public / case-study carousel) · **Pillar:** P1 Build-in-public
- **Hook formula:** Case-study / client outcome first (Formula 4) · **Format:** Carousel (document, intro post ~800 chars)
- **CTA:** genuine operator question ("what happens to your WhatsApp enquiries after 6pm?") + follow/conversation
  (no magnet forced — no existing lead-magnet in `../../lead-magnets/` fits the new niche yet)
- **SEO keywords (woven in):** interior design studio, WhatsApp automation, lead response time, n8n, consult booking
- **Slot:** Tuesday 2026-07-28, 7:30–9:00 AM ET (5:00 PM PKT) — this week's CEO-mandated case-study post
  (2026-07-27 review, directive 5) and the week's designated carousel (the account's only 7%+ ER post to date
  was a carousel, per `../../performance/linkedin-performance-log.md`)
- **Anonymization note:** the client is referred to only as "an interior design studio I worked with." The real
  name (internal: UF Designs) is withheld pending naming permission (CEO directive 3) — never write it into
  post copy. Proof numbers (24h → seconds, 7-8 → 27 consults/mo, ~3.5x, the client quote) are the CEO-confirmed
  figures from `../../strategy/current-strategy.md`; treat as accurate, hedge with "roughly" only if Usama flags
  either number as approximate before publishing.
- **Sources:** consult/response figures + quote from `../../strategy/current-strategy.md` (PROOF TO LEAD WITH
  section); $20k median renovation project value from the Houzz 2026 Houzz & Home Study, per
  `../../research/week-of-2026-07-27.md`
- **QA (self-scored against Agent 5 rubric):** 93/100 PASS · red flags: none
  - Hook 17/18 (result in line 1, case-study formula, well under 210 chars) · Specificity 15/16 (named surface —
    WhatsApp Business API, Meta lead form, LLM node, CRM sheet — plus a verbatim client quote) · Comment-trigger
    14/16 (specific, experience-based close) · Save-worthiness 9/10 (named-step build + before/after) · Pillar
    fit 11/12 · Dwell 9/10 · Format fit 8/8 (carousel matches the save/comment goal) · Hashtags 4/4 (zero) ·
    Voice 6/6 (no em dashes, no banned phrases)
  - Hook-Payoff Integrity: PASS — cover promises an outcome + "here's how we built it" (a process claim); slides
    3-6 deliver the ordered steps of that one build, not a mislabeled count. Offer legibility: PASS — plain-
    language line present in both the intro post and the close slide.
  - Projected engagement: HIGH (named-step carousel + before/after numbers + a genuine near-failure slide)

---

**INTRO POST (text above the carousel):**

An interior design studio was answering WhatsApp enquiries in 24 hours.

Now it's seconds.

Consults went from roughly 7-8 a month to roughly 27.

Here's the situation before we touched anything.

The studio runs Meta ads for kitchen and full-home renovation work. Real interest, real budget. Houzz's research puts the median renovation spend at around $20k, so every enquiry that sat unanswered was a shot at a project that size going quiet.

The ads were never the problem. The gap was between "someone messages" and "someone actually replies." The owner was on client sites most of the day. A WhatsApp enquiry would land, get seen, and wait. Sometimes a full day.

So we built a system that replies the second the message lands, asks the questions a designer would actually ask (budget, room, timeline), and books the consult straight into the calendar, no human required until the call is already confirmed.

One month in, running live, the owner's own words: "big difference, saving me so much time."

Full build, slide by slide, in the carousel below.

What happens right now to the enquiries that land on your WhatsApp after 6pm?

**CAROUSEL SLIDES:**

1. **Cover:** Hero stat "7-8 → 27 CONSULTS/MONTH." Headline: an interior design studio's WhatsApp enquiries went from a 24-hour wait to an instant reply. Payoff: "→ Here's exactly how we built it."
2. **The before:** Every enquiry was a race the studio was losing. Meta ads brought in real leads (kitchen remodels, full home renovations, $20k+ projects per Houzz). But the owner was on client sites most of the day: a WhatsApp message would land, get seen, and sit, sometimes a full day before a reply went out.
3. **Step 1 (Trigger):** A webhook watches the WhatsApp Business API and the Meta lead form. A new enquiry fires the workflow in under a second. No polling, no missed message.
4. **Step 2 (Reply):** A real-sounding reply goes out first, not a form. An LLM node drafts the first response in the studio's own voice and sends it over WhatsApp before anything else happens. That's what kills the "seen, no reply" feeling.
5. **Step 3 (Qualify):** The system asks what a designer would ask. One question at a time, inside the same WhatsApp thread: project type, rough budget band, timeline. No forms, no app to download.
6. **Step 4 (Book + log):** Once qualified, the flow holds a slot on the studio's calendar, confirms it back over WhatsApp, and logs the lead (project type, budget band, source ad) to a CRM sheet, so nothing depends on memory.
7. **What nearly broke it (stop slide):** Version one asked too much, too fast. Leads went quiet mid-chat. The first build fired three qualifying questions in one message before saying anything human, and reply rate inside the thread dropped hard in the first 48 hours. People were ghosting the bot, not the studio. Fix: one question per message, a warm line before any question, human handoff if a lead stalls twice.
8. **The result:** WhatsApp response, 24 hours to seconds. Consults booked, roughly 7-8/month to 27 in one month live (~3.5x). Quote: "Big difference, saving me so much time." (the studio owner). Source note: self-reported, one month of live data.
9. **Close:** "The fix was never more ads. It was answering the enquiries already coming in." What happens to your WhatsApp enquiries after 6pm right now? Follow for more real builds like this one.

**FIRST COMMENT:** none needed — no link or asset referenced in this post.

---

# Media brief

**Build tool:** Claude Design project "Brand system design for social media carousels" (Green Room kit v1.2) —
https://claude.ai/design/p/5790bcce-f02c-4647-a1dd-9837aee8c75f (not Canva). Copy
`../../../carousels/green-room/carousel-multichannel-outbound.dc.html` as the starting template, swap slide
copy per below, keep the chip / code-plate / author-badge / footer markup as-is. Render via
`google-chrome --headless --disable-gpu --print-to-pdf` on the `-print.dc.html` variant, or screenshot each
1080×1350 slide directly.

- **Type:** LinkedIn document post (carousel), 9 slides, 1080×1350 each, Green Room v1.2 system.
- **Concept (whole deck):** BG-MAIN emerald flow-field at deep zoom (~220-250%) on interior slides, lighter
  zoom on cover/close; one red pattern-break slide for the near-failure moment; before/after table + hero stat
  on the result slide; author badge fixed bottom-right on every slide; footer counter `NN/09`.
- **Slide-by-slide visual direction:**
  1. Cover — quote-frame border; hero stat "7-8 → 27 CONSULTS/MONTH" in Signal Green Anton (biggest element);
     headline "AN INTERIOR DESIGN STUDIO'S ENQUIRIES: 24-HOUR WAIT → INSTANT REPLY" in Bone White Anton; payoff
     "→ Here's exactly how we built it"; 110px author badge.
  2. Before — chip "THE BEFORE"; two short body paragraphs; illustrative (non-real) dimmed WhatsApp-style chat
     mock showing an unanswered message with an old timestamp.
  3. Step 1 — chip "STEP 1 · TRIGGER"; webhook/lightning-bolt icon tile; small code plate, generic webhook
     snippet, rotated -1.2° with traffic-light dots.
  4. Step 2 — chip "STEP 2 · REPLY"; chat-bubble icon tile; code plate showing a generic "auto-reply drafted"
     snippet.
  5. Step 3 — chip "STEP 3 · QUALIFY"; checklist icon tile; small spec card listing the three qualifying
     fields (project type / budget / timeline).
  6. Step 4 — chip "STEP 4 · BOOK + LOG"; calendar icon tile; calendar card component (green selected-day
     circle) paired with a small CRM-row spec card.
  7. Pattern break (stop) — full red frame, red chip "WHAT NEARLY BROKE IT," red radial glow overlay, no green
     accents on this slide.
  8. Result — before/after 2×2 table (dimmed "before" column, Signal Green "after" column): response time row +
     consults/month row; hero stat "27 CONSULTS THIS MONTH"; quote in the quote-frame treatment; small

> **[TRUNCATED]** the source draft was cut off mid-sentence here during transfer between sessions.
> Slide 8's remaining direction and slide 9 (Close) need re-deriving from the slide list above before rendering.
