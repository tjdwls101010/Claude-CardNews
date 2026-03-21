# CSS Patterns for Card News

Non-obvious CSS settings specific to 1080x1350px card news. This document covers only what you're likely to get wrong or forget -- standard CSS knowledge (flexbox, grid, positioning) is assumed.

---

## 1. Card Frame Foundation

Every card HTML file must establish a fixed viewport. The card is not responsive -- it renders at exactly 1080x1350px and gets captured as a PNG at 2x retina resolution (2160x2700px actual).

```css
.card {
    position: relative;
    width: 1080px;
    height: 1350px;
    overflow: hidden;
    word-break: keep-all;  /* Korean text: break at word boundaries, not mid-syllable */
}
```

`overflow: hidden` is critical: it cleanly clips any elements that intentionally or accidentally extend beyond the card boundary. Without it, protruding decorative elements or oversized background images create visible overflow.

`word-break: keep-all` prevents Korean text from breaking mid-word. Without this, a line break can split a word like "정치개혁" into "정치개" and "혁", which is visually jarring and semantically wrong.

### Font Declarations

Paperlogy requires 9 separate `@font-face` declarations (one per weight 100-900). Use **absolute paths** to the font files in the skill's assets directory -- relative paths break when the HTML file is in a different working directory.

```css
@font-face {
    font-family: 'Paperlogy';
    src: url('/absolute/path/to/assets/fonts/Paperlogy-4Regular.ttf') format('truetype');
    font-weight: 400;
}
/* Repeat for weights 100, 200, 300, 500, 600, 700, 800, 900 */
```

Always include `-webkit-font-smoothing: antialiased` on the body for crisp text rendering on retina displays. Without it, text can appear slightly blurry or thick on macOS.

### Body Wrapper

The body centers the card on a neutral background for preview purposes when the HTML is opened directly in a browser:

```css
body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: #f0f0f0;
    font-family: 'Paperlogy', sans-serif;
    -webkit-font-smoothing: antialiased;
}
```

---

## 2. CSS Variable System

### Required Variables

Every card must define these variables in `:root`. All color references throughout the card should use these variables -- never hard-code hex values in individual elements.

```css
:root {
    --color-primary: #2563EB;    /* Main accent -- extracted from brand/topic */
    --color-accent: #60A5FA;     /* Lighter variation of primary */
    --color-bg: #0F0F0F;         /* Card background */
    --color-surface: #1A1A2E;    /* Elevated surface (panels, cards-within-cards) */
    --color-text: #FFFFFF;       /* Primary text */
    --color-text-dim: #888888;   /* Secondary text, gray dimming target */
    --color-text-muted: #555555; /* Tertiary text, near-invisible metadata */
    --pad: 40px;                 /* Base padding from card edges */
}
```

### Text Color Hierarchy

The three text colors create a visual hierarchy without changing font size or weight:
- `--color-text`: Full brightness. The words you want the viewer to read first
- `--color-text-dim` (#888): Gray dimming. Supporting text that provides context but shouldn't compete with key content
- `--color-text-muted` (#555): Near-invisible. Source attributions, dates, metadata that should be present but not noticed

This three-tier system is the CSS implementation of the "emphasis by reduction" principle. The key text doesn't need special coloring -- it stands out because everything around it is dimmed.

### Series Consistency

All cards in a series must share identical `:root` variable values. When starting a new card, copy the `:root` block from the first card verbatim. Changing even one variable (e.g., making `--color-primary` slightly different on card 5) breaks the visual cohesion of the series.

---

## 3. Card Type Structures

### Cover Card Layer Stack

The cover card uses a multi-layer z-index sandwich to create depth:

| Layer | z-index | Content |
|-------|---------|---------|
| Background photo | 0 | `<img>` with `object-fit: cover`, fills entire card |
| Top gradient | 1 | Subtle darkening from top edge for visual cohesion (200px height, opacity 0.6→0) |
| Bottom gradient | 1 | Strong darkening from bottom for text readability (multi-stop, 6-7 opacity values) |
| Watermark text | 2 | Large English keyword at 3-5% opacity |
| Main content | 5 | Title, subtitle, tag -- positioned at the bottom of the card |
| Corner anchors | 10 | Page number, brand name, date, "+" mark |

The content sits at z:5 (not z:2 or z:3) to leave room for additional decorative layers without restructuring the entire stack.

### Body Card Structure

Body cards are simpler -- typically no background photo. The structure is:
- Corner anchors (z:10) at absolute positions
- A flex column for the main content area
- An accent bar (small colored rectangle, ~60x4px) before the title to signal the card's color identity
- Title → body text → optional illustration, flowing top to bottom

### Ending Card

The ending card must be **as visually dense as body cards** -- this is the most common mistake. Structure it like a cover card (background treatment + text overlay) but with centered content: a quote or vision statement, quotation marks as decorative elements, and the brand name at the bottom.

---

## 4. Gradient Overlay Patterns

### Bottom-Heavy Gradient (Most Common)

For text positioned at the bottom of a cover card, use a multi-stop gradient that transitions gradually from opaque at the bottom to transparent at the top. The key is using 6-7 stops rather than 2 -- this creates a cinematic, natural-feeling transition rather than a harsh line:

```css
background: linear-gradient(to top,
    rgba(10, 22, 40, 0.99) 0%,
    rgba(10, 22, 40, 0.97) 18%,
    rgba(10, 22, 40, 0.92) 30%,
    rgba(10, 22, 40, 0.75) 42%,
    rgba(10, 22, 40, 0.35) 58%,
    rgba(10, 22, 40, 0.08) 75%,
    rgba(10, 22, 40, 0.0) 100%
);
```

Use the card's background color (not pure black) as the gradient base -- this ensures the gradient blends seamlessly into the card rather than introducing an off-tone dark band.

### Top Gradient for Cohesion

A subtle gradient from the top edge (200px height, opacity 0.6→0.0) ties the background photo to the card's overall tone. Without it, the top of the card can feel disconnected -- especially when the photo is bright and the card's text area is dark.

### Direction Follows Text

The gradient direction must always originate from where the text sits:
- Text at bottom → gradient from bottom
- Text on left → gradient from left
- Text covering most of the card → full-coverage overlay (single semi-transparent layer)

---

## 5. Non-obvious CSS Gotchas

### Images: Files, Never Base64

Embedding images as base64 data URIs bloats the HTML file to megabytes, causing slow rendering and potential memory issues in Playwright during PNG conversion. Always reference images as separate files: `<img src="./images/photo.png">`.

### drop-shadow vs box-shadow for Transparent PNGs

`box-shadow` applies to the rectangular bounding box of the element -- useless for transparent PNG cutouts because it creates a visible rectangle around the image. `filter: drop-shadow()` follows the actual silhouette of the image content, producing a natural shadow or glow that traces the subject's outline.

```css
/* Correct: shadow follows the person's silhouette */
.cutout { filter: drop-shadow(0 0 30px rgba(255,255,255,0.2)); }

/* Wrong: shadow forms a rectangle around the entire image box */
.cutout { box-shadow: 0 0 30px rgba(255,255,255,0.2); }
```

### White Glow After rembg

After removing a background with rembg, the cutout placed on a dark card needs a white glow to avoid looking "pasted on":

```css
filter: drop-shadow(0 0 30px rgba(255,255,255,0.2));
```

### Page Number Styling

The current page number should be visually distinct from the total. Use weight and opacity contrast:
- Current number: `font-weight: 600; color: rgba(255,255,255,0.6)`
- Separator and total: `font-weight: 300; color: rgba(255,255,255,0.3)`

Example: **01** / 03 -- the current page anchors the eye while the total recedes.

### Korean Typography Baseline

For Korean text at card news scale:
- `line-height: 1.4-1.6` for body text (tighter than web defaults)
- `letter-spacing: -0.02em` for body (slightly tighter than Latin defaults because Korean characters are already spaced within their em-square)
- `word-break: keep-all` on the card container (prevents mid-word breaks)
