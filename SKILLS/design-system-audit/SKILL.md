---
name: design-system-audit
description: Use when auditing UI components, shared primitives, design tokens, visual consistency, spacing, typography, color, interaction states, accessibility drift, component APIs, duplicate patterns, or design-system adoption in a frontend codebase.
---

# Design System Audit

## Overview

Audit design systems by comparing actual product UI to reusable primitives and tokens. Focus on drift that affects maintainability, accessibility, consistency, or user comprehension.

## Workflow

1. Inventory relevant components, tokens, styles, and representative consumers. Include one-offs, wrapper components, and any local overrides that bypass the shared system.
2. Identify duplicates, token drift, inconsistent states, inaccessible variants, and missing coverage for default, hover, focus, active, disabled, loading, error, and empty states.
3. Check component APIs for over-specific props, unstable dimensions, hard-coded values, and migration risk.
4. Capture evidence with screenshots, code references, and any breakpoint or responsive behavior that changes the component shape.
5. Prioritize findings by blast radius and user impact.
6. Recommend narrow fixes and migration steps.

Use `references/audit-checklist.md` for component, token, state, and evidence coverage.

## Decision Rules

- Prefer semantic tokens over literal colors, spacing, radius, and typography values.
- Treat inaccessible focus, contrast, motion, or keyboard behavior as a blocker even if the visual design looks consistent.
- If a shared component change would affect many consumers, name the migration path and whether a temporary wrapper is safer.
- If a state is missing from the inventory, confirm whether it is intentionally unsupported before recommending a new variant.

## Output Contract

Return exactly: `Scope`, `Inventory`, `Findings`, `Recommended Fixes`, `Migration Notes`, `Validation`, `Residual Risk`.

## Stop Conditions

Stop when requested changes would alter brand-critical tokens, shared component behavior, or many consumers without approval and migration scope.
