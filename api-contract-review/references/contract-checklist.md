# Contract Checklist

## Request Shape

- Names are stable, explicit, and consistent with existing APIs.
- Required fields are minimal.
- Units, time zones, locale behavior, and precision are documented.
- Validation distinguishes malformed, unauthorized, forbidden, conflict, and not found.
- Bulk operations define partial failure behavior.

## Response Shape

- Success response includes only data the consumer is allowed to see.
- Null, empty, missing, default, and unknown states are intentional.
- Enums allow forward-compatible handling.
- Pagination has stable ordering and cursor semantics.
- Error response shape is machine-readable and documented.

## Operational Semantics

- Auth and authorization boundaries are explicit.
- Idempotency keys or duplicate handling are defined for retryable writes.
- Rate limits and retry behavior are documented.
- Webhooks and events define ordering, redelivery, deduplication, and schema version.
- Observability includes request IDs, correlation IDs, and safe logging fields.

## Test Targets

- Happy path.
- Invalid input.
- Unauthorized and forbidden.
- Missing resource.
- Conflict or duplicate write.
- Pagination boundaries.
- Backward compatibility fixture.
- Idempotent retry or duplicate event.
