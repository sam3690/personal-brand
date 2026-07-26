# Brand Design System — "Green Room" Kit v1.2

Source of truth for all LinkedIn/social carousel, banner, CTA, and featured-post visuals.
Synced from the Claude Design project **"Brand system design for social media carousels"**:
https://claude.ai/design/p/5790bcce-f02c-4647-a1dd-9837aee8c75f (owner: Usama, editable).

**Local copy:** `carousels/green-room/` — the actual `.dc.html` decks, runtime (`support.js` /
`deck-stage.js`), and the `grain.png` texture, synced from that project. See
`carousels/green-room/README.md` for the render pipeline and the one manual step still open
(two background/headshot images exceed the design-sync tool's 256 KiB read cap — see below).
Second-brain note: `brain/Brand Design System.md`.

This **supersedes** the older kit in `carousels/carousel.html` / `carousels/linkedin-banner.html`
(Tailwind, emerald/gold/Playfair Display) for all new carousels and banners. Those files still work
and aren't deleted, but Green Room is the standard going forward.

## 1. Brand essence
Dark emerald, film-grain, condensed all-caps display type. Editorial-poster energy adapted for
tech/automation content: code blocks, workflow snippets, stats — not stock imagery. One idea per
slide, one hot gradient per slide, everything else near-black.

## 2. Color
| Token | Hex | Use |
|---|---|---|
| Ink Green | `#05130C` | deep background base |
| Forest | `#123B24` | gradient midpoint |
| Field Green | `#1E7A42` | gradient hot edge (one corner/edge only) |
| Signal Green | `#2FBF66` | accent: emphasized headline words, numbers, chips, code keywords |
| Bone White | `#F2F6F3` | headlines, quote marks, avatar ring |
| Frame Stroke | `rgba(255,255,255,0.5)` | 3px frame borders, dividers |
| Panel | `#0E1F16` | code-block / card fill |
| Code text | `#CFE8D8` (vars `#7FD9A4`) | inside code plates |
| Stop Red | `#E5484D` | pattern-break slide ONLY (max 1 per carousel) |

Rule: BG-MAIN image crop is the background (see §3) — no CSS gradient backgrounds; the stop slide
layers a red radial glow over the same BG-MAIN crop. Signal Green is earned, not decorative.

## 3. Background & texture
**BG-MAIN (`bg-main.png`) is the one and only background** for all posts, carousels, banners,
featured media and CTA images: a grainy emerald flow-field (deep ink-green shadow bands + soft
desaturated-sage glows), grain already baked in — no extra noise overlay, no CSS gradients.
- Banners / CTA / featured posts: **light zoom** — `background-size: ~140–160%`, position
  `~50% 40–45%`: sage glows visible top and bottom.
- Carousel slides: **deeper zoom** — `background-size: ~220–250%`, positioned on the darker
  mid-band with only a hint of glow at the edges.
- Shift the crop window per slide/format for rhythm; never center a glow behind text.
- Stop slide: same BG-MAIN deep crop, with a strong red radial glow layered on top
  (`rgba(229,72,77,0.65)` from the bottom edge + `0.4` top-right, sized 100% 100%) instead of green.
- Code plates/screenshots still sit on the slightly rotated low-opacity plate.

## 4. Typography
| Role | Font | Spec |
|---|---|---|
| Display / headlines | **Anton** | ALL CAPS, line-height 1.04–1.06, 76–96px; hero stats 110–280px; one phrase per headline in Signal Green |
| Body copy | **Archivo** 400/600 | 34–40px, line-height 1.5–1.55, `rgba(242,246,243,0.88)` |
| Labels, chips, code | **JetBrains Mono** | chips 26px/600/letter-spacing 0.1em; code 30px/1.75; footer 24px |

Never below 24px on a 1080×1350 slide. Google Fonts CDN: `Anton`, `Archivo:wght@400;500;600;700`,
`JetBrains+Mono:wght@400;600`.

## 5. Components
- **Quote frame** (cover + close): inset `64px 64px 96px`, 3px Frame Stroke border, padding
  `72px 64px`. Anton quote marks 150px / line-height 1, opening at `top:-40px; left:36px`, closing
  at `bottom:-40px; right:36px` (straddling the border).
- **Buttons (brand standard)**: filled Signal Green (`linear-gradient(180deg, #2FBF66, #23A155)`),
  white 700 text, radius 12px, padding ~14px 30px, **hard offset shadow**
  `-5px 7px 0 #124D2B` + soft glow `0 0 34px rgba(47,191,102,0.4)`. Optional trailing white line
  icon. Outline pills are NEVER buttons/CTAs.
- **Label chips**: solid Signal Green, white 700 text, radius 8px, small offset shadow
  `-3px 4px 0 rgba(18,77,43,0.9)` — kicker lines and punchline bars ("Helping You Build").
- **Tag pills**: grey outline (`2px rgba(255,255,255,0.55)`), dark translucent fill
  `rgba(5,19,12,0.55)`, white 600 text, full-round — non-clickable descriptors only ("GTM Agents").
- **Scribble arrow**: hand-drawn curly arrow, Signal Green, 5px round-cap stroke, points at the
  CTA or headline.
- **Calendar card**: white card, radius 18px, dark text, selected day = green circle —
  booking-CTA visual.
- **Day-marker chips**: pill, 3px Signal Green border, green mono text (`DAY 0`,
  `STEP 1 · INTAKE`) — timeline markers inside carousels only, never CTAs. Red variant on stop
  slide only.
- **Channel icon tiles**: 80px rounded square, 3px Frame Stroke border, 40px white 1.8-stroke
  line icon (mail / LinkedIn / phone). Dashed border + 0.55 opacity = "neglected channel".
- **Code plate**: Panel fill, 2px `rgba(47,191,102,0.35)` border, radius 14px, traffic-light
  dots, `rotate(-1.2deg)`, heavy shadow `0 30px 70px rgba(0,0,0,0.5)`. Same tilt for screenshots.
- **Hero stat**: Anton, Signal Green, biggest element on the slide.
- **Before/after table**: 2×2 grid, 3px Frame Stroke borders, left column dimmed, right column
  Signal Green.
- **Author badge** (bottom-right of EVERY slide, replaces topic label):
  - Round headshot (head + slight shoulders crop), white ring, + "USAMA **AYOUB**" in Anton
    (surname in Signal Green).
  - Slides 1 & last: avatar 110px / 4px ring, name 40px.
  - Interior slides: avatar 64px / 3px ring, name 26px.
  - Fixed position across all slides — never shifts between slides.
- **Footer**: `left/right 64–88px, bottom 36px`, mono 24px counter `NN / NN` left, author badge
  right.

## 5b. Banner / CTA / Featured-post formats
- **Profile banner** (wide ~1584×396): headline block centered-left of the headshot — green label
  chip kicker → Anton white headline → Signal Green sub-line → row of tag pills → green punchline
  chip. Outline "Book a Free Audit" lockup top-left with a green circular icon. Scribble arrow from
  headline toward headshot.
- **CTA post** (landscape 1200×628): Anton headline (white line + green line), filled green button
  below, scribble arrow pointing up at the button, headshot right.
- **Booking post**: white calendar card left (round headshot overlapping its top), Anton headline +
  short Archivo body right, filled green button with mail icon.
- Headshot cutouts ARE allowed on banners/CTA/featured posts (unlike carousel interiors).

## 6. Slide anatomy (9-slide carousel)
1. **Cover** — quote frame + hero stat + hook headline + payoff line ("→")
2. **Problem** — chip + headline + 2 body paragraphs + supporting visual row
3–6. **Steps** — chip (DAY N / STEP N) + icon tile + headline + one paragraph + code plate or
   spec card
7. **Pattern break (stop)** — red frame, red chip, red kill-phrase in headline
8. **Result** — before/after table + hero stat + source note
9. **Close** — quote frame + save/comment CTA pills + follow prompt

Rhythm rules: max 2 background treatments per carousel; the red slide is the only pattern break;
every emphasized headline phrase gets Signal Green; CTAs are chip-style pills.

## 7. Voice
Punchy, provocative, data-led. Headlines are claims, not topics ("Opened, no reply? LinkedIn
fires."). Body copy: one specific mechanism per slide, no filler. Numbers over adjectives.

## Local sync status
| Asset | Synced? |
|---|---|
| `Brand System.dc.html` → `carousels/green-room/brand-system.dc.html` | ✅ complete |
| `Carousel - Multichannel Outbound.dc.html` → `carousels/green-room/carousel-multichannel-outbound.dc.html` | ✅ complete (this week's carousel, Post 2, Wed 2026-07-22 slot) |
| Print variant → `carousels/green-room/carousel-multichannel-outbound-print.dc.html` | ✅ complete |
| `support.js`, `deck-stage.js` (runtime) | ✅ complete |
| `grain.png` | ✅ complete |
| `bg-main.png` (the one background for everything) | ❌ **exceeds the design-sync tool's 256 KiB read cap — manual export needed** |
| `headshot-round.png` | ❌ **same 256 KiB cap issue — manual export needed** |
| `uploads/*.png` (reference/mood images) | not synced — not required for rendering, low priority |

**To finish:** open the project link above in a browser, download `bg-main.png` and
`headshot-round.png`, drop them into `carousels/green-room/` with those exact filenames. Every
`.dc.html` in that folder references them by relative path and will render correctly the moment
they land — no other changes needed.

## How to build the next carousel/banner
1. Open `carousels/green-room/brand-system.dc.html` in a browser for the live token/component
   reference.
2. Copy `carousels/green-room/carousel-multichannel-outbound.dc.html` as a starting template —
   swap slide copy per the 9-slide anatomy (§6), keep the component markup (chips, code plates,
   author badge, footer) as-is.
3. Render: `google-chrome --headless --disable-gpu --print-to-pdf=<name>.pdf --print-to-pdf-no-header "<file>-print.dc.html"` (same pipeline as `carousels/carousel.html`, permission already
   granted in `carousels/.claude/settings.local.json`) — or open directly in a browser and
   screenshot each 1080×1350 slide.
4. Drop the media brief for the post per `content/agents/x/x2-media-brief.md` format, referencing
   this file instead of "Canva template."
