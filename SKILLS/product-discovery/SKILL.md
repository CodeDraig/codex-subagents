---
name: product-discovery
description: Use when shaping ambiguous product ideas, feature requests, user problems, opportunity framing, acceptance criteria, success metrics, non-goals, product risks, or deciding the smallest useful release before implementation planning.
---

# Product Discovery

## Overview

Convert fuzzy product intent into a testable software outcome. Keep discovery grounded in users, observable behavior, constraints, risk, and decisions engineering can act on.

## Workflow

1. Frame the problem: identify target users, current pain, desired behavior change, current workaround, and the decision needed now.
2. Separate evidence from assumptions. Mark each assumption as safe, risky, or must-confirm using `references/discovery-brief.md`.
3. Define success: product metric, user-visible acceptance criteria, operational constraints, quality bar, and anti-goals.
4. Select validation: interview, prototype, concierge test, instrumentation, usability test, support-ticket analysis, or narrow build slice.
5. Cut scope: remove work that does not prove or deliver the core outcome; mark what can be manual, mocked, deferred, or explicitly out of scope.
6. Hand off: produce a brief that design, architecture, and implementation agents can execute.

Read `references/discovery-brief.md` when a full brief or assumption table is needed.

## Decision Rules

- Treat the target user, success metric, and business constraint as must-confirm when any one would materially change the feature shape.
- Acceptance criteria must describe visible behavior, including empty, error, permission, loading, recovery, and audit states when relevant.
- Do not turn preferences into requirements without evidence. Label them as hypotheses and choose a validation method.
- The smallest useful release should prove one user job or operational outcome; split unrelated personas, workflows, or admin goals.
- Handoff UX flow ambiguity to `ux-flow-architect`, shared component implications to `design-system-engineer`, architecture tradeoffs to `systems-architect`, and execution sequencing to `technical-planner`.

## Validation Guidance

- Prefer direct evidence: user interviews, support tickets, product analytics, sales notes, usage traces, field observations, or prototype tests.
- Choose the cheapest validation that can change the decision: paper prototype for flow, clickable prototype for comprehension, concierge process for feasibility, instrumented slice for behavior.
- If discovery depends on market norms or competitor behavior, hand that research to `market-researcher` using $competitive-research.
- Stop before implementation when the release cannot be evaluated by a reviewer, test, metric, or named owner decision.

## Output Contract

Return exactly: `Problem Frame`, `Users And Jobs`, `Evidence`, `Assumptions`, `Validation Plan`, `Acceptance Criteria`, `Non-Goals`, `Smallest Useful Release`, `Risks`, `Handoffs`, `Open Questions`.

## Stop Conditions

Stop when the target user, success metric, or required business constraint is unknown and would change the feature shape. Do not choose architecture or implementation details unless product constraints require them.
