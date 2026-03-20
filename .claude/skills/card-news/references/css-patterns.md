# CSS Patterns for Card News

A collection of CSS code snippets that can be copied and used directly when generating card news.
All patterns are based on 1080x1350px (4:5 aspect ratio) card news and use the Paperlogy font.

---

## 1. Base Template

The base boilerplate for card news HTML files. Every card starts from this structure.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card News</title>
<style>

/* ================================================
   Paperlogy font declarations (9 weight levels, 100-900)
   Replace FONTS_DIR with the actual absolute path
   ================================================ */
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-1Thin.ttf') format('truetype'); font-weight: 100; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-2ExtraLight.ttf') format('truetype'); font-weight: 200; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-3Light.ttf') format('truetype'); font-weight: 300; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-4Regular.ttf') format('truetype'); font-weight: 400; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-5Medium.ttf') format('truetype'); font-weight: 500; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-6SemiBold.ttf') format('truetype'); font-weight: 600; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-7Bold.ttf') format('truetype'); font-weight: 700; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-8ExtraBold.ttf') format('truetype'); font-weight: 800; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-9Black.ttf') format('truetype'); font-weight: 900; font-style: normal; }

/* ================================================
   Reset and base settings
   ================================================ */
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: #f0f0f0;
    font-family: 'Paperlogy', sans-serif;
    font-weight: 400;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ================================================
   Root container (1080x1350px, 4:5 aspect ratio)
   ================================================ */
.card {
    position: relative;
    width: 1080px;
    height: 1350px;
    overflow: hidden;
    background: var(--bg-color, #FFFFFF);
    color: var(--text-color, #1A1A1A);
}

/* ================================================
   CSS variable template - Color palette
   Swap these values per project to change the overall tone.
   3-color restriction principle: use only primary, secondary, and accent.
   ================================================ */
:root {
    /* Background/foreground base colors */
    --bg-color: #FFFFFF;
    --text-color: #1A1A1A;

    /* 3-color palette (swap per project) */
    --primary-color: #2B2B2B;      /* Main color - titles, emphasis elements */
    --secondary-color: #6B6B6B;    /* Secondary color - sub-text, dividers */
    --accent-color: #3A7BDE;       /* Accent color - keyword highlights */

    /* Dimming grays (reverse-emphasis: mute surroundings to make the key content stand out) */
    --dim-gray: #AAAAAA;
    --light-gray: #E5E5E5;

    /* Spacing base values */
    --pad: 72px;                   /* Default inner padding for cards */
    --pad-sm: 36px;                /* Narrow padding */
}

/* ================================================
   Korean text base handling
   ================================================ */
.card {
    word-break: keep-all;          /* Word-level line breaking for Korean */
    line-height: 1.5;
    letter-spacing: -0.02em;       /* Slightly tightened body text tracking */
}

</style>
</head>
<body>

<div class="card">
    <!-- Card content goes here -->
</div>

</body>
</html>
```

---

## 2. Typography Presets

Typography is the core of card news quality.
Tighten letter-spacing to create a "chunky" feel, and specify font-weight using explicit numeric values.
Always use numbers (100-900) instead of `font-weight: bold`.

### 2-1. Main Title

```css
/* Main title - The largest text on the card. Use conclusion-style sentences. */
.title-main {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 900;              /* Black - Maximum weight for visual impact */
    font-size: 64px;
    line-height: 1.2;
    letter-spacing: -0.05em;       /* Tighten tracking significantly for chunky feel */
    color: var(--text-color);
    word-break: keep-all;
}

/* Slightly lighter main title variant */
.title-main--light {
    font-weight: 800;              /* ExtraBold */
    font-size: 56px;
}
```

### 2-2. Subtitle

```css
/* Subtitle - Section headings, sub-topics */
.title-sub {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 700;              /* Bold */
    font-size: 36px;
    line-height: 1.3;
    letter-spacing: -0.03em;
    color: var(--primary-color);
}

/* SemiBold variant - Softer feel */
.title-sub--soft {
    font-weight: 600;              /* SemiBold */
    font-size: 32px;
}
```

### 2-3. Body Text

```css
/* Body - For explanations and content delivery */
.text-body {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 400;              /* Regular */
    font-size: 28px;
    line-height: 1.6;
    letter-spacing: -0.02em;
    color: var(--text-color);
    word-break: keep-all;
}

/* Body medium - Slightly emphasized body text */
.text-body--medium {
    font-weight: 500;              /* Medium */
}
```

### 2-4. Caption

```css
/* Caption - Sources, supplementary notes, meta information */
.text-caption {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 300;              /* Light */
    font-size: 20px;
    line-height: 1.4;
    letter-spacing: -0.01em;
    color: var(--secondary-color);
}

/* Ultra-thin caption - Very small auxiliary text */
.text-caption--thin {
    font-weight: 200;              /* ExtraLight */
    font-size: 18px;
}
```

### 2-5. Gray Dimming Helpers

Instead of adding red to emphasize, mute surrounding text to gray -- a "reverse highlighting" technique.
This is a core technique used by professional designers.

```css
/* Tone down non-essential text to gray - Key text naturally stands out */
.dim {
    color: var(--dim-gray) !important;
}

/* Lighter dimming */
.dim--light {
    color: #CCCCCC !important;
}

/* Dimming for slide transitions - Darkens previous items */
.dim--inactive {
    opacity: 0.3;
    transition: opacity 0.3s ease;
}

/* Active items stay bright */
.dim--active {
    opacity: 1;
    font-weight: 700;
}
```

### 2-6. Keyword Highlight

Wrap only 1-2 key words in a sentence with `<span>` for emphasis.

```css
/* Keyword emphasis - accent color + increased weight */
.highlight {
    color: var(--accent-color);
    font-weight: 700;
}

/* Background highlight - Highlighter pen effect */
.highlight--bg {
    background: linear-gradient(transparent 50%, rgba(58, 123, 222, 0.15) 50%);
    padding: 0 4px;
    font-weight: 600;
}

/* Underline highlight */
.highlight--underline {
    text-decoration: underline;
    text-decoration-color: var(--accent-color);
    text-underline-offset: 6px;
    text-decoration-thickness: 3px;
    font-weight: 600;
}
```

**HTML usage example:**
```html
<p class="text-body">
    <span class="dim">What tastes</span>
    <span class="highlight">sweet</span>
    <span class="dim">is also</span>
    <span class="highlight">good</span>
    <span class="dim">for you</span>
</p>
```

---

## 3. Layout Patterns

### 3-1. Full-Bleed Single Column

A layout where text occupies the entire screen. Used for impactful message delivery.

```css
/* Full-bleed single column layout */
.layout-fullbleed {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: var(--pad);
    text-align: center;
}
```

```html
<!-- Full-bleed single column HTML structure -->
<div class="card">
    <div class="layout-fullbleed">
        <h1 class="title-main">Key message goes here</h1>
        <p class="text-body" style="margin-top: 32px;">Supporting description text</p>
    </div>
</div>
```

### 3-2. Two-Column Split (Text + Image)

A left-right split layout. Suitable for explaining temporal flow or cause-and-effect relationships.

```css
/* Two-column split layout - Left: text, Right: image */
.layout-split {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
}

/* Text area */
.layout-split__text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--pad);
}

/* Image area */
.layout-split__image {
    width: 100%;
    height: 100%;
    overflow: hidden;
}

.layout-split__image img {
    width: 100%;
    height: 100%;
    object-fit: cover;             /* Fill area while maintaining aspect ratio */
}
```

```html
<!-- Two-column split HTML structure -->
<div class="card">
    <div class="layout-split">
        <div class="layout-split__text">
            <h2 class="title-sub">Section Title</h2>
            <p class="text-body" style="margin-top: 24px;">Description content</p>
        </div>
        <div class="layout-split__image">
            <img src="IMAGE_PATH" alt="">
        </div>
    </div>
</div>
```

### 3-3. Top Image + Bottom Text

A top-bottom split layout suitable for conclusion-reason-example structures.

```css
/* Top image + bottom text layout */
.layout-top-image {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-rows: 55% 45%;   /* Image takes a slightly larger proportion */
}

/* Image area */
.layout-top-image__visual {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
}

.layout-top-image__visual img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Text area */
.layout-top-image__content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--pad) var(--pad) var(--pad) var(--pad);
}
```

```html
<!-- Top image + bottom text HTML structure -->
<div class="card">
    <div class="layout-top-image">
        <div class="layout-top-image__visual">
            <img src="IMAGE_PATH" alt="">
        </div>
        <div class="layout-top-image__content">
            <h2 class="title-sub">Title</h2>
            <p class="text-body" style="margin-top: 20px;">Body content</p>
        </div>
    </div>
</div>
```

### 3-4. Center Focus

Places the key element large and centered on screen. Uses Big-Medium-Small hierarchy.

```css
/* Center focus layout */
.layout-center {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: var(--pad);
    text-align: center;
}

/* Big - Eye-catching main visual (50-60% of screen) */
.layout-center__hero {
    font-size: 120px;
    font-weight: 900;
    letter-spacing: -0.05em;
    line-height: 1.1;
    color: var(--accent-color);
    margin-bottom: 40px;
}

/* Medium - Key text (30% of screen) */
.layout-center__body {
    font-size: 32px;
    font-weight: 500;
    line-height: 1.5;
    color: var(--text-color);
    max-width: 800px;
}

/* Small - Metadata (10% of screen) */
.layout-center__meta {
    font-size: 20px;
    font-weight: 300;
    color: var(--secondary-color);
    margin-top: 40px;
}
```

```html
<!-- Center focus HTML structure (number emphasis example) -->
<div class="card">
    <div class="layout-center">
        <div class="layout-center__hero">6x</div>
        <div class="layout-center__body">Achieved 6x growth in 3 years</div>
        <div class="layout-center__meta">As of 2023 | Annual Revenue Report</div>
    </div>
</div>
```

### 3-5. Grid-Based Multi-Item

Evenly distributes multiple items. Automatically maintains visual balance.

```css
/* Grid-based multi-item layout */
.layout-grid {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: var(--pad);
}

/* Grid header area */
.layout-grid__header {
    margin-bottom: 48px;
}

/* Item grid - auto-fit for even distribution */
.layout-grid__items {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(2, 1fr);   /* 2-column default */
    gap: 32px;
    align-content: center;
}

/* 3-column variant */
.layout-grid__items--col3 {
    grid-template-columns: repeat(3, 1fr);
}

/* Each item card */
.layout-grid__item {
    background: var(--light-gray);
    border-radius: 20px;
    padding: 36px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.layout-grid__item-title {
    font-weight: 700;
    font-size: 28px;
    margin-bottom: 12px;
    color: var(--primary-color);
}

.layout-grid__item-desc {
    font-weight: 400;
    font-size: 22px;
    line-height: 1.5;
    color: var(--secondary-color);
}
```

```html
<!-- Grid multi-item HTML structure -->
<div class="card">
    <div class="layout-grid">
        <div class="layout-grid__header">
            <h2 class="title-sub">4 Key Points</h2>
        </div>
        <div class="layout-grid__items">
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">01</div>
                <div class="layout-grid__item-desc">First item description</div>
            </div>
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">02</div>
                <div class="layout-grid__item-desc">Second item description</div>
            </div>
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">03</div>
                <div class="layout-grid__item-desc">Third item description</div>
            </div>
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">04</div>
                <div class="layout-grid__item-desc">Fourth item description</div>
            </div>
        </div>
    </div>
</div>
```

### 3-6. Corner Anchor Positioning

Places small elements (page numbers, logos, decorations) at the four corners of the card for visual stability.
A "blind text nailed to all four corners" technique.

```css
/* Corner anchor system - Places elements at the four corners of the card */

/* Top-left anchor (typically logo or brand name) */
.anchor-tl {
    position: absolute;
    top: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 600;
    font-size: 18px;
    color: var(--secondary-color);
    z-index: 10;
}

/* Top-right anchor (typically page number) */
.anchor-tr {
    position: absolute;
    top: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 300;
    font-size: 18px;
    color: var(--secondary-color);
    z-index: 10;
}

/* Bottom-left anchor (typically source, date) */
.anchor-bl {
    position: absolute;
    bottom: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 300;
    font-size: 16px;
    color: var(--secondary-color);
    z-index: 10;
}

/* Bottom-right anchor (typically decorative symbol) */
.anchor-br {
    position: absolute;
    bottom: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 200;
    font-size: 20px;
    color: var(--secondary-color);
    z-index: 10;
}

/* Decorative cross mark */
.anchor-cross {
    font-weight: 200;
    font-size: 24px;
    color: var(--dim-gray);
}
```

```html
<!-- Corner anchor HTML structure -->
<div class="card">
    <!-- 4 corner anchors -->
    <div class="anchor-tl">BrandName</div>
    <div class="anchor-tr">01</div>
    <div class="anchor-bl">2026.03</div>
    <div class="anchor-br"><span class="anchor-cross">+</span></div>

    <!-- Main content -->
    <div class="layout-fullbleed">
        <h1 class="title-main">Body content</h1>
    </div>
</div>
```

---

## 4. Visual Effects

### 4-1. Gradient Mask (Ensuring Text Readability Over Images)

When placing text over a background image, use a gradient to reduce the image's visual dominance
and ensure text readability. Choose direction based on text position.

```css
/* Gradient mask - Bottom to top (when text is at the bottom) */
.gradient-mask--bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 60%;
    background: linear-gradient(
        to top,
        rgba(0, 0, 0, 0.85) 0%,
        rgba(0, 0, 0, 0.5) 40%,
        rgba(0, 0, 0, 0) 100%
    );
    z-index: 1;
}

/* Gradient mask - Left to right (when text is on the left) */
.gradient-mask--left {
    position: absolute;
    top: 0;
    left: 0;
    width: 60%;
    height: 100%;
    background: linear-gradient(
        to right,
        rgba(0, 0, 0, 0.9) 0%,
        rgba(0, 0, 0, 0.6) 40%,
        rgba(0, 0, 0, 0) 100%
    );
    z-index: 1;
}

/* Gradient mask - Full cover (when pushing the image entirely to background) */
.gradient-mask--full {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1;
}

/* Text above gradient must have a higher z-index */
.gradient-mask--content {
    position: relative;
    z-index: 2;
    color: #FFFFFF;
}
```

```html
<!-- Gradient mask usage example -->
<div class="card">
    <!-- Background image -->
    <img src="IMAGE_PATH" alt="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">

    <!-- Bottom gradient mask -->
    <div class="gradient-mask--bottom"></div>

    <!-- Text (placed above the gradient) -->
    <div class="gradient-mask--content" style="position: absolute; bottom: 0; left: 0; padding: 72px;">
        <h1 class="title-main" style="color: #fff;">Title text</h1>
        <p class="text-body" style="color: rgba(255,255,255,0.8); margin-top: 20px;">Subtitle text</p>
    </div>
</div>
```

### 4-2. Glassmorphism Card

A frosted glass panel effect over a complex background. Maintains background context while ensuring text readability.

```css
/* Glassmorphism panel - For light backgrounds */
.glass-panel {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 24px;
    padding: 48px;
}

/* Glassmorphism panel - For dark backgrounds */
.glass-panel--dark {
    background: rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 48px;
    color: #FFFFFF;
}

/* Glassmorphism panel - Heavy blur (when there is a lot of text) */
.glass-panel--heavy {
    background: rgba(255, 255, 255, 0.35);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 24px;
    padding: 48px;
}
```

```html
<!-- Glassmorphism usage example -->
<div class="card" style="background: url('IMAGE_PATH') center/cover no-repeat;">
    <div style="display: flex; justify-content: center; align-items: center; width: 100%; height: 100%; padding: 72px;">
        <div class="glass-panel">
            <h2 class="title-sub">Text on glass effect</h2>
            <p class="text-body" style="margin-top: 20px;">Readable body text</p>
        </div>
    </div>
</div>
```

### 4-3. Soft Shadow Presets

Use high transparency (alpha 0.4-0.5) and wide blur spread for an elegant feel.
Heavy, hard shadows are a common cause of an amateurish look.

```css
/* --- Soft shadows for light backgrounds --- */

/* Text soft shadow */
.shadow-text--light {
    text-shadow: 0px 2px 12px rgba(0, 0, 0, 0.08);
}

/* Box soft shadow - Light */
.shadow-box--light-sm {
    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.06);
}

/* Box soft shadow - Medium */
.shadow-box--light-md {
    box-shadow: 0px 8px 32px rgba(0, 0, 0, 0.1);
}

/* Box soft shadow - Strong */
.shadow-box--light-lg {
    box-shadow: 0px 16px 48px rgba(0, 0, 0, 0.12);
}

/* --- Soft shadows for dark backgrounds --- */

/* Text soft shadow (dark background) */
.shadow-text--dark {
    text-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
}

/* Box soft shadow - For dark backgrounds */
.shadow-box--dark-md {
    box-shadow: 0px 8px 32px rgba(0, 0, 0, 0.4);
}

.shadow-box--dark-lg {
    box-shadow: 0px 16px 60px rgba(0, 0, 0, 0.5);
}
```

### 4-4. White Glow Effect (For Dark Backgrounds)

Adds a white halo behind subjects or text on dark backgrounds for an elegant highlight effect.

```css
/* White glow - Applied to images (drop-shadow follows PNG outline) */
.glow-white {
    filter: drop-shadow(0px 0px 30px rgba(255, 255, 255, 0.3));
}

/* White glow - Strong */
.glow-white--strong {
    filter: drop-shadow(0px 0px 50px rgba(255, 255, 255, 0.5));
}

/* White glow - Applied to text */
.glow-white--text {
    text-shadow:
        0px 0px 20px rgba(255, 255, 255, 0.3),
        0px 0px 40px rgba(255, 255, 255, 0.15);
}

/* White glow - Applied to boxes */
.glow-white--box {
    box-shadow:
        0px 0px 30px rgba(255, 255, 255, 0.15),
        0px 0px 60px rgba(255, 255, 255, 0.08);
}

/* Color glow - Glowing effect using the accent color */
.glow-accent {
    filter: drop-shadow(0px 0px 30px var(--accent-color));
}
```

### 4-5. Background Typography Watermark

Place an English keyword at an extremely large size with 5% opacity as a background decoration in empty space.
A trendy technique commonly used on web landing pages.

```css
/* Background typography watermark */
.bg-watermark {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'Paperlogy', sans-serif;
    font-weight: 900;
    font-size: 240px;              /* Extremely large size */
    color: rgba(0, 0, 0, 0.05);   /* 5% opacity - Subtle like a background */
    white-space: nowrap;
    z-index: 0;                    /* Place behind other content */
    pointer-events: none;          /* Pass through click events */
    user-select: none;
    letter-spacing: -0.03em;
    line-height: 1;
}

/* Watermark - For dark backgrounds (white text) */
.bg-watermark--light {
    color: rgba(255, 255, 255, 0.05);
}

/* Watermark - Rotated variant */
.bg-watermark--rotated {
    transform: translate(-50%, -50%) rotate(-15deg);
}

/* Watermark - Top-aligned variant */
.bg-watermark--top {
    top: 15%;
    transform: translate(-50%, -50%);
}
```

```html
<!-- Background typography watermark usage example -->
<div class="card">
    <!-- Watermark (placed at the very back) -->
    <div class="bg-watermark">CONTENTS</div>

    <!-- Actual content -->
    <div class="layout-fullbleed" style="position: relative; z-index: 1;">
        <h1 class="title-main">Table of Contents</h1>
    </div>
</div>
```

### 4-6. Dimming Overlay

An overlay that reduces background image brightness or applies a color tint to ensure text readability.

```css
/* Dimming overlay - Semi-transparent black */
.overlay-dim {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.45);
    z-index: 1;
}

/* Dimming overlay - Heavy (when there is a lot of text) */
.overlay-dim--heavy {
    background: rgba(0, 0, 0, 0.65);
}

/* Dimming overlay - Light (when you want to preserve the image) */
.overlay-dim--light {
    background: rgba(0, 0, 0, 0.25);
}

/* Dimming overlay - Brand color overlay */
.overlay-brand {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--accent-color);
    opacity: 0.75;
    mix-blend-mode: multiply;
    z-index: 1;
}

/* For content above the overlay */
.overlay-content {
    position: relative;
    z-index: 2;
}
```

---

## 5. Card Series Patterns

Card news consists of multiple cards in a series, so consistent patterns for cover/body/closing are needed.

### 5-1. Cover Card (First Card)

An eye-catching first slide. Full-bleed image + gradient + large title combination.
The cover background image can be reused on the ending card for a bookend effect.

```css
/* Cover card layout */
.card-cover {
    position: relative;
    width: 100%;
    height: 100%;
}

/* Cover background image */
.card-cover__bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 0;
}

/* Cover gradient (darkens from bottom to top) */
.card-cover__gradient {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 70%;
    background: linear-gradient(
        to top,
        rgba(0, 0, 0, 0.8) 0%,
        rgba(0, 0, 0, 0.4) 50%,
        rgba(0, 0, 0, 0) 100%
    );
    z-index: 1;
}

/* Cover text area (positioned at bottom) */
.card-cover__content {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 0 var(--pad) 80px var(--pad);
    z-index: 2;
    color: #FFFFFF;
}

/* Cover main title */
.card-cover__title {
    font-weight: 900;
    font-size: 72px;
    line-height: 1.15;
    letter-spacing: -0.05em;
    color: #FFFFFF;
    word-break: keep-all;
}

/* Cover subtitle */
.card-cover__subtitle {
    font-weight: 400;
    font-size: 28px;
    line-height: 1.4;
    color: rgba(255, 255, 255, 0.75);
    margin-top: 24px;
}

/* Cover tag/category label */
.card-cover__tag {
    display: inline-block;
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--accent-color);
    margin-bottom: 20px;
    padding: 6px 16px;
    border: 1px solid var(--accent-color);
    border-radius: 100px;
}
```

```html
<!-- Cover card HTML structure -->
<div class="card">
    <div class="card-cover">
        <!-- Background image -->
        <img class="card-cover__bg" src="IMAGE_PATH" alt="">

        <!-- Gradient -->
        <div class="card-cover__gradient"></div>

        <!-- Corner anchors -->
        <div class="anchor-tl" style="color: rgba(255,255,255,0.6);">BrandName</div>
        <div class="anchor-tr" style="color: rgba(255,255,255,0.6);">01</div>

        <!-- Text -->
        <div class="card-cover__content">
            <div class="card-cover__tag">CATEGORY</div>
            <h1 class="card-cover__title">The key title of<br>the card news goes here</h1>
            <p class="card-cover__subtitle">Write the subtitle or summary here</p>
        </div>
    </div>
</div>
```

### 5-2. Content Card (Body Card)

The middle cards that deliver information. Clean whitespace and typographic hierarchy are key.

```css
/* Content card layout */
.card-content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: var(--pad);
    background: var(--bg-color);
}

/* Content card top area (category + page number) */
.card-content__header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 48px;
}

.card-content__category {
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.03em;
    color: var(--accent-color);
}

.card-content__page {
    font-weight: 300;
    font-size: 18px;
    color: var(--dim-gray);
}

/* Content card body area */
.card-content__body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Content card title */
.card-content__title {
    font-weight: 800;
    font-size: 48px;
    line-height: 1.25;
    letter-spacing: -0.04em;
    color: var(--text-color);
    margin-bottom: 32px;
    word-break: keep-all;
}

/* Content card body text */
.card-content__text {
    font-weight: 400;
    font-size: 26px;
    line-height: 1.7;
    color: var(--secondary-color);
    word-break: keep-all;
}

/* Content card divider */
.card-content__divider {
    width: 60px;
    height: 3px;
    background: var(--accent-color);
    margin-bottom: 32px;
    border: none;
}

/* Content card footer (source, supplementary info) */
.card-content__footer {
    margin-top: auto;
    padding-top: 32px;
    font-weight: 300;
    font-size: 18px;
    color: var(--dim-gray);
}
```

```html
<!-- Content card HTML structure -->
<div class="card">
    <div class="card-content">
        <div class="card-content__header">
            <span class="card-content__category">TOPIC</span>
            <span class="card-content__page">03</span>
        </div>
        <div class="card-content__body">
            <hr class="card-content__divider">
            <h2 class="card-content__title">Write the conclusion as the title</h2>
            <p class="card-content__text">
                <span class="dim">Instead of listing topics,</span>
                <span class="highlight">deliver the key conclusion</span>
                <span class="dim">in a single sentence.</span>
                Professionals never leave the audience to interpret on their own.
            </p>
        </div>
        <div class="card-content__footer">Source: Paperlogy Design Guide</div>
    </div>
</div>
```

### 5-3. Ending Card (Last Card)

An emotional closing instead of "Thank you." Reuse the cover card background for a bookend effect.

```css
/* Ending card layout */
.card-ending {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: var(--pad);
}

/* Ending card - Dark background (cinematic ending) */
.card-ending--dark {
    background: #0A0A0A;
    color: #FFFFFF;
}

/* Ending main message (a single sentence with a quote or vision) */
.card-ending__message {
    font-weight: 300;
    font-size: 40px;
    line-height: 1.6;
    letter-spacing: -0.02em;
    color: rgba(255, 255, 255, 0.9);
    max-width: 800px;
    word-break: keep-all;
}

/* Emphasis within the ending message */
.card-ending__message strong {
    font-weight: 700;
    color: #FFFFFF;
}

/* Quotation mark decoration */
.card-ending__quote-mark {
    font-size: 120px;
    font-weight: 100;
    line-height: 1;
    color: rgba(255, 255, 255, 0.15);
    margin-bottom: -20px;
}

/* Quote attribution (person name, etc.) */
.card-ending__author {
    font-weight: 400;
    font-size: 22px;
    color: rgba(255, 255, 255, 0.5);
    margin-top: 40px;
    letter-spacing: 0.02em;
}

/* Ending bottom brand info */
.card-ending__brand {
    position: absolute;
    bottom: var(--pad-sm);
    left: 50%;
    transform: translateX(-50%);
    font-weight: 300;
    font-size: 18px;
    color: rgba(255, 255, 255, 0.3);
    letter-spacing: 0.1em;
}

/* Ending with reused image background (bookend effect) */
.card-ending--with-bg {
    position: relative;
}

.card-ending--with-bg::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);    /* Dark overlay on top of the cover image */
    z-index: 1;
}

.card-ending--with-bg > * {
    position: relative;
    z-index: 2;
}
```

```html
<!-- Ending card HTML structure (cinematic ending) -->
<div class="card">
    <div class="card-ending card-ending--dark">
        <div class="card-ending__quote-mark">"</div>
        <p class="card-ending__message">
            Good design is as little<br>
            <strong>design as possible</strong>
        </p>
        <p class="card-ending__author">-- Dieter Rams</p>
        <div class="card-ending__brand">BRAND NAME</div>
    </div>
</div>

<!-- Ending card HTML structure (reused cover background - bookend effect) -->
<div class="card">
    <div class="card-ending card-ending--with-bg" style="background: url('COVER_IMAGE_PATH') center/cover no-repeat;">
        <div class="card-ending__quote-mark">"</div>
        <p class="card-ending__message">Closing message</p>
        <div class="card-ending__brand">BRAND NAME</div>
    </div>
</div>
```

### 5-4. Page Number Indicator

Elegant page display. The slash and total page count are grayed out so only the current number stands out.

```css
/* Page number indicator - Default */
.page-indicator {
    font-family: 'Paperlogy', sans-serif;
    font-size: 18px;
    letter-spacing: 0.05em;
}

/* Current page number */
.page-indicator__current {
    font-weight: 600;
    color: var(--text-color);
}

/* Separator and total page count (toned down to gray) */
.page-indicator__total {
    font-weight: 300;
    color: var(--dim-gray);
}

/* Page indicator - Progress bar variant */
.page-progress {
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    background: var(--accent-color);
    z-index: 10;
    /* Set width inline as a percentage: e.g., width: 30% (page 3 of 10) */
}

/* Page indicator - Dot variant */
.page-dots {
    display: flex;
    gap: 8px;
    align-items: center;
}

.page-dots__dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--light-gray);
}

/* Current page dot */
.page-dots__dot--active {
    width: 24px;
    border-radius: 4px;
    background: var(--accent-color);
}
```

```html
<!-- Page number - Numeric style -->
<div class="anchor-tr page-indicator">
    <span class="page-indicator__current">03</span>
    <span class="page-indicator__total"> / 10</span>
</div>

<!-- Page number - Progress bar style (page 3 of 10 = 30%) -->
<div class="page-progress" style="width: 30%;"></div>

<!-- Page number - Dot style -->
<div class="anchor-tr page-dots">
    <div class="page-dots__dot"></div>
    <div class="page-dots__dot"></div>
    <div class="page-dots__dot--active page-dots__dot"></div>
    <div class="page-dots__dot"></div>
    <div class="page-dots__dot"></div>
</div>
```