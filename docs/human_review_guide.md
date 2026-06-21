# Human Review Guide

Human review is result-oriented. The Agent completes routine design-system extraction, implementation, capture, comparison, reporting, and repair without asking for approval at every step.

## What The User Reviews

- Component Review Portal
- Screen Review Portal
- Issues Requiring Human Review

The user is not expected to inspect source code, raw token data, schemas, intermediate JSON, or script logs.

## When The Agent Escalates

Escalate only for:

- `unmapped_token`
- `unmapped_component`
- `conflicting_component_mapping`
- `figma_structure_ambiguous`
- `component_visual_blocker`
- `screen_visual_blocker`
- `design_system_conflict`
- `user_detected_issue`

Provide both screenshots, affected scope, registry/report references, attempted traceback, and the exact decision needed.

## When The User Finds A Problem

Trace the issue through screen assembly, component implementation, design token, Figma mapping, and renderer differences. Repair the earliest incorrect layer, regenerate affected evidence and portals, and report downstream impact.

Human feedback does not authorize a downstream visual patch when the root cause is a shared component or token.

