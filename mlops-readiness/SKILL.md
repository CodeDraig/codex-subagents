---
name: mlops-readiness
description: Use when reviewing model registry, deployment, monitoring, reproducibility, drift, rollback, or model release controls.
---

# MLOps Readiness

## Overview

Use this skill to assess whether a model is ready to move through registry, release, monitoring, and rollback controls without creating uncontrolled production risk.

## Workflow

1. Confirm the model version, registry record, and promotion source.
2. Check reproducibility inputs: code, data snapshot, environment, seeds, and artifact hashes.
3. Review deployment shape, runtime dependencies, and approval gates.
4. Define monitoring for quality, drift, freshness, latency, and failure rates.
5. Verify rollback path, release ownership, and mutation boundaries.

Use `references/model-operations-checklist.md` for operations review.

## Output Contract

Return exactly: `Release State`, `Registry Status`, `Reproducibility`, `Monitoring Plan`, `Drift and Rollback`, `Approval Boundaries`, `Open Questions`.

## Stop Conditions

Stop when deployment, registry, production monitoring, or rollback actions could mutate remote infrastructure or production behavior without approval.
