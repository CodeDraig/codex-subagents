---
name: design-system-audit
description: Use when auditing UI components, shared primitives, design tokens, visual consistency, spacing, typography, color, interaction states, accessibility drift, component APIs, duplicate patterns, or design-system adoption in a frontend codebase.
---

# Design System Audit

## Overview

Audit design systems by comparing actual product UI to reusable primitives and tokens. Focus on drift that affects maintainability, accessibility, consistency, or user comprehension.

## Workflow

1. Inventory relevant components, tokens, styles, and representative consumers.
2. Identify duplicates, one-offs, token drift, inconsistent states, and inaccessible variants.
3. Check component APIs for over-specific props, missing states, unstable dimensions, and migration risk.
4. Prioritize findings by blast radius and user impact.
5. Recommend narrow fixes and migration steps.

Use `references/audit-checklist.md` for review coverage.

## Output Contract

Return exactly: `Scope`, `Inventory`, `Findings`, `Recommended Fixes`, `Migration Notes`, `Validation`, `Residual Risk`.

## Stop Conditions

Stop when requested changes would alter brand-critical tokens, shared component behavior, or many consumers without approval and migration scope.
