---
name: book-metadata-packaging
description: Use when preparing book metadata, positioning, back-cover copy, BISAC/category suggestions, keywords, comparable-title notes, retailer descriptions, accessibility metadata, launch assets, and publication-package checks; not for deceptive marketing or guaranteed sales claims.
---

# Book Metadata Packaging

## Overview

Prepare discoverability and publication-package materials that accurately represent the book, align with production metadata, and preserve rights, accessibility, and platform constraints.

## Workflow

1. Restate title, subtitle, author, format, edition, audience, genre or category, publication path, price or territorial assumptions, ISBN status, and platform constraints.
2. Align core metadata across manuscript, cover, title page, copyright, ISBN record, retailer fields, catalog copy, author bio, keywords, and accessibility data.
3. Draft or review positioning assets: short description, long description, back-cover copy, author bio, comp titles, category rationale, keywords, tagline, and launch blurbs.
4. Check claims, endorsements, permissions, age/category fit, sensitive content flags, series numbering, accessibility fields, alt text, and retailer or distributor limitations.
5. Produce a package tracker with metadata gaps, copy options, validation needs, owner approvals, and handoffs to production, permissions, fact-checking, or audience packaging.

Use `references/book-metadata-packaging-checklist.md` for package fields and blocker checks.

## Decision Rules

- Metadata must match across title, subtitle, author name, contributors, edition, ISBN, series, trim or format, and publication date before release.
- Marketing copy should be accurate to the manuscript; do not invent awards, credentials, endorsements, reviews, sales rankings, or comparative performance.
- Category and keyword suggestions must reflect reader expectations and platform rules, not only search-volume opportunism.
- Treat missing permissions, unverifiable endorsements, cover/text mismatch, accessibility gaps, and title-page metadata conflicts as release blockers.
- For scholarly or journal work, hand submission-specific package requirements to `journal-submission-specialist`.

## Output Contract

Return exactly: `Package Scope`, `Metadata Alignment`, `Positioning Copy`, `Category And Keywords`, `Asset Gaps`, `Risks And Approvals`, `Files Changed`, `Handoffs`.
Include field names, platform or file locations, and whether copy is draft, revised, or ready for owner review.

## Stop Conditions

Stop when asked to fabricate endorsements, reviews, credentials, sales claims, awards, accessibility compliance, permissions status, or platform approval.
