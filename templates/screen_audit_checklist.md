# Screen Audit Checklist

## Component Gate

- [ ] The required Figma components exist in `component_inventory.json`.
- [ ] Core components completed automatic visual checks.
- [ ] Required components are `ready_for_use` in `component_registry.json`.
- [ ] No screen-local approximate component replaces an unmapped component.

## Capture Conditions

- [ ] The screen maps to the correct Figma frame.
- [ ] Device size and scale match.
- [ ] OS/system conditions are recorded.
- [ ] Color scheme matches.
- [ ] Locale and content state match.
- [ ] Safe Area, NavigationBar, and TabBar conditions match.

## Visual Review

- [ ] Main structure and hierarchy match.
- [ ] Every Figma component instance uses the corresponding `ready_for_use` component.
- [ ] Component variant and state are correct.
- [ ] Spacing, color, typography, radius, and shadow use the resolved token mapping.
- [ ] Icons are correct.
- [ ] Image ratio and cropping are correct.
- [ ] Empty, loading, and error states are correct.
- [ ] No component internals are overridden from the screen.

## Evidence And Scope

- [ ] Runtime screenshot exists.
- [ ] Figma reference screenshot exists.
- [ ] Screenshot comparison is complete.
- [ ] `visual_diff_report.json` is updated and schema-valid.
- [ ] No unresolved `high` or `blocker` issue remains.
- [ ] Every `requires_human_review` issue names a concrete decision.
- [ ] Candidate Baseline is updated.
- [ ] Screen Review Portal is regenerated.
- [ ] No out-of-scope file or behavior was modified.
