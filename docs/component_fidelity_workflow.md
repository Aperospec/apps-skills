# Component Fidelity Workflow

The Component Quality Gate turns the Figma design system into a visually checked local iOS component library before dependent screens are assembled. It is an Agent-operated quality process, not a per-component human approval process.

## Automated Flow

```text
Figma design system
  -> token_mapping.json
  -> component_inventory.json
  -> local iOS components and Component Catalog
  -> Figma and iOS component screenshots
  -> component_diff_report.json
  -> Agent repairs
  -> component_registry.json
  -> Candidate Baseline
  -> Component Review Portal
  -> screen assembly with ready_for_use components
```

## Inspect And Inventory

Read component sets, variants, states, styles, tokens, assets, dimensions, and Auto Layout. Create one inventory entry per component family and prioritize base components before composite and page-specific components.

The Agent performs this inventory automatically. The user is not asked to approve each token or component record.

## Organize Tokens

Map Figma colors, typography, spacing, radii, shadows, icon sizes, and applicable motion values to the target project's token system.

Tokens are internal consistency infrastructure. Escalate only when a token is unmapped, conflicting, ambiguous, missing, or implicated by a user-detected issue.

## Implement Components And Catalog

Create or complete components in the target project's established component-library architecture without assuming SwiftUI or UIKit. Support major Figma variants and states and render them in a Component Catalog, fixture, preview, or test surface suitable for screenshots.

Do not draw component appearance inside a screen or add approximate substitutes.

## Capture, Compare, And Repair

For every reviewed variant and state:

1. export the Figma component reference
2. capture the isolated iOS runtime result
3. compare dimensions, layout, typography, tokens, icons, images, shadows, and states
4. write `component_diff_report.json`
5. automatically repair issues whose root cause is known
6. recapture and update the report

Pixel comparison is supporting evidence. Semantic inspection determines whether the correct component, variant, state, and tokens were used.

## Component Status

- `ready_for_use`: automatic evidence checks completed and no blocking exception remains
- `needs_fix`: the Agent identified a repair and must complete it before normal use
- `requires_human_review`: ambiguity requires a user decision
- `blocked`: evidence, access, or implementation capability prevents use
- `deprecated`: the component must no longer be selected

Screen assembly may continue without per-component user confirmation when required components are `ready_for_use`.

## Baselines And Review Portal

Generate a Candidate Baseline after stable component evidence exists. Upgrade it to an Accepted Baseline only after a batch or delivery is explicitly accepted; do not request approval for each component baseline.

Add each component to the Component Review Portal with reference, runtime, optional diff image, Agent conclusion, current status, exception summary, registry/report references, and token traceback references.

## Root-Cause Repair

Repair in this order:

1. component implementation
2. variant and state behavior
3. token mapping
4. component structure
5. local component parameters

Never compensate for a component defect with screen-specific overrides. Revalidate every affected screen after a shared component or token changes.

