# Textual Witness Description

## Purpose

Describe the supplied witnesses of a text and their provenance, extent, relations, and inspection limits before transcription or editorial comparison.

## Intake

Capture the research/editorial question, supplied manuscripts/editions/images/transcripts, repository identifiers, versions, source metadata, and required descriptive granularity.

## Workflow

1. Assign stable witness identifiers tied to supplied sources; distinguish the physical/documentary witness from a scan, OCR file, transcription, or later edition representing it.
2. Record title/incipit, attributed author, date or range and its basis, repository/shelfmark if supplied, extent, language/script, completeness, and visible or documented features relevant to the task.
3. Map which passages each witness actually covers and identify lacunae, fragmentary material, unreadable areas, and inaccessible portions.
4. Describe reported relationships separately from demonstrated agreements or inferred dependence. Preserve uncertainty about dating, attribution, and lineage.
5. Return a witness register and a comparison/transcription handoff with stable locations and explicit inspection boundaries.

Read [witness-description-kit.md](../artifacts/witness-description-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- A filename or catalog attribution is evidence to record, not proof of date, authorship, or textual priority.
- A modern transcription is not the original witness; its editorial interventions require their own provenance.
- Shared readings alone do not establish direct copying or a complete stemma.
- Physical characteristics cannot be verified from a plain transcription.

## Verification

- Check identifiers and cited locations against the supplied packet; distinguish observed, catalog-reported, and inferred details.
- Verify the overlap of passages before requesting collation.
- Record inaccessible or uninspected material without implying it was examined.

## Output Contract

Return exactly: `Witness Register`, `Provenance And Representations`, `Extent And Coverage`, `Reported Or Inferred Relations`, `Uncertainties`, `Verification`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Hand transcription to `documentary-transcriber`, aligned comparison to `variant-collator`, edition policy to `critical-edition-editor`, and collection-level archival hierarchy to `collection-description-specialist`.

## Boundaries

Do not alter source records, invent provenance or shelfmarks, or certify dating/authenticity from insufficient evidence. Use the [TEI primary-source guidance](https://tei-c.org/release/doc/tei-p5-doc/en/html/PH.html) when source representation or encoding choices matter.
