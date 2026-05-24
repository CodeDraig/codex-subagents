---
name: implementation-planning
description: Use when turning approved designs, specs, ADRs, or product briefs into executable implementation plans with phases, file ownership, dependencies, validation commands, rollout gates, test coverage, and agent handoff boundaries.
---

# Implementation Planning

## Overview

Create implementation plans that are executable by agents with little context. Plans must make ownership, ordering, validation, and integration explicit.

## Workflow

1. Map files and responsibilities before tasks.
2. Identify dependencies, sequencing, and possible parallel work.
3. Split work into reviewable phases with disjoint write sets where possible.
4. Define validation for every phase: tests, build, lint, manual checks, migration checks, or review gates.
5. Add rollout, rollback, docs, and monitoring when user-facing or operational behavior changes.

Use `references/plan-template.md` for the full structure.

## Output Contract

Return exactly: `Plan Summary`, `File Map`, `Phases`, `Parallelization`, `Validation`, `Rollout And Rollback`, `Risks`, `Open Questions`.

## Stop Conditions

Stop when requirements contradict, file ownership collides, a phase has no validation path, or the design is not approved enough to implement safely.
