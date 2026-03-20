# Photo Processing Guide for Card News

A comprehensive reference for processing user-provided photographs in card news and promotional materials. Covers tool selection, Pillow operations, AI-powered creative edits, CSS filters, HTML integration patterns, and multi-photo collage composition.

All scripts referenced below live in `<skill_dir>/scripts/`. Always activate the virtual environment before running any script:

```bash
source <skill_dir>/scripts/.venv/bin/activate
```

---

## 1. Tool Decision Criteria

Four tools are available for photo processing. Each has a distinct sweet spot. Choosing the wrong tool wastes time or produces inferior results.

### Quick-Reference Decision Table

| "I want to..." | Use this tool | Why |
|---|---|---|
| Crop a photo to 4:5 card ratio | **Pillow** (`process_photo.py --crop`) | Deterministic geometry operation |
| Resize to 1080x1350 | **Pillow** (`process_photo.py --resize`) | Exact pixel dimensions needed |
| Convert to black-and-white | **Pillow** (`process_photo.py --grayscale`) | Simple color-space conversion |
| Increase/decrease brightness | **Pillow** (`process_photo.py --brightness`) | Precise numeric control (e.g., 1.3x) |
| Increase/decrease contrast | **Pillow** (`process_photo.py --contrast`) | Precise numeric control |
| Increase/decrease saturation | **Pillow** (`process_photo.py --saturation`) | Precise numeric control |
| Build a multi-photo collage | **Pillow** (`process_photo.py --composite`) | Layout defined by coordinates in JSON |
| Process 10 photos identically | **Pillow** (`process_photo.py --batch`) | Parallel mechanical processing |
| Apply a cinematic color grade | **Nano Banana** (`generate_image.py --input`) | Creative, hard-to-code transformation |
| Make a photo look like vintage film | **Nano Banana** (`generate_image.py --input`) | Style transfer via natural language |
| Change the mood/atmosphere | **Nano Banana** (`generate_image.py --input`) | Subjective, AI excels at interpretation |
| Extend the background (outpainting) | **Nano Banana** (`generate_image.py --input`) | Generative content creation |
| Remove or add elements | **Nano Banana** (`generate_image.py --input`) | Content-aware generation |
| Apply a live tint on an HTML card | **CSS filters** | Effect is part of the design layer, reversible |
| Grayscale only in the browser | **CSS filters** (`filter: grayscale(1)`) | No need to produce a new file |
| Add a warm/cool tone at render time | **CSS filters** (`filter: sepia() hue-rotate()`) | Combinable with other CSS effects |
| Blur a background photo behind text | **CSS filters** (`filter: blur()`) | Applied dynamically, original file untouched |
| Remove the background from a person | **rembg** | Dedicated ML model for segmentation |
| Create a transparent cutout | **rembg** | Outputs PNG with alpha channel |

### Decision Flowchart

```
Is the desired effect mechanical and precisely specified?
  |
  +-- YES --> Can it be described by exact numbers (pixels, ratios, factors)?
  |             |
  |             +-- YES --> Use Pillow (process_photo.py)
  |             +-- NO  --> Use Nano Banana (generate_image.py --input)
  |
  +-- NO  --> Is the effect creative / subjective / easier to describe in words?
                |
                +-- YES --> Use Nano Banana (generate_image.py --input)
                +-- NO  --> Should the effect be part of the HTML/CSS layer?
                              |
                              +-- YES --> Use CSS filters
                              +-- NO  --> Do you need background removal?
                                            |
                                            +-- YES --> Use rembg
                                            +-- NO  --> Re-evaluate requirements
```

### When to Combine Tools (Pipeline Patterns)

Many real tasks require chaining tools in sequence:

| Pipeline | Steps |
|---|---|
| Photo as full-bleed card background | Pillow (crop 4:5 + resize 1080x1350) then CSS (gradient overlay + brightness) |
| Person floating over colored bg | rembg (remove background) then HTML (place cutout with CSS positioning) |
| Dramatic B&W editorial card | Pillow (grayscale + contrast 1.4) then CSS (brightness filter for fine-tuning) |
| Vintage film look | Nano Banana (apply vintage film style) then Pillow (resize to card dimensions) |
| Multi-photo mood board | Pillow (composite collage) then CSS (overall tint filter on the composite) |
| Cinematic hero photo | Nano Banana (color grade) then Pillow (crop 4:5 + resize) then rembg if cutout needed |

---

## 2. Pillow Operations for Card News

### 2.1 Smart Crop to Card Ratio (4:5)

Centers the crop on the image. Wider-than-target images lose sides; taller-than-target images lose top/bottom.

```bash
python <skill_dir>/scripts/process_photo.py \
  --crop 4:5 \
  --input ./photos/user_photo.jpg \
  --output ./images/photo_cropped.png
```

Other useful ratios:
- `1:1` -- square (icon, profile)
- `16:9` -- wide banner
- `3:2` -- classic landscape
- `2:3` -- tall portrait
- `9:16` -- story format

### 2.2 Resize to Card Dimensions

After cropping to the correct ratio, resize to the exact card pixel dimensions.

```bash
python <skill_dir>/scripts/process_photo.py \
  --resize 1080x1350 \
  --input ./images/photo_cropped.png \
  --output ./images/photo_ready.png
```

Common target dimensions:
- `1080x1350` -- full card (4:5)
- `1080x675` -- top or bottom half of a card
- `1080x1080` -- square card
- `540x675` -- half-width panel (for side-by-side layouts)

**Crop + resize pipeline** (two sequential commands):

```bash
python <skill_dir>/scripts/process_photo.py \
  --crop 4:5 --input photo.jpg --output temp_crop.png

python <skill_dir>/scripts/process_photo.py \
  --resize 1080x1350 --input temp_crop.png --output photo_final.png
```

### 2.3 Grayscale Conversion

Converts to luminance (L mode) then back to RGB so the file remains 3-channel and compatible with HTML `<img>` tags.

```bash
python <skill_dir>/scripts/process_photo.py \
  --grayscale \
  --input ./photos/user_photo.jpg \
  --output ./images/photo_bw.png
```

The underlying Pillow operation uses the ITU-R 601-2 luma formula:

```
L = R * 299/1000 + G * 587/1000 + B * 114/1000
```

### 2.4 Brightness, Contrast, and Saturation Adjustment

Factors are floating-point multipliers where 1.0 means "no change".

| Factor | Effect |
|---|---|
| 0.0 | Minimum (black for brightness, gray for contrast, grayscale for saturation) |
| 0.5 | Halved |
| 1.0 | Original (no change) |
| 1.3 | Moderately increased |
| 1.5 | Noticeably increased |
| 2.0 | Doubled |

**Brightness only:**

```bash
python <skill_dir>/scripts/process_photo.py \
  --brightness 0.7 \
  --input photo.jpg --output photo_dark.png
```

**Contrast only:**

```bash
python <skill_dir>/scripts/process_photo.py \
  --contrast 1.4 \
  --input photo.jpg --output photo_punchy.png
```

**Saturation only:**

```bash
python <skill_dir>/scripts/process_photo.py \
  --saturation 0.3 \
  --input photo.jpg --output photo_desaturated.png
```

**Combined adjustments** (all three at once):

```bash
python <skill_dir>/scripts/process_photo.py \
  --brightness 0.8 --contrast 1.3 --saturation 0.5 \
  --input photo.jpg --output photo_moody.png
```

#### Recommended Presets for Card News

| Effect | Brightness | Contrast | Saturation | Use case |
|---|---|---|---|---|
| Darken for text overlay | 0.6 | 1.1 | 0.8 | Background photo under white text |
| High-impact editorial | 1.0 | 1.5 | 0.4 | Bold, desaturated magazine look |
| Soft pastel | 1.2 | 0.9 | 0.6 | Light, airy, feminine feel |
| Vivid pop | 1.1 | 1.2 | 1.5 | Bright, energetic social media |
| Dramatic dark | 0.5 | 1.6 | 0.3 | Intense, moody, cinematic |
| Faded film | 1.1 | 0.8 | 0.7 | Nostalgic, relaxed look |

### 2.5 Multi-Photo Composite (Collage)

Uses a layout JSON file to layer multiple images onto a single canvas.

```bash
python <skill_dir>/scripts/process_photo.py \
  --composite layout.json \
  --output ./images/collage.png
```

See Section 6 for complete layout JSON documentation and examples.

### 2.6 Batch Processing

Process multiple photos in parallel with a single command.

**batch.json:**

```json
[
  {"action": "crop", "input": "photo1.jpg", "output": "photo1_crop.png", "ratio": "4:5"},
  {"action": "crop", "input": "photo2.jpg", "output": "photo2_crop.png", "ratio": "4:5"},
  {"action": "resize", "input": "photo1_crop.png", "output": "photo1_final.png", "dimensions": "1080x1350"},
  {"action": "resize", "input": "photo2_crop.png", "output": "photo2_final.png", "dimensions": "1080x1350"},
  {"action": "grayscale", "input": "photo3.jpg", "output": "photo3_bw.png"},
  {"action": "adjust", "input": "photo4.jpg", "output": "photo4_dark.png", "brightness": 0.6, "contrast": 1.3, "saturation": 0.5}
]
```

```bash
python <skill_dir>/scripts/process_photo.py --batch batch.json
```

Batch mode uses a thread pool (max 4 workers) for parallel execution. Note that the jobs within a single batch run concurrently, so jobs that depend on the output of other jobs (e.g., crop then resize) must be in separate batch files or run sequentially as individual commands.

**Two-pass batch pattern** (crop first, then resize):

```bash
# Pass 1: crop all photos
python <skill_dir>/scripts/process_photo.py --batch batch_crop.json

# Pass 2: resize all cropped photos
python <skill_dir>/scripts/process_photo.py --batch batch_resize.json
```

---

## 3. Nano Banana Photo Editing

`generate_image.py --input` sends the photo to the Gemini model along with a text instruction. The AI interprets the instruction creatively, producing a new image. This is ideal when the desired transformation is easier to describe in words than to code.

### 3.1 Basic Usage

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "INSTRUCTION HERE" \
  --input ./photos/original.jpg \
  --output ./images/edited.png
```

The `--aspect-ratio` flag controls the output dimensions. Use `4:5` for card backgrounds, `1:1` for square crops, `16:9` for banners.

### 3.2 Color Grading

Apply color corrections and grading that would require complex LUT operations in code.

**Cool blue cinematic:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Apply a cool blue cinematic color grade. Shift shadows toward deep teal, keep highlights slightly warm. Increase contrast slightly. Preserve all details and composition." \
  --input photo.jpg --output photo_blue_cinema.png
```

**Warm golden hour:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Apply a warm golden hour color grade. Bathe the scene in soft amber light as if shot during sunset. Warm highlights, slightly orange midtones, deep warm shadows. Keep the image natural, not over-processed." \
  --input photo.jpg --output photo_golden.png
```

**High-contrast teal and orange:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Apply a teal-and-orange color grade popular in Hollywood films. Push shadows toward teal/cyan, push highlights and skin tones toward warm orange. Strong contrast. Cinematic feel." \
  --input photo.jpg --output photo_teal_orange.png
```

**Muted pastel:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Apply a muted pastel color grade. Reduce saturation to about 40%, lift the blacks so shadows are not pure black, shift overall tone toward soft lavender-gray. Airy, editorial magazine feel." \
  --input photo.jpg --output photo_pastel.png
```

### 3.3 Style Transfer

Transform the visual style of a photo while preserving its content.

**Vintage film photograph:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Make this photo look like it was shot on Kodak Portra 400 film. Add subtle film grain, slightly faded blacks, warm color cast, gentle halation around highlights. Keep the composition and content identical." \
  --input photo.jpg --output photo_film.png
```

**Magazine editorial:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Transform this photo into a high-end fashion magazine editorial style. Sharp details, slightly desaturated colors, strong directional lighting feel, crisp contrast. Professional retouched look." \
  --input photo.jpg --output photo_editorial.png
```

**Polaroid / instant photo:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Make this look like an old Polaroid instant photograph. Slightly washed-out colors, soft warm tint, reduced contrast, subtle light leak in one corner. Nostalgic feeling." \
  --input photo.jpg --output photo_polaroid.png
```

### 3.4 Mood Change

Alter the emotional atmosphere of a photo.

**Dramatic and intense:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Make this photo more dramatic and intense. Deepen the shadows, increase contrast, add slight vignette around the edges, make colors richer and more saturated. Epic, powerful feeling." \
  --input photo.jpg --output photo_dramatic.png
```

**Calm and serene:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Make this photo feel calm and serene. Soften the light, reduce contrast slightly, add a gentle cool blue undertone, make everything feel quiet and peaceful." \
  --input photo.jpg --output photo_serene.png
```

**Dark and moody:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Make this photo dark and moody. Heavily darken the image, crush the blacks, leave only key highlights visible, add a subtle blue-gray color cast. Noir thriller feeling." \
  --input photo.jpg --output photo_noir.png
```

### 3.5 Background Extension (Outpainting)

Extend the photo beyond its original boundaries. Useful when a portrait photo needs to fill a wider or taller card layout.

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Extend the background naturally in all directions. Continue the existing environment seamlessly. Keep the main subject exactly as is. The extended areas should look like they were always part of the original photo." \
  --input photo.jpg \
  --aspect-ratio 4:5 \
  --output photo_extended.png
```

### 3.6 Element Removal / Addition

**Remove an object:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Remove the [describe object and its location] from the image. Fill the area naturally with the surrounding background. Keep everything else identical." \
  --input photo.jpg --output photo_cleaned.png
```

**Add an element:**

```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Add [describe element] to the [describe location in the image]. Make it look natural and consistent with the existing lighting and style." \
  --input photo.jpg --output photo_augmented.png
```

### 3.7 Prompt Writing Tips for Photo Editing

1. **Be specific about what to preserve**: Always include phrases like "keep the composition identical", "preserve all details", "do not change the subject".
2. **Describe the target, not the process**: Say "the shadows should be teal" rather than "shift the blue channel in the shadows".
3. **Reference real-world analogies**: Film stocks (Portra, Ektar), movies (Blade Runner look), time of day (golden hour, blue hour) are all effective descriptors.
4. **State intensity**: "subtle", "moderate", "strong", "extreme" help the model calibrate.
5. **Mention what NOT to do**: "Do not over-saturate", "Do not add artificial lens flare" can prevent unwanted side effects.

### 3.8 Batch Mode for Multiple Photo Edits

```json
[
  {
    "prompt": "Apply cool blue cinematic color grade. Preserve all details.",
    "input": "./photos/photo1.jpg",
    "output": "./images/photo1_graded.png",
    "aspect_ratio": "4:5"
  },
  {
    "prompt": "Apply cool blue cinematic color grade. Preserve all details.",
    "input": "./photos/photo2.jpg",
    "output": "./images/photo2_graded.png",
    "aspect_ratio": "4:5"
  }
]
```

```bash
python <skill_dir>/scripts/generate_image.py --batch photo_edits.json
```

---

## 4. CSS Filter Recipes

CSS filters are applied at render time in the HTML card. They do not modify the source image file. This makes them ideal for effects that should be part of the design system -- reversible, combinable, and adjustable without regenerating images.

### Syntax Reference

```css
filter: <function1>(<value>) <function2>(<value>) ...;
```

Available functions: `grayscale()`, `brightness()`, `contrast()`, `saturate()`, `sepia()`, `hue-rotate()`, `blur()`, `invert()`, `opacity()`, `drop-shadow()`.

### 4.1 Blue Tint (Political Poster / Corporate)

Creates a cold, authoritative blue tone often seen in political campaign materials and corporate presentations.

```css
.photo-blue-tint {
    filter: saturate(0.3) brightness(0.6) contrast(1.4) sepia(1) hue-rotate(180deg);
}
```

Breakdown: desaturate heavily, darken, boost contrast, apply sepia (shifts to brown), then rotate hue 180 degrees (brown becomes blue).

**Variant -- lighter blue tint:**

```css
.photo-blue-tint-light {
    filter: saturate(0.4) brightness(0.75) contrast(1.2) sepia(0.8) hue-rotate(180deg);
}
```

### 4.2 Grayscale (Black and White)

Clean black-and-white conversion for editorial and documentary aesthetics.

```css
/* Full grayscale */
.photo-grayscale {
    filter: grayscale(1);
}

/* High-contrast B&W (punchy editorial) */
.photo-grayscale-contrast {
    filter: grayscale(1) contrast(1.4) brightness(1.05);
}

/* Faded B&W (soft, nostalgic) */
.photo-grayscale-faded {
    filter: grayscale(1) contrast(0.85) brightness(1.15);
}
```

### 4.3 Dramatic Dark (High Contrast + Low Brightness)

Intense, moody look for cards with bold white text overlaid on photos.

```css
.photo-dramatic-dark {
    filter: brightness(0.4) contrast(1.6) saturate(0.6);
}
```

**Variant -- dramatic dark with blue shift:**

```css
.photo-dramatic-dark-blue {
    filter: brightness(0.35) contrast(1.5) saturate(0.4) sepia(0.3) hue-rotate(180deg);
}
```

### 4.4 Warm Vintage

Nostalgic, film-like warmth reminiscent of 1970s photography.

```css
.photo-warm-vintage {
    filter: sepia(0.4) saturate(1.3) brightness(1.05) contrast(1.1) hue-rotate(-10deg);
}
```

**Variant -- heavy vintage (polaroid-like):**

```css
.photo-heavy-vintage {
    filter: sepia(0.6) saturate(1.1) brightness(1.1) contrast(0.9);
}
```

### 4.5 Cool Professional

Clean, slightly cool tone for business and tech content. Projects competence and modernity.

```css
.photo-cool-professional {
    filter: saturate(0.8) brightness(1.05) contrast(1.1) hue-rotate(10deg);
}
```

**Variant -- steel gray (desaturated cool):**

```css
.photo-steel-gray {
    filter: saturate(0.3) brightness(0.9) contrast(1.2) hue-rotate(15deg);
}
```

### 4.6 Sepia / Retro

Classic sepia tone for historical or retro themed content.

```css
/* Standard sepia */
.photo-sepia {
    filter: sepia(0.8) contrast(1.1) brightness(1.05);
}

/* Sepia with slight warmth */
.photo-sepia-warm {
    filter: sepia(0.7) saturate(1.2) contrast(1.1) brightness(1.0) hue-rotate(-5deg);
}

/* Faded retro (Instagram-like) */
.photo-faded-retro {
    filter: sepia(0.3) saturate(1.4) contrast(0.9) brightness(1.1);
}
```

### 4.7 Additional Useful Recipes

**Soft dreamy glow** (pair with a blurred duplicate behind the sharp image):

```css
.photo-dreamy {
    filter: brightness(1.1) contrast(0.95) saturate(1.2) blur(0.5px);
}
```

**Duotone effect** (combine with CSS `mix-blend-mode`):

```css
.photo-duotone-container {
    position: relative;
    background: #1a3a5c; /* Dark tone color */
}

.photo-duotone-container img {
    filter: grayscale(1) contrast(1.2);
    mix-blend-mode: multiply;
    opacity: 0.85;
}

.photo-duotone-container::after {
    content: '';
    position: absolute;
    inset: 0;
    background: #3a7bde; /* Light tone color */
    mix-blend-mode: lighten;
}
```

**Vignette effect** (CSS only, no filter needed):

```css
.photo-vignette {
    position: relative;
}

.photo-vignette::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.6) 100%);
    pointer-events: none;
}
```

### 4.8 Combining CSS Filters with Overlay Gradients

For card backgrounds, CSS filters are often paired with gradient overlays to ensure text readability.

```css
.card-bg-photo {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.5) contrast(1.2) saturate(0.7);
}

.card-bg-gradient {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        rgba(0,0,0,0.3) 0%,
        rgba(0,0,0,0.0) 40%,
        rgba(0,0,0,0.0) 60%,
        rgba(0,0,0,0.7) 100%
    );
    z-index: 1;
}

.card-text {
    position: relative;
    z-index: 2;
}
```

---

## 5. Photo Integration Patterns

These are HTML/CSS patterns for placing photos within card news layouts. Each pattern includes the full markup structure.

### 5.1 Full-Bleed Background Photo + Gradient Overlay + Text

The photo fills the entire card. A gradient ensures text is readable. This is the most common cover card pattern.

```html
<div class="card" style="position: relative; width: 1080px; height: 1350px; overflow: hidden;">

    <!-- Background photo -->
    <img src="./images/photo_bg.png"
         style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
                filter: brightness(0.55) contrast(1.2) saturate(0.8);" />

    <!-- Gradient overlay (dark at bottom for text) -->
    <div style="position: absolute; inset: 0;
                background: linear-gradient(to bottom,
                    rgba(0,0,0,0.1) 0%,
                    rgba(0,0,0,0.0) 30%,
                    rgba(0,0,0,0.5) 70%,
                    rgba(0,0,0,0.85) 100%);
                z-index: 1;"></div>

    <!-- Text content -->
    <div style="position: absolute; bottom: 80px; left: 60px; right: 60px; z-index: 2;">
        <p style="font-size: 20px; font-weight: 300; color: rgba(255,255,255,0.7);
                  margin-bottom: 16px; letter-spacing: 0.1em; text-transform: uppercase;">
            Category Label
        </p>
        <h1 style="font-size: 72px; font-weight: 900; color: #FFFFFF;
                   line-height: 1.15; letter-spacing: -0.04em; word-break: keep-all;">
            Main Title Goes Here
        </h1>
        <p style="font-size: 26px; font-weight: 400; color: rgba(255,255,255,0.8);
                  margin-top: 24px; line-height: 1.5;">
            Supporting description text for context.
        </p>
    </div>

</div>
```

**Variant -- gradient from left:**

Use `linear-gradient(to right, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 50%, transparent 100%)` when text is positioned on the left side.

**Variant -- radial spotlight:**

```css
background: radial-gradient(ellipse at 30% 70%, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 60%, transparent 100%);
```

### 5.2 Photo in Lower Half + Text in Upper Half

A clean split layout. The upper portion contains the title and body text on a solid or gradient background; the lower portion features the photo.

```html
<div class="card" style="position: relative; width: 1080px; height: 1350px; overflow: hidden;
                         background: #0A1628;">

    <!-- Upper half: text -->
    <div style="position: absolute; top: 0; left: 0; right: 0; height: 650px;
                padding: 60px; display: flex; flex-direction: column; justify-content: center;">
        <p style="font-size: 18px; font-weight: 300; color: rgba(255,255,255,0.5);
                  letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 24px;">
            Section Label
        </p>
        <h2 style="font-size: 56px; font-weight: 800; color: #FFFFFF;
                   line-height: 1.2; letter-spacing: -0.04em; word-break: keep-all;">
            The Title Statement
        </h2>
        <p style="font-size: 24px; font-weight: 400; color: rgba(255,255,255,0.7);
                  margin-top: 28px; line-height: 1.6;">
            Body text explaining the key point. Keep it concise.
        </p>
    </div>

    <!-- Lower half: photo -->
    <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 700px; overflow: hidden;">
        <img src="./images/photo_lower.png"
             style="width: 100%; height: 100%; object-fit: cover;" />
        <!-- Fade top edge into the background color -->
        <div style="position: absolute; top: 0; left: 0; right: 0; height: 120px;
                    background: linear-gradient(to bottom, #0A1628 0%, transparent 100%);"></div>
    </div>

</div>
```

**Variant -- photo on top, text on bottom:** Swap the positions and change the gradient direction to `linear-gradient(to top, ...)`.

### 5.3 Person Cutout (rembg) Floating Over Colored Background

Use `rembg` to remove the background first, then position the cutout over a designed background. This creates a dynamic, editorial look.

**Step 1 -- Remove background:**

```bash
rembg i ./photos/person.jpg ./images/person_cutout.png
```

**Step 2 -- HTML layout:**

```html
<div class="card" style="position: relative; width: 1080px; height: 1350px; overflow: hidden;
                         background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">

    <!-- Decorative glow behind the person -->
    <div style="position: absolute; top: 200px; left: 50%; transform: translateX(-50%);
                width: 700px; height: 700px; border-radius: 50%;
                background: radial-gradient(circle, rgba(58,123,222,0.25) 0%, transparent 70%);
                z-index: 1;"></div>

    <!-- Person cutout -->
    <img src="./images/person_cutout.png"
         style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%);
                height: 1000px; width: auto; object-fit: contain;
                filter: drop-shadow(0 0 40px rgba(255,255,255,0.15));
                z-index: 2;" />

    <!-- Text overlay (in front of cutout or behind, depending on z-index) -->
    <div style="position: absolute; top: 60px; left: 60px; right: 60px; z-index: 3;">
        <h1 style="font-size: 64px; font-weight: 900; color: #FFFFFF;
                   line-height: 1.2; letter-spacing: -0.04em;">
            Person Name or Title
        </h1>
        <p style="font-size: 28px; font-weight: 400; color: rgba(255,255,255,0.7);
                  margin-top: 16px;">
            Role or subtitle text
        </p>
    </div>

</div>
```

Key techniques:
- `filter: drop-shadow(0 0 40px rgba(255,255,255,0.15))` adds a soft glow around the cutout edges on dark backgrounds.
- A `radial-gradient` circle behind the person creates depth.
- Z-index layering: background (z:1) < person (z:2) < text (z:3), or place text at z:1 to have the person overlap it.

### 5.4 Multi-Photo Collage as Background

First, build the collage with `process_photo.py --composite`, then use it as a card background.

**Step 1 -- Build collage** (see Section 6 for layout details):

```bash
python <skill_dir>/scripts/process_photo.py \
  --composite collage_layout.json \
  --output ./images/collage_bg.png
```

**Step 2 -- Use in HTML:**

```html
<div class="card" style="position: relative; width: 1080px; height: 1350px; overflow: hidden;">

    <!-- Collage as background -->
    <img src="./images/collage_bg.png"
         style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
                filter: brightness(0.4) contrast(1.1) saturate(0.5);" />

    <!-- Dark overlay for readability -->
    <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.5); z-index: 1;"></div>

    <!-- Glassmorphism panel -->
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                width: 800px; padding: 60px;
                background: rgba(255,255,255,0.08);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255,255,255,0.12);
                border-radius: 24px;
                z-index: 2;">
        <h2 style="font-size: 48px; font-weight: 800; color: #FFFFFF;
                   text-align: center; letter-spacing: -0.03em;">
            Summary Title
        </h2>
        <p style="font-size: 24px; font-weight: 400; color: rgba(255,255,255,0.8);
                  text-align: center; margin-top: 24px; line-height: 1.6;">
            Summary content or key takeaway.
        </p>
    </div>

</div>
```

### 5.5 Photo Inside a Shaped Container

Place a photo within a circle, rounded rectangle, or custom shape using CSS `clip-path` or `border-radius`.

**Circle:**

```html
<div style="width: 500px; height: 500px; border-radius: 50%; overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            margin: 0 auto;">
    <img src="./images/photo.png"
         style="width: 100%; height: 100%; object-fit: cover;" />
</div>
```

**Rounded rectangle:**

```html
<div style="width: 700px; height: 500px; border-radius: 32px; overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.25);">
    <img src="./images/photo.png"
         style="width: 100%; height: 100%; object-fit: cover;" />
</div>
```

**Hexagonal clip-path:**

```html
<div style="width: 500px; height: 500px;
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            overflow: hidden;">
    <img src="./images/photo.png"
         style="width: 100%; height: 100%; object-fit: cover;" />
</div>
```

**Diagonal cut:**

```html
<div style="width: 1080px; height: 700px;
            clip-path: polygon(0 0, 100% 0, 100% 80%, 0 100%);
            overflow: hidden;">
    <img src="./images/photo.png"
         style="width: 100%; height: 100%; object-fit: cover;" />
</div>
```

**Photo with border/frame effect:**

```html
<div style="padding: 8px; background: linear-gradient(135deg, #3a7bde, #e040fb);
            border-radius: 24px; display: inline-block;">
    <div style="width: 600px; height: 400px; border-radius: 16px; overflow: hidden;">
        <img src="./images/photo.png"
             style="width: 100%; height: 100%; object-fit: cover;" />
    </div>
</div>
```

---

## 6. Collage Composition

Build multi-photo compositions using `process_photo.py --composite`. This is a Pillow-based operation that layers multiple images onto a single canvas according to a JSON layout specification.

### 6.1 Layout JSON Format

```json
{
    "canvas": {
        "width": 1080,
        "height": 1350,
        "bg": "#000000"
    },
    "layers": [
        {
            "image": "path/to/photo.png",
            "x": 0,
            "y": 0,
            "width": 1080,
            "height": 675,
            "opacity": 1.0,
            "grayscale": false
        }
    ]
}
```

**Canvas properties:**

| Property | Type | Required | Description |
|---|---|---|---|
| `width` | int | Yes | Canvas width in pixels |
| `height` | int | Yes | Canvas height in pixels |
| `bg` | string | No | Background color (hex). Default: `"#000000"` |

**Layer properties:**

| Property | Type | Required | Description |
|---|---|---|---|
| `image` | string | Yes | Path to the image file |
| `x` | int | No | Horizontal position (left edge). Default: 0 |
| `y` | int | No | Vertical position (top edge). Default: 0 |
| `width` | int | No | Resize to this width. If only width given, height scales proportionally |
| `height` | int | No | Resize to this height. If only height given, width scales proportionally |
| `opacity` | float | No | Layer opacity (0.0 = fully transparent, 1.0 = fully opaque). Default: 1.0 |
| `grayscale` | bool | No | Convert this layer to grayscale. Default: false |

**Sizing behavior:**
- Both `width` and `height` specified: image is resized to exact dimensions (may distort).
- Only `width` specified: height scales proportionally.
- Only `height` specified: width scales proportionally.
- Neither specified: image is placed at its original size.

**Layer order:** Layers are rendered from first to last (index 0 is bottommost, last index is topmost). Use this for overlapping compositions.

### 6.2 Common Collage Patterns

#### 2x2 Grid

Four equal-sized photos in a grid. Suitable for showing multiple aspects of a topic.

```json
{
    "canvas": {"width": 1080, "height": 1350, "bg": "#000000"},
    "layers": [
        {"image": "photo1.png", "x": 0,   "y": 0,   "width": 536, "height": 671},
        {"image": "photo2.png", "x": 544, "y": 0,   "width": 536, "height": 671},
        {"image": "photo3.png", "x": 0,   "y": 679, "width": 536, "height": 671},
        {"image": "photo4.png", "x": 544, "y": 679, "width": 536, "height": 671}
    ]
}
```

(The 8px gaps between cells: 536 + 8 + 536 = 1080, 671 + 8 + 671 = 1350.)

#### 3-Column Grid

Three photos side by side, occupying the full height.

```json
{
    "canvas": {"width": 1080, "height": 1350, "bg": "#000000"},
    "layers": [
        {"image": "photo1.png", "x": 0,   "y": 0, "width": 356, "height": 1350},
        {"image": "photo2.png", "x": 362, "y": 0, "width": 356, "height": 1350},
        {"image": "photo3.png", "x": 724, "y": 0, "width": 356, "height": 1350}
    ]
}
```

#### Featured + Supporting (1 Large + 2 Small)

One dominant photo with two smaller supporting photos below.

```json
{
    "canvas": {"width": 1080, "height": 1350, "bg": "#000000"},
    "layers": [
        {"image": "hero.png",     "x": 0,   "y": 0,   "width": 1080, "height": 900},
        {"image": "support1.png", "x": 0,   "y": 908, "width": 536,  "height": 442},
        {"image": "support2.png", "x": 544, "y": 908, "width": 536,  "height": 442}
    ]
}
```

#### Diagonal Split

Two photos split diagonally. Achieved by overlapping two photos and using opacity to manage the visual split. (For a true diagonal clip, the result must be finished with CSS `clip-path` in HTML.)

```json
{
    "canvas": {"width": 1080, "height": 1350, "bg": "#000000"},
    "layers": [
        {"image": "photo_left.png",  "x": 0, "y": 0, "width": 1080, "height": 1350, "opacity": 1.0},
        {"image": "photo_right.png", "x": 540, "y": 0, "width": 540, "height": 1350, "opacity": 1.0}
    ]
}
```

For a true diagonal effect, use CSS in the HTML card:

```html
<div style="position: relative; width: 1080px; height: 1350px; overflow: hidden;">
    <img src="photo1.png" style="position: absolute; inset: 0; width: 100%; height: 100%;
         object-fit: cover; clip-path: polygon(0 0, 60% 0, 40% 100%, 0 100%);" />
    <img src="photo2.png" style="position: absolute; inset: 0; width: 100%; height: 100%;
         object-fit: cover; clip-path: polygon(60% 0, 100% 0, 100% 100%, 40% 100%);" />
</div>
```

#### Layered Stack with Fading

Multiple photos stacked with decreasing opacity, creating a depth effect.

```json
{
    "canvas": {"width": 1080, "height": 1350, "bg": "#111111"},
    "layers": [
        {"image": "bg_photo.png",   "x": 0, "y": 0, "width": 1080, "height": 1350, "opacity": 0.3, "grayscale": true},
        {"image": "mid_photo.png",  "x": 100, "y": 150, "width": 880, "height": 1050, "opacity": 0.6},
        {"image": "front_photo.png","x": 200, "y": 300, "width": 680, "height": 750, "opacity": 1.0}
    ]
}
```

### 6.3 Using Opacity and Grayscale Per Layer

Opacity and grayscale are per-layer settings that enable sophisticated compositions.

**Use cases for reduced opacity:**
- Background photos behind text: `"opacity": 0.3` to `0.5`
- Ghost/watermark effect: `"opacity": 0.1`
- Layered depth: progressively higher opacity for foreground layers

**Use cases for grayscale:**
- Mixed color/B&W compositions: featured photo in color, supporting photos in grayscale
- Highlighting a specific photo: one layer in color (`"grayscale": false`), rest in grayscale

**Example -- highlight one photo in a grid:**

```json
{
    "canvas": {"width": 1080, "height": 1350, "bg": "#000000"},
    "layers": [
        {"image": "photo1.png", "x": 0,   "y": 0,   "width": 536, "height": 671, "grayscale": true, "opacity": 0.6},
        {"image": "photo2.png", "x": 544, "y": 0,   "width": 536, "height": 671, "grayscale": false, "opacity": 1.0},
        {"image": "photo3.png", "x": 0,   "y": 679, "width": 536, "height": 671, "grayscale": true, "opacity": 0.6},
        {"image": "photo4.png", "x": 544, "y": 679, "width": 536, "height": 671, "grayscale": true, "opacity": 0.6}
    ]
}
```

### 6.4 Pre-Processing Photos Before Compositing

Photos usually need preparation before being placed in a collage. Run the crop/resize first:

```bash
# Step 1: Prepare photos at the exact sizes needed for the collage cells
python <skill_dir>/scripts/process_photo.py --batch prep.json
```

**prep.json:**

```json
[
    {"action": "crop", "input": "raw/photo1.jpg", "output": "prepped/photo1.png", "ratio": "1:1"},
    {"action": "resize", "input": "prepped/photo1.png", "output": "prepped/photo1.png", "dimensions": "536x536"},
    {"action": "crop", "input": "raw/photo2.jpg", "output": "prepped/photo2.png", "ratio": "4:5"},
    {"action": "resize", "input": "prepped/photo2.png", "output": "prepped/photo2.png", "dimensions": "536x671"}
]
```

Note: While `--composite` can resize images via the `width`/`height` properties, pre-cropping ensures the subject is properly centered before the collage scales the image.

```bash
# Step 2: Compose the collage
python <skill_dir>/scripts/process_photo.py \
  --composite collage_layout.json \
  --output ./images/final_collage.png
```

### 6.5 Full Example: Before/After Comparison Card

A common card news pattern showing a before/after transformation.

**prep_compare.json** (crop both photos to matching size):

```json
[
    {"action": "crop", "input": "photos/before.jpg", "output": "images/before_crop.png", "ratio": "1:2"},
    {"action": "resize", "input": "images/before_crop.png", "output": "images/before_ready.png", "dimensions": "536x1350"},
    {"action": "crop", "input": "photos/after.jpg", "output": "images/after_crop.png", "ratio": "1:2"},
    {"action": "resize", "input": "images/after_crop.png", "output": "images/after_ready.png", "dimensions": "536x1350"}
]
```

**compare_layout.json:**

```json
{
    "canvas": {"width": 1080, "height": 1350, "bg": "#000000"},
    "layers": [
        {"image": "images/before_ready.png", "x": 0, "y": 0, "width": 536, "height": 1350, "grayscale": true},
        {"image": "images/after_ready.png", "x": 544, "y": 0, "width": 536, "height": 1350}
    ]
}
```

```bash
python <skill_dir>/scripts/process_photo.py --batch prep_compare.json
python <skill_dir>/scripts/process_photo.py --composite compare_layout.json --output images/comparison.png
```

The left half is automatically grayscale (the "before" state), while the right half is in full color (the "after" state).
