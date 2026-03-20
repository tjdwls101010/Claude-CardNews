# Nano Banana Image Prompt Guide for Card News

A Nano Banana prompt guide specialized for card news illustration generation.
Restructured for card news workflows based on meta-prompt principles and official API documentation.

---

## 1. Core Principles

### Use Descriptive Scene Descriptions, Not Keyword Lists

Nano Banana's greatest strength is its deep natural language understanding. Do not list keywords separated by commas. Instead, write prompts as descriptive sentences that explain the scene.

Bad example: `icon, money, growth, green, 3D, clay style`
Good example: `A cheerful 3D clay-style icon of a small green plant sprouting from a golden coin, rendered with soft rounded edges and a matte tactile texture. The background is pure white. No text.`

### Layout > Style

Layout (spatial structure, placement, margins) takes priority over artistic style. In card news, secure the area where text will be placed first, then determine the style.

### Edit, Don't Re-roll

If the generated image is 80% satisfactory, do not regenerate from scratch. Use multi-turn editing to adjust only the desired parts. It is far more efficient to keep successful elements while changing only what is needed.

### Write All Prompts in English

Nano Banana delivers optimal performance with English prompts. Even if the concept is in Korean, the final prompt must always be written in English.

### Use Affirmative Statements Instead of Negations

Do not write "without X" or "no X." Instead, describe the desired state in affirmative terms.

Bad example: `no clutter, no text, no complex background`
Good example: `a clean, uncluttered composition with a solid white background and ample negative space`

### Supported Aspect Ratios Reference

Available aspect_ratio values in the API: `1:1`, `1:4`, `1:8`, `2:3`, `3:2`, `3:4`, `4:1`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `21:9`

Resolution options (Gemini 3 and above): `512`, `1K`, `2K`, `4K`

---

## 2. Card News Illustration Categories

### Icons and Symbols (1:1)

Icons that visually convey key concepts within card news body content. Used either after background removal (rembg) or placed directly on a white background.

**3D Clay Style Icons**

```
A colorful 3D clay-style icon of a glowing light bulb with a small gear inside, rendered with soft rounded edges, matte tactile texture, and gentle ambient occlusion shadows. The design is playful and slightly oversized with chibi-like proportions. The background must be pure white. No text.
```

```
A 3D clay-style icon of a shield with a checkmark in the center, rendered in soothing teal and white tones with soft rounded geometry and a subtle contact shadow beneath. The surface has a smooth matte finish like hand-molded clay. The background must be pure white. No text.
```

**Flat Design Icons**

```
A flat design icon of a megaphone emitting colorful sound waves, using a limited palette of coral, navy, and warm yellow. The shapes are geometric and clean with bold outlines and absolutely no gradients. Centered on a pure white background. No text.
```

```
A minimal flat design icon of a calendar page with a star marking today's date, using a two-tone palette of soft blue and bright orange. Clean geometric shapes with uniform line weight. The background must be pure white. No text.
```

**Kawaii Style**

```
A kawaii-style sticker of a happy coffee cup character with blushing cheeks and tiny arms giving a thumbs-up. The design features bold clean outlines, simple cel-shading, and a vibrant pastel color palette. The background must be pure white. No text.
```

---

### Concept Illustrations (1:1 or 4:5)

Illustrations that visually explain abstract concepts or complex ideas.

**Isometric Scenes**

```
A clean isometric illustration of a small workspace scene showing a desk with a laptop, a potted plant, a coffee mug, and floating notification icons above the screen. The style is modern vector art with soft pastel colors, gentle shadows, and clean edges. The composition is centered with generous white space around the scene. No text.
```

```
A 45-degree isometric miniature 3D illustration of a tiny factory processing raw data into gold bars, with conveyor belts, gears, and glowing screens. The style uses soft refined textures with subtle PBR materials and gentle lighting. Clean solid-colored background in light gray. No text.
```

**Metaphorical Visualization**

```
A conceptual illustration showing a person standing at a crossroads where one path is paved with golden bricks leading to a bright sunrise, and the other path fades into fog. The style is modern editorial illustration with clean lines, a limited color palette of warm gold and cool blue-gray, and significant negative space on the upper portion for text overlay. No text in the image.
```

```
A metaphorical illustration of a small seedling growing through a crack in a concrete floor, with warm sunlight streaming down from above. The style is clean vector illustration with soft gradients, using a palette of fresh green, warm yellow, and neutral gray. The upper two-thirds of the image is intentionally left as open space with a soft gradient. No text.
```

**Infographic Elements**

```
A clean, modern illustration of three ascending platforms like a podium, each holding a different icon: a book on the lowest, a brain on the middle, and a rocket on the highest. The style is flat design with subtle depth through layered shadows, using a cohesive palette of indigo, teal, and warm coral. White background with clean composition. No text.
```

---

### Background Images (4:5)

Used as the full background for card news slides. The key priority is securing sufficient space for text placement.

**Minimalist + Negative Space**

```
A minimalist composition with a single small succulent plant positioned in the bottom-right corner of the frame. The background is a vast, seamless gradient from warm off-white to very pale peach, creating significant negative space covering at least 70 percent of the canvas for text overlay. Soft, diffused lighting from the top left. The image should be in 4:5 portrait format.
```

```
A minimalist composition featuring delicate abstract geometric lines in thin gold strokes, clustered in the bottom-left corner of the frame. The rest of the canvas is clean off-white with a subtle paper texture, providing ample negative space for text placement. Soft even lighting throughout. Portrait orientation 4:5.
```

**Gradients and Abstract Backgrounds**

```
An abstract background with soft flowing gradients transitioning from deep navy blue at the bottom to warm coral at the top, with subtle organic wave shapes creating gentle depth. The texture is smooth and digital with a slight grain. The composition leaves the central area relatively clear and uniform for text readability. Portrait format 4:5.
```

```
A soft abstract background with large overlapping translucent circles in muted pastel tones of lavender, mint, and pale rose against a clean white base. The shapes are concentrated toward the edges, leaving the center open and clear. Gentle diffused lighting with a calm, modern aesthetic. 4:5 portrait format.
```

**Themed Scene Backgrounds**

```
A dreamy, slightly out-of-focus photograph of a cozy library interior with warm ambient lighting from table lamps. Bookshelves line the background in soft bokeh. The foreground is intentionally empty with a smooth gradient into the blurred scene, creating a natural text overlay zone in the upper half. Shot with a 50mm lens at f/1.8 for maximum background blur. Warm, inviting color tones. 4:5 portrait format.
```

---

### Header and Banner Images (16:9 or 3:2)

Wide-format images used as covers or top banners for card news series.

**Wide Scenes**

```
A panoramic illustration of a vibrant cityscape at golden hour, with warm sunlight reflecting off modern glass buildings. The left third of the composition features the detailed city scene, while the right two-thirds transitions into a soft gradient of warm amber tones, providing clean space for a title and subtitle. Modern editorial illustration style with clean lines and rich color. 16:9 landscape format.
```

```
A wide establishing shot of a peaceful mountain landscape at dawn, with layers of misty blue mountains receding into the distance. The scene is composed with the mountain peaks on the left side and an expansive gradient sky on the right, creating natural text placement area. Soft pastel tones of blue, lavender, and warm pink. Photorealistic style with dreamy atmosphere. 3:2 landscape format.
```

**Panoramic Illustrations**

```
A wide panoramic flat illustration of a connected digital ecosystem, showing tiny isometric buildings, data streams, and people interacting with floating screens, all arranged along a gentle horizontal S-curve. The style uses a cohesive palette of teal, white, and soft coral with clean vector shapes. Generous white space above and below the central band of activity. 16:9 format.
```

---

## 3. Style Consistency Strategy

Card news consists of multiple slides, so maintaining visual consistency across the entire series is critical.

### Establish Style on the First Card

When generating the first image of a series, define the style as specifically as possible. Use this definition as a "style anchor" and apply it identically to all subsequent images.

Elements to include in the style anchor:
- Art style: flat vector, 3D clay, watercolor, editorial illustration, etc.
- Color palette: specify 2-4 concrete colors
- Outline style: bold outlines, thin lines, no outlines
- Lighting direction and quality: soft diffused, warm directional, etc.
- Overall mood: playful, professional, serene, etc.

### Using Reference Images

Nano Banana can process up to 14 reference images simultaneously. When the first card produces a satisfactory image, attach that image as a reference and specify its role.

```
Apply the exact same visual style, color palette, and illustration technique from the provided reference image. Create a new scene showing [new scene description] while maintaining identical line weight, shading approach, and overall aesthetic.
```

Pattern for assigning roles to reference images:
- **Style/Aesthetic**: `Apply the color palette and illustration style from Image A`
- **Lighting/Atmosphere**: `Match the lighting and color temperature from Image B`
- **Identity/Character**: `Use Image C for the character's facial features and identity`

### "Maintain the same visual style" Pattern

The default pattern used every time when generating subsequent cards:

```
Maintain the exact same visual style as the reference image -- same line weight, same color palette, same shading technique, same level of detail. Only change the subject matter to [new subject]. Keep the background treatment and overall composition approach consistent.
```

---

## 4. Background Handling

### White Background Pattern (for rembg or direct use)

When generating icons or objects that will have their background removed via rembg, generating on a pure white background yields the highest quality background removal results.

```
[Object description]. The background must be pure white with no shadows, gradients, or textures. The object should be cleanly separated from the background with crisp edges. No text.
```

When shadows are needed (used without background removal):

```
[Object description]. The background is pure white. A soft, subtle contact shadow sits directly beneath the object to give it grounding. No other shadows or elements in the background. No text.
```

### Solid Color Background (Card Palette Matching)

Pattern for specifying background colors to match card news brand colors:

```
[Object description]. The background is a solid, flat, uniform [color name + hex code description] color with no gradients, patterns, or textures. The object is centered with generous padding around it. No text.
```

Example:

```
A 3D clay-style icon of a rising bar chart with an upward arrow. The background is a solid, flat, uniform soft blue color matching a calm sky tone. The icon is centered with generous spacing. Soft ambient lighting. No text.
```

### Choosing Between Full Background and Transparent Background

**Full background use**: Background images that cover the entire card slide, or illustrations that need to convey a specific atmosphere. Secure text areas within the prompt in advance.

**White/solid background (transparent after rembg) use**: Icons, stickers, individual objects, and other elements that need to be freely positioned on HTML/CSS layouts. Generate on a pure white background and then remove the background with rembg.

---

## 5. Prompt Templates

Replace the `[PLACEHOLDER]` sections in the templates below with actual values.

### Icon Generation Template

```
A [STYLE: 3D clay-style / flat design / kawaii-style] icon of [SUBJECT: icon topic and specific description], rendered with [RENDERING: soft rounded edges and matte texture / clean geometric shapes and bold outlines / bold clean outlines and simple cel-shading]. The color palette uses [COLORS: 2-3 specific colors]. The background must be pure white. No text.
```

Usage example:

```
A 3D clay-style icon of a padlock with a glowing keyhole, rendered with soft rounded edges and matte texture. The color palette uses deep navy blue and bright gold accents. The background must be pure white. No text.
```

### Concept Illustration Template

```
A [STYLE: isometric / editorial / conceptual] illustration depicting [SCENE: descriptive narration of the scene]. The visual metaphor conveys the idea of [CONCEPT: the concept to communicate]. The style is [ART_STYLE: modern vector art with soft gradients / clean flat design with subtle depth / hand-drawn illustration with watercolor textures], using a cohesive palette of [COLORS: color palette]. The composition leaves [SPACE: the upper third / the right half / generous margins] open as negative space for text overlay. No text in the image. [ASPECT: 1:1 square format / 4:5 portrait format].
```

Usage example:

```
A conceptual illustration depicting a person climbing a staircase made of open books, each step revealing a different skill icon. The visual metaphor conveys the idea of continuous learning and professional growth. The style is modern vector art with soft gradients, using a cohesive palette of warm coral, deep teal, and cream. The composition leaves the upper third open as negative space for text overlay. No text in the image. 4:5 portrait format.
```

### Background Image Template

```
A [MOOD: minimalist / dreamy / vibrant / serene] background composition featuring [ELEMENT: description of background visual elements], positioned in the [POSITION: bottom-right / edges / lower portion] of the frame. The [BACKGROUND: remaining area / upper two-thirds / center] is [TREATMENT: a vast empty off-white canvas / a smooth gradient from X to Y / clean and clear], creating significant negative space for text overlay covering at least [PERCENT: 60-70] percent of the canvas. [LIGHTING: Soft diffused lighting from the top left / Warm ambient glow / Even gentle illumination]. [ASPECT: 4:5 portrait format / 9:16 vertical format].
```

Usage example:

```
A serene background composition featuring soft watercolor cherry blossom petals scattered in the bottom-right corner of the frame. The upper two-thirds is a smooth gradient from pale rose to clean white, creating significant negative space for text overlay covering at least 65 percent of the canvas. Soft diffused lighting from the top left. 4:5 portrait format.
```

### Style Reference Template (Series Consistency)

Used by attaching a reference when generating follow-up images after the first image:

```
Using the provided reference image as the definitive style guide, create a new illustration showing [NEW_SCENE: new scene description]. Match exactly the following from the reference: the illustration technique, line weight, shading style, color palette, level of detail, and background treatment. The only change should be the subject matter. [ASPECT: maintain the same ratio].
```

Usage example:

```
Using the provided reference image as the definitive style guide, create a new illustration showing a team of three people collaborating around a holographic dashboard with floating data charts. Match exactly the following from the reference: the illustration technique, line weight, shading style, color palette, level of detail, and background treatment. The only change should be the subject matter. 1:1 square format.
```

### Image Editing Template (Refinement)

For when the generated image is mostly satisfactory but needs partial adjustments:

**Color Change**:
```
Keep everything identical but change the color of [TARGET: target element] from [CURRENT: current color] to [NEW: new color]. Preserve all other elements exactly as they are, including the lighting, composition, and style.
```

**Background Replacement**:
```
Maintain the subject perfectly but replace the background with [NEW_BG: new background description]. Ensure the subject's edges, lighting, and shadows integrate naturally with the new background.
```

**Element Addition**:
```
Add [ELEMENT: detailed description of the element to add] to the [POSITION: location]. Ensure the new element matches the existing lighting, perspective, and visual style. Keep everything else exactly the same.
```

**Element Removal**:
```
Remove the [TARGET: element to remove] from the scene and fill the area naturally with the surrounding background. Keep everything else exactly the same, preserving the original style, lighting, and composition.
```

**Mood Adjustment**:
```
Keep everything identical but adjust the overall mood to be [MOOD: warmer / cooler / more dramatic / brighter]. [SPECIFIC: Add warm golden hour lighting from the right / Shift the color temperature toward cool blue tones / Increase the contrast and deepen the shadows]. Preserve the composition and all objects exactly as they are.
```

---

## 6. Common Issues and Solutions

### Text Is Not Rendered Accurately

When text must be included in the image (rare in card news, but may be needed for covers):
- Wrap the text in double quotes: `with the text "Hello" in the center`
- Limit to 3-5 words
- Describe the font descriptively: `clean bold sans-serif` (do not use specific font names)
- Using Nano Banana Pro (Gemini 3 Pro Image) provides higher text rendering quality

### Composition Does Not Match Intent

- Include an explicit shot type: close-up, medium shot, wide shot
- Specify the camera angle: eye level, slightly elevated 45-degree angle, top-down
- Describe the object's position within the frame specifically: `positioned in the bottom-right corner of the frame`
- Describe spatial relationships: `the icon is centered with generous padding on all sides`

### Lighting Does Not Meet Expectations

- Specify the direction of light: `soft lighting from the top-left`
- Specify the quality of light: `soft diffused light`, `hard directional light`
- Use specific time-of-day references: `golden hour warmth`, `cool overcast daylight`
- Describe the lighting setup: `three-point softbox setup`, `rim lighting from behind`

### Inconsistency Across Repeated Generations

- Use multi-turn editing instead of regenerating from scratch
- Attach successful results as reference images
- Write style definitions as technically and specifically as possible
- Include the same style anchor phrase in all subsequent prompts

### Background Is Not Clean (for rembg)

- Always include `The background must be pure white`
- Add `with no shadows, gradients, or textures on the background`
- Specify `cleanly separated from the background with crisp edges`
- If still unresolved: `isolated object on a seamless pure white studio backdrop, product photography lighting`

### Illustration Is Too Complex or Cluttered

- Use a structured prompt format to explicitly define components
- Explicitly reserve white space: `allocate at least 30 percent of the canvas to white space`
- Add constraints: `clean composition with minimal elements`, `no overlapping objects`
- However, keep constraints to 2-3 at most (too many constraints limit the model's creativity)

### Unintended Changes During Editing

- Always include `Keep everything else exactly the same`
- Specifically identify the target of the change: `change only the background color`, `modify only the icon in the center`
- Specify elements to preserve: `preserving the original style, lighting, and composition`
- Request only one change at a time (requesting multiple changes simultaneously can produce unintended results)

---

## Appendix: Frequently Used Quality Keywords for Card News Production

The keywords below have been validated to consistently produce good results. Insert them at appropriate positions in the prompt.

**Illustration Quality**: `clean composition`, `crisp edges`, `cohesive color palette`, `soft ambient occlusion`, `gentle shadows`

**Background Related**: `clean background`, `pure white background`, `seamless gradient`, `significant negative space`, `ample space for text overlay`

**Style Related**: `flat design`, `vector art`, `3D clay style`, `soft matte texture`, `bold clean outlines`, `simple cel-shading`, `modern editorial illustration`

**Mood Related**: `soft natural light`, `warm inviting tones`, `calm and professional`, `playful and approachable`, `serene and minimal`
