# Validation Checks

Install optional lightweight dependencies:

```bash
python3 -m pip install jsonschema Pillow
```

Validate templates:

```bash
python3 scripts/validate_registry.py --schema schemas/token_mapping.schema.json --file templates/token_mapping.example.json
python3 scripts/validate_registry.py --schema schemas/component_inventory.schema.json --file templates/component_inventory.example.json
python3 scripts/validate_report.py --schema schemas/component_diff_report.schema.json --file templates/component_diff_report.example.json
python3 scripts/validate_registry.py --schema schemas/component_registry.schema.json --file templates/component_registry.example.json
python3 scripts/validate_registry.py --schema schemas/screen_registry.schema.json --file templates/screen_registry.example.json
python3 scripts/validate_report.py --schema schemas/visual_diff_report.schema.json --file templates/visual_diff_report.example.json
python3 scripts/validate_registry.py --schema schemas/baseline_manifest.schema.json --file templates/baseline_manifest.example.json
python3 scripts/validate_registry.py --schema schemas/review_portal.schema.json --file templates/component_review_portal.example.json
python3 scripts/validate_registry.py --schema schemas/review_portal.schema.json --file templates/screen_review_portal.example.json
python3 scripts/validate_registry.py --schema schemas/design_fidelity_config.schema.json --file templates/design_fidelity.config.example.json
```

Generate a combined Review Portal:

```bash
python3 scripts/generate_review_portal.py \
  --component-gallery templates/component_review_portal.example.json \
  --screen-gallery templates/screen_review_portal.example.json \
  --output /tmp/design-fidelity-review-portal.html
```

Also validate all JSON in `examples/minimal/`, run every script with `--help`, and run the Skill validator.

Image comparison is auxiliary and must not be treated as semantic visual acceptance.

