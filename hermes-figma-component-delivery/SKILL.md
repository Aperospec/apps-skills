---
name: hermes-figma-component-delivery
description: Use when Hermes or Codex is asked to implement, refine, or verify Figma-driven UI components for app development. Enforces a Figma-first evidence workflow: read repo workflow docs and active task docs if present, inspect exact Figma node chains, extract measurable values before coding, preserve component hierarchy, avoid guessing design values, and finish with build plus visual verification.
---

# Hermes Figma Component Delivery

Use this skill for component-focused UI work when Figma is the design source of truth and the target is implementation code such as SwiftUI.

## Read First

Before any code changes:

- read the repo workflow doc if one exists, such as `HERMES_WORKFLOW.md`
- read the active task doc if one exists, such as `HERMES_TASK_*.md`

Those files define repo-specific guardrails. This skill operationalizes them and fills the gap when the repo does not already enforce a strict design-delivery process.

## Non-Negotiable Rules

- Figma is the geometry source of truth.
- Do not write or change hard-coded geometry values until the exact Figma node chain has been inspected.
- If a required node or measurement cannot be obtained, stop and report a blocker.
- Do not flatten parent, child, and inner component layers into one redraw when Figma defines them separately.
- Do not expand a component task into a full page unless the task explicitly asks for that.
- Do not treat cross-system properties as direct equivalents without proof.
Example: Figma vector `strokeWeight` is not automatically equivalent to SF Symbol `Font.Weight`.

## Required Execution Order

1. Read the repo workflow doc and active task doc when present.
2. Restate the task scope and hard constraints.
3. Inspect the exact Figma page and node chain.
4. Extract only the measurements needed for implementation:
   - width and height
   - corner radius
   - padding and spacing
   - relative alignment or offsets
   - inner element sizes
   - color values only when the task depends on them
5. Report the inspected node chain and measured values before coding.
6. Implement only the in-scope component chain.
7. Build the app when the environment allows it.
8. Run visual verification against the Figma target when the environment allows it.
9. Report residual mismatch risks honestly.

## Implementation Guidance

- Preserve independent code structures for each Figma layer that must remain separately controllable.
- Prefer direct geometric implementation over loose stylistic approximation when the design depends on exact shape.
- If system primitives are only approximate, say so explicitly.
- If custom geometry is needed for accuracy, implement the geometry directly.
- When a prior assumption is disproved by Figma inspection, correct the assumption instead of defending the earlier implementation.

## Verification Standard

Do not claim `exact match`, `fully identical`, or `no risk` unless visual comparison has actually been performed.

Use these labels precisely:

- `Measured match`: values were taken from Figma and implemented in code.
- `Geometric high-fidelity`: structure and geometry closely match, but final pixel rendering may still vary.
- `Visually verified`: output was compared against Figma and no visible difference was found at the checked scale.

If visual verification has not been done, state that clearly and list likely residual risks such as antialiasing, subpixel alignment, or renderer differences.

## Output Contract

Use this report structure after each task:

1. Relevant workflow constraints followed
2. Figma page and exact inspected node chain
3. Measured Figma values used
4. Changed files
5. Visual or structural adjustments made
6. Build result
7. Visual verification result
8. Remaining mismatch risks

## Blocker Contract

If blocked, report:

1. Missing node or missing measurement
2. Why the data could not be obtained
3. What work was intentionally not started
4. What exact next access or clarification is needed

## When Not To Use This Skill

- Pure product logic work with no Figma dependency
- Broad app refactors unrelated to component fidelity
- Tasks explicitly scoped to non-visual backend or data behavior
