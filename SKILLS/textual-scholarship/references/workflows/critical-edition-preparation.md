# Critical Edition Preparation

## Purpose

Prepare an edited text, apparatus, and editorial account from documented witnesses and explicit editorial choices.

## Intake

Capture edition purpose/readers, witness register and transcriptions, collation, base-text or parallel-text policy, normalization, apparatus scope, proposed emendations, and target format.

## Workflow

1. State the editorial method: documentary, reading, eclectic/critical, parallel, or another specified approach. Record the basis for any base text and avoid presenting a provisional policy as settled author/editor approval.
2. Prepare the actual edited text under that policy. Preserve source locations and distinguish retained witness readings, normalization, supplied text, and conjectural emendations.
3. Build an apparatus that matches the chosen scope: which witnesses, which variants, positive/negative reporting if applicable, and how entries attach to the edited text.
4. Write the editorial introduction or notes explaining sources, selection principles, normalization, uncertainty, and unresolved readings. Keep arguments for readings separate from the witness attestations.
5. Reconcile text, apparatus, witness list, notes, and references after every substantive change; deliver a qualified edition draft when some decisions remain open.

Read [critical-edition-preparation-kit.md](../artifacts/critical-edition-preparation-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- There is no universal best base-text method; the project’s purpose and evidence determine the declared approach.
- An editor’s plausible emendation is not an attested reading and must be marked as intervention.
- Do not erase a competing reading merely because the edition selects another.
- Missing evidence permits an explicit lacuna or provisional decision, not an invented original text.

## Verification

- Verify each apparatus reading against the collation and source locations; check that witness sigla and text anchors resolve.
- Compare edited text with the declared policy and intervention log.
- Parse optional XML and validate against the actual supplied TEI schema/customization before claiming conformance; separately inspect human-readable presentation.

## Output Contract

Return exactly: `Edited Text`, `Editorial Policy`, `Critical Apparatus`, `Editorial Introduction`, `Unresolved Readings`, `Verification`, `Files Changed`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Use `textual-witness-analyst`, `documentary-transcriber`, and `variant-collator` for source work; hand publication proof and layout checks to `proofreader` and `publication-format-reviewer`.

## Boundaries

Do not claim a reconstructed original, source inspection, or encoding conformance beyond the evidence. The [TEI critical apparatus chapter](https://tei-c.org/release/doc/tei-p5-doc/en/html/TC.html) informs representation choices without prescribing the project’s editorial method.
