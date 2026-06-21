# Agent Task Template

```text
Use $figma-ios-design-fidelity and execute the workflow autonomously.

Target project: TARGET_PROJECT_PATH
Figma file/page: FIGMA_FILE_OR_PAGE
Target screens: SCREEN_LIST
Allowed paths: ALLOWED_PATHS

Build the internal design system first:
- extract token_mapping.json
- build component_inventory.json
- implement the local component library and Component Catalog
- capture and compare component screenshots
- generate component_diff_report.json
- auto-fix known root causes
- mark usable components ready_for_use
- create Candidate Baselines
- generate the Component Review Portal

Then assemble and validate screens:
- use only ready_for_use components
- capture and compare screen screenshots
- generate visual_diff_report.json
- auto-fix known root causes
- generate the Screen Review Portal

Do not ask for routine token, component, or stage-by-stage approval.
Ask only for explicit exception codes defined by the Skill.
Do not redesign, handwrite approximate components, override component internals,
or modify anything outside ALLOWED_PATHS.

Deliver both Review Portals, Issues Requiring Human Review, a self-check,
baseline changes, and the modified-scope summary.
```

