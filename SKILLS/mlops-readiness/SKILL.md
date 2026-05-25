---
name: mlops-readiness
description: Use when reviewing model registry, deployment, monitoring, reproducibility, drift, rollback, or model release controls that need approval boundaries and operational checks.
---

# MLOps Readiness

## Overview

Use this skill to assess whether a model is ready to move through registry, release, monitoring, and rollback controls without creating uncontrolled production risk.

## Workflow

1. Confirm the model version, registry record, promotion source, and whether the artifact in the registry is the exact one under review.
2. Check reproducibility inputs: code, data snapshot, environment, seeds, artifact hashes, and any required preprocessing version.
3. Review deployment shape, runtime dependencies, approval gates, and what can change without reapproval.
4. Define monitoring for quality, drift, freshness, latency, error rate, saturation, and the owner for each alert.
5. Verify rollback path, release ownership, mutation boundaries, and whether the inference SLO can be observed from the available telemetry.
6. Confirm that no registry promotion, deploy, or production mutation is implied before approval is granted.

Use `references/model-operations-checklist.md` for operations review.

## Output Contract

Return exactly: `Release State`, `Registry Status`, `Reproducibility`, `Monitoring Plan`, `Drift and Rollback`, `Approval Boundaries`, `Open Questions`, `Operational Evidence`, `Release Notes`.

## Stop Conditions

Stop when deployment, registry, production monitoring, rollback actions, or approval gates could mutate remote infrastructure or production behavior without explicit authorization.
