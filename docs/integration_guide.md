# Integration Guide

The kit is framework-neutral and must be connected to an external iOS project.

## Copy The Skill

Copy `skills/figma_ios_design_fidelity/` into the target project's agent-skill location. Keep the referenced `docs/`, `schemas/`, and templates accessible, or adjust links in the copied Skill.

## Git Submodule

Add this repository as a submodule under a tools or agent directory:

```bash
git submodule add REPOSITORY_URL tools/design-fidelity-kit
```

Reference the Skill and schemas from that stable path. Pin and update the submodule through the target project's normal review process.

## External Tool Repository

Keep this repository separate and call its scripts with paths to files in the target project:

```bash
python3 DESIGN_FIDELITY_KIT/scripts/validate_registry.py \
  --schema DESIGN_FIDELITY_KIT/schemas/component_registry.schema.json \
  --file TARGET_PROJECT/design-fidelity/component_registry.json
```

## Project Setup

Create a target-project directory for:

- configuration
- token mapping
- component inventory and registry
- screen registry
- Figma reference screenshots
- iOS runtime screenshots
- component and screen reports
- Candidate and Accepted Baselines
- Component and Screen Review Portals

Do not copy fictional example names into production unchanged. Do not assume an existing UI-test target, snapshot library, SwiftUI preview, or UIKit harness; use the project's established architecture.

The recommended human-facing deliverable is the Review Portal. Token files, schemas, and reports are structured Agent records and do not require routine user inspection.
