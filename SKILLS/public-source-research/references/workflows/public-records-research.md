# Public Records Research

## Purpose

Research official records with reproducible search scope, careful entity disambiguation, procedural context, and privacy minimization.

## Workflow

1. Restate the person or entity, jurisdiction, record type, date range, purpose, authoritative identifiers, known aliases, and decision the search supports.
2. Build an official-source plan covering the correct registry, court, regulator, procurement portal, sanctions authority, corporate filing system, and archived official pages.
3. Search exact identifiers first, then controlled name and alias variants. Preserve the query, filters, retrieval date, source status, access limitation, and material non-matches.
4. Disambiguate every candidate using stable IDs, jurisdiction, address at the relevant time, birth or incorporation date, officers, counsel, case number, or other independent attributes. Never merge on name similarity alone.
5. Record procedural posture and status exactly. Separate filing, allegation, charge, judgment, dismissal, settlement, inactive registration, and current enforceable status from claims about underlying conduct.
6. Minimize private personal data, reconcile contradictions and stale records, assign a match confidence, and identify the next official record needed.

Read [public-records-search-checklist.md](../artifacts/public-records-search-checklist.md) when you need source planning, identity matching, procedural language, retrieval evidence, and privacy review.

## Decision Rules

- Treat a unique authoritative identifier as the strongest match evidence. Without one, require at least two independent matching attributes and no material contradiction.
- Treat copies of the same filing, syndicated databases, and summaries derived from one record as one evidence lineage, not independent corroboration.
- Describe allegations, complaints, charges, investigations, and sanctions proceedings as procedural facts; do not convert them into proof of conduct or guilt.
- Distinguish current, historical, pending, stayed, dismissed, expired, dissolved, inactive, and superseded status using the issuing authority's date and terminology.
- When a requester demands a binary match, do not force a possible candidate into either category. Put confirmed or explicitly labeled probable results in `Matches`, excluded identities in `Non-Matches`, and unresolved candidates in `Entity Disambiguation` and `Caveats`.
- Record a non-match when a searched source, identifier, jurisdiction, and date range are known. Do not claim that no record exists beyond the search scope.
- Exclude irrelevant home addresses, relatives, identifiers, and sensitive personal details even when technically public.

## Validation Guidance

- Prefer the issuing court, regulator, registry, procurement authority, sanctions authority, or official archive over commercial aggregators and search snippets.
- Cite the source URL, jurisdiction, record or docket number, filing date, status, retrieval date, and relevant page or entry.
- Mark required fields as `not supplied` or `not available` when a closed packet omits them; never infer missing authority, date, status, or URL values.
- Save or hash an official document only when authorized and useful for version or authenticity tracking; report access restrictions without bypassing them.
- Cross-check material identity matches against a second authoritative attribute or source, especially for common names and adverse records.
- Mark the result inconclusive when official access, stable identifiers, jurisdiction coverage, or current status cannot be established.

## Output Contract

Return exactly: `Search Scope`, `Records Checked`, `Matches`, `Non-Matches`, `Entity Disambiguation`, `Caveats`, `Source Links`, `Next Records To Check`, `Handoffs`.

For every match, include source authority, record identifier, date and status, matched attributes, conflicting attributes, procedural meaning, retrieval date, confidence, and privacy redactions.

## Stop Conditions And Handoffs

Stop when asked to obtain sealed, hacked, credentialed, paid-private, unlawfully disclosed, or access-restricted records; to expose irrelevant personal data; or to treat a weak identity match as established.

Hand legal authority or interpretation to `legal-research-analyst` or counsel, claim corroboration to `source-verification-analyst`, publication-risk review to `standards-ethics-editor` or `news-fact-checker`, and broader collection planning to `osint-research-lead`.
