# Nano Banana Image Prompt Guide

How to write effective prompts for card news illustration generation using Nano Banana (Gemini image generation). This guide covers the principles behind good prompts -- not the API parameters (those are in SKILL.md).

---

## 1. Core Prompt Principles

### Describe Scenes, Not Tag Lists

Nano Banana's strength is deep natural language understanding. Keyword-separated prompts ("icon, money, growth, green, 3D") produce generic, unfocused results because the model treats each word independently without understanding relationships. Descriptive sentences ("A cheerful 3D clay-style icon of a small green plant sprouting from a golden coin, with soft rounded edges and matte texture") give the model spatial relationships, material properties, and compositional intent.

### Layout Before Style

In card news, the illustration must coexist with text. This means the **spatial layout** of the image (where negative space falls, where the subject sits) is more important than the artistic style. Always specify where the text overlay area should be before describing the aesthetic: "The upper third of the image is intentionally left as open space with a soft gradient" comes before "modern editorial illustration style."

Without explicit layout instructions, the model tends to center subjects and fill the frame -- leaving no room for text.

### Edit, Don't Regenerate

When a generated image is 80% satisfactory, use edit mode (`--input`) to refine rather than regenerating from scratch. Regeneration discards everything that worked; editing preserves the good parts and changes only what's needed. This is especially critical for maintaining style consistency across a series -- each full regeneration risks drifting the style.

### English Only, Affirmative Statements

Write all prompts in English for optimal model performance. Describe what you *want*, not what you don't want. "A clean, uncluttered composition with a solid white background" is far more effective than "no clutter, no text, no complex background" because the model is better at generating toward a described target than away from a negated one.

Always end prompts with **"No text."** -- this single directive prevents the model from rendering unwanted text labels, watermarks, or captions in the image.

---

## 2. Card News Illustration Categories

Each category has a natural aspect ratio and a specific role in the card layout.

### Icons and Symbols (1:1)

Small visual elements that represent concepts within body cards. Always generate on a **pure white background** so rembg can cleanly remove the background for placement on any card color. Styles: 3D clay (playful, modern), flat design (clean, corporate), kawaii (approachable, casual).

Key prompt elements: specify the style, describe the object in detail, include material/texture properties ("soft rounded edges, matte tactile texture"), end with "The background must be pure white. No text."

### Concept Illustrations (1:1 or 4:5)

Metaphorical scenes that visually explain abstract ideas -- a person climbing a staircase of books (continuous learning), a seedling growing through concrete (resilience). These require explicit negative space reservation because they share the card with title and body text.

Key prompt elements: describe the scene narratively, state the visual metaphor, specify the art style and color palette, explicitly reserve text overlay area ("the upper third is open space").

### Background Images (4:5)

Full-card backgrounds that set the mood. The critical challenge is ensuring at least 60-70% of the canvas is clean enough for text overlay. Minimalist compositions (small subject in one corner, vast gradient filling the rest) or atmospheric abstracts (soft flowing gradients, translucent geometric shapes) work best.

Key prompt elements: specify where visual elements cluster (bottom-right, edges), describe the empty area explicitly ("significant negative space covering at least 70% of the canvas"), specify lighting and color tone.

### Header Banners (16:9 or 3:2)

Wide images for cover cards or top sections. The effective pattern is scene-on-one-side: detailed visual content on the left third, smooth gradient transition to clean space on the right two-thirds for title placement.

---

## 3. Style Consistency Across a Series

The biggest quality issue in AI-illustrated card news is **inconsistent style across cards**. Card 1 might have a warm, detailed 3D look while Card 3 drifts to a flat, cool aesthetic. The viewer perceives this as different designers working on different slides -- it breaks the series' cohesion.

### Establish a Style Anchor

On the first card's illustration, define the style as precisely as possible:
- Art style: "3D clay-style" / "flat vector" / "editorial illustration"
- Color palette: name 2-4 specific colors
- Outline treatment: "bold clean outlines" / "no outlines, soft edges"
- Lighting: "soft diffused ambient" / "warm directional from top-left"
- Mood: "playful and approachable" / "professional and serene"

This definition becomes the style anchor that all subsequent prompts reference.

### Reference Images Are Mandatory

After the first card produces a satisfactory illustration, attach it as `--refs` for **every subsequent generation**. Without a reference image, the model has no visual target for consistency -- it interprets style descriptions differently each time.

Include the consistency phrase in every follow-up prompt:
> "Maintain the exact same visual style as the reference image -- same line weight, color palette, shading technique, level of detail. Only change the subject matter to [new subject]."

For character consistency across cards:
> "Same character as in the reference image, identical rendering style, same color temperature and texture."

---

## 4. Background Handling for rembg

### Pure White Background

When generating icons or objects that will have their background removed with rembg, the cleanest results come from pure white backgrounds:
> "The background must be pure white with no shadows, gradients, or textures. The object should be cleanly separated from the background with crisp edges."

If the background still comes out dirty (subtle gradients or shadows), add:
> "Isolated object on a seamless pure white studio backdrop, product photography lighting."

### Solid Color Background

When matching the card's color palette, specify the exact color:
> "The background is a solid, flat, uniform deep navy (#0A1628) with no gradients or patterns."

### When to Remove vs Keep Backgrounds

- **Remove (rembg):** Icons, objects, or characters that need to float on the card's designed background. Generate on white, then remove
- **Keep as-is:** Full-card background images, atmospheric scenes, or illustrations where the background is part of the composition
- **Keep but process:** When the generated background color roughly matches the card but needs refinement -- use CSS filters or Nano Banana edit mode to adjust

---

## 5. Editing Prompts

When refining a generated image with `--input`, the key risk is unintended changes: the model might "improve" parts you wanted to keep.

### Preservation First

Always include: **"Keep everything else exactly the same."** Then specify what to preserve explicitly: "Preserve the original style, lighting, and composition."

### One Change Per Edit

Request only one modification at a time. Multiple simultaneous changes ("change the background to blue AND add a hat AND make it warmer") produce unpredictable results because the model tries to optimize all changes at once and may compromise on each.

### Describe Targets, Not Processes

Say "the shadows should be teal" rather than "shift the blue channel in the shadows." Reference real-world analogies for creative effects: film stocks ("Kodak Portra 400 warmth"), time of day ("golden hour lighting"), and movies ("Blade Runner color palette") are effective because the model understands these references.

State intensity: "subtle," "moderate," "strong," or "extreme" helps the model calibrate the magnitude of the change.

---

## 6. Troubleshooting

### Text Doesn't Render Correctly
Wrap text in double quotes, limit to 3-5 words, describe the font style ("clean bold sans-serif") rather than naming a specific font. In card news, text rendering in images is rarely needed -- HTML text layers are almost always superior.

### Composition Misses Intent
Add explicit shot type (close-up, medium, wide), camera angle (eye level, 45-degree elevated, top-down), and subject position ("positioned in the bottom-right corner of the frame").

### Style Drifts Across Series
Always use `--refs` with the first card's image. If drift persists, include the full style anchor description in addition to the reference image. Check that aspect ratios are consistent across cards.

### Background Not Clean Enough for rembg
Escalate the purity instructions: "seamless pure white studio backdrop, product photography lighting, absolutely no shadows or gradients touching the background surface."

**Review diagnostic:** After generating all illustrations for a series, view them side by side. If any card's illustration feels like it belongs to a different series, regenerate it with stronger `--refs` usage and an explicit style anchor phrase.
