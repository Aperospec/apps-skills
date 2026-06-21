#!/usr/bin/env python3
"""Auxiliary pixel-difference check only.

True UI fidelity acceptance still requires semantic visual review, component
mapping, design-token verification, and final human confirmation where needed.
"""

import argparse
import json
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compare two images and write a JSON pixel-difference result."
    )
    parser.add_argument("--reference", required=True, help="Figma reference image")
    parser.add_argument("--runtime", required=True, help="iOS runtime image")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.0,
        help="Allowed differing-pixel ratio from 0.0 to 1.0 (default: 0.0)",
    )
    parser.add_argument("--diff-image", help="Optional output path for a diff image")
    return parser.parse_args()


def load_pillow():
    try:
        from PIL import Image, ImageChops
    except ImportError:
        print(
            "Error: Pillow is required for image comparison. "
            "Install it with 'python3 -m pip install Pillow'.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return Image, ImageChops


def open_rgba(Image, path):
    try:
        with Image.open(path) as image:
            return image.convert("RGBA")
    except FileNotFoundError:
        print(f"Error: image not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(f"Error: cannot read image '{path}': {exc}", file=sys.stderr)
        raise SystemExit(2)


def main():
    args = parse_args()
    if not 0.0 <= args.threshold <= 1.0:
        print("Error: --threshold must be between 0.0 and 1.0.", file=sys.stderr)
        return 2

    Image, ImageChops = load_pillow()
    reference = open_rgba(Image, args.reference)
    runtime = open_rgba(Image, args.runtime)

    reference_size = list(reference.size)
    runtime_size = list(runtime.size)
    size_match = reference.size == runtime.size
    canvas_size = (
        max(reference.width, runtime.width),
        max(reference.height, runtime.height),
    )

    reference_canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    runtime_canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    reference_canvas.paste(reference, (0, 0))
    runtime_canvas.paste(runtime, (0, 0))

    diff = ImageChops.difference(reference_canvas, runtime_canvas)
    differing_pixels = sum(
        1 for pixel in diff.getdata() if any(channel != 0 for channel in pixel)
    )
    total_pixels = canvas_size[0] * canvas_size[1]
    difference_ratio = differing_pixels / total_pixels if total_pixels else 0.0
    exceeds_threshold = difference_ratio > args.threshold

    result = {
        "reference": str(Path(args.reference)),
        "runtime": str(Path(args.runtime)),
        "reference_size": reference_size,
        "runtime_size": runtime_size,
        "size_match": size_match,
        "differing_pixels": differing_pixels,
        "total_pixels": total_pixels,
        "pixel_difference_ratio": difference_ratio,
        "threshold": args.threshold,
        "exceeds_threshold": exceeds_threshold,
        "diff_image": str(Path(args.diff_image)) if args.diff_image else None,
        "semantic_review_required": True,
    }

    if args.diff_image:
        diff_path = Path(args.diff_image)
        diff_path.parent.mkdir(parents=True, exist_ok=True)
        diff.save(diff_path)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if exceeds_threshold or not size_match else 0


if __name__ == "__main__":
    raise SystemExit(main())

