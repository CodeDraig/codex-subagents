---
name: product-discovery
description: Use when shaping ambiguous product ideas, feature requests, user problems, opportunity framing, acceptance criteria, success metrics, non-goals, product risks, or deciding the smallest useful release before implementation planning.
---

# Product Discovery

## Overview

Convert fuzzy product intent into a testable software outcome. Keep discovery grounded in users, observable behavior, constraints, and decisions engineering can act on.

## Workflow

1. Frame the problem: identify target users, current pain, desired behavior change, and the decision needed now.
2. Separate evidence from assumptions. Mark each assumption as safe, risky, or must-confirm.
3. Define success: product metric, user-visible acceptance criteria, operational constraints, and anti-goals.
4. Cut scope: remove work that does not prove or deliver the core outcome.
5. Hand off: produce a brief that design, architecture, and implementation agents can execute.

Read `references/discovery-brief.md` when a full brief or assumption table is needed.

## Output Contract

Return exactly: `Problem Frame`, `Users And Jobs`, `Evidence`, `Assumptions`, `Acceptance Criteria`, `Non-Goals`, `Smallest Useful Release`, `Risks`, `Open Questions`.

## Stop Conditions

Stop when the target user, success metric, or required business constraint is unknown and would change the feature shape. Do not choose architecture or implementation details unless product constraints require them.
