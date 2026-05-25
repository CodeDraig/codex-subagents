---
name: data-modeling
description: Use when designing or reviewing entities, schemas, migrations, indexes, query access patterns, retention, deletion, lineage, data ownership, backfills, analytical models, caches, search indexes, or data consistency tradeoffs.
---

# Data Modeling

## Overview

Model data from invariants and access patterns, not object names. A good model protects ownership, consistency, deletion, performance, and future migrations.

## Workflow

1. Identify invariants, owners, lifecycle, and access patterns. Map which service or team owns each entity and which users or tenants can mutate it.
2. Choose storage shape: relational, document, event, analytical, cache, search, or hybrid.
3. Define constraints, indexes, consistency, deletion, retention, audit, and lineage. Make query filters, sorts, joins, and cardinality explicit before naming tables or collections.
4. Plan migrations and backfills with rollback limits. Prefer expand-before-contract, idempotent backfills, and phased cleanup over one-shot rewrites.
5. Define validation queries and fixtures. Include orphan, duplicate, null, tenant-isolation, and index-usage checks.

Use `references/model-checklist.md` for review coverage and validation queries.

## Decision Rules

- Model tenant or ownership boundaries first; never bury them in application code alone.
- Index for the actual query shape, not theoretical future use. If a query path does not exist yet, do not pre-optimise it without evidence.
- If deletion, retention, or export are requirements, design them into the primary model rather than treating them as afterthoughts.
- If a backfill can fail midway, require an idempotent rerun and a measurable checkpoint before cleanup.

## Output Contract

Return exactly: `Access Patterns`, `Invariants`, `Recommended Model`, `Rejected Models`, `Migration Plan`, `Validation Queries`, `Operational Risks`.

## Stop Conditions

Stop when the model could lose required history, break tenant isolation, make deletion impossible, or require an irreversible backfill without approval.
