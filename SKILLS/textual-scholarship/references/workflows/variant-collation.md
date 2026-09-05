# Variant Collation

## Purpose

Align supplied witnesses and produce an inspectable record of textual variation under a declared comparison policy.

## Intake

Capture witness IDs and versions, source/transcription provenance, overlapping passages, base or parallel comparison choice, normalization rules, and which variation matters to the project.

## Workflow

1. Confirm passage overlap and establish stable segment anchors without assuming identical line or page numbers across witnesses.
2. Declare comparison treatment for case, punctuation, spelling, whitespace, abbreviations, additions, omissions, substitutions, and transpositions. Retain raw readings alongside normalized comparison forms.
3. Align equivalent units and identify variants. Inspect alignment boundaries manually where segmentation, repeated phrases, transposition, or missing material can mislead a diff.
4. Record each locus with witness readings, source locations, type of difference, coverage, and uncertainty. Keep absence due to a lacuna separate from an attested omission.
5. Return the collation table or requested encoded artifact, plus policy and unresolved alignment issues. Do not silently promote a variant to the preferred reading.

Read [variant-collation-kit.md](../artifacts/variant-collation-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- Normalization can suppress meaningful differences; make suppressed classes explicit and preserve recoverability.
- A missing witness segment is not automatically evidence of deliberate omission.
- String difference identifies candidates, not textual causes or genealogical relationships.
- Conjectures and editorial emendations are not witness attestations.

## Verification

- Recheck each variant against supplied witness text and its anchors.
- Inspect unchanged spans around difficult alignments and verify witness coverage per locus.
- For encoded output, check witness IDs and anchors resolve; parse XML and use a supplied schema only when available.

## Output Contract

Return exactly: `Collation`, `Comparison Policy`, `Witness And Locus Map`, `Alignment Queries`, `Verification`, `Files Changed`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Return source uncertainties to `documentary-transcriber` and `textual-witness-analyst`; hand editorial selection and apparatus presentation to `critical-edition-editor`.

## Boundaries

Do not overwrite witness readings, fabricate attestations, or infer a stemma from an unexamined diff. Use the [TEI critical apparatus guidance](https://tei-c.org/release/doc/tei-p5-doc/en/html/TC.html) when apparatus encoding is requested.
