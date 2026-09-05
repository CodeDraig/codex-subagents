# Documentary Transcription

## Purpose

Produce a traceable transcription of supplied textual sources with an explicit policy for layout, spelling, abbreviations, corrections, and uncertainty.

## Intake

Capture source images or documents, witness IDs, locations, target format, diplomatic/normalized expectations, allowed OCR tools, and the phenomena relevant to the edition.

## Workflow

1. Define the transcription policy before applying systematic changes: line/page breaks, original spelling, punctuation, abbreviations, deletions/additions, damaged or unclear text, and normalization.
2. Transcribe the assigned source units, retaining stable source anchors. Treat OCR as a candidate reading that requires comparison, not as a verified source.
3. Represent uncertainty, illegibility, gaps, supplied text, and editorial expansions with declared conventions. Distinguish what is visible from what is reconstructed.
4. If a normalized reading is requested, retain the diplomatic/source layer or a reversible mapping of interventions rather than silently overwriting it.
5. Compare the transcription with the source in a second pass, focusing on easily confused characters, omitted lines, repeated words, marginal additions, and page transitions. Deliver actual transcribed text and coverage.

Read [documentary-transcription-kit.md](../artifacts/documentary-transcription-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- Do not modernize spelling or punctuation during a diplomatic transcription unless the policy explicitly permits it.
- A conjectural expansion must remain distinguishable from letters visible in the source.
- Do not fill a gap solely because the sentence becomes grammatical.
- If source quality prevents certainty, local uncertainty markers permit useful transcription of the rest.

## Verification

- Check every claimed transcribed unit against its source when available; state any sampled or unverified OCR coverage.
- Verify line/page anchors, declared notation, and separation of transcription from normalization.
- Parse XML when used and validate against the supplied schema if available; well-formedness alone is not TEI conformance.

## Output Contract

Return exactly: `Transcription`, `Transcription Policy`, `Source Anchors`, `Uncertain Readings`, `Editorial Interventions`, `Coverage And Checks`, `Files Changed`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Use `textual-witness-analyst` for source identity, `variant-collator` for comparison, and `critical-edition-editor` for normalized or critical presentation policy.

## Boundaries

Preserve originals and do not claim unseen pages were transcribed. Consult [TEI source representation](https://tei-c.org/release/doc/tei-p5-doc/en/html/PH.html) only when encoding source phenomena is part of the requested output.
