#!/usr/bin/env python3
"""Nano Banana (Gemini) image generation script for card news illustrations."""

import argparse
import os
import sys
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


def generate_from_text(client, model, prompt, aspect_ratio, image_size, output_path):
    """Mode 1: Text-to-image generation."""
    response = client.models.generate_content(
        model=model,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=image_size,
            ),
        ),
    )
    return _save_response_image(response, output_path)


def edit_image(client, model, prompt, input_path, aspect_ratio, image_size, output_path):
    """Mode 2: Image editing (text + image -> image)."""
    input_image = Image.open(input_path)
    response = client.models.generate_content(
        model=model,
        contents=[prompt, input_image],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=image_size,
            ),
        ),
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
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=image_size,
            ),
        ),
    )
    return _save_response_image(response, output_path)


def _save_response_image(response, output_path):
    """Extract and save image from API response."""
    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(output_path)
            print(f"Image saved: {output_path}")
            return True
    print("Error: No image in response", file=sys.stderr)
    return False


def main():
    parser = argparse.ArgumentParser(description="Generate images with Nano Banana API")
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--output", required=True, help="Output PNG file path")
    parser.add_argument("--input", help="Input image for editing mode (Mode 2)")
    parser.add_argument("--refs", nargs="+", help="Reference images for multi-ref mode (Mode 3)")
    parser.add_argument(
        "--aspect-ratio",
        default="1:1",
        help="Aspect ratio (1:1, 4:5, 16:9, 3:2, 2:3, 3:4, 9:16, etc.)",
    )

    args = parser.parse_args()
    config = load_config()

    client = genai.Client(api_key=config["api_key"])

    # Determine mode
    if args.input:
        # Mode 2: Image editing
        print(f"Mode: Image editing | Input: {args.input}")
        success = edit_image(
            client, config["model"], args.prompt, args.input,
            args.aspect_ratio, config["image_size"], args.output,
        )
    elif args.refs:
        # Mode 3: Multi-reference
        print(f"Mode: Multi-reference | Refs: {args.refs}")
        success = generate_with_refs(
            client, config["model"], args.prompt, args.refs,
            args.aspect_ratio, config["image_size"], args.output,
        )
    else:
        # Mode 1: Text-to-image
        print("Mode: Text-to-image")
        success = generate_from_text(
            client, config["model"], args.prompt,
            args.aspect_ratio, config["image_size"], args.output,
        )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
