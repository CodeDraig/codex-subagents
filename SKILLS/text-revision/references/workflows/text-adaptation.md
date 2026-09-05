# Text Adaptation

## Purpose

Produce complete adaptations of supplied text for a new audience, medium, length, or purpose while making consequential transformations inspectable.

## Intake

Capture source/version, target artifact and audience, language, target extent, required facts or passages, permitted omissions/invention, medium constraints, and desired attribution.

## Workflow

1. Identify the source’s core claims, narrative turns, voice, and audience assumptions; distinguish what must survive from what can change.
2. Map source units to retained, condensed, expanded, reordered, transformed, or omitted target units, with reasons tied to the new purpose.
3. Write the complete adapted text in the target form. Change explanation, examples, pacing, and signposting to suit the reader without quietly changing evidence or stance.
4. Check losses and additions: removed caveats, simplified mechanisms, fictionalized scenes, changed speaker relationships, and format-dependent meaning.
5. Deliver the adaptation and a concise source-to-target map; identify unadapted units and queries that affect fidelity.

Read [text-adaptation-kit.md](../artifacts/text-adaptation-kit.md) when preparing the working record or checking the example against a similar request.

## Decision Rules

- An abridgment may omit material but must not reverse the source’s conclusion through selective deletion.
- Plain language should explain a difficult idea, not replace it with a false easier claim.
- Do not add factual qualifiers for fluency. A source that mentions a survey does not establish that it was brief or recent; preserve what is known and leave its duration or date unspecified.
- Translation across languages belongs with the translation workflow; adaptation may additionally change audience or form.
- Invented examples can serve an adaptation when allowed and clearly distinguished from reported events.

## Verification

- Compare required claims, qualifications, and protected passages before and after.
- Check target length, audience assumptions, navigation, and medium constraints.
- Measure hard word limits and any reported exact count with an available counter such as `wc -w` on the delivered text. State whether a title is included; revise and recount if the text falls outside the requested range.
- Account for consequential omissions/additions and ensure the actual target text is complete.

## Output Contract

Return exactly: `Adapted Text`, `Source To Target Map`, `Transformation Decisions`, `Fidelity And Format Checks`, `Open Queries`, `Files Changed`, `Handoffs`.
Include supplied source or manuscript locations where relevant; distinguish applied changes, recommendations, unverified details, and coverage still outstanding. Put the requested text in the text section or identify the actual output file.

## Handoffs

Use `text-translator` for language transfer, `script-development-editor` for production scripts, and `reader-experience-reviewer` for target-audience review.

## Boundaries

Do not conceal transformations that change meaning or claim rights/approval that were not supplied. Work on an adaptation copy and preserve source provenance.
