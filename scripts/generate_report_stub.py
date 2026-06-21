#!/usr/bin/env python3
"""Generate a blank screen visual-difference report from a screen registry."""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a visual_diff_report.json stub from screen_registry.json."
    )
    parser.add_argument(
        "--screen-registry", required=True, help="Path to screen_registry.json"
    )
    parser.add_argument(
        "--screen-name",
        help="Screen name to select; required when the registry has multiple screens",
    )
    parser.add_argument("--output", required=True, help="Output report path")
    return parser.parse_args()


def load_registry(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Error: registry not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"Error: invalid registry JSON: {exc}", file=sys.stderr)
        raise SystemExit(2)


def select_screen(registry, screen_name):
    screens = registry.get("screens")
    if not isinstance(screens, list) or not screens:
        print("Error: registry must contain a non-empty 'screens' array.", file=sys.stderr)
        raise SystemExit(2)

    if screen_name:
        matches = [screen for screen in screens if screen.get("screen_name") == screen_name]
        if len(matches) != 1:
            print(
                f"Error: expected one screen named '{screen_name}', found {len(matches)}.",
                file=sys.stderr,
            )
            raise SystemExit(2)
        return matches[0]

    if len(screens) != 1:
        print(
            "Error: --screen-name is required when the registry contains multiple screens.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return screens[0]


def main():
    args = parse_args()
    registry = load_registry(args.screen_registry)
    screen = select_screen(registry, args.screen_name)
    screen_name = screen.get("screen_name")
    required = [
        "screen_name",
        "reference_screenshot_path",
        "runtime_screenshot_path",
    ]
    missing = [key for key in required if not screen.get(key)]
    if missing:
        print(
            "Error: selected screen is missing: " + ", ".join(missing),
            file=sys.stderr,
        )
        return 2

    report = {
        "report_id": f"{screen_name}-REPLACE_WITH_REPORT_ID",
        "screen_name": screen_name,
        "figma_reference": screen["reference_screenshot_path"],
        "runtime_screenshot": screen["runtime_screenshot_path"],
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "failed",
        "issues": [],
        "notes": (
            "Stub only. Perform screenshot comparison and semantic review before "
            "setting the final status."
        ),
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Created report stub: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

