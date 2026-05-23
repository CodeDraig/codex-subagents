---
name: citation-integrity-review
description: Use when checking citations, quote accuracy, source provenance, citation formatting, and claim-to-source alignment in scholarly or formal writing.
---

# Citation Integrity Review

## Overview

Check whether citations support the claims attached to them. Prioritize provenance, accuracy, quote boundaries, source currency, and transparent uncertainty.

## Workflow

1. Inventory claims, citations, quotations, tables, figures, and source links.
2. Verify each claim against the cited source when source text is available.
3. Flag unsupported, overstated, miscited, stale, duplicate, retracted, or inaccessible sources.
4. Check citation format consistency and missing bibliographic fields.
5. Produce a correction log with source evidence and unresolved checks.

Use `references/citation-integrity-checklist.md` for claim and citation checks.

## Output Contract

Return exactly: `Citation Scope`, `Checked Claims`, `Citation Defects`, `Quote Issues`, `Format Issues`, `Retraction Or Currency Risks`, `Correction Log`, `Unverified Items`.

## Stop Conditions

Stop when asked to fabricate citations, assert inaccessible source contents, alter quotes beyond allowed edits, hide citation defects, or imply verification that was not performed.
