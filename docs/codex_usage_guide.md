# Codex Usage Guide

Codex should execute the full workflow autonomously in the target iOS repository. It should not repeatedly ask the user to approve tokens, components, screenshots, reports, or routine fixes.

## Copyable Target-Project Task

```text
Use $figma-ios-design-fidelity.

Target project: TARGET_PROJECT_PATH
Figma file/page: FIGMA_FILE_OR_PAGE
Target screens: SCREEN_LIST
Allowed paths: ALLOWED_PATHS

Autonomously execute:
1. Agent Internal Design System Build
   - extract token_mapping.json
   - create component_inventory.json
   - implement or audit the local component library and Component Catalog
   - capture Figma and iOS component screenshots
   - generate component_diff_report.json
   - auto-fix traceable issues
   - update component_registry.json with ready_for_use status
   - create Candidate Baselines
   - generate the Component Review Portal
2. Agent Internal Screen Assembly
   - assemble screens only from ready_for_use components
   - select correct variants and states
   - do not handwrite approximate components or override component internals
3. Agent Internal Screen Fidelity QA
   - capture matching Figma and iOS screen screenshots
   - generate visual_diff_report.json
   - auto-fix traceable issues
   - create Candidate Baselines
   - generate the Screen Review Portal
4. Human Result Review
   - deliver both portals and Issues Requiring Human Review
5. Traceback & Repair
   - trace user feedback to screen assembly, component implementation,
     design token, Figma mapping, or renderer differences
   - repair the root cause and regenerate affected evidence

Only request user input for:
- unmapped_token
- unmapped_component
- conflicting_component_mapping
- figma_structure_ambiguous
- component_visual_blocker
- screen_visual_blocker
- design_system_conflict
- user_detected_issue

Do not ask the user to inspect Swift source, raw token data, JSON schema,
intermediate reports, or each construction step.

Finish with:
- Component Review Portal
- Screen Review Portal
- Issues Requiring Human Review
- self-check
- modified-scope summary
- Candidate and Accepted Baseline changes
```

