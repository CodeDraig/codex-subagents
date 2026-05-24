---
name: release-readiness
description: Use when checking releases, deployments, migrations, feature flags, rollout plans, rollback paths, release notes, package publishing, production readiness, support readiness, or go/no-go decisions before shipping software.
---

# Release Readiness

## Overview

Treat release as risk management. Verify what changes, how it rolls out, who detects failure, and how to reverse or mitigate it.

## Workflow

1. Identify release scope, artifacts, environments, and owners.
2. Check build, tests, migrations, config, flags, docs, support notes, and monitoring.
3. Define rollout stages and stop criteria.
4. Define rollback or mitigation, including irreversible steps.
5. Produce go/no-go recommendation.

Use `references/readiness-checklist.md` for release gates.

## Output Contract

Return exactly: `Readiness Status`, `Scope`, `Validation`, `Rollout Steps`, `Rollback Steps`, `Monitoring`, `Support Notes`, `Blockers`, `Go No-Go`.

## Stop Conditions

Stop when migrations, flags, credentials, rollback path, or production blast radius are undefined for a risky release.
