---
name: analytics-engineering
description: Use when defining metric contracts, semantic layers, BI-ready transformations, dashboard validation, dbt-style models, or stakeholder metric definitions.
---

# Analytics Engineering

## Overview

Use this skill to turn business definitions into durable analytics assets. Keep metric grain, ownership, transformation logic, and dashboard behavior explicit.

## Workflow

1. Restate the metric question, consumer, and business decision it supports.
2. Define the grain, dimensions, filters, and ownership before writing transformations.
3. Map the metric into a semantic layer or dbt-style model with stable naming and lineage.
4. Validate the dashboard or BI output against source totals, known slices, and edge cases.
5. Call out breaking changes, stakeholder impacts, and required communication before release.

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

## Stop Conditions

Stop when the metric grain is undefined, the contract would break downstream dashboards, the transformation logic cannot be traced to source data, or the stakeholder definition is missing.
