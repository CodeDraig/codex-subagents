---
name: api-contract-review
description: Use when designing or reviewing HTTP APIs, OpenAPI specs, GraphQL schemas, RPC interfaces, SDK surfaces, event schemas, webhooks, module contracts, versioning, compatibility, pagination, errors, retries, idempotency, or consumer-facing integration changes.
---

# API Contract Review

## Overview

Review contracts as promises to consumers. The skill focuses on whether an interface is understandable, compatible, secure, observable, and testable before implementation or release.

## Workflow

1. Identify the contract surface.
   - Route, schema, operation, event, webhook, SDK method, generated client, or internal module boundary.
   - Read the proposed contract and nearby existing patterns before judging it.

2. Identify consumers and compatibility constraints.
   - Human UI, mobile app, third-party client, backend service, batch job, SDK, webhook receiver, or internal module.
   - Determine whether this is new, additive, behavior-changing, or breaking.

3. Review shape and semantics.
   - Use `references/contract-checklist.md` for request/response, errors, auth, pagination, filtering, idempotency, versioning, and observability.
   - Prefer explicit fields and documented state transitions over ambiguous booleans or overloaded strings.

4. Review failure behavior.
   - Check validation errors, auth failures, rate limits, retries, partial success, timeouts, duplicate delivery, and backward-compatible defaults.

5. Define tests and examples.
   - Provide example requests/responses or event payloads.
   - Name required contract tests, schema validation, compatibility tests, and client fixture updates.

## Compatibility Rules

Additive changes are usually safe when existing consumers can ignore new fields and defaults preserve behavior.

Breaking changes include:

- Removing or renaming fields.
- Changing field type, unit, enum value meaning, nullability, or default behavior.
- Making optional input required.
- Changing status codes or error shapes clients rely on.
- Altering pagination, sorting, idempotency, or retry semantics.
- Emitting events with new required handling by existing consumers.

If a breaking change is required, include versioning, migration path, deprecation window, and client update plan.

## Output Contract

Return exactly these sections:

- `Contract Surface`: files, routes, schemas, operations, events, or module boundaries reviewed.
- `Consumers`: known callers and compatibility assumptions.
- `Findings`: severity-ordered issues with concrete contract impact.
- `Recommended Shape`: specific request, response, event, or schema changes.
- `Examples`: representative valid and invalid payloads.
- `Required Tests`: contract, compatibility, validation, auth, idempotency, and error tests.
- `Migration Notes`: deprecation, versioning, rollout, and client coordination.
- `Open Questions`: decisions that require product or owner input.

## Stop Conditions

Stop and ask the parent agent when:

- Consumer list is unknown and the contract is not clearly internal.
- A requested change is breaking but no migration path is approved.
- Auth, tenant isolation, data exposure, or privacy implications are ambiguous.
- The contract depends on guarantees the implementation cannot provide, such as exactly-once delivery without supporting infrastructure.
