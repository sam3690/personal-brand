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
