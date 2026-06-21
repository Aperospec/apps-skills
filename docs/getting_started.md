# Getting Started

## Prepare The Inputs

1. Identify the Figma file, component-library page, target frame node IDs, and relevant component node IDs.
2. Prepare the external iOS project and identify its local component-library location.
3. Copy the example configuration and replace all fictional values.
4. Prepare paths for `token_mapping.json`, inventories, registries, reports, baselines, and Review Portals.
5. Match the target device, OS version, scale, locale, color scheme, and data state.

The Agent should complete routine setup and generation automatically.

## Run The Component Quality Gate First

1. Extract token mappings and inventory the Figma component library.
2. Implement or audit local iOS components in dependency order.
3. Generate a Component Catalog.
4. Export Figma component reference screenshots.
5. Capture isolated iOS component runtime screenshots.
6. Create component diff reports and automatically fix traceable issues.
7. Set usable components to `ready_for_use`.
8. Create Candidate Baselines and the Component Review Portal.

Read `component_fidelity_workflow.md` for the full gate.

## Assemble And Validate A Screen

1. Add the screen and review regions to `screen_registry.json`.
2. Assemble the screen from `ready_for_use` registry components.
3. Export the Figma frame reference screenshot.
4. Capture the iOS runtime screenshot.
5. Generate a report stub:

```bash
python3 scripts/generate_report_stub.py \
  --screen-registry path/to/screen_registry.json \
  --screen-name SCREEN_NAME \
  --output path/to/visual_diff_report.json
```

6. Compare images as supporting evidence:

```bash
python3 scripts/compare_images.py \
  --reference references/SCREEN_NAME.png \
  --runtime runtime/SCREEN_NAME.png \
  --output reports/SCREEN_NAME.pixel-diff.json \
  --diff-image reports/SCREEN_NAME.diff.png
```

7. Perform semantic review and complete `visual_diff_report.json`.
8. Automatically patch traceable root causes.
9. Create a Candidate Baseline and Screen Review Portal.
10. Present only unresolved exceptions to the user.

The user reviews visual results through the portals. Internal JSON and schemas remain available for Agent traceback.
