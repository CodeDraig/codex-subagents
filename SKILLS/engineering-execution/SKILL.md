---
name: engineering-execution
description: Use when coordinating multi-agent execution, technical sequencing, integration risks, ownership boundaries, or delivery coherence.
---

# Engineering Execution

## Overview

Use this skill to keep a multi-slice implementation coherent. The goal is a clear execution order, stable ownership, and validation that matches the actual dependency graph.

## Workflow

1. Break the work into owned slices with explicit inputs and outputs.
2. Order slices by dependency and user-visible blast radius. Keep user-facing changes until prerequisite contracts, data paths, or shared helpers are stable unless the user change is the blocker.
3. Map dependencies, handoffs, and blocking assumptions. Call out shared files, APIs, configs, migrations, and generated artifacts so concurrent work can avoid collisions.
4. Preserve existing user changes and concurrent edits. Treat unknown local edits as intentional until verified, and prefer additive adjustments over rewrites on shared surfaces.
5. Define validation gates for each slice and for the combined delivery. Escalate when a slice has no validation path, needs environment access, or requires owner approval for integration testing.
6. Confirm the final handoff is complete, reviewable, and reversible where needed.

Use `references/delivery-coordination-checklist.md` for execution planning and conflict boundaries.

## Decision Rules

- If two slices touch the same file or schema, serialize the write path or split the file boundary before parallelizing.
- If a shared dependency is not ready, do not start downstream work that would only create rework.
- If rollout or verification depends on data migration, feature flags, or external systems, include a rehearsal or escalation step in the sequence.
- If changes could break a user-visible workflow, preserve the old path until the new one is validated.

## Output Contract

Return exactly: `Scope Decomposition`, `Ownership and Dependencies`, `Integration Risks`, `Validation Gates`, `Handoffs`, `Recommended Sequence`, `Open Questions`.

## Stop Conditions

Stop when ownership, dependency order, user-change preservation, or validation gates are unresolved.
