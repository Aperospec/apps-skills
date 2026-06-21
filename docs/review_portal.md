# Review Portal

The Review Portal is the primary human-facing output of the Design Fidelity Kit. It lets users review visual results without reading source code, schemas, token files, JSON records, or script logs.

It may be static HTML or Markdown with an image directory. Structured JSON remains an Agent and tooling record.

## Component Review Portal

Each component entry displays:

- component name and Figma component name
- Figma reference screenshot
- iOS runtime screenshot
- optional diff image
- Agent visual-check conclusion
- current quality status
- exception summary
- component registry reference
- component diff-report reference
- related token or traceback references

Use status `ready_for_use`, `needs_fix`, `requires_human_review`, `blocked`, or `deprecated`.

## Screen Review Portal

Each screen entry displays:

- screen name
- Figma reference screenshot
- iOS runtime screenshot
- optional diff image
- Agent visual-check conclusion
- current status
- exception summary
- screen registry reference
- visual diff-report reference
- related component and traceback references

## Issues Requiring Human Review

Collect entries with `requires_human_review: true` in a prominent section. State the exception code, visual evidence, affected scope, and exact decision needed.

Routine `needs_fix` issues should be repaired automatically before presentation when feasible.

## Generation

Create a manifest conforming to `schemas/review_portal.schema.json`, then run:

```bash
python3 scripts/generate_review_portal.py \
  --component-gallery path/to/component-review.json \
  --screen-gallery path/to/screen-review.json \
  --output path/to/review-portal.html
```

Either gallery input is optional, but at least one is required. Image paths may be relative to the generated HTML or absolute/file URLs appropriate for the target environment.

