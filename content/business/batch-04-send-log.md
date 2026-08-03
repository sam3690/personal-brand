# Batch 04 send log (interior design, current niche)

Source: `prospects/batch-04-2026-07-23-austin-local.csv` (Apify Google Maps, Austin). CSV mixes
interior-design/staging prospects with off-niche roofing/med-spa rows from the same scrape; only the
9 interior-design + home-staging rows were sent, per current-strategy.md niche (interior design +
adjacent high-ticket home-design studios). Roofing and med-spa rows left unsent, off-niche.

Personalization: fetched each site's About/homepage to find the owner's name where available and
greeted by first name instead of generic "Hi,". No verified personal (non-hello@/info@) email address
was found for any of the 9 — sent to the best available business address in the CSV in all cases.
MX records verified for all domains before sending (Google Workspace or Microsoft 365 all resolved);
one recipient (vivahomestagingdesign@gmail.com) uses gmail.com, trivially valid.

## Touch 1 (day 0, sent 2026-07-27 18:33 PKT)
- SENT interiors@austindesigngroup.com (Austin Design Group, 4.9★/8) messageId: 19fa3c7ceff7793c hubspotEngagementId: 386491337403 hubspotContactId: 526399494860 — no owner name found, generic greeting
- SENT hello@livingoak.com (Living Oak Interior Design, 5★/19 — owner Laura Williams, Founder & Principal Designer) messageId: 19fa3c7cf204bd95 hubspotEngagementId: 386308028101 hubspotContactId: 526691551942
- SENT hello@hicountrypaperworks.com (Hi-Country Paperworks, 5★/63 — owner Steve Vaneman) messageId: 19fa3c7cf0664dbd hubspotEngagementId: 386534712033 hubspotContactId: 526725986028
- SENT hello@wilandfaye.com (Wil and Faye Interiors LLC, 5★/40 — founder Brooklynn) messageId: 19fa3c7cfd2bf483 hubspotEngagementId: 386308028115 hubspotContactId: 526687924940
- SENT info@nextlevelaustin.com (Next Level Austin, 4.7★/13) messageId: 19fa3c7d494fd77e hubspotEngagementId: 386534712048 hubspotContactId: 526831100624 — no owner name found, generic greeting
- SENT vivahomestagingdesign@gmail.com (Viva Home Staging Design, 4.9★/34 — owner Ruth Xiomara) messageId: 19fa3c7d5e5c3d51 hubspotEngagementId: 386287058647 hubspotContactId: 526689565428
- SENT info@allisonjaffe.com (Allison Jaffe Interior Design, 4.9★/27 — owner Allison Jaffe, per business name) messageId: 19fa3c7d430f6ee5 hubspotEngagementId: 386491337414 hubspotContactId: 526687155907
- SENT sosospiffysales@gmail.com (Spiffy Home Staging & Design, 5★/6 — owner Barbara Cooney, CEO) messageId: 19fa3c7d517bfefa hubspotEngagementId: 386537810662 hubspotContactId: 526716901095
- SENT info@turnstyleid.com (Turnstyle Interior Design, 4.7★/14) messageId: 19fa3c7dba9c911b hubspotEngagementId: 386537810663 hubspotContactId: 526385425090

All 9 contacts + engagements logged to HubSpot, portal 246685260. — no owner name found, generic greeting

9/9 sent, no immediate bounces detected as of this run (checked Gmail for mailer-daemon replies).
Note: one bounce in batch-03 (Dave Anderson) took 3 days to surface as a permanent failure after an
initial delayed-retry notice — re-check this batch's threads on/before touch 2 (due 2026-07-30) for
any bounces that land later.

Touch 2 due 2026-07-30. Touch 3 due 2026-08-03.

Off-niche rows in the CSV, not sent (kept for reference, not a future niche): Bill Sprauer Austin
Roofing, Glowing Skin Med Spa, Austin Aesthetic Atelier, Light Touch Aesthetics, NeoSkin Spa, Glo Med
Spa Austin, Ace Roofing, Spa Sway, Priority Roofing, HD Roofing and Repairs, Dayton Co. Roofing,
NakedMD Med Spa, Austin Roofing Company & Water Damage, Bobcat Roofing.

## Touch 2 (day 3, due 2026-07-30, sent 2026-07-30 18:26 PKT, on time)
Sent as in-thread replies (GMAIL_REPLY_TO_THREAD). All 9 threads re-checked for bounces/replies before
sending (GMAIL_FETCH_MESSAGE_BY_THREAD_ID on each) — none found, clean SENT-only threads, no late
bounces surfaced. The `[LOOM LINK]` placeholder in outreach-scripts.md is still unfilled (directive #4,
Usama has not recorded it yet) — dropped that line rather than send a broken/invented link; replaced
with an offer to send the video ("Want me to?").

- [2026-07-30 18:26 PKT] TOUCH2 SENT interiors@austindesigngroup.com (Austin Design Group) messageId: 19fb32ed6b96b822 hubspotEngagementId: 387291439842 hubspotContactId: 526399494860
- [2026-07-30 18:26 PKT] TOUCH2 SENT hello@livingoak.com (Living Oak Interior Design, Laura Williams) messageId: 19fb32ed7395d977 hubspotEngagementId: 387291439845 hubspotContactId: 526691551942
- [2026-07-30 18:26 PKT] TOUCH2 SENT hello@hicountrypaperworks.com (Hi-Country Paperworks, Steve Vaneman) messageId: 19fb32edf553bcd4 hubspotEngagementId: 387291379424 hubspotContactId: 526725986028
- [2026-07-30 18:26 PKT] TOUCH2 SENT hello@wilandfaye.com (Wil and Faye Interiors LLC, Brooklynn) messageId: 19fb32ede729dc36 hubspotEngagementId: 387295750894 hubspotContactId: 526687924940
- [2026-07-30 18:26 PKT] TOUCH2 SENT info@nextlevelaustin.com (Next Level Austin) messageId: 19fb32edf684096a hubspotEngagementId: 387291318001 hubspotContactId: 526831100624
- [2026-07-30 18:26 PKT] TOUCH2 SENT vivahomestagingdesign@gmail.com (Viva Home Staging Design, Ruth Xiomara) messageId: 19fb32edf58d6b2b hubspotEngagementId: 387291163341 hubspotContactId: 526689565428
- [2026-07-30 18:26 PKT] TOUCH2 SENT info@allisonjaffe.com (Allison Jaffe Interior Design) messageId: 19fb32ee94fb7350 hubspotEngagementId: 387291486934 hubspotContactId: 526687155907
- [2026-07-30 18:26 PKT] TOUCH2 SENT sosospiffysales@gmail.com (Spiffy Home Staging & Design, Barbara Cooney) messageId: 19fb32ee933e8506 hubspotEngagementId: 387277419252 hubspotContactId: 526716901095
- [2026-07-30 18:26 PKT] TOUCH2 SENT info@turnstyleid.com (Turnstyle Interior Design) messageId: 19fb32ee8e3a939f hubspotEngagementId: 387291768517 hubspotContactId: 526385425090

9/9 sent, no immediate bounces. Touch 3 due 2026-08-03.

## Touch 3 (day 7, due 2026-08-03, sent 2026-08-03 20:50 PKT, on time)

**Growth Lead decision (2026-08-03 run):** current-strategy.md flagged an unresolved conflict same day
this touch came due: the CEO repositioned the niche from interior-design to "automation operator" and
explicitly noted batch-04 still targets the old niche, leaving two options ("re-source to
automation operators or run the interior list to completion as a separate test"). Growth Lead resolved
it: send touch 3 (a breakup/closing email, not new off-niche pitch expansion) and then **close batch-04
permanently**. No batch-05 interior, no further interior sourcing. All new sourcing from here is
automation-operator only.

Sent as in-thread replies (GMAIL_REPLY_TO_THREAD). All 9 threads re-checked for bounces/replies before
sending (GMAIL_FETCH_MESSAGE_BY_THREAD_ID on each) — none found, clean SENT-only threads (2 messages
each, both from us), no late bounces or replies surfaced. Also swept the general inbox for any reply
received since the 07-30 run — none from any prospect domain, across any batch.

- [2026-08-03 20:50 PKT] TOUCH3 SENT interiors@austindesigngroup.com (Austin Design Group) messageId: 19fc8513a450b280 hubspotEngagementId: 388180998871 hubspotContactId: 526399494860
- [2026-08-03 20:50 PKT] TOUCH3 SENT hello@livingoak.com (Living Oak Interior Design, Laura Williams) messageId: 19fc8513aa91a41d hubspotEngagementId: 388261389031 hubspotContactId: 526691551942
- [2026-08-03 20:50 PKT] TOUCH3 SENT hello@hicountrypaperworks.com (Hi-Country Paperworks, Steve Vaneman) messageId: 19fc8513aaadb4db hubspotEngagementId: 388234485438 hubspotContactId: 526725986028
- [2026-08-03 20:50 PKT] TOUCH3 SENT hello@wilandfaye.com (Wil and Faye Interiors LLC, Brooklynn) messageId: 19fc8513a23d4fac hubspotEngagementId: 388256842445 hubspotContactId: 526687924940
- [2026-08-03 20:50 PKT] TOUCH3 SENT info@nextlevelaustin.com (Next Level Austin) messageId: 19fc8514016534c9 hubspotEngagementId: 388261036731 hubspotContactId: 526831100624
- [2026-08-03 20:50 PKT] TOUCH3 SENT vivahomestagingdesign@gmail.com (Viva Home Staging Design, Ruth Xiomara) messageId: 19fc85141c5232b8 hubspotEngagementId: 388167080661 hubspotContactId: 526689565428
- [2026-08-03 20:50 PKT] TOUCH3 SENT info@allisonjaffe.com (Allison Jaffe Interior Design) messageId: 19fc851416052ade hubspotEngagementId: 388251628249 hubspotContactId: 526687155907
- [2026-08-03 20:50 PKT] TOUCH3 SENT sosospiffysales@gmail.com (Spiffy Home Staging & Design, Barbara Cooney) messageId: 19fc85141672fedf hubspotEngagementId: 388260695799 hubspotContactId: 526716901095
- [2026-08-03 20:50 PKT] TOUCH3 SENT info@turnstyleid.com (Turnstyle Interior Design) messageId: 19fc8514615304c0 hubspotEngagementId: 388260802249 hubspotContactId: 526385425090

9/9 sent, no immediate bounces. **Batch-04 sequence is now COMPLETE and CLOSED.** No further sends to
this batch, no batch-05 interior. Reply rate: 0/9. Combined pipeline (batch-01 through batch-04):
0/31 contacted, 0 replies, 22 days in for the oldest batch. See linkedin-connect-todo.md: no new
entries this run (batch-04's CSV has no LinkedIn URLs, Apify Google Maps source).
