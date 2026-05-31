---
name: line-copyediting-workflows
description: Use when performing or planning line edits, copyedits, consistency passes, style-sheet updates, query logs, readability fixes, and manuscript cleanup before proofing; not for developmental restructuring or final publisher approval.
---

# Line Copyediting Workflows

## Overview

Improve sentence-level clarity, consistency, style, and correctness while preserving author voice and maintaining a traceable query and style record.

## Workflow

1. Restate manuscript type, audience, edit level, house style, dialect, file format, tracked-change expectations, deadline, and whether the pass is line edit, copyedit, or cleanup.
2. Check clarity, rhythm, redundancy, transitions, voice consistency, dialogue mechanics, jargon, inclusive language, grammar, punctuation, spelling, capitalization, hyphenation, numerals, and citation style.
3. Maintain or create a style sheet covering names, terms, spelling, capitalization, abbreviations, chronology, measurements, citations, and intentional exceptions.
4. Create a query log for ambiguity, factual uncertainty, continuity conflicts, permissions questions, missing references, and author-owned choices.
5. Produce an edit summary with representative changes, unresolved queries, style decisions, risks, and handoffs to proof, fact-checking, permissions, or production.

Use `references/line-copyediting-checklist.md` for pass planning and style-sheet coverage.

## Decision Rules

- Preserve voice unless the user explicitly requests heavier rewriting; flag rather than flatten dialect, register, humor, or deliberate repetition.
- Do not make silent factual changes; query factual uncertainty and route verification to fact-checking or citation review.
- Treat inconsistent names, dates, terminology, chapter numbering, citation style, and unresolved queries as proof blockers.
- Keep developmental recommendations separate from line edits when structure, chapter order, or argument architecture is the real blocker.
- Use examples sparingly when the manuscript is large; show patterns, representative edits, and repeatable rules rather than rewriting every sentence in chat.

## Output Contract

Return exactly: `Edit Scope`, `Style Sheet`, `Representative Edits`, `Query Log`, `Consistency Risks`, `Proof Handoff`, `Owner Decisions`, `Files Changed`, `Handoffs`.
Include file paths or manuscript locations when editing local files, and note whether changes were applied or recommended only.

## Stop Conditions

Stop when asked to hide substantive changes, erase attribution, fabricate citations, remove legally required disclosures, rewrite into undisclosed ghostwritten authorship, or claim final proof approval without owner review.
