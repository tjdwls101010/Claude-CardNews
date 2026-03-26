# Card News Design Principles

Design guide for 1080x1350px card news. Organized in three layers: **Foundation** (structural logic) → **Techniques** (card-news-specific execution) → **Signature Style** (Paperology defaults, conditionally applied). Use as both creation guide and review diagnostic.

---

# Layer 0: Intentionality

When something looks wrong, ask **"what's too similar?"** before asking what to change. Most card news design problems are unintentional similarity — two elements that differ slightly but not enough, creating *conflict* rather than contrast. A weight of 400 next to 500 looks like a mistake. A gap of 20px next to 24px looks accidental. Either make them the same or make them obviously different.

---

# Layer 1: Foundation

Apply the four structural principles in order: **Proximity → Alignment → Repetition → Contrast.** This is also the diagnostic order — when a card looks "off," check Proximity first. Fixing an earlier-layer issue often resolves what seemed like a later-layer problem.

---

## 1. Proximity

The card-news-specific insight: **gap ratio is hierarchy.** When every gap is the same (e.g., 20px between all elements), the card reads as a flat list with no structure.

- **Intra-group gap** (title + subtitle, icon + label, stat + description): 8-16px — these form a single visual unit
- **Inter-group gap** (title block ↔ body block, body ↔ footer): 32-48px — distinct sections
- Aim for roughly 3:1 ratio between inter-group and intra-group. The ratio communicates hierarchy; absolute values are secondary.

**Squint test**: Squint at the rendered PNG until text blurs. Count visual clusters. Target: 2-4 clusters (title zone, content zone, footer, maybe image zone). 6+ clusters = elements need tighter grouping. 1 blob = no internal structure.

The inverse matters equally: a caption equidistant between two images belongs to neither. Move it decisively close to the one it describes.

---

## 2. Alignment

**One alignment axis per card.** Body cards: flush-left (creates the strongest structural backbone). Cover/ending cards: centered is a valid conscious choice — but if centering, vary line lengths dramatically so it reads as obviously centered rather than accidentally off-axis.

The card-news trap: flush-left text with an image that doesn't share any text edge → trapped white space between them. Fix: snap the image's left edge to the text's left edge, or its right edge to the card's right padding boundary.

In CSS: a consistent `padding-left` (e.g., 48px) establishes the primary alignment edge. `grid-template-columns` creates additional invisible guides. All text blocks, image edges, and decorative elements should relate to these edges.

---

## 3. Repetition

CSS variables are Repetition implemented as engineering. Extend beyond colors to all design tokens:

```css
:root {
  --color-primary: ...; --color-accent: ...; --color-neutral: ...;
  --gap-tight: 12px; --gap-section: 36px; --padding-card: 44px;
  --title-size: 84px; --title-weight: 800;
  --body-size: 26px; --body-weight: 400;
}
```

The moment one card hard-codes a raw value that breaks the token system, it feels like a different designer made it. This applies to spacing and typography as much as color.

Across a series: same corner element pattern, same heading-to-body size ratio, same accent usage pattern on every card. This is what makes 8-10 cards feel like one series rather than a random collection.

---

## 4. Contrast

**The central problem in AI-generated card news is timid differentiation.** Claude naturally gravitates toward moderate, "safe" choices — weight 500 vs 600, size 32px vs 40px. This produces conflict, not contrast. The card looks uncertain rather than professional.

### Conflict thresholds for 1080x1350px
These are empirically observed thresholds where differences stop reading as intentional:
- **Weight**: gap <200 units reads as conflict (400 vs 500 ✗, 400 vs 700 ✓)
- **Size**: ratio <2:1 reads as conflict (36px vs 42px ✗, 28px vs 84px ✓)
- **Color**: two hues at similar HSL lightness merge — grayscale mental test catches this

### Stacking contrasts
Single-dimension contrast is weak. Each hierarchy transition should differ in 2-3 dimensions simultaneously. Title → body should differ in size AND weight AND tracking, not size alone. The table in the Typography section below shows a tested stacking pattern.

### Bold variation
When breaking a series pattern for emphasis (question card, reveal card, transition), break it dramatically. A card that's slightly different looks like an error. A card that's boldly different looks like a statement.

---

# Layer 2: Techniques

Each section addresses card-news-specific knowledge that goes beyond general design principles.

---

## 5. Typography

> Foundation: **Contrast**, **Repetition**

Paperlogy's 9 weights (100-900) in a single sans serif family means structure contrast (serif vs sans serif) is unavailable. Compensate by exploiting all other dimensions aggressively.

### Tested stacking pattern for Paperlogy at 1080x1350px

| Element | Size | Weight | Form | Tracking | Line-Height |
|---------|------|--------|------|----------|-------------|
| Hero stat | 120-160px | 800-900 | lowercase | -0.03em | 1.0 |
| Title | 72-96px | 700-800 | mixed | -0.03em | 1.05-1.15 |
| Subtitle label | 16-20px | 500-600 | ALL CAPS | +0.08em | 1.4 |
| Body text | 24-28px | 400 | lowercase | 0 | 1.4-1.5 |
| Caption/source | 14-18px | 300 | ALL CAPS | +0.05em | 1.3 |

Notice: every adjacent pair differs in 3+ dimensions. Title → Body: size (3:1), weight (800→400), tracking, line-height. Subtitle → Body: size, form (CAPS→lowercase), tracking.

### Non-obvious typography decisions

**Form contrast via case**: ALL CAPS + wide tracking works for short labels (2-4 words max). Beyond 4-5 words, all caps degrades readability because word silhouettes become uniform rectangles. Body text and long titles always stay in sentence case.

**Typographic color**: squint at the card — each text block should read as a different shade of density. If all blocks look the same gray, increase variation (adjust weight spread, line-height differences, or tracking differences). Title blocks should feel like dense dark masses; captions should feel like airy light textures.

**Reverse type compensation**: white text on dark backgrounds appears ~10% smaller and thinner (optical illusion). Compensate: bump weight one level (e.g., 700→800) or add 2-4px to size. This is especially important since card news frequently uses dark-background cards.

**Emphasis by reduction**: dim non-essential text to gray (#888) instead of coloring keywords. The eye is drawn to the brightest element in a field of muted tones. Red for emphasis triggers danger/warning response — use only when that's the intended effect. Within a sentence, accent 1-2 keywords with color + heavier weight; dim the rest.

**Hero numbers as graphic elements**: statistics (120-160px) serve dual roles as both information and the Big visual anchor. A giant "6x" draws the eye before any title text. Weight 900 is reserved for these oversized decorative uses and watermark text.

---

## 6. Color

> Foundation: **Contrast**, **Repetition**

### Selection by relationship and content mood

| Relationship | Best for |
|---|---|
| Complementary (opposites) | High-energy: product launches, shocking statistics |
| Analogous (adjacent) | Calm: wellness, reflective content, tutorials |
| Split complement | Sophisticated: analysis, premium thought leadership |
| Triadic | Dynamic: infographics (requires tint/shade to avoid childish look) |

### The tint/shade escape from cliché

Pure hues carry cultural associations (red+green = Christmas, red+yellow+blue = children's toys). Professional palettes use shades (HSL L=25-40%) or tints (L=65-85%) with reduced saturation (S=40-60%). The color relationship stays; the cliché disappears.

```css
/* Split complement example — sophisticated analysis tone */
--color-primary: hsl(220, 45%, 30%);   /* deep navy (shade) */
--color-accent: hsl(30, 50%, 55%);     /* muted amber */
--color-neutral: hsl(40, 5%, 96%);     /* warm off-white */
```

### Warm/cool weight asymmetry

The fixed 80/20 chromatic ratio should flex by temperature:
- **Warm accent** (red, orange, yellow): 10-15% surface area — warm colors are visually loud
- **Cool accent** (blue, green, purple): 20-25% surface area — cool colors need more presence

Don't aim for equal visual weight between warm and cool — the warm color will always overpower.

### 3-Color Discipline
Lock exactly 3 chromatic roles as CSS variables (primary + accent + neutral). Everything else achromatic. Every additional chromatic color dilutes the accent's impact.

### Image-derived palettes
When a card uses a photo, extract the palette from the image rather than imposing a preset. Pick the dominant color, expand via color wheel relationships. This guarantees natural harmony between imagery and typography.

---

## 7. Layout

> Foundation: **Proximity**, **Alignment**, **Contrast**

### Focal point through dramatic contrast

Every card needs one element that's overwhelmingly different from everything else. Not a polite 60-30-10% ratio — a **dramatic** anchor. Hero numbers (120-160px), oversized titles, full-bleed images. It's OK to set body text small if the focal point earns the first glance.

### Content semantics drive layout
- Timeline / cause-and-effect → LR split (left-to-right = causation)
- Conclusion + reasoning → TB (headline-then-explanation = downward flow)
- Title + image + description → Z-pattern (natural scan path)

### Dual-scale design
Card news is first viewed at ~50% in feed grids, then tapped to full size. After generating, mentally shrink to half — the focal point and title must still be identifiable.

### Asymmetry check
Empty space on one side of a card might be: (a) trapped white space from alignment failure, or (b) intentional breathing room anchored to a strong flush-left edge. The difference is whether the asymmetry follows an alignment edge. If it does, it's a feature. If it doesn't, fix the alignment.

---

## 8. Background Treatment

> Foundation: **Contrast** (foreground/background hierarchy)

Background is the stage, not the star. When text density rises, actively suppress the background.

- **Title only**: brightness 0.7
- **Title + 2-3 body lines**: brightness 0.4 + slight blur
- **5+ dense lines**: brightness 0.2, strong blur, or glassmorphism panel

Gradient masks follow text position (text at bottom → dark gradient from bottom). Use 6-7 opacity stops for a cinematic transition, not a harsh 2-stop cutoff.

Glassmorphism is effective when background context matters (maps, cityscapes) — the viewer senses the environment through the blur without distraction.

---

## 9. Depth & Shadow

> Foundation: **Contrast** (depth hierarchy)

- **Soft shadows only**: alpha 0.1-0.15, wide blur. Sharp dark shadows = amateur.
- **White glow after rembg on dark cards**: `filter: drop-shadow(0 0 30px rgba(255,255,255,0.2))` — creates backlighting. Use `drop-shadow` (follows silhouette) not `box-shadow` (rectangular).
- **Z-index layering**: background(0) → gradient(1) → text(3) → cutout(4). Text behind a person cutout creates movie-poster depth.

---

## 10. Content Structure

> Foundation: **Contrast**, **Proximity**

- **Tesla Rule**: titles are conclusions, not topics. "EV Sales Surge 42% YoY" not "EV Market Status." Exception: question-format for explanatory content, event name for announcements.
- **Jargon simplification**: "ROI maximization" → "getting more value for the investment."
- **Q&A pagination**: split a surprising stat across two cards — Card A: question (tension), Card B: answer (impact).
- **Bookending**: match cover and ending visual tone. End with a vision statement, never "감사합니다."
- **Sequential dimming**: when explaining items from a shared list (one per card), keep all items visible but dim inactive ones to opacity 0.3.

---

## 11. Density & Sizing

> Foundation: **Proximity**, **Contrast**

Card news is an information delivery format — 85-95% canvas utilization is the target. But density should result from intentional Proximity-based grouping, not space-filling.

**Trapped vs intentional white space**: the enemy is trapped white space (accidental gaps from Proximity/Alignment failure). White space anchored to alignment edges and serving a structural role (group separation, breathing room around a focal point) is not a defect.

### Reference values (calibrated through 4 testing iterations at 1080x1350px)
- Padding: 36-48px | Intra-group gaps: 8-16px | Inter-group gaps: 24-48px
- Titles: 72-96px | Body: 24-28px | Illustrations: 600-900px wide
- Background photos: full-bleed edge-to-edge (any gap looks like a rendering error)
- Ending cards need equal density and care as body cards — sparse endings are the most common amateur mistake

**Squint test (refined)**: look for areas with no structural role — not "empty" areas, but areas that don't serve grouping, contrast, or alignment. Those are dead zones.

---

# Layer 3: Signature Style — Paperology Defaults

These are Paperology-specific techniques, effective defaults for informational content. They are **style choices, not universal principles** — evaluate against content tone.

### Corner Anchors
Small elements at all four corners (page number, brand, date, "+") create invisible framing.
- **Apply**: informational, business, political content
- **Evaluate**: casual, humor
- **Likely omit**: emotional, memorial, minimal, premium

### Background Typography (Watermark)
Thematic English keyword, weight 900, 150-200px+, opacity 3-5%, z-index 0.
- **Apply**: low text-density cards (covers, dividers, endings) where background feels barren
- **Omit**: high text-density cards (noise), content where understated mood is the point

### Decorative Shapes
Geometric elements at opacity 0.08-0.15. Above 0.15, they compete with content.
- **Apply**: when reinforcing an alignment edge or repetition pattern (structural role)
- **Omit**: when the motivation is "this area is empty" — ask first whether the space serves Proximity or Contrast

---

# Diagnostic Triage

When a card looks "off," check in Foundation order:

1. **Proximity**: Are related elements grouped? Is there a gap ratio? Squint: how many clusters? (2-4 target)
2. **Alignment**: One dominant axis? All elements on shared edges? Trapped white space?
3. **Repetition**: Consistent treatment patterns? Does this card belong with the series?
4. **Contrast**: Clear focal point? All differences obviously intentional? Any conflict (similar-but-not-same)?
5. **Typography**: 2-3+ contrast dimensions between hierarchy levels? Uniform density when squinting? Reverse type compensated?
6. **Color**: Grayscale test pass? Warm/cool ratio appropriate? Tints/shades or raw pure hues?
