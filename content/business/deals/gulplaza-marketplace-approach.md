# GulPlazaOnline.com — how to approach, talk, and quote
Created: 2026-08-18 · Inbound from a community contact · Prospect: Khuwaja Muhammad Adeel, founder, self-funded
Source doc: `GulPlazaOnline_Final_Marketplace_Proposal.docx` (16 sections, Daraz-competitor multi-vendor marketplace)

## 1. What the doc actually is
- It reads as AI-generated: tidy tables, "Recommended:", zero cost figures, zero timeline, zero headcount.
  That matters. It means the scope is an **aspiration written by a tool**, not a costed plan a technical
  person stood behind. He probably does not know what any line in it costs.
- Scope in the doc = customer web + customer app + seller dashboard + seller app + admin panel +
  marketplace API + payment/commission engine + KYC engine + search/recsys + AI discovery layer +
  promo engine + returns/refunds + notifications + analytics.
- Honest sizing: **6 to 9 months, team of 4 to 6.** A credible custom MVP alone is 3 to 4 months.
- The doc itself (section 15) says a formal spec and module acceptance criteria must exist before large
  scale development. Use his own document to sell the paid blueprint.

## 2. The 1-month demand: do not accept it, do not refuse it, reframe it
The blockers are not coding speed. They are:
- Payment gateway onboarding (Safepay / PayFast / JazzCash) needs a registered company + business bank
  account. Merchant approval is weeks, not days, and it is out of your control.
- Seller KYC, seller recruitment, and catalogue loading. A marketplace with no sellers is a dead site.
- App store review + developer accounts for React Native.
- Courier integration and returns/refund operations.

**Reframe:** "You cannot have that scope in 30 days. You CAN have a real marketplace live in 30 days,
taking real orders from real sellers. Then we build the custom platform on top of what the first 60
days of real orders teach us."

## 3. The 30-day build that is actually deliverable
Do NOT hand-build Next.js + Medusa multi-vendor in 30 days. Buy the vendor logic.
- **WooCommerce + Dokan Pro** gives you out of the box: seller registration, seller dashboard,
  commissions, withdrawals/payouts, product moderation, seller analytics, verification badges,
  vendor inquiry/chat. That is 60% of the doc, already built and battle-tested.
- Custom work on top (this is what he is actually paying you for):
  orange/white theme from his final UI direction, homepage bank-card savings strip + coupon engine,
  Make an Offer on eligible categories, Quick Search (Meilisearch or Algolia), trust badges,
  COD + one online method, order tracking + WhatsApp notifications, admin ops.
- Alternative if he wants something more marketplace-native than WordPress: **CS-Cart Multi-Vendor**
  (one-time license, purpose-built marketplace, vendor panels + payouts included). Mention once, do not
  turn the call into a tech survey.
- Honest downside to state out loud: a later migration to the custom Next.js/Medusa platform costs
  money. Frame it as the price of being live in 30 days instead of 30 weeks, and it is a price paid
  from revenue instead of savings.

## 4. Qualification call — ask ALL of these before any number
1. Sellers: how many are committed today, by name? Are these Gul Plaza shopkeepers (the Karachi market)?
   If yes, that is the whole moat and it changes the build priority. If zero, the project is theatre.
2. Company: registered with SECP? NTN? Business bank account? Without these there is no online payment
   gateway at launch and it is COD only. That is a fact about Pakistan, not a limitation of the build.
3. Deliveries: TCS / Leopards / M&P / Trax account, or seller-fulfilled? Who eats a failed COD delivery?
4. Who wrote this document, is that person staying involved, and is anyone else quoting on it?
5. Budget range for phase one, and where the money comes from (savings or investor).
6. Why 30 days? Is there a real date behind it (an event, an investor, a lease) or is it just impatience?
   If real, the deadline is a constraint to design around. If not, it is negotiable.
7. Who runs the marketplace daily after launch: seller support, disputes, moderation, refunds?
8. Is he hiring a contractor or looking for a founding technical partner? Settle this before pricing.

## 5. Quote structure (PKR)
Never quote a single number for this. Quote a ladder.

| Phase | What | Price | Time |
|---|---|---|---|
| 0. Blueprint | Product spec, data model, module-by-module acceptance criteria, clickable prototype | **100,000** (credited against Phase 1) | 5–7 days |
| 1. Live marketplace | The 30-day build in section 3. Web only. Sellers transacting. | **750,000** (band 650k–850k) | 30 days |
| 2. Platform | Online payments live, KYC workflow, AI Discover v1, full Make an Offer, analytics | 600,000–900,000 | quoted after traction |
| 3. Apps | React Native, both stores | 900,000–1,200,000 | quoted after traction |
| Retainer | Hosting, maintenance, seller support tooling, feature velocity | 90,000/month | ongoing |

- **Licenses and infra are billed at cost and paid by him, on his own accounts:** Dokan Pro, hosting,
  domain, plugins, search. Roughly 80,000–100,000 first year. Say this explicitly or it comes out of
  your fee.
- **Excluded from every phase, in writing:** product photography, catalogue data entry, seller
  recruitment, courier contracts, legal/policy pages, content writing. Offer "onboard your first 10
  sellers" as a separate line if he wants it.
- If his budget is under 300,000: descope hard. One category, 5 sellers, COD only, no AI, no offers
  engine. **PKR 250,000.** Or walk. Do not build the doc's scope for a startup price.
- If he offers equity: equity is fine **on top of** cash, never instead of it. A pre-revenue
  marketplace share is worth zero until it is worth something.

## 6. Terms to hold
- 50% advance before work starts. Milestone 2 at seller dashboard live. Balance before production DNS cutover.
- Domain, hosting, gateway and store accounts in HIS name, you get access. Same rule as the bakery deal.
- Source handed over at final payment, not before.
- Scope change = written change order = new price. The doc has 14 modules; he will remember more of them
  every week. This clause is the entire difference between a profitable project and a death march.
- Your own constraint: this is 20–30 hrs/week for a month, not 10–15. Decide that before you say yes.

## 7. Opening message (send this, do not quote yet)
> Read the whole document. The direction is right, and the differentiators are the right ones:
> Verified, Make an Offer, bank card savings and Local are the reasons someone picks you over Daraz.
>
> Two straight things before we talk money.
>
> That scope is a 6 to 9 month build for a team. Customer web, customer app, seller app, seller
> dashboard, admin, commission engine, KYC, search, AI discovery, returns. Anyone who tells you they
> will ship all of it in 30 days will either not ship it, or hand you something that breaks the first
> week real sellers are on it.
>
> But you can have a real marketplace live in 30 days, taking real orders. Web first, sellers
> onboarding themselves, commissions and payouts working, bank card offers live, Make an Offer on the
> categories where it fits, COD plus one payment method. Then we build the custom platform on top of
> what the first 60 days of real orders teach us, funded by those orders.
>
> Before I put a number on anything I want 30 minutes, because the price turns on things the document
> does not cover. How many sellers are committed today, whether there is a registered company for the
> payment gateway, who handles delivery, and what you need to be true 90 days from now.
>
> Are you free [day] evening or [day]?

## 8. If he pushes back "I need the whole thing in a month"
> I can promise you 30 days. I cannot promise you 30 days AND that scope, and I would rather lose the
> project than take your money for a date I know is not real. Pick the 30 days and I will tell you
> exactly what fits inside it. Pick the scope and I will give you a real timeline for it. Both are
> honest answers. Only one of them is a lie.

Then stop talking. If he still wants the fantasy, he will go find someone who sells it to him, and that
person will fail with his money instead of yours.
