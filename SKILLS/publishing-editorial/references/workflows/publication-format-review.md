# Publication Format Review

## Purpose

Inspect a supplied publication artifact for structural, visual, navigation, and accessibility defects using evidence appropriate to its actual format.

## Intake

Capture file/version, intended formats/readers/devices, authoritative content, supplied specifications, fonts/assets, available inspection tools, and required accessibility or submission checks.

## Workflow

1. Inventory actual artifacts and available tools before promising checks. Separate source-document structure, exported structure, rendered presentation, and interactive/navigation behavior.
2. For plain text/Markdown inspect encoding, heading hierarchy, links, code or verse whitespace, and reader order. For DOCX/ODT inspect styles, fields, notes, tracked changes/comments, tables, alt text, and package relationships with document-aware tooling or ZIP/XML inspection.
3. For PDF inspect extracted text and rendered pages, font/glyph issues, clipping, reading order, links, bookmarks, and tagging when tools expose them. For EPUB inspect package/manifest/spine/navigation, content links, metadata, images, and reflow; use an available EPUB validator and reading/rendering tool separately.
4. For optional TEI/XML check well-formedness, references, and the supplied schema/customization. Do not equate XML parsing with semantic or accessibility conformance.
5. Report located defects, executed checks, tool versions when relevant, and unavailable checks. Compare content across formats only for the supplied versions and extent.

Read [publication-format-review-kit.md](../artifacts/publication-format-review-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- A successful export or parser exit does not prove visual, navigational, or accessibility correctness.
- Accessibility claims must name the aspects and evidence actually checked; do not infer certification from alt-text presence.
- Preserve meaningful whitespace and reading order in poetry, drama, tables, and apparatus.
- Missing tools permit a specific inspection plan and partial findings, not fabricated validation results.

## Verification

- Check internal links/anchors and package references with available parsers; inspect representative and problem-prone rendered pages where possible.
- Record actual tool commands or UI inspections, versions, inspected coverage, and failures.
- Distinguish a defect in the artifact from an environment/tool failure and state the smallest next check needed.

## Output Contract

Return exactly: `Artifact Scope`, `Format And Structure Findings`, `Visual And Navigation Findings`, `Accessibility Evidence`, `Executed Checks`, `Unavailable Checks`, `Required Corrections`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Send text corrections to `proofreader`, source restructuring to `documentation-engineer` or the owning editor, and release sequencing to `production-editor`.

## Boundaries

This role reviews supplied artifacts without changing them. Do not install global converters, claim unavailable tool results, or grant publication/accessibility certification.
