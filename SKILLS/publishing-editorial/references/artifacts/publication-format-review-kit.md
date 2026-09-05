# Publication Format Review: Working Kit

## Working Record

- Check matrix: artifact/version | property | tool/manual method | result | evidence/location | coverage.
- Format cues: Markdown hierarchy/links; DOCX/ODT styles/fields/revisions; PDF render/tags; EPUB spine/nav/reflow; TEI schema/anchors.
- Evidence labels: parsed; visually inspected; interaction tested; not checked; failed because of environment.

## Worked Example

An EPUB ZIP contains a navigation link to chapter3.xhtml#end, but no element has id="end". Package parsing finds the broken target. A PDF text extraction from the same book succeeds, but no pages were rendered; the report records text extraction and leaves visual layout unverified.

## Failure Case

Failure: call both files accessible because they open, or claim EPUB validation when the validator is absent. Correction: name the checks actually run and leave missing aspects explicit.
