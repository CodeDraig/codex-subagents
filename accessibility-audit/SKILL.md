---
name: accessibility-audit
description: Use when reviewing UI, workflows, forms, navigation, components, keyboard behavior, focus management, screen-reader semantics, ARIA, labels, contrast, motion, target size, WCAG issues, or accessibility regressions.
---

# Accessibility Audit

## Overview

Audit accessibility by user task. Prioritize barriers that prevent perceiving, navigating, understanding, correcting, or completing work.

## Workflow

1. Identify task, route/component, user goal, and assistive contexts.
2. Inspect keyboard path, focus order, semantics, labels, roles, names, announcements, contrast, target size, motion, and errors.
3. Reproduce issues with code references, DOM behavior, screenshots, or manual steps.
4. Prioritize by user impact.
5. Recommend concrete fixes and regression tests.

Use `references/a11y-checklist.md` for coverage.

## Output Contract

Return exactly: `Reviewed Task`, `Findings`, `Evidence`, `Remediation`, `Regression Tests`, `Residual Risk`.

## Stop Conditions

Stop when no user task, component, route, screenshot, or source artifact is available to evaluate.
