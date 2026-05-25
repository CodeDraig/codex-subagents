---
name: citation-integrity-review
description: Use when checking citations, quote accuracy, bibliographic matching, source provenance, citation formatting, and claim-to-source alignment in scholarly or formal writing; not for stylistic editing or unsourced paraphrase cleanup.
---

# Citation Integrity Review

## Overview

Check whether citations support the claims attached to them. Prioritize provenance, quote boundaries, page or section evidence, source currency, and transparent uncertainty.

## Workflow

1. Inventory claims, citations, quotations, tables, figures, and source links.
2. Match each citation to the bibliographic record and verify author, title, venue, year, DOI or URL, and access date when available.
3. Verify the exact claim, quotation, page, or section against the cited source when source text is available.
4. Flag unsupported, overstated, miscited, stale, duplicate, retracted, corrected, preprint-only, inaccessible, or source-laundered items.
5. Produce a correction log with source evidence, quote boundaries, and unresolved checks.

Use `references/citation-integrity-checklist.md` for claim and citation checks.

## Decision Rules

- Every material claim needs a traceable supporting location; if the support is indirect, say so explicitly.
- Quotes must match verbatim and stay within the cited boundaries; note any paraphrase drift or excerpt truncation.
- Retractions, corrections, and expressions of concern outrank the original citation when assessing current reliability.
- If a source cannot be opened or the relevant page or section is missing for a high-stakes claim, mark it unverified rather than inferring content.

## Output Contract

Return exactly: `Citation Scope`, `Checked Claims`, `Citation Defects`, `Quote Issues`, `Format Issues`, `Retraction Or Currency Risks`, `Correction Log`, `Unverified Items`.
Include the source location used for each checked item and the reason each defect matters.

## Stop Conditions

Stop when asked to fabricate citations, assert inaccessible source contents, alter quotes beyond allowed edits, hide citation defects, or imply verification that was not performed.
