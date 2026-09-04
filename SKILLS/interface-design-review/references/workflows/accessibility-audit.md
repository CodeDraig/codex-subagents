# Accessibility Audit

## Purpose

Audit accessibility by user task. Prioritize barriers that prevent perceiving, navigating, understanding, correcting, or completing work.

## Workflow

1. Identify task, route/component, user goal, and assistive contexts.
2. Inspect keyboard path, focus order, semantics, labels, roles, names, announcements, contrast, target size, motion, and errors.
3. Reproduce issues with code references, DOM behavior, screenshots, or manual steps.
4. Prioritize by user impact.
5. Recommend concrete fixes and regression tests.

Read [a11y-checklist.md](../artifacts/a11y-checklist.md) when the audit needs a complete task-level check and impact-based severity rating.

## Output Contract

Return exactly: `Reviewed Task`, `Findings`, `Evidence`, `Remediation`, `Regression Tests`, `Residual Risk`.

## Handoffs

Hand component or interaction fixes to the owning frontend or design-system role, and unresolved assistive-technology or policy interpretation to the named accessibility reviewer.

## Stop Conditions

Stop when no user task, component, route, screenshot, or source artifact is available to evaluate.
