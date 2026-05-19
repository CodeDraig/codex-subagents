# Delivery Coordination Checklist

## Scope Decomposition

- Each slice has a clear owner.
- Each slice has a bounded output contract.
- Shared surfaces are listed once.

## Ownership and Dependencies

- Dependency order is explicit.
- Blocking relationships are named.
- Cross-slice handoffs are unambiguous.

## Integration Risks

- Shared files or APIs are called out.
- Merge conflicts or interface drift are anticipated.
- Rollout sequencing is stated.

## Validation Gates

- Validation commands or checks are mapped to each slice.
- Final combined validation is defined.
- Regressions have an owner for follow-up.

## Handoffs and Readiness

- Downstream consumers are named.
- Open questions are limited to unresolved dependencies.
- Final acceptance criteria are explicit.
