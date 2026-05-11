# Data Model Checklist

## Design Inputs

- Entities and relationships.
- Read and write frequency.
- Query filters, sorting, pagination, and joins.
- Consistency requirements.
- Ownership and tenant boundaries.
- Retention, deletion, export, and audit needs.

## Migration Planning

- Expand before contract.
- Backfill idempotently.
- Validate row counts and invariants.
- Keep rollback realistic; some data migrations are not reversible.

## Validation Queries

- Orphan detection.
- Duplicate detection.
- Null or invalid state detection.
- Tenant isolation checks.
- Index usage or query plan checks.
