# Dependency Risk Model

## Rating Guide

| Rating | Use When | Typical Action |
| --- | --- | --- |
| Low | Dev-only tool, patch/minor upgrade, no breaking notes, narrow usage, validation available. | Upgrade with focused validation. |
| Medium | Runtime package, peer dependency changes, broad imports, moderate transitive churn, or weak tests. | Upgrade in a bounded PR with targeted checks and rollback. |
| High | Major upgrade, auth/security/crypto/data path, native module, runtime support change, abandoned package, or large lockfile churn. | Plan explicitly; consider staged rollout or replacement. |
| Critical | Active exploit, sensitive data exposure, remote code execution, malicious package signal, compromised maintainer, or no safe patched version. | Escalate; mitigate immediately and document residual risk. |

## Evidence Checklist

- Manifest files changed.
- Lockfiles changed.
- Package-manager version and install mode.
- Direct import or CLI usage.
- Peer dependency and engine requirements.
- Changelog, release notes, migration guide, or advisory source.
- License and maintenance status when relevant.
- Tests or commands that exercise affected behavior.

## Common Traps

- Treating transitive upgrades as harmless because source imports did not change.
- Accepting automated PRs without checking lockfile churn.
- Upgrading a dev tool that changes generated production output.
- Fixing an advisory by adding an override that the package manager does not actually apply.
- Ignoring peer dependency warnings because installation succeeded.
