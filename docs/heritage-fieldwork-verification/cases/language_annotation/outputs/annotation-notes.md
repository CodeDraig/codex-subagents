# Annotation notes

## Annotation Context

- Source: `inputs/packet.md`, synthetic verification packet; source transcript version V1.
- Session/source identifier: TR1; speaker: S1 for U1--U3.
- Language/variety: the packet calls this a miniature synthetic language and supplies no variety label.
- Representation inspected: supplied text transcript and supplied analysis G1 only. No audio file was supplied or heard.
- Access: all use is permitted for this synthetic exercise.

## Annotated Text

| Segment | Time (s) | Speaker | Source form | Gloss | Translation | Status |
| --- | --- | --- | --- | --- | --- | --- |
| U1 | 1.0--2.5 | S1 | na ki tu | 1SG SEE BIRD | I see a bird | complete-supported |
| U2 | 3.0--4.2 | S1 | na lo tu | 1SG [UNRESOLVED] BIRD | [unresolved: no supplied translation] | partial-unresolved-analysis |
| U3 | 5.0--6.4 | S1 | tu ki na | BIRD SEE 1SG | A bird sees me | complete-supported |

The TSV counterpart is `outputs/segments.tsv`.

## Tier And Transcription Policy

- `source_form` is the supplied V1 transcript verbatim, including its spacing and spelling. It is the attested text tier.
- `gloss` is a token-aligned analytical tier built only from G1: `na` = `1SG`, `ki` = `SEE`, and `tu` = `BIRD`. `[UNRESOLVED]` marks that G1 contains no entry or analysis for `lo`; it is analytical uncertainty, not uncertainty about the supplied transcription.
- `translation` reproduces the G1 free translations for U1 and U3. The bracketed U2 value is an explicit unresolved marker, not a translation.
- No separate morpheme segmentation is proposed: the source spacing is retained without asserting that it establishes linguistic word boundaries.
- `status` identifies whether all requested tiers are supported or whether an analysis remains unresolved.

## Source Anchors

| Segment | Source anchor | Time (s) | Source/version |
| --- | --- | --- | --- |
| U1 | TR1:1 | 1.0--2.5 | packet transcript V1; analysis G1 |
| U2 | TR1:2 | 3.0--4.2 | packet transcript V1; analysis G1 |
| U3 | TR1:3 | 5.0--6.4 | packet transcript V1; analysis G1 |

## Uncertain Analyses

- U2 / `lo`: clearly present in the supplied text transcript, but its gloss, grammatical category, and role are not supplied by G1. No proposed analysis is made.
- U2: G1 supplies no free translation. It remains unresolved rather than being inferred from the parallel forms.

## Editorial Changes

- Created an annotation derivative only; `inputs/packet.md` was not edited.
- Copied all source forms, source anchors, times, and speaker labels unchanged from the supplied packet.
- Added structured gloss, translation, and status tiers; added no normalization, retokenization, correction, or reconstruction.

## Checks And Limits

- TSV parsing and schema check: passed; 3 data rows have the seven requested columns in the requested order.
- Segment IDs: unique (U1, U2, U3).
- Time bounds: all supplied start/end values parse as numeric and each start is earlier than its end. The transcript specifies no recording duration, so bounds against total recording length cannot be tested.
- Source comparison: each `source_form`, time value, and source anchor was checked against the accessible text packet. Audio coverage: none; no audio was supplied or heard, so acoustic inspection was not performed.
- No existing EAF or other structured annotation format was supplied; no EAF/schema validation applies. Speaker review and file-format validation beyond TSV parsing were not performed.

## Owner Questions

- Can a recording or speaker review establish the analysis and translation of U2, especially `lo`?
- If a language/variety label or a recording-duration bound exists, should it be added to the source metadata?

## Files Changed

- `outputs/segments.tsv` (created)
- `outputs/annotation-notes.md` (created)

## Handoffs

- No handoff performed. If U2 needs elicitation or speaker follow-up, hand the session gap to `linguistic-session-designer`; a separately requested lexical record for `lo` belongs with `lexicon-corpus-curator`.
