# Photo Processing Guide

How to choose and combine tools when processing user-provided photographs for card news and promotional materials. This guide covers the judgment behind tool selection -- CLI usage details are in SKILL.md.

---

## 1. Tool Selection -- Four Categories of Work

The four available tools each have a distinct sweet spot. Choosing the wrong tool wastes time or produces inferior results.

### Mechanical Operations → Pillow (process_photo.py)

Use Pillow when the transformation can be described by exact numbers: crop to 4:5 ratio, resize to 1080x1350px, set brightness to 0.7, convert to grayscale. Pillow is deterministic -- the same input and parameters always produce the same output. It's instant and predictable, which makes it ideal for bulk processing and pipeline stages where precision matters.

### Creative Transformations → Nano Banana (generate_image.py --input)

Use Nano Banana when the desired effect is easier to describe in words than in numbers: "apply a cool blue cinematic color grade," "make this look like vintage film," "extend the background naturally." The AI interprets creative intent in ways that would require complex code to replicate (color grading involves LUT tables, film emulation requires grain simulation + color curve manipulation). The tradeoff is non-determinism -- the same prompt may produce slightly different results each time.

### Render-time Effects → CSS Filters

Use CSS filters when the effect should be part of the design layer rather than baked into the image file. CSS filters are reversible (change a line of CSS and reconvert), combinable (chain multiple filters), and adjustable without regenerating the source image. They're ideal for effects that might need fine-tuning during the visual review loop: "the photo is a bit too bright" → adjust `brightness(0.5)` to `brightness(0.4)` and reconvert.

### Background Removal → rembg

Use rembg for one specific task: separating a person or object from its background to create a transparent PNG cutout. This is a specialized ML model purpose-built for segmentation -- don't try to achieve this with CSS or Pillow.

---

## 2. Common Pipelines

Most real tasks require chaining tools in sequence. The order matters.

| Goal | Steps |
|------|-------|
| Photo as full-bleed card background | Pillow (crop 4:5 → resize 1080x1350) then CSS (gradient overlay + brightness/contrast filter) |
| Person floating over designed bg | rembg (remove background) → HTML (position cutout + add white glow drop-shadow) |
| Dramatic B&W editorial card | Pillow (grayscale + contrast 1.4) → CSS (brightness fine-tuning) |
| Vintage or cinematic look | Nano Banana ("apply Kodak Portra style") → Pillow (crop + resize to card dims) |
| Multi-photo mood board | Pillow (crop each photo → composite collage) → CSS (overall tint filter on the composite) |
| Cinematic hero with cutout | Nano Banana (color grade the photo) → Pillow (crop + resize) → rembg (if cutout needed) |

**Why this order matters:** Pillow handles geometry first (crop/resize ensures correct dimensions), then Nano Banana applies creative effects (color grading on the right-shaped canvas), then rembg removes backgrounds (on the already-graded image so the cutout carries the intended color treatment). CSS filters come last because they're applied at render time.

---

## 3. CSS Filter Recipes

These are tested filter combinations for common card news photo treatments. The values are calibrated -- small changes in order or magnitude produce noticeably different results.

### Blue Tint (Political, Corporate, Authoritative)
```css
filter: saturate(0.3) brightness(0.6) contrast(1.4) sepia(1) hue-rotate(180deg);
```
The chain works by: desaturating heavily → darkening → boosting contrast → applying sepia (shifts to brown) → rotating hue 180 degrees (brown becomes blue). The result is a cold, high-contrast image that conveys authority. Lighten with `brightness(0.75)` and `saturate(0.4)` for a softer variant.

### Dramatic Dark (Moody, Intense)
```css
filter: brightness(0.4) contrast(1.6) saturate(0.6);
```
Aggressive darkening with boosted contrast creates deep blacks and bright highlights. Desaturation keeps colors from looking garish in the high-contrast treatment. Ideal under bold white text.

### Warm Vintage (Nostalgic, Relaxed)
```css
filter: sepia(0.4) saturate(1.3) brightness(1.05) contrast(1.1) hue-rotate(-10deg);
```
Light sepia adds warmth, boosted saturation makes colors richer despite the sepia wash, slight brightness lift prevents muddiness, negative hue rotation pushes further toward warm amber.

### High-Contrast B&W (Editorial, Documentary)
```css
filter: grayscale(1) contrast(1.4) brightness(1.05);
```
Full grayscale conversion, then contrast boost for punchy blacks and whites. The slight brightness lift prevents the image from feeling too dark after the contrast increase.

### Cool Professional (Business, Tech)
```css
filter: saturate(0.8) brightness(1.05) contrast(1.1) hue-rotate(10deg);
```
Subtle desaturation tames distracting colors, slight brightness and contrast lifts add clarity, small hue rotation toward blue imparts a cool, modern tone.

### Faded Film (Instagram-like, Casual)
```css
filter: sepia(0.3) saturate(1.4) contrast(0.9) brightness(1.1);
```
Light sepia + boosted saturation creates the signature "faded but colorful" look. Reduced contrast softens the image, and brightness lift prevents it from feeling dim.

---

## 4. Nano Banana Photo Editing Tips

When using `generate_image.py --input` for creative photo edits, the quality of the result depends heavily on how you communicate with the model.

### Be Specific About What to Keep

The most common failure is unintended changes to parts of the image you wanted preserved. Always include preservation instructions: "Keep the composition identical," "Preserve all details and facial features," "Do not alter the subject's position or expression."

### Use Real-World References

Film stocks, movies, and time-of-day references are highly effective because the model understands these visual vocabularies:
- "Kodak Portra 400 warmth" → specific film grain + warm color cast
- "Golden hour lighting" → warm amber light from a low angle
- "Blade Runner color palette" → teal shadows, orange highlights, high contrast
- "Wes Anderson aesthetic" → pastel symmetry, deliberate framing

### State the Intensity

Without intensity guidance, the model defaults to moderate changes that may feel underwhelming. Use explicit intensity markers: "subtle" (barely noticeable), "moderate" (clearly visible but natural), "strong" (dramatic transformation), "extreme" (stylized, potentially unrealistic).

### Outpainting for Card Dimensions

When a portrait photo needs to fill a 4:5 card, use Nano Banana to extend the background naturally rather than stretching or adding black bars. Set `--aspect-ratio 4:5` and prompt: "Extend the background naturally in all directions. Continue the existing environment seamlessly. Keep the main subject exactly as is."

---

## 5. Collage Composition Principles

When building multi-photo compositions with `process_photo.py --composite`:

### Pre-crop Before Compositing

Always crop photos to their target cell ratios *before* placing them in the collage. The composite command can resize images, but it doesn't crop -- placing an uncropped landscape photo into a portrait cell will stretch it. Crop first with `--crop`, then let the composite resize to exact cell dimensions.

### Common Collage Patterns

- **2x2 Grid:** Four equal cells with 8px gaps (536 + 8 + 536 = 1080). The most balanced layout for showing multiple aspects of a topic
- **Featured + Supporting:** One large photo (full width, top 65%) with two smaller photos below (half width each). Creates clear visual hierarchy
- **Layered Stack:** Multiple photos stacked with decreasing opacity (back: 0.3, mid: 0.6, front: 1.0). Creates depth effect
- **Before/After Split:** Two photos side by side. Make the "before" grayscale and the "after" full color for immediate visual contrast

### Per-Layer Grayscale for Emphasis

To highlight one photo in a grid, set all other layers to `"grayscale": true` with reduced opacity (0.6). The single color photo becomes the unmistakable focal point -- the same "emphasis by reduction" principle from typography applied to photographs.

### Diagonal Splits

True diagonal compositions (photos meeting at an angle) are better achieved with CSS `clip-path` in the HTML card rather than Pillow compositing. Pillow can't do non-rectangular masks, but CSS `clip-path: polygon(...)` can create any shape.

---

## 6. Pillow Adjustment Presets

Tested brightness/contrast/saturation combinations for common card news effects. Factor 1.0 = no change.

| Effect | Brightness | Contrast | Saturation | When to use |
|--------|-----------|----------|------------|-------------|
| Darken for text overlay | 0.6 | 1.1 | 0.8 | Background photo under white text -- dark enough to read, subtle contrast lift |
| High-impact editorial | 1.0 | 1.5 | 0.4 | Bold, desaturated magazine look -- colors become muted accents |
| Soft pastel | 1.2 | 0.9 | 0.6 | Light, airy feel -- lifted brightness, softened contrast |
| Vivid pop | 1.1 | 1.2 | 1.5 | Bright, energetic social media -- boosted everything |
| Dramatic dark | 0.5 | 1.6 | 0.3 | Intense, cinematic -- crushed blacks, minimal color |
| Faded film | 1.1 | 0.8 | 0.7 | Nostalgic, relaxed -- reduced contrast lifts the blacks |

**When to use Pillow presets vs CSS filters vs Nano Banana:** Pillow presets produce a permanent file change -- use them when the adjustment is a known, fixed step in the pipeline (e.g., always darken backgrounds to 0.6). CSS filters are better when you might need to tweak during the visual review loop. Nano Banana is for creative effects that can't be achieved with numeric adjustments alone.

**Review diagnostic:** If a photo-based card's mood feels wrong, first try adjusting the CSS filter values (fastest iteration). If the needed change is more creative (color grading, style transfer), use Nano Banana edit mode. Resort to Pillow only for precise numeric adjustments that CSS filters can't express (e.g., exact saturation value).
