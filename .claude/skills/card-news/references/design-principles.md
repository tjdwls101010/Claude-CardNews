# Card News Design Principles (Based on Paperlogy)

> This document outlines the core design principles to apply when generating HTML/CSS-based card news (1080x1350px, 4:5 aspect ratio, optimized for Instagram).
> It includes both explicit rules (formal knowledge) and tacit knowledge (designer intuition) derived from Paperlogy design review videos and publications, along with CSS implementation code.

---

## 1. Typography Engine

### 1-1. Font Weight Rules -- Paperlogy 100-900

**Principle:** Using `font-weight: bold` is prohibited. You must explicitly specify numeric weight values (100-900) from the Paperlogy variable font.

**Weight usage by purpose:**
- `100-200` (ExtraLight/Light): Decorative background watermark text, source attribution
- `300-400` (Light/Regular): Body text, supplementary descriptions
- `500-600` (Medium/SemiBold): Subheadings, emphasized body text
- `700-800` (Bold/ExtraBold): Main titles, key keywords
- `900` (Black): Cover titles, words requiring high impact

```css
/* Base typography system */
:root {
  --font-primary: 'Paperlogy', sans-serif;
  --weight-light: 300;
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-bold: 700;
  --weight-extrabold: 800;
  --weight-black: 900;
}

h1 {
  font-family: var(--font-primary);
  font-weight: var(--weight-extrabold); /* 800 explicit */
}

.body-text {
  font-family: var(--font-primary);
  font-weight: var(--weight-regular); /* 400 explicit */
}

/* Patterns that must never be used */
/* font-weight: bold;  -- prohibited */
/* Direct use of <b> tag -- prohibited */
```

**When to use:** Must be applied to all text elements
**Prohibited:** Using the `font-weight: bold` keyword, overusing the `<b>` tag

---

### 1-2. Letter-spacing Rules

**Principle:** Title text should have tightened letter-spacing to create a visual 'chunk' effect. Body text should maintain the default value or be slightly widened.

```css
/* Titles: tighten letter-spacing for chunk effect */
h1, h2, .title {
  letter-spacing: -0.03em;
}

/* Large numbers/impact text: even tighter */
.impact-number {
  letter-spacing: -0.05em;
}

/* Body text: default or slightly wider */
.body-text {
  letter-spacing: 0;
}

/* Small captions/labels: widen for readability */
.caption, .label {
  letter-spacing: 0.05em;
  font-size: 0.75rem;
  text-transform: uppercase;
}
```

**When to use:** Negative letter-spacing must be applied to all headings (h1, h2)
**Prohibited:** Applying excessive negative letter-spacing to body text (reduces readability)

---

### 1-3. Gray Dimming Technique (Reverse-emphasis)

**Principle:** Instead of coloring the text you want to emphasize in red, dim the non-essential text to gray so that the key content naturally stands out. Beginners use red for emphasis, but this conveys a sense of warning or danger. Professionals leave the emphasized portion as-is and gray out the rest.

```css
/* Dimming non-essential text */
.dimmed {
  color: #999999;
}

/* Key text retains the main color */
.highlighted {
  color: var(--text-primary); /* white or black */
  font-weight: var(--weight-bold);
}

/* Practical example -- emphasis within a single sentence */
/* HTML: <p class="dimmed">Something <span class="highlighted">sweet</span> for the mouth is also <span class="highlighted">good</span> for the body</p> */
.dimmed .highlighted {
  color: var(--text-primary);
  font-weight: var(--weight-extrabold);
}
```

**When to use:** When only specific keywords need emphasis within a sentence or list
**Prohibited:** Using red (`#FF0000` family) for emphasis. Unless specifically instructed otherwise, completely exclude red tones from accent colors.

---

### 1-4. Serif vs Sans-serif Usage Criteria

**Principle:** 95% of the entire document uses sans-serif (Paperlogy). Serif or handwritten fonts are used only as accents in the following cases.

| Situation | Font Type | Example |
|-----------|-----------|---------|
| Information delivery, data, body text | Sans-serif (Paperlogy) | All default text |
| Emotional questions, quotations | Serif or handwritten | "What does it mean to be a content planner?" |
| Specific brand mentions | That brand's font | Brand-specific typefaces |
| Background watermarks | Cursive or extra-bold sans-serif | "Contents", "Introduction" |

```css
/* Font change when emotional text is detected */
.emotional-text {
  font-family: 'Nanum Myeongjo', serif;
  font-style: italic;
  font-weight: var(--weight-light);
}

/* Quotations */
.quote {
  font-family: 'Nanum Myeongjo', serif;
  font-weight: var(--weight-regular);
  font-size: 1.4rem;
  line-height: 1.8;
  border-left: 3px solid var(--color-accent);
  padding-left: 1.2rem;
}
```

**When to use:** Moments requiring emotional transition, quotations, interrogative sentences
**Prohibited:** Applying serif fonts to the entire body, mixing 3 or more fonts in a single card

---

### 1-5. Background Typography Watermark Technique

**Principle:** When empty space feels barren, place an English keyword relevant to the page as a background element -- extremely large and extremely transparent. This is a very common technique in modern web design (landing pages).

```css
.bg-typography {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: var(--font-primary);
  font-weight: var(--weight-black); /* 900 */
  font-size: 12rem; /* Extremely large */
  color: rgba(255, 255, 255, 0.05); /* 5% opacity -- subtle */
  z-index: 0; /* Placed behind all content */
  white-space: nowrap;
  pointer-events: none;
  user-select: none;
  letter-spacing: -0.03em;
  text-transform: uppercase;
}

/* On dark backgrounds */
.dark-bg .bg-typography {
  color: rgba(255, 255, 255, 0.04);
}

/* On light backgrounds */
.light-bg .bg-typography {
  color: rgba(0, 0, 0, 0.03);
}
```

**When to use:** Pages with low text density such as covers, table of contents, and chapter divider slides
**Prohibited:** Setting opacity above 10% (makes it look like a foreground element), placement that overlaps with body text and harms readability

---

## 2. Color Pipeline

### 2-1. Extracting a Representative Color from the Subject/Brand

**Principle:** Extract one dominant color from the brand logo or main image, and use it as the accent color throughout the entire card news series. When the subject is clearly defined (e.g., Spotify -> green, Kakao -> yellow), directly specify that brand color.

```css
/* Lock extracted color as CSS variables */
:root {
  --color-primary: #1DB954;   /* Main color extracted from brand/subject */
  --color-accent: #1ED760;    /* Lighter variation of the main color */
  --color-neutral: #191414;   /* Achromatic base background */
}

/* All accent elements reference only these variables */
.highlight { color: var(--color-primary); }
.accent-bg { background-color: var(--color-accent); }
.card-bg { background-color: var(--color-neutral); }
```

**When to use:** Decided once at the initial stage of card news creation, then consistently applied across all cards
**Prohibited:** Using different accent colors on each card

---

### 2-2. The Rule of 3 Colors

**Principle:** The number of colors used in a single card must never exceed 3. Compose with Primary color + Accent color + Neutral color.

```css
:root {
  /* Define exactly 3 -- no additional colors allowed */
  --color-primary: #2563EB;     /* Main accent color (blue family) */
  --color-accent: #60A5FA;      /* Secondary accent (lighter variation of main) */
  --color-neutral-dark: #1F2937;  /* Dark neutral */
  --color-neutral-mid: #6B7280;   /* Mid neutral */
  --color-neutral-light: #F3F4F6; /* Light neutral */

  /* Text colors are also neutral-based */
  --text-primary: #FFFFFF;
  --text-secondary: #9CA3AF;
  --text-muted: #6B7280;
}
```

**When to use:** An absolute rule applied to all card news
**Prohibited:** Using 4 or more chromatic colors, rainbow-like multi-color combinations

---

### 2-3. The 80% Achromatic Tone Principle

**Principle:** Approximately 80% of the total card area should be filled with achromatic colors (black/white/gray), and chromatic colors should only be used within the remaining 20%. This is what allows the accent color to actually function as an 'accent.'

```css
/* Background is achromatic */
.card {
  width: 1080px;
  height: 1350px;
  background-color: #0F0F0F; /* Near black */
  color: #FFFFFF;
}

/* Accent color only on small areas */
.accent-bar {
  width: 60px;
  height: 4px;
  background-color: var(--color-primary);
  margin-bottom: 1rem;
}

.keyword {
  color: var(--color-primary);
  /* Apply only to 1-2 key words within the entire text */
}
```

**When to use:** Always
**Prohibited:** Filling the entire background with a chromatic color (chapter dividers excepted), applying the accent color to all body text

---

### 2-4. CSS Variable Locking Pattern

**Principle:** Lock the color palette determined in the first card as CSS variables in `:root`, and enforce that all subsequent cards reference only these variables. Hard-coded color values are prohibited.

```css
/* Defined once in :root -- shared across all cards */
:root {
  --color-primary: #2563EB;
  --color-accent: #60A5FA;
  --color-bg: #0F0F0F;
  --color-surface: #1A1A2E;
  --color-text: #FFFFFF;
  --color-text-dim: #888888;
  --color-border: rgba(255, 255, 255, 0.1);
}

/* Correct usage */
.title { color: var(--color-text); }
.subtitle { color: var(--color-text-dim); }
.highlight { color: var(--color-primary); }

/* Prohibited usage */
/* .title { color: #FF5733; }  -- hard-coding prohibited */
/* .box { background: pink; }  -- not referencing variables prohibited */
```

**When to use:** Applied to all color specifications in all card news
**Prohibited:** Hard-coded colors in inline styles, direct color specification bypassing `:root` variables

---

### 2-5. Dynamic Logo/Text Inversion Based on Background Luminance

**Principle:** When the background is dark, convert logos and text to white; when the background is light, convert them to black. As with the Spotify case, readability takes priority over brand-specific colors.

```css
/* On dark backgrounds -- make logo fully white */
.dark-bg .logo {
  filter: brightness(0) invert(1);
}

/* On light backgrounds -- make logo fully black */
.light-bg .logo {
  filter: brightness(0);
}

/* Automatic text inversion */
.dark-bg { color: #FFFFFF; }
.light-bg { color: #111111; }

/* On mid-tone backgrounds -- add text shadow for readability */
.mid-bg .text-overlay {
  color: #FFFFFF;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
}
```

**When to use:** Must be applied whenever placing logos or text over a background image
**Prohibited:** Dark text on dark backgrounds, light text on light backgrounds (insufficient contrast)

---

## 3. Layout Decision Logic

### 3-1. Content Structure -> Layout Pattern Mapping

**Principle:** Analyze the semantic structure of the text (chronological, narrative, hierarchical) to automatically select the optimal layout pattern. People read screens in Z-pattern, left-to-right (LR), or top-to-bottom (TB) order.

| Content Structure | Layout Pattern | CSS Grid Implementation |
|-------------------|----------------|------------------------|
| Timeline, cause-and-effect, Before/After | Left-Right (LR) layout | `grid-template-columns: 1fr 1fr` |
| Narrative, conclusion->reason->example | Top-Bottom (TB) layout | `grid-template-rows: auto 1fr auto` |
| Title+image+description, clearly hierarchical info | Z-pattern layout | `grid-template-areas` usage |
| Comparison, contrast | Left-Right symmetry | `grid-template-columns: 1fr 1fr` + center divider |
| Enumeration, lists | Grid card type | `grid-template-columns: repeat(2, 1fr)` |

```css
/* Z-pattern layout (most versatile) */
.layout-z {
  display: grid;
  grid-template-areas:
    "title  title"
    "image  desc"
    "footer footer";
  grid-template-columns: 1.2fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1.5rem;
  padding: 3rem;
}

/* Left-Right (LR) layout -- for timelines/comparisons */
.layout-lr {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  padding: 3rem;
  align-items: center;
}

/* Top-Bottom (TB) layout -- for narrative/conclusion-first */
.layout-tb {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 3rem;
  gap: 2rem;
}
```

**When to use:** Decided after content analysis at the initial card composition stage
**Prohibited:** Placing chronological data in top-bottom layout, splitting conclusion-focused content into left-right

---

### 3-2. Big-Medium-Small Sizing (60-30-10% Rule)

**Principle:** Force-classify all elements on a single screen into three size tiers. 'Ambiguous sizes' are not allowed. When everything is the same size, the eye gets fatigued.

- **Big (60%):** Main visual that draws the eye (large image, key number, main title)
- **Medium (30%):** Core text data to convey (subheadings, body summary)
- **Small (10%):** Metadata (page number, source, logo, date)

```css
/* Big: Main title */
.element-big {
  font-size: 3.5rem;
  font-weight: var(--weight-extrabold);
  line-height: 1.1;
  letter-spacing: -0.03em;
}

/* Medium: Body/subheading */
.element-medium {
  font-size: 1.25rem;
  font-weight: var(--weight-regular);
  line-height: 1.6;
}

/* Small: Metadata */
.element-small {
  font-size: 0.75rem;
  font-weight: var(--weight-light);
  color: var(--color-text-dim);
  letter-spacing: 0.05em;
}

/* Large number impact (variation of Big element) */
.impact-number {
  font-size: 6rem;
  font-weight: var(--weight-black);
  letter-spacing: -0.05em;
  line-height: 1;
}
```

**When to use:** An absolute rule applied to all cards
**Prohibited:** Placing all text at similar sizes, composing only with Medium elements without any Big element

---

### 3-3. Corner Anchors -- Visual Stability

**Principle:** Placing small text or symbols at the four corners of a card creates visual boundary lines that dramatically increase the layout's sense of stability.

```css
.card {
  position: relative;
  width: 1080px;
  height: 1350px;
}

/* Top-left: Brand/logo */
.anchor-top-left {
  position: absolute;
  top: 2.5rem;
  left: 2.5rem;
  font-size: 0.8rem;
  font-weight: var(--weight-medium);
  color: var(--color-text-dim);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

/* Top-right: Category/date */
.anchor-top-right {
  position: absolute;
  top: 2.5rem;
  right: 2.5rem;
  font-size: 0.75rem;
  color: var(--color-text-dim);
}

/* Bottom-left: Page number */
.anchor-bottom-left {
  position: absolute;
  bottom: 2.5rem;
  left: 2.5rem;
  font-size: 0.75rem;
  color: var(--color-text-dim);
}

/* Bottom-right: Decorative mark or source */
.anchor-bottom-right {
  position: absolute;
  bottom: 2.5rem;
  right: 2.5rem;
  font-size: 0.75rem;
  color: var(--color-text-dim);
}

/* Page number styling -- emphasize only current number */
.page-number .current {
  color: var(--color-text);
  font-weight: var(--weight-bold);
}
.page-number .separator,
.page-number .total {
  color: var(--color-text-dim);
}
/* Example: <span class="current">03</span><span class="separator"> / </span><span class="total">08</span> */
```

**When to use:** Applied to all cards (anchors placed in at least 2 corners)
**Prohibited:** Anchor elements being too large or visually prominent (they should be Small elements)

---

### 3-4. Four-quadrant Visual Weight Balance

**Principle:** When the screen is divided into four quadrants, if only one quadrant is abnormally heavy while the rest are empty, it looks unstable. Place decorative SVG shapes or background elements in empty quadrants to balance the weight.

```css
/* Decorative elements to fill empty space */
.decorative-shape {
  position: absolute;
  opacity: 0.08;
  pointer-events: none;
  user-select: none;
}

/* Circle decoration -- place in empty quadrant */
.deco-circle {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  border: 2px solid var(--color-primary);
  opacity: 0.1;
}

/* Line decoration */
.deco-line {
  width: 120px;
  height: 2px;
  background-color: var(--color-primary);
  opacity: 0.15;
}

/* Dot pattern decoration */
.deco-dots {
  display: grid;
  grid-template-columns: repeat(3, 6px);
  gap: 8px;
}
.deco-dots span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--color-text-dim);
  opacity: 0.3;
}
```

**When to use:** After placing main content, when there are areas that look visually empty
**Prohibited:** Decorative elements being more noticeable than content, overuse of decorative elements

---

### 3-5. Grid-Breaking -- Intentional Overflow

**Principle:** When numbers or decorative elements are placed so they protrude beyond the text box boundary, it adds dynamism to a static layout. However, it must be an 'intentional break' -- it should not look like an accidental overflow.

```css
/* Layout where numbering breaks through card boundaries */
.numbered-item {
  position: relative;
  padding-left: 4rem;
  margin-bottom: 2rem;
}

.numbered-item .number {
  position: absolute;
  left: -1.5rem; /* Intentional protrusion outside the container */
  top: 50%;
  transform: translateY(-50%);
  font-size: 5rem;
  font-weight: var(--weight-black);
  color: var(--color-primary);
  opacity: 0.15;
  line-height: 1;
}

/* Effect where image extends beyond card edge */
.overflow-image {
  position: absolute;
  right: -2rem; /* Protrusion to the right */
  bottom: 0;
  width: 60%;
  /* Apply overflow: hidden to the card for a clean clip */
}

.card {
  overflow: hidden; /* Cleanly cuts protruding elements at card boundary */
}
```

**When to use:** Numbered lists, large decorative text, protruding parts of background images
**Prohibited:** Clipping key text, applying overflow to all elements (limit to 1-2 accent points)

---

## 4. Background & Readability

### 4-1. Gradient Mask Technique

**Principle:** When placing text over a background image, lay a gradient behind the text that transitions from the background tone to transparent to ensure readability. This simultaneously prevents the background image from distracting the eye (reduces its role) and creates a natural blending effect.

```css
/* Basic gradient mask -- for bottom text */
.gradient-mask-bottom::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60%;
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.95) 0%,
    rgba(0, 0, 0, 0.7) 40%,
    rgba(0, 0, 0, 0) 100%
  );
  z-index: 1;
  pointer-events: none;
}

/* For left-side text (when image is on the right) */
.gradient-mask-left::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 60%;
  background: linear-gradient(
    to right,
    rgba(0, 0, 0, 1) 0%,
    rgba(0, 0, 0, 0.6) 50%,
    rgba(0, 0, 0, 0) 100%
  );
  z-index: 1;
}

/* Full-screen overlay (protects all text over image) */
.gradient-mask-full::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

/* Text must be placed above the mask */
.gradient-mask-bottom .content,
.gradient-mask-left .content,
.gradient-mask-full .content {
  position: relative;
  z-index: 2;
}
```

**When to use:** Must be applied whenever placing text over a background image. The gradient direction is dynamically determined based on text position.
**Prohibited:** Placing text directly over an image without a gradient

---

### 4-2. Glassmorphism

**Principle:** When placing text over a complex background (maps, intricate photos, etc.), apply a semi-transparent glass pane effect to preserve the background context while ensuring text readability.

```css
.glass-panel {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 2rem;
}

/* Light glass over dark backgrounds */
.glass-light {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
}

/* Dark glass over light backgrounds */
.glass-dark {
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
}
```

**When to use:** When placing text blocks over complex image backgrounds, when the background context (e.g., maps, cityscapes) needs to be preserved
**Prohibited:** Applying glassmorphism on solid-color backgrounds (pointless), blur values so high that the background becomes completely invisible

---

### 4-3. Semi-transparent Overlay

**Principle:** When you need to preserve the entire image while requiring text readability, lay a single-color semi-transparent layer over the image.

```css
/* Image container */
.image-overlay-container {
  position: relative;
  background-image: url('...');
  background-size: cover;
  background-position: center;
}

/* Semi-transparent overlay */
.image-overlay-container::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.55);
  z-index: 1;
}

/* Brand color overlay */
.brand-overlay::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: rgba(37, 99, 235, 0.75); /* Brand color + transparency */
  z-index: 1;
}

.image-overlay-container .content {
  position: relative;
  z-index: 2;
}
```

**When to use:** When placing text on full-bleed image backgrounds
**Prohibited:** Overlay transparency being too low (below 0.1) making text unreadable

---

### 4-4. Background Role Reduction Principle

**Principle:** The background is the 'stage,' not the 'lead actor.' Beginners want to fill the background with flashy images, but professionals boldly cover images with gradients or push them away with whitespace when the image might interfere with the text.

```css
/* When text density is high -- strongly suppress the background */
.text-heavy .bg-image {
  opacity: 0.15;
  filter: blur(3px);
}

/* When text density is low -- preserve the background */
.text-light .bg-image {
  opacity: 0.6;
  filter: none;
}

/* Metaphorical background (for contextual delivery) */
.contextual-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0.1; /* Extremely low opacity */
  z-index: 0;
}
```

**When to use:** Information-heavy cards with large amounts of text
**Prohibited:** Keeping the background image strong when there is a lot of text

---

### 4-5. Image Dimming/Blur as Text Density Increases

**Principle:** As the text area grows larger, lower the background image brightness or strengthen the blur.

```css
/* Background treatment stages by text density */

/* Stage 1: Low text (title only) */
.density-low .bg-image {
  filter: brightness(0.7);
}

/* Stage 2: Medium text (title + 2-3 lines of body) */
.density-medium .bg-image {
  filter: brightness(0.4) blur(2px);
}

/* Stage 3: High text (5+ lines of body) */
.density-high .bg-image {
  filter: brightness(0.2) blur(5px);
}

/* Dynamic filter application pattern */
.bg-image {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
  transition: filter 0.3s ease;
}
```

**When to use:** In all cases where text is placed over a background image
**Prohibited:** Maintaining identical background brightness regardless of text volume

---

## 5. Shadow & Depth

### 5-1. Soft Drop Shadow Rules

**Principle:** Shadows should have high transparency (40-50%) and wide blur to create a soft, diffused spread. Dark, harsh shadows are the hallmark of an amateur.

```css
/* Correct soft shadow */
.soft-shadow {
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}

/* Text soft shadow */
.text-soft-shadow {
  text-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

/* Card/panel soft shadow */
.card-shadow {
  box-shadow:
    0 4px 6px rgba(0, 0, 0, 0.05),
    0 12px 24px rgba(0, 0, 0, 0.1);
}

/* Deeper shadow for hover/emphasis */
.elevated-shadow {
  box-shadow:
    0 8px 16px rgba(0, 0, 0, 0.08),
    0 24px 48px rgba(0, 0, 0, 0.15);
}

/* -- Prohibited patterns -- */
/* box-shadow: 2px 2px 5px black;  -- too dark and harsh */
/* text-shadow: 1px 1px 0 #000;    -- 90s web aesthetic */
```

**When to use:** Cards, panels, image frames, and other elements that need a floating appearance
**Prohibited:** Sharp shadows without blur, shadows with opacity 0.8 or above, using the `black` keyword

---

### 5-2. White Glow on Dark Backgrounds

**Principle:** When placing a background-removed (cutout) person/object PNG on a dark background, using a white shadow instead of a black one creates a halo (glow) effect that makes the subject stand out in an elegant way.

```css
/* White glow for PNG images on dark backgrounds */
.white-glow {
  filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.25));
}

/* Stronger glow (for hero images) */
.white-glow-strong {
  filter: drop-shadow(0 0 40px rgba(255, 255, 255, 0.35));
}

/* Brand color glow */
.brand-glow {
  filter: drop-shadow(0 0 30px rgba(37, 99, 235, 0.4));
}

/* Compound glow (white + brand color) */
.dual-glow {
  filter:
    drop-shadow(0 0 15px rgba(255, 255, 255, 0.2))
    drop-shadow(0 0 40px rgba(37, 99, 235, 0.3));
}
```

**When to use:** When placing transparent-background PNG images on dark (#000-#333) backgrounds
**Prohibited:** Applying white glow on light backgrounds (invisible), glow opacity 0.6 or above (creates a smeared look)

---

### 5-3. Z-index Layering (Background -> Text -> Cutout Image)

**Principle:** When placing person/object images, use a 3-layer sandwich structure of 'background - text/logo - cutout image' to give a flat card a 3D-like sense of depth.

```css
.card {
  position: relative;
  overflow: hidden;
}

/* Layer 1: Background image */
.layer-bg {
  position: absolute;
  inset: 0;
  z-index: 1;
  background-size: cover;
  background-position: center;
}

/* Layer 2: Gradient overlay */
.layer-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.8) 0%,
    rgba(0, 0, 0, 0) 60%
  );
}

/* Layer 3: Text/logo (positioned behind the subject) */
.layer-text {
  position: relative;
  z-index: 3;
}

/* Layer 4: Cutout (background-removed) image (topmost) */
.layer-cutout {
  position: absolute;
  z-index: 4;
  /* Comes above text to create depth */
}
```

**When to use:** Cover/profile cards with person photos or product images
**Prohibited:** Stacking 4 or more layers (becomes complex), illogical layer ordering

---

### 5-4. Drop-shadow Filter for Transparent PNGs

**Principle:** For transparent-background PNG images, use `filter: drop-shadow()` instead of `box-shadow` to create a shadow that follows the image silhouette.

```css
/* box-shadow applies to the entire rectangular box -- unsuitable for transparent PNGs */
/* .png-image { box-shadow: 0 4px 8px rgba(0,0,0,0.3); }  -- prohibited */

/* drop-shadow follows the image silhouette -- suitable for transparent PNGs */
.png-image {
  filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.3));
}

/* Light drop-shadow on dark backgrounds */
.dark-bg .png-image {
  filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.25));
}

/* Dark drop-shadow on light backgrounds */
.light-bg .png-image {
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.15));
}
```

**When to use:** When adding shadows to PNG/SVG images with transparent backgrounds
**Prohibited:** Using `box-shadow` on transparent PNGs (creates a rectangular shadow)

---

## 6. Content Structuring

### 6-1. Tesla Rule: The Title is the Conclusion

**Principle:** Write the 'conclusion' in the title, not the 'topic.' Do not make the audience think to interpret it. Elon Musk writes "Tesla has created 125,000 jobs over the past decade" instead of "Job Creation Trends Over 10 Years."

**How to apply:**
- Never use noun-ending titles (e.g., "...Trends," "...Analysis," "...Comparison").
- If there is a key figure, it must be included in the title.
- Reading the title alone should fully convey the card's message.

| Bad Example (Topic-style) | Good Example (Conclusion-style) |
|---------------------------|--------------------------------|
| Domestic EV Market Status | Domestic EV Sales Surge 42% Year-over-Year |
| Consumer Preference Analysis | 7 Out of 10 Gen Z Consumers Choose Eco-friendly Products |
| Revenue Trends | Q3 Revenue Surpasses 20 Billion, Achieving All-time Record |

**When to use:** Applied to the main title (h1) of every card
**Prohibited:** Titles ending with "About...", "...Status", "...Analysis", "...Comparison" and other noun-ending forms

---

### 6-2. 3-Keyword Extraction

**Principle:** Compress long descriptive sentences into 3 core noun-form keywords. Remove all predicates. Separate and arrange them as 3 independent text blocks.

```css
/* 3-keyword layout */
.keyword-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  text-align: center;
}

.keyword-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.keyword-box .number {
  font-size: 2.5rem;
  font-weight: var(--weight-black);
  color: var(--color-primary);
  letter-spacing: -0.03em;
}

.keyword-box .label {
  font-size: 0.9rem;
  font-weight: var(--weight-medium);
  color: var(--color-text-dim);
}
```

**When to use:** When summarizing information or conveying key points
**Prohibited:** Listing 4 or more keywords (cognitive overload), placing full descriptive sentences inside boxes

---

### 6-3. Simplify Jargon to a Middle-school Reading Level

**Principle:** Amateurs overuse difficult jargon to appear smart, but experts (like Spotify) speak in simple words that even a middle-schooler can understand. "Jargon overuse is the enemy of presentations."

**How to apply:**
- When industry jargon or difficult terminology is detected, convert it to everyday language.
- When an abbreviation is used for the first time, it must be spelled out with an explanation.
- Allow a maximum of 1 piece of jargon per sentence.

| Before | After |
|--------|-------|
| ROI will be maximized | Returns relative to investment will increase significantly |
| KPI achievement rate improvement | Key goal achievement rate improvement |
| Create synergy | Achieve greater results together |

**When to use:** Applied at the text preprocessing stage for all text
**Prohibited:** Over-simplifying in card news targeted at experts (adjust based on audience)

---

### 6-4. Question -> Answer Pagination (Pagination for Impact)

**Principle:** When there is a surprising figure or plot twist, do not put everything on a single card. Create curiosity with a question on the first card, then reveal the answer/result on the next.

**Structure:**
```
[Card A] "How much did it grow in 3 years?"
  -> Background: dark and minimal, large question mark or curiosity-inducing image

[Card B] "6x Growth"
  -> Background: bright and high-impact design, giant number + ascending graph
```

```css
/* Question card style */
.question-card {
  background-color: var(--color-bg);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.question-card .question {
  font-size: 2.2rem;
  font-weight: var(--weight-bold);
  line-height: 1.4;
  color: var(--color-text);
}

/* Answer card style -- maximize impact */
.answer-card {
  background-color: var(--color-primary);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.answer-card .answer-number {
  font-size: 8rem;
  font-weight: var(--weight-black);
  letter-spacing: -0.05em;
  color: #FFFFFF;
  line-height: 1;
}
```

**When to use:** Surprising figures, plot twists, Before/After comparisons
**Prohibited:** Converting all information into question-answer format (overuse becomes tedious), 3 or more consecutive question cards

---

### 6-5. Emotional Divider Placement

**Principle:** If dry data and text continue uninterrupted, the reader gets fatigued. Whenever a chapter changes, insert a 'divider' with an emotional image and metaphorical copy to give the brain a rest.

```css
/* Divider slide */
.divider-card {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  overflow: hidden;
}

/* Full background image */
.divider-card .bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
}

/* Dark overlay */
.divider-card .bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
}

/* Chapter title */
.divider-card .chapter-title {
  position: relative;
  z-index: 2;
  font-size: 2.5rem;
  font-weight: var(--weight-extrabold);
  color: #FFFFFF;
  letter-spacing: -0.02em;
}

/* Emotional sub-copy */
.divider-card .sub-copy {
  position: relative;
  z-index: 2;
  font-size: 1rem;
  font-weight: var(--weight-light);
  color: rgba(255, 255, 255, 0.7);
  margin-top: 1rem;
  font-family: 'Nanum Myeongjo', serif; /* Emotional typeface */
}
```

**When to use:** Must be inserted whenever a major topic (H1 level) changes
**Prohibited:** Putting detailed information or data in the divider (it is purely for emotional transition), keeping background/text colors identical to body cards during chapter transitions

---

### 6-6. Bookending Technique

**Principle:** Reusing the same image/background/mood from the first card (intro) on the last card (outro) creates a sense of completion, as if the content were a self-contained film.

**Implementation:**
- Store the background image URL used in the intro as a variable.
- Reuse the same image in the outro.
- Place an emotional closing sentence or CTA (Call to Action) on the outro.

```css
/* Intro and outro reference the same CSS variable */
:root {
  --hero-bg-image: url('...');
}

.intro-card,
.outro-card {
  background-image: var(--hero-bg-image);
  background-size: cover;
  background-position: center;
}
```

**When to use:** When concluding a card news series of 5 or more cards
**Prohibited:** Intro/outro images having completely different tones

---

### 6-7. Cinematic Ending

**Principle:** Ending with "Thank you," "Thank You," or "Q&A" leaves no lasting impression. Close with the most moving or visionary single sentence from the content's context, or a famous person's quote.

| Bad Ending | Good Ending |
|------------|-------------|
| Thank you | "The future we are building has already begun" |
| Thank You | A single sentence capturing the project's core vision |
| It's Q&A time | A contextually relevant famous quote + attribution |

```css
/* Cinematic ending card */
.cinematic-ending {
  background-color: #000000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 4rem;
}

.cinematic-ending .closing-quote {
  font-family: 'Nanum Myeongjo', serif;
  font-size: 1.8rem;
  font-weight: var(--weight-regular);
  color: #FFFFFF;
  line-height: 1.8;
  max-width: 80%;
}

.cinematic-ending .attribution {
  margin-top: 2rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.5);
  font-weight: var(--weight-light);
}
```

**When to use:** The final card of a card news series
**Prohibited:** Writing only "Thank you" on an otherwise empty card, closing with generic greetings

---

## 7. Icon & Asset Consistency

### 7-1. Single Icon Family Rule

**Principle:** Within a single card news series, icons must come from the same family (pack). Mixing icons of different styles creates visual clutter.

**Selection criteria:**
- Determine the icon style that matches the overall card news tone on the first card.
- Use only that same style across all subsequent cards.

| Style | Characteristics | Suitable Tone |
|-------|----------------|--------------|
| Line | Clean, minimal | Business, tech |
| Filled | Solid, intuitive | Information delivery, education |
| Duotone | Refined, modern | Branding, marketing |

**When to use:** Decided during first card design, consistently applied across the entire series
**Prohibited:** Using Line icons on card 1 and Filled icons on card 2

---

### 7-2. Stroke/Fill/Corner Consistency -- CSS Variable Control

**Principle:** Unify the stroke width, fill method (fill/outline), and corner radius (border-radius) of all icons and shape elements using CSS variables.

```css
:root {
  /* Icon/asset style variables -- decided once on the first card */
  --icon-size: 48px;
  --icon-stroke-width: 1.5px;
  --icon-color: var(--color-primary);
  --icon-bg: rgba(37, 99, 235, 0.1);
  --icon-radius: 12px;

  /* Unified corner radius for all shapes */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-full: 9999px;
}

/* Icon container */
.icon-container {
  width: var(--icon-size);
  height: var(--icon-size);
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--icon-bg);
  border-radius: var(--icon-radius);
}

/* Force unified SVG icon style */
.icon-container svg {
  width: 24px;
  height: 24px;
  stroke: var(--icon-color);
  stroke-width: var(--icon-stroke-width);
  fill: none; /* Force Line style */
}

/* Unified corner radius for all cards/panels */
.panel { border-radius: var(--radius-md); }
.tag { border-radius: var(--radius-full); }
.image-frame { border-radius: var(--radius-lg); }
```

**When to use:** Applied to all visual elements including icons, shapes, and card panels
**Prohibited:** Using different border-radius for each element, SVG icons having inconsistent stroke-width

---

### 7-3. No Mixing of 3D and Flat Styles

**Principle:** Within a single card news series, never mix 3D rendered icons and flat (2D) icons. It completely breaks the tone.

**Decision criteria:**
- Business/information delivery -> Flat or Line style
- Casual/emotional -> 3D Clay or Illustrated style
- Once decided, maintain throughout the entire series

**When to use:** Decided during first card design, applied across the entire series
**Prohibited:** Using 3D emoji on card 1 and Flat icons on card 3

---

### 7-4. Applying the Color Palette to Icons

**Principle:** Icon colors must also stay within the color palette defined in section 2-1 (--color-primary, --color-accent). Do not use the icon's original colors as-is.

```css
/* Force override icon colors to brand palette */
.icon svg path {
  fill: var(--color-primary);
}

.icon svg {
  stroke: var(--color-primary);
}

/* Inactive icons use achromatic colors */
.icon-inactive svg path {
  fill: var(--color-text-dim);
}

/* Convert icon color via CSS filter (for raster image icons) */
.icon-img {
  filter: brightness(0) saturate(100%);
  /* Then re-colorize to desired color */
}
```

**When to use:** Applied to all icons sourced externally
**Prohibited:** Keeping the various original colors of icons intact (breaks the palette)

---

## 8. Advanced Techniques

### 8-1. Dimming Effect

**Principle:** When explaining one item in depth among several, keep only the item being explained bright and lower the opacity of the rest (opacity 0.3) to force visual focus. This is especially effective when explaining items one by one across multiple card news cards.

```css
/* Default state for all items */
.item-list .item {
  opacity: 0.3;
  transition: opacity 0.3s ease;
}

/* Active (currently being explained) item */
.item-list .item.active {
  opacity: 1;
  font-weight: var(--weight-bold);
}

/* Practical example: card explaining the 3rd item out of 5 */
/*
  1. Item A  (opacity: 0.3)
  2. Item B  (opacity: 0.3)
  3. Item C  (opacity: 1, bold, color: primary)  <-- currently being explained
  4. Item D  (opacity: 0.3)
  5. Item E  (opacity: 0.3)
*/

.item.active {
  opacity: 1;
  color: var(--color-primary);
  font-weight: var(--weight-bold);
  transform: scale(1.02);
}

.item:not(.active) {
  opacity: 0.3;
  color: var(--color-text-dim);
}
```

**When to use:** Series cards that sequentially explain items from a list, when highlighting a specific item in comparative analysis
**Prohibited:** Applying dimming unnecessarily when there is nothing to dim, opacity below 0.1 (completely invisible)

---

### 8-2. Device Mockup Framing

**Principle:** Placing app screens, website captures, or video content as plain rectangular images looks amateurish. Embedding them inside CSS-built device frames (smartphones, browsers, etc.) instantly adds sophistication.

```css
/* Smartphone mockup frame (CSS only) */
.phone-mockup {
  position: relative;
  width: 280px;
  aspect-ratio: 9 / 19.5;
  background: #1a1a1a;
  border-radius: 36px;
  padding: 12px;
  box-shadow:
    0 0 0 2px #333,
    0 20px 60px rgba(0, 0, 0, 0.4);
}

.phone-mockup .screen {
  width: 100%;
  height: 100%;
  border-radius: 24px;
  overflow: hidden;
  background-size: cover;
  background-position: top center;
}

/* Notch */
.phone-mockup::before {
  content: '';
  position: absolute;
  top: 12px;
  left: 50%;
  transform: translateX(-50%);
  width: 35%;
  height: 28px;
  background: #1a1a1a;
  border-radius: 0 0 16px 16px;
  z-index: 10;
}

/* Browser window mockup */
.browser-mockup {
  background: #2a2a2a;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.3);
}

.browser-mockup .toolbar {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 10px 14px;
  background: #3a3a3a;
}

.browser-mockup .toolbar .dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.browser-mockup .toolbar .dot:nth-child(1) { background: #ff5f57; }
.browser-mockup .toolbar .dot:nth-child(2) { background: #ffbd2e; }
.browser-mockup .toolbar .dot:nth-child(3) { background: #28ca41; }

.browser-mockup .viewport {
  width: 100%;
  aspect-ratio: 16 / 10;
  background-size: cover;
  background-position: top center;
}
```

**When to use:** When showing app screens, websites, social media posts, and other digital content
**Prohibited:** Putting all images in mockups (landscape photos do not need mockups), mockup size occupying more than 80% of the card

---

### 8-3. Background Typography Watermark (Detailed Implementation)

**Principle:** An advanced version of the watermark technique covered in section 1-5. Includes various placement patterns and effects.

```css
/* Pattern 1: Center watermark */
.watermark-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 12rem;
  font-weight: var(--weight-black);
  color: rgba(255, 255, 255, 0.04);
  white-space: nowrap;
  pointer-events: none;
  z-index: 0;
}

/* Pattern 2: Rotated watermark */
.watermark-rotated {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-15deg);
  font-size: 10rem;
  font-weight: var(--weight-black);
  color: rgba(255, 255, 255, 0.03);
  white-space: nowrap;
  pointer-events: none;
  z-index: 0;
}

/* Pattern 3: Bottom-anchored watermark */
.watermark-bottom {
  position: absolute;
  bottom: -2rem;
  right: -1rem;
  font-size: 14rem;
  font-weight: var(--weight-black);
  color: rgba(255, 255, 255, 0.03);
  line-height: 1;
  pointer-events: none;
  z-index: 0;
}

/* Pattern 4: Repeating pattern watermark */
.watermark-pattern {
  position: absolute;
  inset: 0;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
  gap: 2rem;
  opacity: 0.02;
  pointer-events: none;
  z-index: 0;
  transform: rotate(-10deg);
  overflow: hidden;
}
```

**When to use:** Cards with low text density such as covers, dividers, and endings
**Prohibited:** Using watermarks on cards with heavy body text (harms readability), opacity above 8% (causes distraction)

---

### 8-4. Mesh Gradient Background

**Principle:** When a solid-color background is too plain and a photo background interferes with text, use a mesh gradient where multiple colors blend softly like an aurora.

```css
/* Basic mesh gradient -- layered radial-gradients */
.mesh-gradient {
  background-color: #0a0a0a;
  background-image:
    radial-gradient(
      ellipse at 20% 50%,
      rgba(37, 99, 235, 0.3) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 80% 20%,
      rgba(139, 92, 246, 0.25) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 60% 80%,
      rgba(6, 182, 212, 0.2) 0%,
      transparent 50%
    );
}

/* Warm tone mesh gradient */
.mesh-gradient-warm {
  background-color: #0a0a0a;
  background-image:
    radial-gradient(
      ellipse at 30% 40%,
      rgba(234, 88, 12, 0.25) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 70% 70%,
      rgba(168, 85, 247, 0.2) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 50% 10%,
      rgba(239, 68, 68, 0.15) 0%,
      transparent 50%
    );
}

/* Minimal mesh (single-color based) */
.mesh-gradient-subtle {
  background-color: var(--color-bg);
  background-image:
    radial-gradient(
      ellipse at 30% 50%,
      rgba(37, 99, 235, 0.08) 0%,
      transparent 60%
    );
}
```

**When to use:** When an atmospheric background is needed but images cannot be used, such as covers and dividers
**Prohibited:** Using 3 or more chromatic colors in the mesh (creates clutter), applying flashy mesh to data-centric cards (causes distraction)

---

## Appendix: Card News Base Frame (1080x1350px)

```css
/* Card news base container */
.card-news {
  width: 1080px;
  height: 1350px;
  position: relative;
  overflow: hidden;
  font-family: var(--font-primary);
  background-color: var(--color-bg);
  color: var(--color-text);
}

/* Safe Area -- content must be placed within this area */
.card-news .safe-area {
  position: absolute;
  top: 60px;
  right: 60px;
  bottom: 60px;
  left: 60px;
  display: flex;
  flex-direction: column;
}

/* Complete CSS variable system */
:root {
  /* Typography */
  --font-primary: 'Paperlogy', sans-serif;
  --font-serif: 'Nanum Myeongjo', serif;
  --weight-light: 300;
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-bold: 700;
  --weight-extrabold: 800;
  --weight-black: 900;

  /* Colors -- dynamically determined at card news creation time */
  --color-primary: #2563EB;
  --color-accent: #60A5FA;
  --color-bg: #0F0F0F;
  --color-surface: #1A1A2E;
  --color-text: #FFFFFF;
  --color-text-dim: #888888;
  --color-text-muted: #555555;
  --color-border: rgba(255, 255, 255, 0.1);

  /* Spacing */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2.5rem;
  --space-xl: 4rem;

  /* Border Radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-full: 9999px;

  /* Icon System */
  --icon-size: 48px;
  --icon-stroke-width: 1.5px;
  --icon-color: var(--color-primary);

  /* Shadow */
  --shadow-soft: 0 8px 32px rgba(0, 0, 0, 0.12);
  --shadow-elevated: 0 16px 48px rgba(0, 0, 0, 0.2);
}
```

---

## Appendix: Checklist (Verification Items After Card Generation)

After generating card news HTML, the following items must be verified.

### Typography
- [ ] Are numeric values (400, 700, 800, etc.) used instead of `font-weight: bold`
- [ ] Is negative `letter-spacing` applied to titles
- [ ] Is the Big-Medium-Small three-tier size hierarchy clear
- [ ] Are font types limited to 2 or fewer (sans-serif + serif)

### Color
- [ ] Are chromatic colors limited to 3 or fewer
- [ ] Do all colors reference CSS variables (no hard-coding)
- [ ] Is text readability ensured against the background
- [ ] Was red not used for emphasis

### Layout
- [ ] Are corner anchors placed in at least 2 corners
- [ ] Is the visual weight balanced across four quadrants
- [ ] Is the appropriate layout pattern (Z/LR/TB) applied based on content structure

### Background
- [ ] Is a gradient mask or overlay applied to text over images
- [ ] Is background brightness adjusted according to text density

### Content
- [ ] Is the title a conclusion-style sentence (not a noun-ending form)
- [ ] Has jargon been simplified to plain language
- [ ] Does the final card have a cinematic ending rather than "Thank you"

### Consistency
- [ ] Is the icon style (Line/Filled) unified across the entire series
- [ ] Do shadow styles follow the soft shadow rules
- [ ] Is the corner radius (border-radius) consistent throughout
