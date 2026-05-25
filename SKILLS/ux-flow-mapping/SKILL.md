---
name: ux-flow-mapping
description: Use when mapping user journeys, task flows, screen states, interaction states, empty/error/loading/recovery paths, permission flows, destructive actions, onboarding, forms, navigation, or UX acceptance criteria before UI implementation.
---

# UX Flow Mapping

## Overview

Map workflows before screens. A useful UX flow names the user goal, every meaningful state, the transitions between them, and the recovery path when things go wrong.

## Workflow

1. Identify user goal, actor, entry point, and exit condition. If the flow has multiple entrances or exits, list them separately.
2. Map the happy path and note the completion criteria for the task.
3. Add states: first use, repeat use, loading, empty, partial, error, permission denied, success, interruption, recovery, and destructive confirmation.
4. Define copy and validation behavior for decision points, including what the user can do next after each failure.
5. Hand off state table and implementation implications.

Use `references/state-table.md` for complex flows and state coverage.

## Decision Rules

- Every meaningful state needs an exit or recovery path.
- Permission-denied states must preserve user work and explain the next allowed action.
- Destructive confirmation copy must be specific about the effect, scope, and reversibility.
- If the flow depends on unknown user data, note the missing input rather than inventing the branch.

## Output Contract

Return exactly: `User Goal`, `Flow Map`, `State Table`, `Edge Cases`, `Copy Guidance`, `Accessibility And Localization Notes`, `Implementation Implications`.

## Stop Conditions

Stop when the flow lacks a recoverable error path, hides destructive consequences, or requires unknown user information that changes the design.
