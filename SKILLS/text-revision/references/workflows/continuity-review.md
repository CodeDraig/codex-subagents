# Manuscript Continuity Review

## Purpose

Find evidenced contradictions in entities, time, space, knowledge, terminology, or repeated claims across a manuscript without treating every difference as an error.

## Intake

Identify version, supplied units, genre, chronology/POV rules, canon or terminology records, and whether the pass is full, sampled, or focused.

## Workflow

1. Build a located ledger of recurring entities, events, attributes, terms, and assertions relevant to the assigned scope. Record changes and uncertainty rather than assigning one timeless value.
2. Compare repeated references for chronology, age/duration, geography, objects, relationships, quantities, names, and definitions.
3. For narrative, track narrator reliability and what each character can know at a given point. For nonfiction, compare repeated claims and definitions with their context and source dates.
4. Classify differences as contradiction, explainable change, intentional viewpoint discrepancy, unresolved ambiguity, or uninspected context. Present paired locations and the consequence.
5. Propose the smallest repair options and identify dependent passages to check if one value or event changes. Do not silently select new canon.

Read [continuity-review-kit.md](../artifacts/continuity-review-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- A character’s lie and another character’s correction are not automatically continuity errors.
- Different dates or editions may legitimately support different values; preserve their time scope.
- Missing later chapters cannot prove a setup is never resolved.
- A suspected contradiction needs both conflicting passages or an explicit external constraint.

## Verification

- Re-read both locations for every reported contradiction and verify version/sequence.
- Check timeline arithmetic only from recorded dates or durations; label unknowns.
- Report inspected units and distinguish confirmed conflicts from reader questions.

## Output Contract

Return exactly: `Review Scope`, `Continuity Ledger`, `Confirmed Conflicts`, `Possible Explanations`, `Repair Options`, `Coverage And Checks`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Send repairs to `fiction-drafter`, `nonfiction-drafter`, or `developmental-manuscript-editor`; send source contradictions to `fact-checking-editor` and spelling/style decisions to `line-copy-editor`.

## Boundaries

Review without changing the source manuscript. Do not invent canon, assert unseen coverage, or conflate a proposed repair with an author decision.
