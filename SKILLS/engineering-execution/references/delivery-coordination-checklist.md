# Delivery Coordination Checklist

## Scope Decomposition

- Each slice has a clear owner.
- Each slice has a bounded output contract.
- Shared surfaces are listed once.
- User-facing changes are sequenced after prerequisite changes unless the user-facing work is the dependency.

## Ownership and Dependencies

- Dependency order is explicit.
- Blocking relationships are named.
- Cross-slice handoffs are unambiguous.
- Shared files, schemas, and generated artifacts are called out so concurrent work can avoid collisions.
- Existing user edits and concurrent changes are preserved unless the owner explicitly approves replacement.

## Integration Risks

- Shared files or APIs are called out.
- Merge conflicts or interface drift are anticipated.
- Rollout sequencing is stated.
- Any slice that has no validation path is marked blocked before execution.

## Validation Gates

- Validation commands or checks are mapped to each slice.
- Final combined validation is defined.
- Regressions have an owner for follow-up.
- Escalate when validation needs production access, external systems, or cross-team coordination.

## Handoffs and Readiness

- Downstream consumers are named.
- Open questions are limited to unresolved dependencies.
- Final acceptance criteria are explicit.
