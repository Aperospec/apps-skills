#!/usr/bin/env python3
"""Validate a component or screen visual-difference report against JSON Schema."""

import argparse
import json
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Validate a visual-difference report against a JSON Schema."
    )
    parser.add_argument("--schema", required=True, help="Path to the report schema")
    parser.add_argument("--file", required=True, help="Path to the report JSON")
    return parser.parse_args()


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in '{path}': {exc}", file=sys.stderr)
        raise SystemExit(2)


def main():
    args = parse_args()
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        print(
            "Error: jsonschema is required. "
            "Install it with 'python3 -m pip install jsonschema'.",
            file=sys.stderr,
        )
        return 2

    schema = load_json(args.schema)
    report = load_json(args.file)
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print(f"Error: invalid schema '{args.schema}': {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(report), key=lambda error: list(error.path))
    if errors:
        print(f"Validation failed: {args.file}", file=sys.stderr)
        for error in errors:
            location = ".".join(str(item) for item in error.absolute_path) or "<root>"
            print(f"- {location}: {error.message}", file=sys.stderr)
        return 1

    print(f"Validation passed: {args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

