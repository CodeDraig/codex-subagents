---
name: release-readiness
description: Use when checking releases, deployments, migrations, feature flags, rollout plans, rollback paths, release notes, package publishing, production readiness, support readiness, or go/no-go decisions before shipping software.
---

# Release Readiness

## Overview

Treat release as risk management. Verify what changes, how it rolls out, who detects failure, and how to reverse or mitigate it.

## Workflow

1. Identify release scope, artifacts, environments, and owners.
2. Check build, tests, migrations, config, flags, package/publish artifacts, docs, support notes, and monitoring.
3. Define rollout stages and stop criteria, including staged exposure, feature flags, and who can halt the release.
4. Define rollback or mitigation, including irreversible steps and whether data changes can be undone.
5. Produce go/no-go recommendation with explicit blockers and recovery assumptions.

Use `references/readiness-checklist.md` for release gates and rollback notes.

## Decision Rules

- Do not call a release ready if the rollback path is unknown, untested, or relies on an unavailable owner.
- Treat migrations, package publishing, and client compatibility as release blockers until rehearsed or explicitly accepted.
- If support or release notes are missing for user-visible changes, the release is not ready.
- If flags or staged rollout are part of the plan, verify the default state and the cutover path.

## Output Contract

Return exactly: `Readiness Status`, `Scope`, `Validation`, `Rollout Steps`, `Rollback Steps`, `Monitoring`, `Support Notes`, `Blockers`, `Go No-Go`.

## Stop Conditions

Stop when migrations, flags, credentials, package artifacts, rollback path, or production blast radius are undefined for a risky release.
