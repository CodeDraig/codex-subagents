---
name: dependency-risk-triage
description: Use when evaluating dependency upgrades, lockfile changes, package-manager diffs, security advisories, transitive dependency risk, runtime compatibility, licensing concerns, deprecations, or supply-chain impact before editing manifests or accepting automated upgrade PRs.
---

# Dependency Risk Triage

## Overview

Assess dependency changes as engineering risk, not housekeeping. The goal is to decide whether to upgrade, pin, replace, patch, defer, or remove a dependency with enough evidence to support review and rollback.

## Workflow

1. Identify the dependency surface.
   - Read manifests, lockfiles, package-manager config, advisory text, and changelog or release notes.
   - Capture package name, current version, target version, direct or transitive status, runtime or dev-only usage, and owning module.

2. Classify the change.
   - Security advisory, bugfix, minor upgrade, major upgrade, ecosystem migration, deprecation response, license change, lockfile churn, or dependency removal.
   - Use `references/risk-model.md` when severity, compatibility, or supply-chain exposure is unclear.

3. Inspect compatibility and blast radius.
   - Search for imports, CLI usage, config references, generated files, peer dependency requirements, engine/runtime requirements, native extensions, browser support, and CI images.
   - Treat package-manager lockfile rewrites as code changes that can alter transitive behavior.

4. Decide the action.
   - Upgrade when the risk is understood and validation is feasible.
   - Pin when upstream churn or transitive resolution creates instability.
   - Replace when the dependency is abandoned, unmaintained, toxic to security posture, or too broad for the need.
   - Defer only with a concrete reason, owner, and follow-up trigger.

5. Validate narrowly.
   - Run the smallest test/build/lint/typecheck set that exercises the dependency.
   - If unavailable, explain the missing verification surface and propose the closest manual check.

## Security Advisory Handling

For advisory-driven work:

- Verify the advisory source and affected version range.
- Confirm the vulnerable package is actually present in the resolved dependency graph.
- Determine whether vulnerable code is reachable in this project.
- Check whether the fixed version introduces breaking changes.
- Prefer official patched versions over forks or broad overrides unless time pressure requires a temporary mitigation.

Do not claim a vulnerability is fixed until the manifest and lockfile resolve to a non-affected version and a relevant validation command has run.

## Output Contract

Return exactly these sections:

- `Dependency Surface`: package, current version, target version, direct/transitive status, manifests and lockfiles.
- `Reason For Change`: advisory, feature, bugfix, deprecation, maintenance, or removal.
- `Risk Rating`: Low, Medium, High, or Critical with rationale.
- `Compatibility Notes`: runtime, peer deps, API changes, native builds, licensing, and platform impact.
- `Validation`: commands run, results, and missing coverage.
- `Recommended Action`: upgrade, pin, replace, patch, defer, or remove.
- `Rollback`: how to undo safely.
- `Open Questions`: decisions that require owner approval.

## Stop Conditions

Stop and ask the parent agent before editing when:

- The change alters runtime support, public APIs, license obligations, native build requirements, authentication, cryptography, or deployment infrastructure.
- The lockfile changes many unrelated packages and the package manager reason is unclear.
- A security advisory is high or critical and reachability cannot be assessed.
- Validation would require network, production access, paid services, or destructive operations.
