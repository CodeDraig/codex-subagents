# Book Metadata Packaging

## Purpose

Prepare discoverability and publication-package materials that accurately represent the book, align with production metadata, and preserve rights, accessibility, and platform constraints.

## Intake

Identify the authoritative metadata record or unresolved candidates, manuscript and cover versions, formats/editions, supplied platform specifications, owned fields, and exact copy components requested.

## Workflow

1. Restate title, subtitle, author, format, edition, audience, genre or category, publication path, price or territorial assumptions, ISBN status, and platform constraints.
2. Align core metadata across manuscript, cover, title page, copyright, ISBN record, retailer fields, catalog copy, author bio, keywords, and accessibility data.
3. Draft or review positioning assets: short description, long description, back-cover copy, author bio, comp titles, category rationale, keywords, tagline, and launch blurbs.
4. Check claims, endorsements, permissions, age/category fit, sensitive content flags, series numbering, accessibility fields, alt text, and retailer or distributor limitations.
5. Produce a package tracker with metadata gaps, copy options, validation needs, owner approvals, and handoffs to production, permissions, fact-checking, or audience packaging.

Read [book-metadata-packaging-checklist.md](../artifacts/book-metadata-packaging-checklist.md) when you need package fields and blocker checks.

## Decision Rules

- Metadata must match across title, subtitle, author name, contributors, edition, ISBN, series, trim or format, and publication date before release.
- Marketing copy should be accurate to the manuscript; do not invent awards, credentials, endorsements, reviews, sales rankings, or comparative performance.
- Category and keyword suggestions must reflect reader expectations and platform rules, not only search-volume opportunism.
- Treat missing permissions, unverifiable endorsements, cover/text mismatch, accessibility gaps, and title-page metadata conflicts as release blockers.
- For scholarly or journal work, hand submission-specific package requirements to `journal-submission-specialist`.

- Prepare known metadata and requested copy while unresolved fields remain visible. Do not label the complete package aligned until its actual records agree.

## Verification

- Compare title, subtitle, contributors, edition, identifiers, series, and dates across the actual supplied files.
- Check positioning copy against the manuscript and verified author facts; count required field lengths using the destination’s actual instructions.
- Distinguish suggested categories/accessibility fields from verified classifications or conformance; report unavailable records instead of claiming alignment.

## Output Contract

Return exactly: `Package Scope`, `Metadata Alignment`, `Positioning Copy`, `Category And Keywords`, `Asset Gaps`, `Risks And Approvals`, `Files Changed`, `Handoffs`.
Include field names, platform or file locations, and whether copy is draft, revised, or ready for owner review.

## Stop Conditions

Stop when asked to fabricate endorsements, reviews, credentials, sales claims, awards, accessibility compliance, permissions status, or platform approval.
