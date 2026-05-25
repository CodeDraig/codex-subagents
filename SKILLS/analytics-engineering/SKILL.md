---
name: analytics-engineering
description: Use when defining metric contracts, semantic layers, BI-ready transformations, dashboard validation, dbt-style models, or stakeholder metric definitions that need grain, lineage, freshness, and change-control checks.
---

# Analytics Engineering

## Overview

Use this skill to turn business definitions into durable analytics assets. Keep metric grain, ownership, transformation logic, null semantics, freshness, and dashboard behavior explicit.

## Workflow

1. Restate the metric question, consumer, business decision, and the source-of-truth tables or systems it depends on.
2. Define the grain, dimensions, filters, exclusions, null and empty-state semantics, freshness target, backfill behavior, and ownership before writing transformations.
3. Map the metric into a semantic layer or dbt-style model with stable naming, lineage, joins, and aggregation rules.
4. Check for fanout, duplicate counting, grain mismatches, stale sources, and reconciliation gaps before treating the metric as reusable.
5. Validate the dashboard or BI output against source totals, known slices, boundary dates, cached views, and labels that stakeholders will read.
6. Call out breaking changes, consumer impacts, migration timing, and approval needs before release.

Use `references/metrics-contract-checklist.md` for contract checks.

## Output Contract

Return exactly these sections:

- `Question`
- `Metric Contract`
- `Semantic Layer`
- `Transformations`
- `Dashboard Validation`
- `Stakeholder Definitions`
- `Risks`
- `Validation Evidence`
- `Open Questions`

## Stop Conditions

Stop when the metric grain is undefined, null handling or freshness expectations are missing, the contract would break downstream dashboards, the transformation logic cannot be traced to source data, or the stakeholder definition is missing.
