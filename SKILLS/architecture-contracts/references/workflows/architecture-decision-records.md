# Architecture Decision Records

## Purpose

Write ADRs that preserve why a decision was made, not just what was chosen. A good ADR makes future maintenance, reversal, and review easier.

## Workflow

1. Confirm decision fitness: one decision per ADR, and only when the options are genuinely viable or the tradeoff needs to be preserved for future review.
2. Capture context: constraints, forces, current architecture, triggering problem, and any owner or policy constraints that make some options impossible.
3. Compare options: include rejected alternatives with real tradeoffs, not placeholders. State why each option wins or loses on cost, risk, operability, or reversibility.
4. State decision and consequences: benefits, costs, risks, migration, and reversibility.
5. Define follow-up: validation, owners, rollout, review date, and what evidence would cause the decision to be revisited.

Read [adr-template.md](../artifacts/adr-template.md) when you need drafting and validation structure.

## Decision Rules

- If the work contains multiple unrelated decisions, split it into separate ADRs.
- If a decision is irreversible or expensive to reverse, say so explicitly and include the migration path or acceptance of the lock-in.
- Draft an unapproved choice with `Status: Proposed`, identify the approval owner and pending questions, and preserve the alternatives for review. A proposal does not authorize implementation.
- If the decision is already approved elsewhere, record that approval rather than recreating an unapproved rationale.
- Prefer concrete alternatives tables with option, strengths, weaknesses, and rejection reason.

## Output Contract

Return exactly: `Title`, `Status`, `Context`, `Decision`, `Alternatives`, `Consequences`, `Migration`, `Validation`, `Follow-Up`.

## Stop Conditions

Stop when the decision is actually multiple decisions, key constraints are unknown, or the ADR would hide an irreversible tradeoff. Stop before marking a choice `Accepted` or acting on it without the required owner approval; pending approval does not block a `Proposed` draft.
