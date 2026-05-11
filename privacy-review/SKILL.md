---
name: privacy-review
description: Use when reviewing data collection, personal data, consent, retention, deletion, analytics, logs, AI prompts, exports, subprocessors, user rights, jurisdiction, privacy copy, data minimization, or feature changes that affect data handling.
---

# Privacy Review

## Overview

Review privacy as engineering risk, not legal advice. Identify what data exists, why it is needed, where it flows, how long it lives, who can access it, and how users can control it.

## Workflow

1. Inventory data categories and sources.
2. Map purpose, storage, access, sharing, retention, deletion, and export.
3. Check minimization and user expectations.
4. Review logs, analytics, AI prompts, support tooling, and third parties.
5. Produce remediation tasks and questions for counsel or policy owners.

Use `references/privacy-checklist.md` for coverage.

## Output Contract

Return exactly: `Data Inventory`, `Findings`, `Evidence`, `User Impact`, `Recommended Remediation`, `Counsel Questions`, `Residual Risk`.

## Stop Conditions

Stop when the feature creates sensitive-data collection, cross-border transfer, surveillance, or retention without policy approval.
