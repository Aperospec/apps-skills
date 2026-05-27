---
name: figma-component-delivery
description: "Use when any agent is asked to implement, refine, or verify Figma-driven UI components for app development. Enforces a Figma-first evidence workflow: read repo workflow docs and active task docs, inspect exact Figma node chains, classify all targets before coding, preserve component hierarchy, avoid design guessing, and finish with build plus visual verification."
---

# Figma Component Delivery

Use this skill for component-focused UI work when Figma is the design source of truth and the target is implementation code such as SwiftUI.

## Read First

Before any code changes:

- read the repo workflow doc if one exists, such as `AGENT_WORKFLOW.md`
- read the active task doc if one exists, such as `AGENT_TASK_*.md`

Those files define repo-specific guardrails. This skill operationalizes them and fills the gap when the repo does not already enforce a strict design-delivery process.

## Non-Negotiable Rules

- Figma is the geometry source of truth.
- Do not write or change hard-coded geometry values until the exact Figma node chain has been inspected.
- If a required node or measurement cannot be obtained, stop and report a blocker.
- Do not use SF Symbols, semantic substitutes, or "close enough" placeholders as the final implementation for Figma-defined custom icons.
- Do not flatten parent, child, and inner component layers into one redraw when Figma defines them separately.
- Do not expand a component task into a full page unless the task explicitly asks for that.
- Do not treat cross-system properties as direct equivalents without proof.
Example: Figma vector `strokeWeight` is not automatically equivalent to SF Symbol `Font.Weight`.
- Do not treat build success, grep counts, file diffs, or code structure as a substitute for visual acceptance.
- Do not report work as complete until the required visual acceptance step for the current scope is finished.
- Do not print secrets, tokens, signed URLs, or raw credentials in reports. Redact them.

## Required Preflight Audit

Before implementation, the agent must produce a complete target audit for the current task:

1. Confirm the exact working directory and repo path.
2. Confirm the exact files expected to change.
3. Pull the full Figma target set for the task, not just one sample node.
4. Classify every target into one of:
   - `VECTOR`
   - `IMAGE-SVG`
   - `TEXT`
   - `IMAGE`
   - `GROUP`
5. Decide the implementation strategy for each target before coding:
   - `custom Shape`
   - `Path parser`
   - `text rendering`
   - `imported bitmap asset`
   - `blocked`

If this audit is incomplete, coding must not start.

## Required Execution Order

1. Read the repo workflow doc and active task doc when present.
2. Restate the task scope and hard constraints.
3. Complete the preflight audit for the full target set in scope.
4. Inspect the exact Figma page and node chain.
5. Extract only the measurements needed for implementation:
   - width and height
   - corner radius
   - padding and spacing
   - relative alignment or offsets
   - inner element sizes
   - color values only when the task depends on them
6. Report the inspected node chain, classification, and measured values before coding.
7. Implement only the in-scope component chain or batch.
8. Build the app when the environment allows it.
9. Run visual verification against the exact target scope when the environment allows it.
10. Report residual mismatch risks honestly.

## Batch Discipline

- Large icon or component sets must be split into explicit batches before implementation begins.
- Each batch must have a fixed target list.
- A batch report may contain only:
  - `completed`
  - `blocked`
  - `pending next batch`
- Do not silently pull later-scope targets into the current batch.
- If a later-batch item gets implemented early, report it as `early implemented, pending later batch`; do not count it as complete in the current batch.

## Implementation Guidance

- Preserve independent code structures for each Figma layer that must remain separately controllable.
- Prefer direct geometric implementation over loose stylistic approximation when the design depends on exact shape.
- If system primitives are only approximate, say so explicitly.
- If custom geometry is needed for accuracy, implement the geometry directly.
- When a prior assumption is disproved by Figma inspection, correct the assumption instead of defending the earlier implementation.
- If a general parser or shared shape strategy fails for a target, move that target to a dedicated implementation path instead of forcing a bad fit.
- If a target is `IMAGE` in Figma, use exported image assets for the final implementation; do not leave an SF Symbol stand-in.

## Credential And Tooling Checks

- Before the first Figma-dependent code change, confirm the live Figma access path is valid.
- Prefer the current MCP session path over cached REST credentials.
- If a credential or access path fails, stop and report it immediately instead of repeatedly retrying stale credentials.
- If a token or credential expires mid-task, revalidate the active MCP chain before declaring a blocker.

## Temporary Verification Changes

- Any code change made only to assist verification must be explicitly marked as temporary in the report.
- Temporary verification changes must be restored in the same work cycle after verification.
- Final delivery state must match the intended product or dev-preview state, not the temporary verification layout.
- If a temporary verification change affects an already accepted UI section, restoration is mandatory before completion can be reported.

## Verification Standard

Do not claim `exact match`, `fully identical`, or `no risk` unless visual comparison has actually been performed.

Use these labels precisely:

- `Measured match`: values were taken from Figma and implemented in code.
- `Geometric high-fidelity`: structure and geometry closely match, but final pixel rendering may still vary.
- `Visually verified`: output was compared against Figma and no visible difference was found at the checked scale.

If visual verification has not been done, state that clearly and list likely residual risks such as antialiasing, subpixel alignment, or renderer differences.

For multi-item grids or icon libraries:

- Final acceptance requires a screenshot or equivalent direct capture of the full target set in its rendered UI.
- Partial viewport checks do not count as final acceptance for the whole set.
- Code-level checks such as grep, counts, or asset presence may support a conclusion, but may never replace final visual acceptance.

## Output Contract

Use this report structure after each task:

1. Relevant workflow constraints followed
2. Working directory and files in scope
3. Figma page and exact inspected node chain and target classification
4. Measured Figma values used
5. Changed files
6. Visual or structural adjustments made
7. Build result
8. Visual verification result
9. Remaining mismatch risks

## Blocker Contract

If blocked, report:

1. Missing node or missing measurement
2. Whether the blocker is data, credential, tooling, routing, or environment related
3. Why the data could not be obtained
4. What work was intentionally not started
5. What exact next access or clarification is needed

## Completion Rules

Do not report `done`, `complete`, or `accepted` unless all of the following are true:

- the scoped implementation is present in code
- temporary verification changes have been restored
- build succeeded after restoration
- the scoped visual acceptance step has been completed
- any residual mismatches are either zero or explicitly accepted by the user

## When Not To Use This Skill

- Pure product logic work with no Figma dependency
- Broad app refactors unrelated to component fidelity
- Tasks explicitly scoped to non-visual backend or data behavior
