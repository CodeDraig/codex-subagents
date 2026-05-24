---
name: ux-flow-mapping
description: Use when mapping user journeys, task flows, screen states, interaction states, empty/error/loading/recovery paths, permission flows, destructive actions, onboarding, forms, navigation, or UX acceptance criteria before UI implementation.
---

# UX Flow Mapping

## Overview

Map workflows before screens. A useful UX flow names the user goal, every meaningful state, the transitions between them, and the recovery path when things go wrong.

## Workflow

1. Identify user goal, actor, entry point, and exit condition.
2. Map the happy path.
3. Add states: first use, repeat use, loading, empty, partial, error, permission denied, success, interruption, and destructive confirmation.
4. Define copy and validation behavior for decision points.
5. Hand off state table and implementation implications.

Use `references/state-table.md` for complex flows.

## Output Contract

Return exactly: `User Goal`, `Flow Map`, `State Table`, `Edge Cases`, `Copy Guidance`, `Accessibility And Localization Notes`, `Implementation Implications`.

## Stop Conditions

Stop when the flow lacks a recoverable error path, hides destructive consequences, or requires unknown user information that changes the design.
