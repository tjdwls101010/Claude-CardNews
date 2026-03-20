#!/usr/bin/env python3
"""Nano Banana (Gemini) image generation script for card news illustrations.

Usage:
  # Single image
  python generate_image.py --prompt "..." --output out.png

  # Image editing
  python generate_image.py --prompt "..." --input ref.png --output out.png

  # Multi-reference
  python generate_image.py --prompt "..." --refs img1.png img2.png --output out.png

  # Batch (parallel) - multiple prompts at once
  python generate_image.py --batch batch.json
  # batch.json format: [{"prompt": "...", "output": "out1.png", "aspect_ratio": "1:1"}, ...]
"""

import argparse
import concurrent.futures
import json
import os
import sys
import traceback
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image


def load_config():
    """Load API configuration from .env file."""
    env_path = Path(__file__).parent / ".env"
    load_dotenv(env_path)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env", file=sys.stderr)
        sys.exit(1)

    return {
        "api_key": api_key,
        "model": os.getenv("GOOGLE_MODEL", "gemini-3.1-flash-image-preview"),
        "image_size": os.getenv("IMAGE_SIZE", "2K"),
    }


def _make_image_config(aspect_ratio, image_size):
    return types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
            image_size=image_size,
        ),
    )


def generate_from_text(client, model, prompt, aspect_ratio, image_size, output_path):
    """Mode 1: Text-to-image generation."""
    response = client.models.generate_content(
        model=model,
        contents=[prompt],
        config=_make_image_config(aspect_ratio, image_size),
    )
    return _save_response_image(response, output_path)


def edit_image(client, model, prompt, input_path, aspect_ratio, image_size, output_path):
    """Mode 2: Image editing (text + image -> image)."""
    input_image = Image.open(input_path)
    response = client.models.generate_content(
        model=model,
        contents=[prompt, input_image],
        config=_make_image_config(aspect_ratio, image_size),
    )
    return _save_response_image(response, output_path)


def generate_with_refs(client, model, prompt, ref_paths, aspect_ratio, image_size, output_path):
    """Mode 3: Multi-reference image generation."""
    contents = [prompt]
    for ref_path in ref_paths:
        contents.append(Image.open(ref_path))

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=_make_image_config(aspect_ratio, image_size),
    )
    return _save_response_image(response, output_path)


def _save_response_image(response, output_path):
    """Extract and save image from API response."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(str(output_path))
            print(f"Image saved: {output_path}")
            return True
    print(f"Error: No image in response for {output_path}", file=sys.stderr)
    return False


def _run_single_job(client, config, job):
    """Execute a single generation job. Used by both single and batch modes."""
    prompt = job["prompt"]
    output = job["output"]
    aspect_ratio = job.get("aspect_ratio", "1:1")
    input_path = job.get("input")
    refs = job.get("refs")

    try:
        if input_path:
            return edit_image(
                client, config["model"], prompt, input_path,
                aspect_ratio, config["image_size"], output,
            )
        elif refs:
            return generate_with_refs(
                client, config["model"], prompt, refs,
                aspect_ratio, config["image_size"], output,
            )
        else:
            return generate_from_text(
                client, config["model"], prompt,
                aspect_ratio, config["image_size"], output,
            )
    except Exception as e:
        print(f"Error generating {output}: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return False


def run_batch(client, config, batch_path):
    """Batch mode: run multiple generation jobs in parallel."""
    with open(batch_path) as f:
        jobs = json.load(f)

    print(f"Batch mode: {len(jobs)} jobs, running in parallel...")

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(jobs), 5)) as executor:
        future_to_job = {
            executor.submit(_run_single_job, client, config, job): job
            for job in jobs
        }
        for future in concurrent.futures.as_completed(future_to_job):
            job = future_to_job[future]
            success = future.result()
            results[job["output"]] = success

    succeeded = sum(1 for v in results.values() if v)
    failed = sum(1 for v in results.values() if not v)
    print(f"\nBatch complete: {succeeded} succeeded, {failed} failed")
    return failed == 0


def main():
    parser = argparse.ArgumentParser(description="Generate images with Nano Banana API")
    parser.add_argument("--prompt", help="Text prompt for image generation")
    parser.add_argument("--output", help="Output PNG file path")
    parser.add_argument("--input", help="Input image for editing mode (Mode 2)")
    parser.add_argument("--refs", nargs="+", help="Reference images for multi-ref mode (Mode 3)")
    parser.add_argument(
        "--aspect-ratio",
        default="1:1",
        help="Aspect ratio (1:1, 4:5, 16:9, 3:2, 2:3, 3:4, 9:16, etc.)",
    )
    parser.add_argument(
        "--batch",
        help="Path to batch JSON file for parallel generation",
    )

    args = parser.parse_args()
    config = load_config()
    client = genai.Client(api_key=config["api_key"])

    # Batch mode
    if args.batch:
        success = run_batch(client, config, args.batch)
        sys.exit(0 if success else 1)

    # Single mode (requires --prompt and --output)
    if not args.prompt or not args.output:
        parser.error("--prompt and --output are required (or use --batch)")

    job = {
        "prompt": args.prompt,
        "output": args.output,
        "aspect_ratio": args.aspect_ratio,
        "input": args.input,
        "refs": args.refs,
    }
    success = _run_single_job(client, config, job)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
