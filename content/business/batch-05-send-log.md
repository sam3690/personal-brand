# Batch 05 send log (interior/home-design, Denver metro)

Source: `prospects/batch-05-2026-08-10-denver-local.csv`. Sourcing method note: Recipe 4
(`dm-lane-targeting-spec.md`) specifies Apify Google Maps, but no Apify connector was available to
this session. Sourced instead via manual web research (WebSearch + WebFetch against each business's
own live website) — every business, contact email, and owner name below was individually verified by
visiting the real site before sending. Google review counts/ratings are therefore partial (marked
"unconfirmed" in the CSV where not directly confirmed) since no Google Maps data access was available
this session; this differs from batch-04's fuller review/rating data and should be flagged if it matters
for future qualify decisions.

Metro: Denver, CO (next in Recipe 4's rotation after Austin, which is now fully scraped/contacted).
Segment nouns covered: interior design (4), home staging (1), custom cabinetry (2), custom furniture (2),
landscape design (1) — diversified across Recipe 4's listed segment nouns.

Qualify checks applied per business: single location (not a chain/franchise — Baczewski Luxury,
FBC Remodel, D2D Studio, Design One Interiors were found and rejected specifically for this), real
published contact email found on the business's own site (not a guessed pattern), no overlap with
`dead-addresses.md` (checked), no business whose own product is software/marketing-automation/data/
technical-consulting (peer disqualifier — none of the 10 triggered it, all are genuine home-design trades).

**Compliance note:** `outreach-scripts.md`'s interior-variant touch 1 and touch 3 pricing lines were
rewritten before this send to comply with today's PRICING FRAME ruling in `current-strategy.md`
("$500 is a proof purchase, not a discount... never say founding rate or a struck-through price").
The prior copy said "Two founding spots this month at $500 (normally $1,500)" — banned language.

## Touch 1 (day 0, sent 2026-08-10 18:23 PKT/UTC~13:23 ET)
MX records verified for all domains before sending (all resolved: Outlook, Google Workspace, or
antispam-relay MX records present). All 10 contacts + email engagements logged to HubSpot, portal
246685260.

- SENT info@anekainteriorsinc.com (Aneka Kerlin, Founder, Aneka Interiors, Englewood CO) messageId 19fece92d0980352 hubspotContactId 533351575255 hubspotEngagementId 389654588090
- SENT SensationalHomeStagingCO@gmail.com (Jennie Norris, CEO, Sensational Home Staging, Thornton CO) messageId 19fece92db25ecdf hubspotContactId 533262474974 hubspotEngagementId 389652274923
- SENT inquiry@margaritabravo.com (Margarita Bravo, Founder, Margarita Bravo, Denver CO) messageId 19fece92d069ded5 hubspotContactId 533337563853 hubspotEngagementId 389639580370
- SENT nancysanford@nancysanford.com (Nancy Sanford, Owner, Nancy Sanford Interiors, Denver CO) messageId 19fece92d7cea1da hubspotContactId 533349196536 hubspotEngagementId 389652172488
- SENT erik@adams-custom.com (Steve Adams, Owner, Adams Custom Cabinetry, Lakewood CO) messageId 19fece93074673e4 hubspotContactId 533334304461 hubspotEngagementId 389649259217
- SENT info@landdesignsbycolton.com (Jonathan Colton, Co-Owner, Land Designs by Colton, Wheat Ridge CO) messageId 19fece9312ef9e24 hubspotContactId 533334175453 hubspotEngagementId 389653882575
- SENT mike@houseofalpine.com (Mike Rudd, Founder, House of Alpine, Englewood CO) messageId 19fece933725c046 hubspotContactId 533334437599 hubspotEngagementId 389607603944
- SENT info@atelierid.com (Atelier Interior Design, Denver CO — no owner name found on site, generic greeting) messageId 19fece93363fc963 hubspotContactId 533308641998 hubspotEngagementId 389639580378
- SENT antreasures@gmail.com (Tomasz Dombrowski, Owner, AT Custom Woodworks & Cabinetry, Englewood CO) messageId 19fece93822b81da hubspotContactId 533288913624 hubspotEngagementId 389609647841
- SENT kevin@kevinandersondesigns.com (Kevin Anderson, Owner, Kevin Anderson Designs, Denver CO) messageId 19fece938fd8dcd8 hubspotContactId 533345069766 hubspotEngagementId 389634826999

## Bounces (found 2026-08-10, same run)
- BOUNCED erik@adams-custom.com (Steve Adams, Adams Custom Cabinetry): 550 5.1.1 address not found,
  bounced immediately. DEAD ADDRESS, added to dead-addresses.md, remove from all future sequences.
- Delivered: 9/10.

## Reply sweep (2026-08-10)
Searched inbox for mail from every known prospect domain across batches 01-05 since the last check
(2026-08-03). Zero replies found from any prospect domain, any batch. Combined pipeline reply rate
remains 0/40 contacted (31 prior + 9 delivered from batch-05, excluding the 1 bounce).

Live for touch 2 (due 2026-08-13): all batch-05 prospects except Adams Custom Cabinetry (9 remaining).
Touch 3 due 2026-08-17.
