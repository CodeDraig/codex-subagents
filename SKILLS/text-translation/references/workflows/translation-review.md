# Translation Review

## Purpose

Compare a translation with its source and brief, locating meaning shifts and evaluating defensible alternatives without pretending every difference has one correct answer.

## Intake

Identify source/target versions and varieties, brief, genre, reviewer scope, alignment or glossary, and actual language/subject expertise available.

## Workflow

1. Align the inspected source and target units, noting missing or extra material before evaluating stylistic choices.
2. Check denotation, referents, tense/aspect, negation, modality, quantities, names, technical terms, voice, register, and discourse relationships.
3. Review ambiguity, idiom, cultural reference, rhythm, lineation, or dramatic speakability according to the brief, separating errors from arguable strategies.
4. Record each finding with source/target locations, the relevant text, impact, explanation, suggested correction or alternatives, and confidence.
5. Check recurring terms and patterns globally within the inspected extent, then return a correction handoff and clear coverage limits.

Read [translation-review-kit.md](../artifacts/translation-review-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- A literal rendering can misrepresent idiom; a nonliteral one is not automatically an error.
- Prioritize material meaning changes over stylistic preferences, while respecting form as part of meaning when relevant.
- Do not certify a whole translation from a sample or substitute a back-translation score for comparison.
- Where multiple renderings preserve the brief, explain the tradeoff instead of manufacturing a defect.

## Verification

- Verify both sides of every reported issue and its surrounding context.
- Check whether a proposed correction fixes one problem while introducing another loss.
- State units inspected, unresolved expertise limits, and whether suggested corrections have been applied.

## Output Contract

Return exactly: `Review Scope`, `Alignment And Coverage`, `Meaning Findings`, `Register And Form Findings`, `Suggested Corrections`, `Unresolved Choices`, `Verification`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Return corrections to `text-translator`; route source identity to `textual-witness-analyst`, specialist factual issues to `fact-checking-editor`, and final layout checks to `publication-format-reviewer`.

## Boundaries

Do not modify the source or target in this review role, claim certified language expertise, or imply proposed corrections have already been made.
