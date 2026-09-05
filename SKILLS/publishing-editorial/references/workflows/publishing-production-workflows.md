# Publishing Production Workflows

## Purpose

Support manuscript and scholarly production through structured schedules, editorial passes, style sheets, proof tracking, metadata cleanup, and publication-package readiness.

## Intake

Identify authoritative manuscript and proof versions, supplied assets, production stage, house style, owned files, format targets, required checks, and current owner decisions. Separate a schedule proposal from completed production work.

## Workflow

1. Restate publication type, audience, stage, house style, deadlines, and owner roles.
2. Map manuscript components into the production sequence: copyedit, style sheet, query resolution, proof, indexing, metadata, and final package.
3. Track style decisions, queries, permissions, references, figures, tables, captions, alt text, and indexing needs.
4. Check metadata, asset completeness, accessibility, and proof consistency across title, author, ISBN or ISSN, abstract, keywords, and references.
5. Flag schedule risks, missing assets, unresolved author or editor decisions, and rights issues, then produce a production tracker and next-action list.

Read [production-workflow-checklist.md](../artifacts/production-workflow-checklist.md) when you need publishing coverage.

## Decision Rules

- Hold publication if metadata disagrees across title, author, edition, copyright, keywords, or index records.
- Do not release proof stages with missing figures, captions, alt text, unresolved queries, or broken references unless the owner explicitly accepts the risk.
- Separate copyediting from final approval; a clean pass does not imply publisher signoff.
- Treat permissions, accessibility, and indexing as release blockers when the publication type or house style requires them.

- Use `proofreader`, `publication-format-reviewer`, and `indexing-coordinator` for their distinct checks; use `edition-maintenance-editor` after publication. A production schedule does not itself perform those checks.

## Verification

- Check the asset/version inventory against the actual files and verify that each promised component exists.
- Reconcile prior corrections, outstanding queries, and changed pagination or cross-references before claiming a stage complete.
- Record which format/rendering checks were performed and which derivative files remain to be generated or reviewed.

## Output Contract

Return exactly: `Project Scope`, `Production Schedule`, `Manuscript Components`, `Style Decisions`, `Queries`, `Risks`, `Next Actions`, `Files Changed`, `Handoffs`.
Include proof-stage status, metadata issues, and any hold criteria in the relevant sections.

## Stop Conditions

Stop when asked to plagiarize, hide attribution issues, bypass permissions review, fabricate references, or represent final publisher approval without authorization.
