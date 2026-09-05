# Edition Maintenance

## Purpose

Apply and document post-publication corrections or revised-edition changes across authoritative text and identified derivative artifacts.

## Intake

Capture the current authoritative edition/version, correction evidence, errata or revision brief, affected formats, ownership, stable identifiers, and whether the task is correction, revision, or release preparation.

## Workflow

1. Classify each change as error correction, clarification, substantive revision, updated fact, or production repair; retain the evidence and affected locations.
2. Apply authorized changes to the working source, preserve recoverable prior text, and record the reason and edition/version context.
3. Map dependent artifacts: contents, index, cross-references, translations, metadata, summaries, accessible versions, exports, and published errata. Mark each as updated, needing regeneration, verified, or outside access.
4. Reconcile changed facts and wording across the supplied derivatives without pretending unavailable files or external publications were updated.
5. Prepare correction notes or an edition change log appropriate to the audience, then verify changed units and dependencies before a separate release step.

Read [edition-maintenance-kit.md](../artifacts/edition-maintenance-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- A correction to one file is not a completed update to every published format.
- Substantive revision should not be hidden as a typographical correction.
- A newer fact does not erase what a historical edition said; retain version/time context.
- Do not regenerate or overwrite unowned artifacts solely because they appear in a dependency list.

## Verification

- Compare source before/after and trace every change to the correction record.
- Check affected links, locators, metadata, quoted passages, and derivative versions where available.
- Report exact updated files, executed regeneration checks, and outstanding external or unavailable copies.

## Output Contract

Return exactly: `Revised Text`, `Correction And Edition Log`, `Affected Artifact Map`, `Consistency Checks`, `Outstanding Updates`, `Files Changed`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Use `production-editor` for release sequencing, `indexing-coordinator` for locator changes, `text-translator` for affected translations, and `publication-format-reviewer` for regenerated exports.

## Boundaries

Preserve prior editions and change provenance. Actual redistribution, publishing, or destructive replacement requires its own authorization and evidence.
