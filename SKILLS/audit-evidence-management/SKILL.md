---
name: audit-evidence-management
description: Use when organizing audit evidence, control support, request lists, sampling support, and remediation tracking without issuing audit conclusions or control certifications.
---

# Audit Evidence Management

## Overview

Organize evidence packages for audit, compliance, or control review. Track provenance, sufficiency, and traceability without issuing audit conclusions, signing off controls, or hiding exceptions.

## Workflow

1. Restate audit scope, control or assertion, period, request ID, requester, owner, and deadline.
2. Inventory each item with source system, artifact path, preparer, reviewer, extraction date, access path, retention needs, and whether it is original, export, screenshot, memo, or attestation.
3. Map each item to the control objective, population, sample, test attribute, exception, remediation status, and management response.
4. Check sufficiency and consistency: confirm dates, totals, versions, sampling basis, stale screenshots, unverifiable exports, restricted data, and whether the evidence actually supports the stated control.
5. Produce the request-list status, evidence gaps, exception log, and owner questions needed to resolve open items or obtain approved replacements.

Use `references/audit-evidence-checklist.md` for evidence packaging.

## Output Contract

Return exactly: `Audit Scope`, `Request List`, `Evidence Inventory`, `Traceability Map`, `Sufficiency Review`, `Gaps`, `Exceptions`, `Owner Questions`.

## Stop Conditions

Stop when asked to issue audit opinions, certify controls, alter evidence, conceal exceptions, bypass auditor requests, or disclose restricted material without authorization.
