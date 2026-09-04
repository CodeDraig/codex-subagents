# Data Model Checklist

## Design Inputs

- Entities and relationships.
- Ownership and tenant boundaries.
- Read and write frequency.
- Query filters, sorting, pagination, and joins.
- Consistency requirements.
- Retention, deletion, export, and audit needs.

## Migration Planning

- Expand before contract.
- Backfill idempotently.
- Validate row counts and invariants.
- Keep rollback realistic; some data migrations are not reversible.
- Confirm who owns the source and destination schema before backfilling.
- Note whether cleanup can wait until the new path is fully verified.

## Validation Queries

- Orphan detection.
- Duplicate detection.
- Null or invalid state detection.
- Tenant isolation checks.
- Index usage or query plan checks.
- Retention or deletion verification when the feature includes lifecycle rules.
