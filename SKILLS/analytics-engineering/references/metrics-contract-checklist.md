# Metrics Contract Checklist

## Metric Definition

- Name the metric and the business question.
- Specify the grain, aggregation, and time window.
- Define the numerator, denominator, and any exclusions.
- State null, empty, and zero-value semantics.
- Record freshness and backfill expectations.

## Semantic Layer

- Record source tables, joins, and filter logic.
- Confirm naming, dimensionality, and lineage.
- Note whether the metric is reusable across tools or dashboards.
- Flag ownership of upstream fields and any dependency on derived tables.

## Transformation Checks

- Verify dbt-style model dependencies and staging steps.
- Check for duplicate counting, fanout, and grain mismatches.
- Confirm incremental or snapshot behavior if relevant.
- Validate that filters and joins preserve the intended population.

## Dashboard Validation

- Compare dashboard values to source totals.
- Validate known slices, empty states, and boundary dates.
- Check freshness, cache behavior, and stakeholder-visible labels.
- Reconcile any drill-down or exported query against the same metric definition.

## Change Management

- Identify downstream consumers and owners.
- Document breaking changes and migration timing.
- State the communication or approval needed before release.
- Record whether a backfill, dual-run, or cutover window is required.
