# Acceptance Rules

Target 100% fidelity. Tolerances document renderer behavior; they do not authorize deliberate approximation.

The Agent applies these rules automatically. The user reviews final visual results and unresolved exceptions rather than approving every internal check.

## A. Must Match As Closely As Possible

- screen structure
- component type, hierarchy, variant, and state
- position, dimensions, spacing, padding, and gap
- font, typography token, size, weight, line height, and wrapping
- color, radius, and shadow tokens
- icons and image cropping
- TabBar, NavigationBar, Safe Area, and scrolling structure
- empty, loading, error, selected, and disabled states

At component level, review each supported variant and state independently. A screen cannot compensate for a failed component.

## B. Small Renderer Differences May Exist But Must Be Recorded

- font antialiasing
- shadow-edge rasterization
- alpha-blending edges
- 1-2 px system-rendering differences
- subtle Figma versus iOS rendering differences for the same font
- system status-bar rendering differences

Record these as `low` issues with measured context. Do not silently ignore them and do not use them to excuse structural, token, component, or state mismatches.

## C. Human Confirmation Is Required

- a Figma component has no accepted local mapping
- Figma structure conflicts with the existing iOS component library
- dynamic content changes height or layout
- localization changes line wrapping
- complex illustrations cannot be assessed reliably
- real data differs from reference mock data
- existing tokens cannot express the design
- the agent cannot determine the correct replacement component
- a `high` or `blocker` issue cannot be resolved without changing approved product behavior

Set report status to `requires_human_review`, identify the exact decision needed, and present it in the Review Portal. Do not create an approximation.
