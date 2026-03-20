#!/usr/bin/env python3
"""Convert HTML card news files to PNG using Playwright."""

import argparse
import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def convert_html_to_png(html_path: str, output_path: str = None):
    """Convert a single HTML file to PNG."""
    html_path = Path(html_path).resolve()
    if not html_path.exists():
        print(f"Error: {html_path} not found", file=sys.stderr)
        return False

    if output_path is None:
        output_path = html_path.with_suffix(".png")
    else:
        output_path = Path(output_path).resolve()

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1080, "height": 1350},
            device_scale_factor=2,  # Retina: 2160x2700 actual pixels
        )

        await page.goto(f"file://{html_path}")
        await page.wait_for_load_state("networkidle")

        # Wait for fonts to load
        await page.evaluate("() => document.fonts.ready")
        # Small extra delay for rendering
        await page.wait_for_timeout(500)

        # Screenshot the card area (1080x1350)
        await page.screenshot(
            path=str(output_path),
            clip={"x": 0, "y": 0, "width": 1080, "height": 1350},
        )

        await browser.close()

    print(f"Converted: {html_path.name} -> {output_path.name}")
    return True


async def convert_directory(dir_path: str):
    """Convert all HTML files in a directory to PNG."""
    dir_path = Path(dir_path).resolve()
    html_files = sorted(dir_path.glob("*.html"))

    if not html_files:
        print(f"No HTML files found in {dir_path}", file=sys.stderr)
        return False

    print(f"Found {len(html_files)} HTML files")

    for html_file in html_files:
        await convert_html_to_png(str(html_file))

    print(f"\nAll {len(html_files)} files converted.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Convert HTML card news to PNG")
    parser.add_argument("path", help="HTML file or directory containing HTML files")
    parser.add_argument("--output", help="Output PNG path (for single file only)")

    args = parser.parse_args()
    target = Path(args.path)

    if target.is_file():
        success = asyncio.run(convert_html_to_png(str(target), args.output))
    elif target.is_dir():
        success = asyncio.run(convert_directory(str(target)))
    else:
        print(f"Error: {target} not found", file=sys.stderr)
        success = False

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
