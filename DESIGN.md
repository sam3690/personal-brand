# 🎨 Usama Ayoub — Brand Design Kit

> **Version:** 1.0 · **Date:** June 2025 · **Status:** Confidential  
> **Maintainer:** Usama Ayoub  
> **License:** All rights reserved. Unauthorized use prohibited.

---

## 📋 Table of Contents

- [1. Brand Overview](#1-brand-overview)
- [2. Logo System](#2-logo-system)
- [3. Color Palette](#3-color-palette)
- [4. Typography](#4-typography)
- [5. Spacing & Layout](#5-spacing--layout)
- [6. Patterns & Textures](#6-patterns--textures)
- [7. UI Components](#7-ui-components)
- [8. Iconography](#8-iconography)
- [9. Photography Direction](#9-photography-direction)
- [10. Brand Voice & Tone](#10-brand-voice--tone)
- [11. Brand Applications](#11-brand-applications)
- [12. Do's & Don'ts](#12-dos--donts)
- [13. CSS Variables & Tailwind Config](#13-css-variables--tailwind-config)
- [14. Quick Reference Card](#14-quick-reference-card)

---

## 1. Brand Overview

### Mission
To build a personal brand that reflects professionalism, expertise, and authenticity. Every touchpoint communicates trust, innovation, and a commitment to excellence.

### Vision
To become a recognized name associated with quality work, meaningful connections, and impactful contributions — both online and in every professional interaction.

### Core Values

| Value | Description |
|-------|-------------|
| **Integrity** | Honest, transparent, and consistent in every interaction and deliverable |
| **Innovation** | Embracing new ideas, technologies, and creative approaches to problem-solving |
| **Connection** | Building genuine relationships and fostering meaningful professional bonds |
| **Excellence** | Pursuing the highest quality in every output, no matter the scale |

### Brand Personality
Thoughtful, curious, dependable. Someone you'd want on your team. Professional yet approachable. Confident without arrogance. Warm and human.

---

## 2. Logo System

### Primary Logo

The logo combines a monogram mark with clean typography, balanced by a signature gold accent element.

```
┌─────────────────────────────────────┐
│                                     │
│   ┌──────┐  Usama Ayoub            │
│   │      │  ─────────────           │
│   │  U   │  Personal Brand         │
│   │      │                          │
│   └──┬───┘                          │
│      └─■  (gold accent)             │
│                                     │
└─────────────────────────────────────┘
```

### Logo Construction

| Element | Specification |
|---------|--------------|
| **Monogram** | Letter "U" in Playfair Display Bold |
| **Container** | Rounded square, 1:1 ratio, border-radius: 14px (at 56px size) |
| **Border** | 2.5px solid Emerald (#059669) |
| **Gold Accent** | Small square, bottom-right corner, #D4A853, border-radius: 3px |
| **Letter Fill** | ~60% of container height |
| **Wordmark** | Playfair Display Bold, tracking-tight |

### Logo Variations

| Variation | Use Case |
|-----------|----------|
| **Full Logo (Dark BG)** | Primary usage — dark backgrounds, websites, presentations |
| **Full Logo (Light BG)** | Light print materials, light-themed documents |
| **Mark Only** | Favicons, app icons, social profile photos, watermarks |
| **Mark Reversed** | On emerald/gold backgrounds |
| **Wordmark Only** | When space is constrained horizontally |
| **Abbreviated (UA)** | Small spaces, partner logos, co-branding |

### Clear Space & Minimum Size

- **Clear Space:** Maintain minimum of `X` (height of gold accent square) around all sides
- **Minimum Size (Digital):** 24px
- **Minimum Size (Print):** 8mm
- **Never:** Stretch, skew, rotate, add shadows, change colors, or add outlines

### Logo File Formats

| Format | Use |
|--------|-----|
| `.svg` | Websites, apps, presentations (primary) |
| `.png` @2x | Social media, email signatures |
| `.png` @3x | Retina displays, high-res print |
| `.pdf` | Professional print materials |
| `.eps` | Large format printing, merch |

---

## 3. Color Palette

### Primary Colors

| Color | Hex | RGB | HSL | Usage |
|-------|-----|-----|-----|-------|
| 🟢 **Emerald** | `#059669` | 5, 150, 105 | 160°, 93%, 30% | Primary actions, highlights, links, logo |
| 🟡 **Gold** | `#D4A853` | 212, 168, 83 | 40°, 61%, 58% | Accent elements, badges, premium CTAs |
| ⚫ **Deep Black** | `#0B0D10` | 11, 13, 16 | 220°, 18%, 5% | Primary background, headings |

### Extended Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Emerald Deep | `#064E3B` | Dark emerald variants, gradients |
| Emerald Dark | `#047857` | Hover states, active elements |
| Emerald Light | `#34D399` | Success states, light accents |
| Gold Dark | `#B8903A` | Gold hover states |
| Gold Light | `#E8C97A` | Gold highlights, light accents |
| Warm White | `#F5F0E8` | Light backgrounds, warm tones |

### Neutral Scale

| Token | Hex | Usage |
|-------|-----|-------|
| neutral-950 | `#0B0D10` | Page background |
| neutral-900 | `#13161B` | Secondary background |
| neutral-800 | `#1A1D24` | Cards, containers |
| neutral-700 | `#2A2D35` | Borders, dividers |
| neutral-500 | `#6B7280` | Secondary text |
| neutral-400 | `#9CA3AF` | Placeholder text |
| neutral-200 | `#F3F4F6` | Primary text on dark |
| neutral-50 | `#FAFAFA` | Headings on dark |

### Color Usage Ratios

```
Neutrals  ████████████████████████████████████████████  70%
Emerald   ████████████                                 20%
Gold      ██████                                       10%
```

### Accessibility

| Pairing | Contrast Ratio | WCAG Level |
|---------|---------------|------------|
| #FAFAFA on #0B0D10 | 18.2:1 | AAA ✓ |
| #F3F4F6 on #13161B | 14.8:1 | AAA ✓ |
| #059669 on #0B0D10 | 5.4:1 | AA ✓ |
| #D4A853 on #0B0D10 | 7.2:1 | AAA ✓ |
| #6B7280 on #0B0D10 | 4.6:1 | AA ✓ |
| #FFFFFF on #059669 | 4.2:1 | AA ✓ |

> ⚠️ **Never** use #6B7280 on #1A1D24 for essential text (fails contrast). Always use #9CA3AF or lighter for text on card backgrounds.

---

## 4. Typography

### Type Families

| Role | Font | Weight | Style |
|------|------|--------|-------|
| **Headings** | Playfair Display | 400, 500, 600, 700 | Regular, Italic |
| **Body** | Inter | 300, 400, 500, 600 | Regular |

### Type Scale

| Token | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| `display` | 96px / 6rem | 700 (Serif) | 1.0 | -0.025em | Hero text |
| `h1` | 48px / 3rem | 700 (Serif) | 1.1 | -0.025em | Page titles |
| `h2` | 36px / 2.25rem | 600 (Serif) | 1.2 | -0.02em | Section titles |
| `h3` | 24px / 1.5rem | 500 (Serif) | 1.3 | -0.015em | Subsections |
| `h4` | 18px / 1.125rem | 500 (Sans) | 1.4 | -0.01em | Card titles |
| `body-lg` | 18px / 1.125rem | 400 (Sans) | 1.625 | -0.01em | Lead paragraphs |
| `body` | 16px / 1rem | 400 (Sans) | 1.625 | -0.01em | Body text |
| `body-sm` | 14px / 0.875rem | 400 (Sans) | 1.5 | -0.01em | Secondary text |
| `caption` | 12px / 0.75rem | 500 (Sans) | 1.5 | 0.1em (uppercase) | Labels, captions |
| `micro` | 11px / 0.6875rem | 500 (Sans) | 1.5 | 0.05em | Tiny labels |

### Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
```

### Typography Rules

1. **Headings** → Always Playfair Display, always tight tracking (`-0.025em` to `-0.01em`)
2. **Body** → Always Inter, normal tracking (`-0.01em`)
3. **Captions/Labels** → Inter, uppercase, wider tracking (`0.05em–0.1em`)
4. **Italics** → Reserved for quotes, emphasis within body text, and decorative subheads
5. **Never** → Use Inter for headings or Playfair for body text in production

---

## 5. Spacing & Layout

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Tight gaps, icon padding |
| `space-2` | 8px | Small gaps, inline spacing |
| `space-3` | 12px | List item gaps, small padding |
| `space-4` | 16px | Card padding (small), paragraph gaps |
| `space-5` | 20px | Component spacing |
| `space-6` | 24px | Card padding (standard) |
| `space-8` | 32px | Section inner spacing |
| `space-10` | 40px | Section gaps |
| `space-12` | 48px | Large section spacing |
| `space-16` | 64px | Section top/bottom padding |
| `space-20` | 80px | Major section dividers |
| `space-24` | 96px | Page-level vertical rhythm |
| `space-32` | 128px | Hero-level spacing |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | 6px | Small badges, inline elements |
| `radius-md` | 8px | Input fields, small cards |
| `radius-lg` | 12px | Cards, containers |
| `radius-xl` | 16px | Buttons, large cards |
| `radius-2xl` | 24px | Hero cards, modals |
| `radius-full` | 9999px | Pills, avatars, circular elements |

### Container Widths

| Breakpoint | Max Width | Padding |
|------------|-----------|---------|
| Mobile (<640px) | 100% | 24px |
| Tablet (640–1023px) | 100% | 32px |
| Desktop (1024–1279px) | 1024px | 48px |
| Wide (1280px+) | 1280px | 48px |

### Grid System

```
12-column grid
Gap: 24px (desktop) / 16px (mobile)
Column widths: auto with minmax(0, 1fr)

Common layouts:
- 2 col: grid-cols-2 (md)
- 3 col: grid-cols-3 (lg)
- 4 col: grid-cols-4 (lg)
- Sidebar: grid-cols-[240px_1fr] (xl)
```

---

## 6. Patterns & Textures

### Grid Pattern
```css
background-image:
  linear-gradient(rgba(5,150,105,0.07) 1px, transparent 1px),
  linear-gradient(90deg, rgba(5,150,105,0.07) 1px, transparent 1px);
background-size: 24px 24px;
```
**Use for:** Section backgrounds, tech-themed layouts

### Dot Pattern
```css
background-image: radial-gradient(rgba(5,150,105,0.12) 1px, transparent 1px);
background-size: 16px 16px;
```
**Use for:** Hero sections, feature backgrounds

### Diagonal Lines
```css
background-image: repeating-linear-gradient(
  45deg, transparent, transparent 10px,
  rgba(5,150,105,0.05) 10px, rgba(5,150,105,0.05) 11px
);
```
**Use for:** Divider sections, subtle texture

### Cross-Hatch (Gold)
```css
background-image:
  linear-gradient(45deg, rgba(212,168,83,0.06) 25%, transparent 25%, transparent 75%, rgba(212,168,83,0.06) 75%),
  linear-gradient(45deg, rgba(212,168,83,0.06) 25%, transparent 25%, transparent 75%, rgba(212,168,83,0.06) 75%);
background-size: 20px 20px;
background-position: 0 0, 10px 10px;
```
**Use for:** Premium sections, CTAs

### Gradient Combinations

```css
/* Emerald Depth */
background: linear-gradient(135deg, #059669, #047857);

/* Gold Warmth */
background: linear-gradient(135deg, #D4A853, #B8903A);

/* Dark Surface */
background: linear-gradient(135deg, #0B0D10, #1A1D24);

/* Emerald Glow (for accents) */
background: linear-gradient(135deg, rgba(5,150,105,0.1), rgba(5,150,105,0));

/* Gold Glow (for premium accents) */
background: linear-gradient(135deg, rgba(212,168,83,0.1), rgba(212,168,83,0));
```

> ⚠️ Patterns should always be used at low opacity (5–15%) to maintain readability. Never use patterns under body text.

---

## 7. UI Components

### Buttons

#### Primary Button
```html
<button class="bg-[#059669] hover:bg-[#047857] text-white text-sm font-medium 
  px-6 py-3 rounded-xl transition-colors duration-300">
  Primary Action
</button>
```

#### Gold Button
```html
<button class="bg-[#D4A853] hover:bg-[#B8903A] text-[#0B0D10] text-sm font-medium 
  px-6 py-3 rounded-xl transition-colors duration-300">
  Premium Action
</button>
```

#### Outline Button
```html
<button class="border border-[#2A2D35] text-[#FAFAFA] text-sm font-medium 
  px-6 py-3 rounded-xl hover:border-[#059669]/50 hover:text-[#059669] 
  transition-all duration-300">
  Secondary
</button>
```

#### Ghost Button
```html
<button class="text-[#059669] text-sm font-medium px-6 py-3 rounded-xl 
  hover:bg-[#059669]/10 transition-colors duration-300">
  Tertiary
</button>
```

#### Button Sizes

| Size | Padding | Font Size | Radius |
|------|---------|-----------|--------|
| Small | `px-4 py-2` | 12px | `rounded-lg` (8px) |
| Medium | `px-6 py-3` | 14px | `rounded-xl` (16px) |
| Large | `px-8 py-4` | 16px | `rounded-2xl` (24px) |

#### Button States

| State | Style |
|-------|-------|
| Default | Base styles above |
| Hover | Darken background by 10% |
| Active | Scale 0.98, darken 15% |
| Focus | 2px ring offset, ring-color: emerald |
| Disabled | `opacity-60 cursor-not-allowed` with emerald/20 bg |
| Loading | Replace text with spinner, disable click |

### Tags & Badges

```html
<!-- Emerald Tag -->
<span class="bg-[#059669]/10 text-[#059669] text-xs font-medium px-3 py-1.5 rounded-full">
  Tag
</span>

<!-- Gold Tag -->
<span class="bg-[#D4A853]/10 text-[#D4A853] text-xs font-medium px-3 py-1.5 rounded-full">
  Premium
</span>

<!-- Uppercase Badge -->
<span class="bg-[#059669]/10 text-[#059669] text-[10px] font-semibold 
  uppercase tracking-widest px-3 py-1 rounded-md">
  Badge
</span>

<!-- Solid Badge -->
<span class="bg-[#059669] text-white text-xs font-medium px-3 py-1.5 rounded-full">
  Active
</span>
```

### Cards

#### Default Card
```html
<div class="bg-[#1A1D24] border border-[#2A2D35] rounded-2xl p-6 
  hover:border-[#059669]/30 transition-colors duration-300">
  <!-- Content -->
</div>
```

#### Elevated Card
```html
<div class="bg-[#13161B] border border-[#2A2D35] rounded-2xl p-6 shadow-2xl">
  <!-- Content -->
</div>
```

#### Accent Card
```html
<div class="bg-gradient-to-br from-[#059669]/10 to-[#1A1D24] 
  border border-[#059669]/20 rounded-2xl p-6">
  <!-- Content -->
</div>
```

### Form Elements

#### Input Field
```html
<label class="text-xs font-medium text-[#6B7280] uppercase tracking-wider mb-2 block">
  Label
</label>
<input type="text" placeholder="Placeholder text" 
  class="w-full bg-[#13161B] border border-[#2A2D35] rounded-xl px-4 py-3 
  text-sm text-[#FAFAFA] placeholder-[#6B7280]/50 
  focus:outline-none focus:border-[#059669]/50 transition-colors">
```

#### Textarea
```html
<textarea rows="4" placeholder="Your message..." 
  class="w-full bg-[#13161B] border border-[#2A2D35] rounded-xl px-4 py-3 
  text-sm text-[#FAFAFA] placeholder-[#6B7280]/50 
  focus:outline-none focus:border-[#059669]/50 transition-colors resize-none">
</textarea>
```

### Dividers

```css
/* Subtle divider */
height: 1px;
background: linear-gradient(90deg, transparent, #2A2D35, transparent);

/* Solid divider */
border-bottom: 1px solid #2A2D35;

/* Section divider with margin */
margin: 0 48px;
```

---

## 8. Iconography

### Icon Set
**Primary:** [Lucide Icons](https://lucide.dev/) via [Iconify](https://iconify.design/)

### Usage
```html
<span class="iconify" data-icon="lucide:arrow-right" style="font-size: 20px"></span>
```

### Icon Container
```html
<div class="w-10 h-10 bg-[#059669]/10 rounded-xl flex items-center justify-center">
  <span class="iconify text-[#059669]" data-icon="lucide:layout" style="font-size: 20px"></span>
</div>
```

### Common Icons

| Icon | Name | Usage |
|------|------|-------|
| → | `lucide:arrow-right` | CTAs, links |
| ✉ | `lucide:mail` | Email |
| 🔗 | `lucide:linkedin` | LinkedIn |
| 🐙 | `lucide:github` | GitHub |
| 🐦 | `lucide:twitter` | Twitter/X |
| 📷 | `lucide:instagram` | Instagram |
| 🌐 | `lucide:globe` | Website |
| 📅 | `lucide:calendar` | Dates |
| 🔒 | `lucide:lock` | Security |
| ✨ | `lucide:sparkles` | AI/Featured |
| 💡 | `lucide:lightbulb` | Ideas |
| 👤 | `lucide:user` | Profile |
| 📄 | `lucide:file-text` | Documents |
| ☎ | `lucide:phone` | Phone |
| 📍 | `lucide:map-pin` | Location |

### Icon Sizing

| Size | Value | Usage |
|------|-------|-------|
| xs | 14px | Inline text icons |
| sm | 16px | Buttons, small containers |
| md | 20px | Standard icons, card icons |
| lg | 24px | Feature icons, empty states |
| xl | 32px | Hero icons, large features |

### Social Icon Treatment
```html
<div class="w-12 h-12 bg-[#13161B] border border-[#2A2D35] rounded-xl 
  flex items-center justify-center text-[#6B7280]
  hover:border-[#059669]/50 hover:text-[#059669] 
  transition-all duration-300 cursor-pointer">
  <span class="iconify text-xl" data-icon="lucide:linkedin"></span>
</div>
```

---

## 9. Photography Direction

### Style
- Authentic and professional — never overly staged or stock-like
- Slightly desaturated (10–15%) for a refined feel
- Subtle warm color temperature shift
- No heavy filters, dramatic effects, or artificial lighting

### Composition Rules
- Negative space is essential — don't fill every pixel
- Natural lighting preferred (window light, golden hour)
- Shallow depth of field for subject focus
- Rule of thirds for primary subject placement
- Clean, uncluttered backgrounds

### Approved Subjects
| Category | Examples |
|----------|----------|
| Professional | Headshots, office environments, meetings |
| Workspace | Clean desk setups, minimal tech, notebooks |
| Abstract | Textures, architectural details, nature close-ups |
| Lifestyle | Coffee moments, reading, walking, traveling |

### Image Treatment CSS
```css
.brand-image {
  filter: saturate(0.85) contrast(0.95) brightness(1.02);
  border-radius: 16px;
}
```

### Overlay Pattern (for text on images)
```css
.image-overlay {
  background: linear-gradient(to top, rgba(11,13,16,0.8), transparent);
}
```

---

## 10. Brand Voice & Tone

### Tone Spectrum
```
Formal ─────────────────────── Casual
  |                                  |
  ├── Professional Presentations     ├── Social Media Posts
  ├── Proposals & Reports            ├── Direct Messages
  ├── Email (first contact)          ├── Email (ongoing convo)
  └── LinkedIn About                 └── Stories/Reactions
```

### Writing Guidelines

| Do | Don't |
|----|-------|
| Be clear and direct | Use jargon unnecessarily |
| Show personality | Be overly casual or flip |
| Use active voice | Use passive voice |
| Write short sentences | Write run-on sentences |
| Be specific | Use vague superlatives |
| Use "I" and "you" | Use "we" (it's a personal brand) |
| End with a clear CTA | Leave readers hanging |

### Email Sign-off Hierarchy
1. **Formal:** "Best regards, Usama"
2. **Standard:** "Cheers, Usama"
3. **Casual:** "— Usama"

---

## 11. Brand Applications

### Business Card

**Front (Dark):**
```
┌──────────────────────────────────────┐
│  [U]  Usama Ayoub                    │
│                                      │
│  Professional Title                  │
│  usama@example.com                   │
│  linkedin.com/in/usama-ayoub         │
│  +XX XXX XXXXXXX                     │
└──────────────────────────────────────┘
Size: 3.5" × 2" (90mm × 50mm)
Background: #0B0D10
Border: none (full bleed)
```

**Back (Light):**
```
┌──────────────────────────────────────┐
│                                      │
│            [ U ]                     │
│                                      │
│       usama@example.com              │
│                                      │
└──────────────────────────────────────┘
Background: #F5F0E8
```

### LinkedIn Banner
```
Dimensions: 1584 × 396px (4:1 ratio)
Background: #0B0D10 with grid pattern overlay
Left-aligned text:
  "Usama Ayoub" (Playfair Display, 48px, Bold, White)
  "Tagline here" (Inter, 16px, #6B7280)
Bottom-right: Logo mark (small)
```

### Email Signature
```html
<table cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="border-top: 2px solid #059669; padding-top: 12px;">
      <span style="font-family: Georgia, serif; font-size: 18px; font-weight: bold; color: #111827;">
        Usama Ayoub
      </span><br>
      <span style="font-size: 13px; color: #6B7280;">Professional Title</span><br>
      <span style="font-size: 12px; color: #9CA3AF;">
        <a href="mailto:usama@example.com" style="color: #059669; text-decoration: none;">
          usama@example.com
        </a> · 
        <a href="https://linkedin.com/in/usama-ayoub" style="color: #059669; text-decoration: none;">
          LinkedIn
        </a>
      </span>
    </td>
  </tr>
</table>
```

### Social Media Profile Specs

| Platform | Profile Image | Dimensions |
|----------|--------------|------------|
| LinkedIn | Logo mark on emerald bg | 400 × 400px |
| GitHub | Logo mark on dark bg | 460 × 460px |
| Twitter/X | Logo mark on dark bg | 400 × 400px |
| Instagram | Professional headshot | 320 × 320px |

### Presentation Template
```
Slide Background: #0B0D10
Title: Playfair Display, 44px, Bold, #FAFAFA
Body: Inter, 20px, Regular, #F3F4F6
Accent: #059669 for highlights, #D4A853 for key points
Footer: Logo mark (left) + slide number (right)
```

---

## 12. Do's & Don'ts

### Logo

| ✅ Do | ❌ Don't |
|-------|----------|
| Use on approved backgrounds (dark/light) | Place on busy or clashing backgrounds |
| Maintain clear space around logo | Crowd with other elements |
| Use approved file formats | Use low-res or rasterized versions |
| Scale proportionally | Stretch, skew, or distort |
| Use the correct variation for context | Use dark logo on dark background |

### Colors

| ✅ Do | ❌ Don't |
|-------|----------|
| Stick to the defined palette | Introduce new colors without approval |
| Follow the 70/20/10 ratio | Use emerald and gold equally |
| Ensure text meets WCAG AA contrast | Use muted colors for essential text on dark cards |
| Use gold sparingly for premium feel | Overuse gold — it loses impact |

### Typography

| ✅ Do | ❌ Don't |
|-------|----------|
| Use Playfair for all headings | Use Inter for headings |
| Use Inter for all body/UI text | Use Playfair for body text |
| Follow the type scale | Pick arbitrary sizes |
| Use tight tracking for headings | Add extra spacing to headings |
| Use uppercase + wide tracking for labels | Use sentence case for labels |

### Layout

| ✅ Do | ❌ Don't |
|-------|----------|
| Use consistent spacing from the scale | Eyeball spacing |
| Maintain container max-widths | Let content stretch edge-to-edge on wide screens |
| Use rounded corners consistently | Mix different radii randomly |
| Use patterns at low opacity | Use patterns under body text |

---

## 13. CSS Variables & Tailwind Config

### CSS Custom Properties
```css
:root {
  /* Primary Colors */
  --color-emerald: #059669;
  --color-emerald-light: #34D399;
  --color-emerald-dark: #047857;
  --color-emerald-deep: #064E3B;
  --color-gold: #D4A853;
  --color-gold-light: #E8C97A;
  --color-gold-dark: #B8903A;

  /* Neutrals */
  --color-black: #0B0D10;
  --color-dark: #13161B;
  --color-card: #1A1D24;
  --color-border: #2A2D35;
  --color-muted: #6B7280;
  --color-light: #F3F4F6;
  --color-white: #FAFAFA;
  --color-warm: #F5F0E8;

  /* Typography */
  --font-serif: 'Playfair Display', serif;
  --font-sans: 'Inter', sans-serif;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 24px;
  --radius-full: 9999px;

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 300ms ease;
  --transition-slow: 500ms ease;
  --transition-spring: 500ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### Tailwind Config
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          black: '#0B0D10',
          dark: '#13161B',
          card: '#1A1D24',
          border: '#2A2D35',
          muted: '#6B7280',
          light: '#F3F4F6',
          white: '#FAFAFA',
          emerald: {
            DEFAULT: '#059669',
            light: '#34D399',
            dark: '#047857',
            deep: '#064E3B',
          },
          gold: {
            DEFAULT: '#D4A853',
            light: '#E8C97A',
            dark: '#B8903A',
          },
          warm: '#F5F0E8',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
      },
      borderRadius: {
        'brand-sm': '6px',
        'brand-md': '8px',
        'brand-lg': '12px',
        'brand-xl': '16px',
        'brand-2xl': '24px',
      },
      transitionTimingFunction: {
        'spring': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
      },
    }
  }
}
```

### Global Styles
```css
/* Base */
body {
  background-color: var(--color-black);
  color: var(--color-light);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Headings */
h1, h2, h3, h4 {
  font-family: var(--font-serif);
  color: var(--color-white);
  letter-spacing: -0.025em;
}

/* Selection */
::selection {
  background-color: var(--color-emerald);
  color: white;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--color-black); }
::-webkit-scrollbar-thumb { background: var(--color-border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--color-muted); }

/* Focus Ring */
*:focus-visible {
  outline: 2px solid var(--color-emerald);
  outline-offset: 2px;
}
```

---

## 14. Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│                USAMA AYOUS BRAND KIT                │
├─────────────────────────────────────────────────────┤
│                                                     │
│  LOGO       Monogram "U" + Wordmark                │
│             Playfair Display Bold                   │
│             Gold accent square (bottom-right)       │
│                                                     │
│  COLORS     Primary:   #059669 (Emerald)           │
│             Accent:    #D4A853 (Gold)              │
│             Background: #0B0D10 (Deep Black)        │
│             Border:    #2A2D35                     │
│             Text:      #F3F4F6 / #FAFAFA           │
│             Muted:     #6B7280                     │
│                                                     │
│  FONTS      Headings:  Playfair Display             │
│             Body:      Inter                        │
│             Labels:    Inter Uppercase               │
│                                                     │
│  SPACING    4px base scale (4, 8, 12, 16, 24...)   │
│  RADIUS     sm:6 md:8 lg:12 xl:16 2xl:24           │
│                                                     │
│  ICONS      Lucide via Iconify                      │
│  PATTERNS   Grid, Dots, Diagonal, Cross-hatch      │
│  FRAMEWORK  Tailwind CSS v3.4+                      │
│                                                     │
│  RATIO      70% Neutrals / 20% Emerald / 10% Gold  │
│                                                     │
│  VERSION    1.0 — June 2025                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

> 📌 **Note:** This document is a living reference. As the brand evolves, updates will be versioned and documented here. Always refer to the latest version for current guidelines.

---

*© 2025 Usama Ayoub. All rights reserved.*
