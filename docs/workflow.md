# End-To-End Workflow

The kit keeps component-first engineering while making routine execution autonomous. Human review is result-oriented and exception-driven.

## Phase 1: Agent Internal Design System Build

The Agent automatically:

1. reads the Figma design system
2. extracts or organizes design tokens in `token_mapping.json`
3. creates `component_inventory.json`
4. implements or audits the local iOS component library
5. generates a local Component Catalog
6. exports Figma component reference screenshots
7. captures iOS component runtime screenshots
8. performs component-level visual analysis
9. creates `component_diff_report.json`
10. repairs auto-fixable differences
11. updates `component_registry.json`
12. creates Candidate Baselines
13. generates the Component Review Portal

Components become `ready_for_use` through the automatic Component Quality Gate. Routine work does not wait for per-component user approval.

## Phase 2: Agent Internal Screen Assembly

The Agent reads the exact Figma frame and `screen_registry.json`, then assembles the screen from `ready_for_use` components using correct variants and states.

It configures hierarchy, spacing, Safe Area, NavigationBar, TabBar, and scrolling without hand-built component substitutes or screen-level component-internal overrides.

## Phase 3: Agent Internal Screen Fidelity QA

The Agent:

1. exports the Figma screen reference
2. captures the iOS runtime screenshot
3. performs pixel-assisted and semantic visual analysis
4. creates `visual_diff_report.json`
5. repairs auto-fixable issues
6. repeats capture and comparison
7. creates Candidate Baselines
8. generates the Screen Review Portal

Use this repair order:

1. screen assembly
2. component implementation
3. design token
4. Figma mapping
5. rendering-difference classification

Repair shared component or token defects at their source and revalidate downstream consumers.

## Phase 4: Human Result Review

The user primarily reviews:

- Component Review Portal
- Screen Review Portal
- Issues Requiring Human Review

The user does not need to inspect token files, schemas, Swift source, JSON details, or script logs unless requesting traceback details.

## Phase 5: Traceback And Repair

When the user identifies a problem, the Agent:

1. classifies it as screen assembly, component implementation, design token, Figma mapping, or rendering difference
2. repairs the root cause
3. regenerates affected screenshots
4. updates diff reports and Candidate Baselines
5. regenerates the Review Portal
6. reports the repair and affected scope

Only explicit exception codes in the Skill should interrupt autonomous execution.

