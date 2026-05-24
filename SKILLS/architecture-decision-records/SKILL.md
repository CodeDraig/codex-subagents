---
name: architecture-decision-records
description: Use when documenting, drafting, reviewing, or revising architecture decisions, ADRs, technical tradeoffs, irreversible choices, service boundaries, data ownership, migration paths, rejected alternatives, or decision history.
---

# Architecture Decision Records

## Overview

Write ADRs that preserve why a decision was made, not just what was chosen. A good ADR makes future maintenance, reversal, and review easier.

## Workflow

1. Confirm the decision: one decision per ADR.
2. Capture context: constraints, forces, current architecture, and triggering problem.
3. Compare options: include rejected alternatives with real tradeoffs.
4. State decision and consequences: benefits, costs, risks, migration, and reversibility.
5. Define follow-up: validation, owners, rollout, and review date if needed.

Use `references/adr-template.md` for drafting.

## Output Contract

Return exactly: `Title`, `Status`, `Context`, `Decision`, `Alternatives`, `Consequences`, `Migration`, `Validation`, `Follow-Up`.

## Stop Conditions

Stop when the decision is actually multiple decisions, key constraints are unknown, or the user asks to record an unapproved decision as final.
