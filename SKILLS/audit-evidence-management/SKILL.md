---
name: audit-evidence-management
description: Use when organizing audit evidence, control support, request lists, evidence traceability, and remediation status without issuing audit conclusions.
---

# Audit Evidence Management

## Overview

Organize evidence packages for audit, compliance, or control review. Track provenance and completeness without issuing audit conclusions or signing off controls.

## Workflow

1. Restate audit scope, control or assertion, period, request ID, and owner.
2. Inventory evidence with source, date, preparer, reviewer, system, and access path.
3. Map evidence to control objective, population, sample, exception, and remediation status.
4. Flag gaps, stale artifacts, inconsistent evidence, or privileged/restricted material.
5. Produce a request-list status and owner question log.

Use `references/audit-evidence-checklist.md` for evidence packaging.

## Output Contract

Return exactly: `Audit Scope`, `Request List`, `Evidence Inventory`, `Traceability Map`, `Gaps`, `Exceptions`, `Owner Questions`.

## Stop Conditions

Stop when asked to issue audit opinions, certify controls, alter evidence, conceal exceptions, bypass auditor requests, or disclose restricted material without authorization.
