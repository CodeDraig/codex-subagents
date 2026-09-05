# Indexing Workflows

## Purpose

Create and revise a usable index from inspected text with deliberate term selection, cross-references, and locators tied to a stable source version.

## Intake

Capture index type/readers, supplied text/proofs, version and pagination/anchor scheme, house style, scope/exclusions, and whether locators are final or provisional.

## Workflow

1. Identify concepts, names, works, and reader access points from substantive discussion rather than indexing every word occurrence.
2. Construct headings and subheadings with consistent terminology, disambiguation, synonyms, and cross-references that help the intended reader find material.
3. Attach locators from the actual supplied page map or stable anchors. Distinguish mentions, substantive treatment, ranges, notes, illustrations, and other index categories as required by the brief.
4. Check heading balance, excessive undifferentiated locator strings, circular/dead cross-references, duplicate concepts, sorting, and exclusions.
5. Deliver the actual index or an explicitly provisional term map when pagination is unavailable; reconcile locators after late text or layout changes.

Read [indexing-workflows-kit.md](../artifacts/indexing-workflows-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- Do not invent page numbers or label draft anchors as final print locators.
- A search hit is a candidate access point, not proof of substantive treatment.
- A see-reference must lead to a present heading; see-also should add useful access rather than duplicate a circular chain.
- Index choices reflect reader purpose and house style, not automatic exhaustive word coverage.

## Verification

- Verify locators against inspected source locations and version.
- Resolve every cross-reference and review sorting/heading consistency.
- Check affected locators after supplied repagination and state any unverified coverage.

## Output Contract

Return exactly: `Index`, `Index Scope And Policy`, `Locator Evidence`, `Cross Reference Checks`, `Open Queries`, `Coverage And Checks`, `Files Changed`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Use `production-editor` for pagination/version control, `proofreader` for final locator proofing, and `developmental-manuscript-editor` for unresolved structure.

## Boundaries

Do not claim final index approval or complete inspection from a sample. Preserve the provenance of locator changes and distinguish provisional from final output.
