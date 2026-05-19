# Model Operations Checklist

## Registry and Versioning

- Model version is unique and traceable.
- Registry entry points to the exact artifact.
- Promotion lineage is recorded.

## Reproducibility

- Code revision is pinned.
- Data snapshot or training window is pinned.
- Environment and dependency versions are captured.
- Seeds and artifact hashes are stored.

## Monitoring

- Quality metric monitoring is defined.
- Drift or freshness thresholds are defined.
- Latency, error rate, and saturation checks exist.
- Alert ownership and escalation are clear.

## Rollback and Release Controls

- Rollback path is documented and tested.
- Safe deployment scope is defined.
- Approval gates are explicit.
- Production mutation requires authorization.

## Review Boundaries

- Remote infrastructure changes are out of scope.
- Production release actions stop at approval boundaries.
- Unsafe automation is not assumed.
