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
- Package or publish artifacts are verified when the release ships a distributable.
- Rollout owner and stop/hold criteria are explicit.

## Rollback Notes

- Can code be reverted?
- Can data be reverted?
- Can flag be disabled?
- Is client compatibility preserved?
- Who decides rollback?
- If rollback is partial, document the mitigation path and the residual risk.
