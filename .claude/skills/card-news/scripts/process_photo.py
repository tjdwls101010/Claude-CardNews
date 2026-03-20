#!/usr/bin/env python3
"""Photo processing utility for card news using Pillow.

Handles mechanical photo operations: crop, resize, composite, grayscale.
For creative edits (color grading, style changes), use generate_image.py with --input.

Usage:
  # Smart crop to aspect ratio (centers on content)
  python process_photo.py --crop 4:5 --input photo.jpg --output cropped.png

  # Resize to exact dimensions
  python process_photo.py --resize 1080x1350 --input photo.jpg --output resized.png

  # Grayscale conversion
  python process_photo.py --grayscale --input photo.jpg --output bw.png

  # Composite: layer multiple images (for collages)
  python process_photo.py --composite layout.json --output collage.png

  # Batch: process multiple photos at once
  python process_photo.py --batch batch.json
"""

import argparse
import concurrent.futures
import json
import sys
import traceback
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps


def crop_to_ratio(input_path, output_path, ratio_str):
    """Smart crop to target aspect ratio, centering on content."""
    img = Image.open(input_path)
    w, h = img.size

    # Parse ratio
    rw, rh = map(int, ratio_str.split(":"))
    target_ratio = rw / rh
    current_ratio = w / h

    if current_ratio > target_ratio:
        # Image is wider than target -- crop width
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    elif current_ratio < target_ratio:
        # Image is taller than target -- crop height
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))

    _save(img, output_path)
    print(f"Cropped to {ratio_str}: {input_path} -> {output_path} ({img.size[0]}x{img.size[1]})")
    return True


def resize_to_dimensions(input_path, output_path, dimensions_str):
    """Resize to exact dimensions (e.g., '1080x1350')."""
    img = Image.open(input_path)
    w, h = map(int, dimensions_str.split("x"))
    img = img.resize((w, h), Image.LANCZOS)
    _save(img, output_path)
    print(f"Resized to {w}x{h}: {input_path} -> {output_path}")
    return True


def to_grayscale(input_path, output_path):
    """Convert to grayscale."""
    img = Image.open(input_path).convert("L").convert("RGB")
    _save(img, output_path)
    print(f"Grayscale: {input_path} -> {output_path}")
    return True


def adjust_image(input_path, output_path, brightness=1.0, contrast=1.0, saturation=1.0):
    """Adjust brightness, contrast, and saturation."""
    img = Image.open(input_path)
    if brightness != 1.0:
        img = ImageEnhance.Brightness(img).enhance(brightness)
    if contrast != 1.0:
        img = ImageEnhance.Contrast(img).enhance(contrast)
    if saturation != 1.0:
        img = ImageEnhance.Color(img).enhance(saturation)
    _save(img, output_path)
    print(f"Adjusted (b={brightness}, c={contrast}, s={saturation}): {input_path} -> {output_path}")
    return True


def composite_images(layout_path, output_path):
    """Composite multiple images into a single canvas based on layout JSON.

    Layout JSON format:
    {
      "canvas": {"width": 1080, "height": 1350, "bg": "#000000"},
      "layers": [
        {
          "image": "photo1.png",
          "x": 0, "y": 0,
          "width": 1080,        // optional: resize to this width (height auto)
          "height": 600,        // optional: resize to this height (width auto)
          "opacity": 0.7,       // optional: 0.0 to 1.0
          "grayscale": false    // optional: convert layer to grayscale
        }
      ]
    }
    """
    with open(layout_path) as f:
        layout = json.load(f)

    canvas_cfg = layout["canvas"]
    bg_color = canvas_cfg.get("bg", "#000000")
    canvas = Image.new("RGBA", (canvas_cfg["width"], canvas_cfg["height"]), bg_color)

    for layer in layout["layers"]:
        img = Image.open(layer["image"]).convert("RGBA")

        # Resize if specified
        if "width" in layer and "height" in layer:
            img = img.resize((layer["width"], layer["height"]), Image.LANCZOS)
        elif "width" in layer:
            ratio = layer["width"] / img.size[0]
            img = img.resize((layer["width"], int(img.size[1] * ratio)), Image.LANCZOS)
        elif "height" in layer:
            ratio = layer["height"] / img.size[1]
            img = img.resize((int(img.size[0] * ratio), layer["height"]), Image.LANCZOS)

        # Grayscale if specified
        if layer.get("grayscale"):
            gray = img.convert("L").convert("RGBA")
            # Preserve alpha from original
            r, g, b, a = img.split()
            gr, _, _, _ = gray.split()
            img = Image.merge("RGBA", (gr, gr, gr, a))

        # Apply opacity
        opacity = layer.get("opacity", 1.0)
        if opacity < 1.0:
            r, g, b, a = img.split()
            a = a.point(lambda x: int(x * opacity))
            img = Image.merge("RGBA", (r, g, b, a))

        # Paste onto canvas
        x = layer.get("x", 0)
        y = layer.get("y", 0)
        canvas.paste(img, (x, y), img)

    # Save as RGB PNG
    final = Image.new("RGB", canvas.size, bg_color)
    final.paste(canvas, mask=canvas.split()[3])
    _save(final, output_path)
    print(f"Composite: {len(layout['layers'])} layers -> {output_path} ({canvas_cfg['width']}x{canvas_cfg['height']})")
    return True


def run_batch(batch_path):
    """Batch mode: process multiple photos in parallel.

    batch.json format:
    [
      {"action": "crop", "input": "a.jpg", "output": "a_crop.png", "ratio": "4:5"},
      {"action": "resize", "input": "b.jpg", "output": "b_resized.png", "dimensions": "1080x1350"},
      {"action": "grayscale", "input": "c.jpg", "output": "c_bw.png"},
      {"action": "composite", "layout": "layout.json", "output": "collage.png"}
    ]
    """
    with open(batch_path) as f:
        jobs = json.load(f)

    print(f"Batch mode: {len(jobs)} jobs")

    def run_job(job):
        try:
            action = job["action"]
            if action == "crop":
                return crop_to_ratio(job["input"], job["output"], job["ratio"])
            elif action == "resize":
                return resize_to_dimensions(job["input"], job["output"], job["dimensions"])
            elif action == "grayscale":
                return to_grayscale(job["input"], job["output"])
            elif action == "adjust":
                return adjust_image(
                    job["input"], job["output"],
                    brightness=job.get("brightness", 1.0),
                    contrast=job.get("contrast", 1.0),
                    saturation=job.get("saturation", 1.0),
                )
            elif action == "composite":
                return composite_images(job["layout"], job["output"])
            else:
                print(f"Unknown action: {action}", file=sys.stderr)
                return False
        except Exception as e:
            print(f"Error in job {job}: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            return False

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(run_job, jobs))

    succeeded = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)
    print(f"\nBatch complete: {succeeded} succeeded, {failed} failed")
    return failed == 0


def _save(img, output_path):
    """Save image, creating parent directories if needed."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(output_path))


def main():
    parser = argparse.ArgumentParser(description="Process photos for card news (Pillow-based)")
    parser.add_argument("--input", help="Input image file path")
    parser.add_argument("--output", help="Output image file path")
    parser.add_argument("--crop", help="Crop to aspect ratio (e.g., 4:5, 1:1, 16:9)")
    parser.add_argument("--resize", help="Resize to dimensions (e.g., 1080x1350)")
    parser.add_argument("--grayscale", action="store_true", help="Convert to grayscale")
    parser.add_argument("--brightness", type=float, default=1.0, help="Brightness factor (1.0=unchanged)")
    parser.add_argument("--contrast", type=float, default=1.0, help="Contrast factor (1.0=unchanged)")
    parser.add_argument("--saturation", type=float, default=1.0, help="Saturation factor (1.0=unchanged)")
    parser.add_argument("--composite", help="Path to composite layout JSON file")
    parser.add_argument("--batch", help="Path to batch JSON file for parallel processing")

    args = parser.parse_args()

    # Batch mode
    if args.batch:
        success = run_batch(args.batch)
        sys.exit(0 if success else 1)

    # Composite mode
    if args.composite:
        if not args.output:
            parser.error("--output is required with --composite")
        success = composite_images(args.composite, args.output)
        sys.exit(0 if success else 1)

    # Single file modes (require --input and --output)
    if not args.input or not args.output:
        parser.error("--input and --output are required (or use --batch / --composite)")

    if args.crop:
        success = crop_to_ratio(args.input, args.output, args.crop)
    elif args.resize:
        success = resize_to_dimensions(args.input, args.output, args.resize)
    elif args.grayscale:
        success = to_grayscale(args.input, args.output)
    elif args.brightness != 1.0 or args.contrast != 1.0 or args.saturation != 1.0:
        success = adjust_image(args.input, args.output, args.brightness, args.contrast, args.saturation)
    else:
        parser.error("Specify an operation: --crop, --resize, --grayscale, --brightness/--contrast/--saturation, --composite, or --batch")
        success = False

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
