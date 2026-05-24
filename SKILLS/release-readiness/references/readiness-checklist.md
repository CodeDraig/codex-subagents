# Release Readiness Checklist

## Gates

- Builds pass.
- Targeted tests pass.
- Migrations reviewed and rehearsed if risky.
- Config and secrets known.
- Feature flags or staged rollout defined.
- Observability exists for success and failure.
- Rollback or mitigation is documented.
- Release notes and support impact are ready.

## Rollback Notes

- Can code be reverted?
- Can data be reverted?
- Can flag be disabled?
- Is client compatibility preserved?
- Who decides rollback?
