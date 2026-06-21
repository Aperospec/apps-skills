# Figma-to-iOS Design Fidelity Kit

This repository is a standalone workflow kit for AI Agents implementing iOS interfaces from completed Figma designs with high visual fidelity.

It is not an iOS application, contains no business screens, and does not assume SwiftUI, UIKit, or a specific testing stack.

## Operating Model

```text
Agent builds and validates automatically
  -> Agent generates visual review results
  -> User reviews final results and exceptions
  -> Agent traces feedback to the root cause and repairs it
```

This kit is not designed to make the user approve every token, component, report, or implementation step. The Agent owns routine design-system extraction, component implementation, screenshot capture, visual analysis, report maintenance, and fixable repairs.

## What The User Reviews

- Component Review Portal
- Screen Review Portal
- Issues Requiring Human Review

The user does not need to inspect token files, schemas, source code, intermediate JSON, or script logs unless requesting traceback details.

## Core Principles

- Figma is the sole visual source of truth.
- MCP data is structural evidence, not final visual acceptance.
- Build or audit the local component library before assembling dependent screens.
- Use `ready_for_use` components for screen assembly.
- Compare Figma reference screenshots with iOS runtime screenshots.
- Generate Candidate Baselines automatically for regression tracking.
- Upgrade to Accepted Baselines after a batch or delivery is explicitly accepted, not through per-component approval.
- Escalate only explicit exceptions that the Agent cannot resolve safely.
- Trace user-detected issues through screen assembly, component implementation, design tokens, Figma mapping, and renderer differences.
- Fix root causes rather than applying downstream visual overrides.

## Five-Phase Workflow

1. Agent Internal Design System Build
2. Agent Internal Screen Assembly
3. Agent Internal Screen Fidelity QA
4. Human Result Review
5. Traceback & Repair

See `docs/workflow.md` and `docs/component_fidelity_workflow.md`.

## Review Portal

The Review Portal is the recommended human-facing entry point. It displays Figma references, iOS runtime screenshots, optional diff images, Agent conclusions, quality status, exceptions, and traceability references.

Generate a combined static portal:

```bash
python3 scripts/generate_review_portal.py \
  --component-gallery templates/component_review_portal.example.json \
  --screen-gallery templates/screen_review_portal.example.json \
  --output review-portal.html
```

Read `docs/review_portal.md` for the manifest and presentation contract.

## Repository Layout

- `skills/figma_ios_design_fidelity/`: executable Agent protocol.
- `docs/`: autonomous workflow, acceptance, review, integration, and Codex guidance.
- `schemas/`: contracts for tokens, registries, reports, baselines, and portals.
- `templates/`: fictional examples and reusable task/checklist templates.
- `scripts/`: lightweight image comparison, validation, report, and portal tools.
- `figma/`: reference screenshot export guidance.
- `ios/`: runtime screenshot capture guidance.
- `examples/minimal/`: a stack-neutral fictional integration example.

## External Project Integration

Use the kit as copied Agent instructions, a Git submodule, or an external tools repository. Replace every fictional name, ID, path, and token.

The Agent should autonomously produce:

- `token_mapping.json`
- component inventory and registry
- component and screen screenshots
- component and screen diff reports
- Candidate Baselines
- Component and Screen Review Portals
- exception and scope summaries

Automated pixel comparison is supporting evidence only. Semantic visual inspection and exception-driven human review remain required.

