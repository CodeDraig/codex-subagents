---
name: engineering-execution
description: Use when coordinating multi-agent execution, technical sequencing, integration risks, ownership boundaries, or delivery coherence.
---

# Engineering Execution

## Overview

Use this skill to keep a multi-slice implementation coherent. The goal is a clear execution order, stable ownership, and validation that matches the actual dependency graph.

## Workflow

1. Break the work into owned slices with explicit inputs and outputs.
2. Map dependencies, handoffs, and blocking assumptions.
3. Identify integration risks and shared surfaces early.
4. Define validation gates for each slice and for the combined delivery.
5. Confirm the final handoff is complete, reviewable, and reversible where needed.

Use `references/delivery-coordination-checklist.md` for execution planning.

## Output Contract

Return exactly: `Scope Decomposition`, `Ownership and Dependencies`, `Integration Risks`, `Validation Gates`, `Handoffs`, `Recommended Sequence`, `Open Questions`.

## Stop Conditions

Stop when ownership, dependency order, or validation gates are unresolved.
