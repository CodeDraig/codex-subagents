---
name: osint-research-planning
description: Use when scoping lawful open-source investigations, defining collection lanes, source-quality rules, privacy boundaries, evidence ledgers, and synthesis plans from public sources; not for credentialed access, evasion, doxxing, surveillance, or physical-world targeting.
---

# OSINT Research Planning

## Overview

Plan and coordinate lawful public-source research so collection remains decision-focused, reproducible, privacy-minimizing, and safe.

## Workflow

1. Restate the intelligence question, decision, intended use, subject type, deadline, jurisdiction, owner-defined decision threshold, and what evidence would answer or falsify the question.
2. Run a scope and harm gate before collection. Define public-source boundaries, prohibited data, necessary precision, personal-data limits, evidence access and retention rules, and owner approvals.
3. Decompose the question into collection lanes for official records, primary sources, media, social platforms, geospatial clues, corporate records, technical artifacts, and contradictory evidence.
4. Assign each lane a bounded question, source classes, specialist handoff, dependencies, completion condition, and escalation trigger.
5. Maintain an evidence ledger with source owner, URL or identifier, access date, provenance, relevant extract, confidence, contradictions, personal-data treatment, and fact/inference/allegation label.
6. Synthesize only decision-relevant findings. Preserve uncertainty, unresolved contradictions, negative searches, and the collection steps that remain justified.

Use `references/osint-investigation-plan.md` for the scope gate, lane matrix, source tiers, evidence ledger, and synthesis review.

## Decision Rules

- Public availability is not blanket permission to aggregate, expose, or operationalize personal data. Apply necessity, proportionality, and harm review.
- Do not bypass authentication, access controls, robots or rate limits, paywalls protecting private data, account restrictions, or lawful removal measures.
- Require independent corroboration before reporting a material allegation or a conclusion likely to harm a person or organization.
- Treat current roles, ownership, sanctions, prices, locations, and platform status as volatile; record the access date and verify from authoritative sources.
- Mark planning blocked when the authorized owner has not defined a material domain threshold, lookback period, decision authority, or evidence retention and access rule needed to bound collection.
- Stop collection when additional detail no longer changes the decision and mainly increases personal-data or targeting risk.
- Keep facts, inferences, allegations, and collection leads visibly separate throughout the investigation.

## Validation Guidance

- Prefer official records and original artifacts for factual claims, then use independent reporting or analysis for context and contradiction search.
- Record stable identifiers, versions, archive links, access dates, query terms, negative searches, and source limitations so another researcher can reproduce the path.
- Validate identity, entity, time, and jurisdiction before merging records or transferring findings between collection lanes.
- Treat automated search, scraping, entity resolution, image matching, and network analysis as lead generation until a human reviews source context and false-positive risk.
- Mark a lane blocked rather than filling gaps when access is unlawful, source quality is inadequate, or necessary verification is impossible.

## Output Contract

Return exactly: `Intelligence Question`, `Scope And Boundaries`, `Collection Plan`, `Source Quality Rules`, `Findings`, `Uncertainty`, `Privacy And Safety Notes`, `Next Steps`, `Handoffs`.

For every lane, include the bounded question, assigned agent or owner, allowed sources, evidence standard, completion condition, blockers, and expected handoff artifact.

## Stop Conditions And Handoffs

Stop when the task requires non-public data, credentials, access-control bypass, evasion, stalking, harassment, private-home identification, sensitive-facility targeting, or a dossier whose detail is disproportionate to the public-interest purpose.

Hand official-record collection to `public-records-researcher`, public-media location or time analysis to `geolocation-chronolocation-analyst`, public-network patterns to `social-network-analyst`, narrative harm to `misinformation-risk-analyst`, claim corroboration to `source-verification-analyst`, and publication decisions to `standards-ethics-editor`.
