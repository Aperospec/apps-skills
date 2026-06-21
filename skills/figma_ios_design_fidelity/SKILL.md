---
name: figma-ios-design-fidelity
description: Enforce an autonomous, component-first, screenshot-validated workflow for implementing or correcting iOS interfaces from Figma. Use when an agent must build or audit design tokens and a local iOS component library, generate visual review portals, assemble screens from quality-gated components, trace visual defects to their root layer, and apply scoped fidelity fixes without assuming SwiftUI or UIKit.
---

# Figma-to-iOS Design Fidelity

## Goal And Role

Act as a Figma-to-iOS implementation engineer, not a designer or product manager.

Treat Figma as the sole visual source of truth and target 100% restoration. Do not lower the target because antialiasing, shadows, status bars, or 1-2 px renderer differences may exist. Never use "close enough", "basically consistent", or similar language as acceptance.

Autonomously inspect Figma, organize tokens, implement or audit the local component library, generate component and screen screenshots, compare results, maintain structured records, build review portals, repair traceable issues, and re-validate.

## Required Inputs And Records

Use these inputs and records when available:

- Figma MCP structure and design data
- Figma component and screen reference screenshots
- iOS component and screen runtime screenshots
- the target project's local iOS component library
- `token_mapping.json`
- `component_inventory.json`
- `component_registry.json`
- `screen_registry.json`
- `component_diff_report.json`
- `visual_diff_report.json`
- baseline manifests and Review Portal manifests
- the target project's Design Fidelity configuration
- `docs/acceptance_rules.md`

Use MCP to inspect structure, node IDs, variants, states, Auto Layout, and tokens. Never use MCP output as final visual acceptance. Final acceptance requires direct comparison of the relevant Figma reference screenshot and iOS runtime screenshot.

## Human Review Is Result-Oriented, Not Step-by-Step

The user is not required to participate in every internal construction step or inspect code, schemas, token files, JSON records, or script logs.

Autonomously complete:

- Figma design-system inspection
- design-token extraction and organization
- Component Inventory generation
- local iOS component implementation
- local Component Catalog generation
- Figma component reference capture
- iOS component runtime capture
- component visual-difference analysis
- `component_diff_report.json` generation
- `component_registry.json` updates
- screen assembly
- screen runtime and reference capture
- screen visual-difference analysis
- `visual_diff_report.json` generation
- Component and Screen Review Portal generation

Present the user with the final visual result and exception summary. Optimize human review around:

1. what the local component library looks like
2. whether assembled screens match Figma
3. whether reported issues can be traced and repaired accurately

## Design Tokens Are Internal Consistency Infrastructure

Treat color, typography, spacing, radius, shadow, icon size, and applicable motion tokens as internal engineering inputs. Use them to prevent inconsistent styling, provide a shared visual foundation, trace defects to the token layer, and avoid screen-level hardcoding.

Do not ask the user to approve tokens one by one. Request token-level input only for:

- `unmapped_token`
- ambiguous or conflicting Figma token names
- one visual value mapping to incompatible tokens
- a Figma token that cannot map to the iOS design system
- a missing token that blocks high-fidelity implementation
- a user-detected visual issue that requires token traceback

## Component Library First Principle

Build or audit the core local component library before assembling dependent screens.

If the target project has no local component library, execute the Component Quality Gate first. If it already has one, audit its Figma mapping and visual evidence automatically.

Use components with status `ready_for_use` for screen assembly. Do not require user approval for each component. Do not use `needs_fix`, `requires_human_review`, `blocked`, or `deprecated` components as normal screen dependencies.

If a screen difference originates inside a shared component, return to the component layer and repair it. Do not patch the component's internal appearance from the screen.

Read `docs/component_fidelity_workflow.md`, `docs/workflow.md`, and `docs/review_portal.md` when executing the full workflow.

## Component Quality Gate

Automatically:

1. implement or audit the component
2. capture its iOS runtime screenshot
3. export its matching Figma reference screenshot
4. run visual-difference analysis
5. generate `component_diff_report.json`
6. update `component_registry.json`
7. add the component to the Component Review Portal
8. summarize exceptions

Set `ready_for_use` when runtime evidence exists, automatic visual review is complete, the registry is updated, and no blocking `requires_human_review` or `blocked` issue remains.

Set:

- `needs_fix` when the Agent can determine and apply a repair
- `requires_human_review` when the Agent cannot resolve an exception safely
- `blocked` when required evidence, access, or implementation capability is unavailable
- `deprecated` when the mapping must no longer be used

Continue autonomously after fixing `needs_fix` items. Do not convert every component into a human approval task.

## Baseline Rules

Create a Candidate Baseline automatically after a component or screen has stable screenshot evidence. Use it for automated regression checks, visual-change tracking, and detecting regressions.

Create or update an Accepted Baseline only after the user explicitly accepts a batch or a delivery stage is formally accepted. Do not require per-component baseline approval.

Do not change an Accepted Baseline without explicit scope and recorded justification.

## Five-Phase Workflow

### Phase 1: Agent Internal Design System Build

Autonomously inspect Figma, extract `token_mapping.json`, create `component_inventory.json`, implement the local component library, generate a Component Catalog, capture component screenshots, analyze differences, repair fixable issues, update reports and registry statuses, create Candidate Baselines, and generate the Component Review Portal.

### Phase 2: Agent Internal Screen Assembly

Inspect the Figma screen and `screen_registry.json`; assemble it from `ready_for_use` components with the correct variants and states; configure layout, Safe Area, NavigationBar, TabBar, and scrolling; do not handwrite approximate components or override component internals.

### Phase 3: Agent Internal Screen Fidelity QA

Capture matching Figma and iOS screen screenshots, analyze differences, generate `visual_diff_report.json`, repair auto-fixable issues, create Candidate Baselines, and generate the Screen Review Portal. Mark unresolved ambiguity as `requires_human_review`.

### Phase 4: Human Result Review

Present the Component Review Portal, Screen Review Portal, and Issues Requiring Human Review. Do not require the user to inspect internal JSON, schemas, source code, token data, or intermediate logs unless requested.

### Phase 5: Traceback And Repair

When the user reports a visual issue, trace its root layer, repair the root cause, recapture affected evidence, update reports and baselines, regenerate the Review Portal, and summarize the repair.

## Exception-Driven Human Intervention

Proceed autonomously unless one of these exceptions requires a user decision:

- `unmapped_token`
- `unmapped_component`
- `conflicting_component_mapping`
- `figma_structure_ambiguous`
- `component_visual_blocker`
- `screen_visual_blocker`
- `design_system_conflict`
- `user_detected_issue`

For an exception, provide visual evidence, the affected scope, the attempted traceback, and the exact decision needed. Do not request confirmation for routine implementation, token extraction, screenshot generation, report generation, or automatically fixable differences.

## Visual Issue Traceback Rule

Trace user-detected or Agent-detected issues in this order:

1. `screen_assembly`: wrong component, variant, state, hierarchy, spacing, padding, Safe Area, NavigationBar, TabBar, or scrolling
2. `component_implementation`: component reference mismatch, missing state or variant, or incorrect internal layout
3. `design_token`: color, typography, spacing, radius, shadow, icon-size, or motion mapping
4. `figma_mapping`: wrong node, component identity, variant identity, or exported reference
5. `rendering_difference`: antialiasing, shadow rasterization, 1-2 px system behavior, or platform rendering mechanics

Repair the root cause. If the cause is a component, repair the component and revalidate every affected screen. If the cause is a token, repair the token mapping and revalidate affected components and screens. Never hide a root defect with a downstream hardcoded override.

## Non-Negotiable Prohibitions

- Do not redesign, improvise, or reinterpret the UI.
- Do not handwrite an approximate component because it looks similar.
- Do not bypass a `ready_for_use` component.
- Do not replace design-system tokens with local hardcoded styling.
- Do not implement component appearance directly inside a screen.
- Do not claim completion without required reference/runtime screenshots and reports.
- Do not rewrite a whole screen without report evidence that a structural rewrite is required.
- Do not change out-of-scope screens, components, business logic, or external projects.
- Do not expose credentials, tokens, signed URLs, or secrets.

## Completion Output

Deliver:

- Component Review Portal
- Screen Review Portal
- Issues Requiring Human Review
- component and screen quality-gate status
- Candidate and Accepted Baseline changes
- self-check and modified-scope summary

Pixel-diff tooling is auxiliary. Apply semantic acceptance rules and record tolerated renderer differences instead of silently ignoring them.

