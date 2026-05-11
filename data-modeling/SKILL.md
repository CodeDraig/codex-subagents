---
name: data-modeling
description: Use when designing or reviewing entities, schemas, migrations, indexes, query access patterns, retention, deletion, lineage, data ownership, backfills, analytical models, caches, search indexes, or data consistency tradeoffs.
---

# Data Modeling

## Overview

Model data from invariants and access patterns, not object names. A good model protects ownership, consistency, deletion, performance, and future migrations.

## Workflow

1. Identify invariants, owners, lifecycle, and access patterns.
2. Choose storage shape: relational, document, event, analytical, cache, search, or hybrid.
3. Define constraints, indexes, consistency, deletion, retention, audit, and lineage.
4. Plan migrations and backfills with rollback limits.
5. Define validation queries and fixtures.

Use `references/model-checklist.md` for detailed review.

## Output Contract

Return exactly: `Access Patterns`, `Invariants`, `Recommended Model`, `Rejected Models`, `Migration Plan`, `Validation Queries`, `Operational Risks`.

## Stop Conditions

Stop when the model could lose required history, break tenant isolation, make deletion impossible, or require an irreversible backfill without approval.
