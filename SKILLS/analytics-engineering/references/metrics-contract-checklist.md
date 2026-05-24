# Metrics Contract Checklist

## Metric Definition

- Name the metric and the business question.
- Specify the grain, aggregation, and time window.
- Define the numerator, denominator, and any exclusions.

## Semantic Layer

- Record source tables, joins, and filter logic.
- Confirm naming, dimensionality, and lineage.
- Note whether the metric is reusable across tools or dashboards.

## Transformation Checks

- Verify dbt-style model dependencies and staging steps.
- Check for duplicate counting, fanout, and grain mismatches.
- Confirm incremental or snapshot behavior if relevant.

## Dashboard Validation

- Compare dashboard values to source totals.
- Validate known slices, empty states, and boundary dates.
- Check freshness, cache behavior, and stakeholder-visible labels.

## Change Management

- Identify downstream consumers and owners.
- Document breaking changes and migration timing.
- State the communication or approval needed before release.
