---
name: academic-literature-review
description: Use when synthesizing scholarly literature, building search strategies, screening evidence, identifying gaps, or drafting source-backed research summaries; not for general web research, legal clearance, or unsourced opinion pieces.
---

# Academic Literature Review

## Overview

Support scholarly synthesis by planning a search, screening sources, grading evidence, and preserving uncertainty. Treat every claim as source-bound and stop when the available sources cannot support the requested conclusion.

## Workflow

1. Restate the research question, field, intended audience, date range, source types allowed, inclusion and exclusion criteria, and required citation style.
2. Build the search plan: databases, keywords, synonyms, controlled terms, citation chasing, and exclusion filters; record what was searched so gaps are visible.
3. Screen sources by relevance and quality. Capture source type, venue, publication status, population or corpus, sample size, method, funding, and conflicts when relevant.
4. Grade evidence by strength and risk of bias. Separate direct support from inference, note replication status, compare disagreement, and flag external-validity limits.
5. Synthesize by theme and claim, then list gaps, follow-up searches, and uncertainty that remains after screening.

Use `references/literature-review-checklist.md` for source and synthesis checks.

## Decision Rules

- Prefer primary studies when the question asks about effects, associations, or mechanisms; use reviews and meta-analyses to map the field.
- Down-rank small, uncontrolled, convenience-sample, or indirect-population studies unless the request is explicitly exploratory.
- Separate preprints, accepted manuscripts, and published versions; do not merge them into one evidence item without labeling the status.
- If the source text is inaccessible or the citation metadata is incomplete for a critical claim, stop and flag the item as unverified.

## Output Contract

Return exactly: `Research Question`, `Search Scope`, `Source Inventory`, `Evidence Themes`, `Disagreements`, `Gaps`, `Caveats`, `Citation Needs`.
Include search sources, screening rationale, evidence strength, and unresolved uncertainty in the relevant sections.

## Stop Conditions

Stop when asked to invent citations, overstate unsupported claims, hide uncertainty, write as if expert peer review has occurred, or use inaccessible sources as if verified.
