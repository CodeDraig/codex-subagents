# Line Copyediting Workflows

## Purpose

Improve sentence-level clarity, consistency, style, and correctness while preserving author voice and maintaining a traceable query and style record.

## Intake

Identify the authoritative text, assigned span, edit level, house style/dialect, protected voice and exceptions, file format, and whether the user wants applied edits, tracked changes, or recommendations.

## Workflow

1. Restate manuscript type, audience, edit level, house style, dialect, file format, tracked-change expectations, deadline, and whether the pass is line edit, copyedit, or cleanup.
2. Check clarity, rhythm, redundancy, transitions, voice consistency, dialogue mechanics, jargon, inclusive language, grammar, punctuation, spelling, capitalization, hyphenation, numerals, and citation style.
3. Maintain or create a style sheet covering names, terms, spelling, capitalization, abbreviations, chronology, measurements, citations, and intentional exceptions.
4. Create a query log for ambiguity, factual uncertainty, continuity conflicts, permissions questions, missing references, and author-owned choices.
5. Produce an edit summary with representative changes, unresolved queries, style decisions, risks, and handoffs to proof, fact-checking, permissions, or production.

Read [line-copyediting-checklist.md](../artifacts/line-copyediting-checklist.md) when you need pass planning and style-sheet coverage.

## Decision Rules

- Preserve voice unless the user explicitly requests heavier rewriting; flag rather than flatten dialect, register, humor, or deliberate repetition.
- Do not make silent factual changes; query factual uncertainty and route verification to fact-checking or citation review.
- Treat inconsistent names, dates, terminology, chapter numbering, citation style, and unresolved queries as proof blockers.
- Keep developmental recommendations separate from line edits when structure, chapter order, or argument architecture is the real blocker.
- For large manuscripts, edit the assigned files or units in full and report coverage. Representative examples can explain changes but must not replace the requested edited text.

## Verification

- Compare original and revision for negation, modality, quantities, quotations, referents, and claim strength.
- Check style-sheet decisions across the assigned span, including names, invented terms, dialogue, citations, lists, notes, and cross-references.
- Use a diff or document-aware change inspection when applying edits. For DOCX/ODT, preserve fields, notes, comments, and revision markup with appropriate tooling; for PDF/EPUB, distinguish source correction from export regeneration.

## Output Contract

Return exactly: `Revised Text`, `Edit Scope`, `Style Sheet`, `Representative Edits`, `Query Log`, `Consistency Risks`, `Proof Handoff`, `Owner Decisions`, `Files Changed`, `Handoffs`.
Include file paths or manuscript locations when editing local files, and note whether changes were applied or recommended only.

## Stop Conditions

Do not hide substantive changes, erase attribution, fabricate citations, remove required disclosures, make false authorship claims, or claim final proof approval without owner review. Complete commissioned or assisted rewriting is supported when requested.

For recommendation-only or diagnostic requests, identify revisions as proposed; when applied editing is requested, put the actual revised text or output-file location in `Revised Text`.
