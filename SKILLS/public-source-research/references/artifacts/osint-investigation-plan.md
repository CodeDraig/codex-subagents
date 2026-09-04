# OSINT Investigation Plan

## Intelligence Question

- Decision to support:
- Exact question and excluded questions:
- Intended use and audience:
- Subject type: public institution, organization, public figure, or private person:
- Jurisdictions and date range:
- Deadline and required confidence:
- Evidence that would support, contradict, or leave the question unresolved:

## Owner Decisions Before Collection

- Domain definition and materiality threshold:
- Lookback period and status date:
- Decision authority and required confidence:
- Evidence access, retention, deletion, and sharing rules:
- Approved specialists and escalation owners:

Mark affected lanes blocked rather than inventing these rules.

## Scope And Harm Gate

- Confirm a lawful public-source basis for each collection lane.
- Record prohibited sources, sensitive attributes, unnecessary identifiers, and precision limits.
- Identify risks of harassment, discrimination, retaliation, physical targeting, or disproportionate aggregation.
- Name the owner who can approve any high-risk expansion; absence of approval keeps the lane closed.

## Collection Lane Matrix

| Lane | Typical sources | Required output | Specialist handoff |
| --- | --- | --- | --- |
| Official records | Registries, dockets, filings, sanctions, procurement portals | Record log with identifiers, status, dates, and non-matches | `public-records-researcher` |
| Primary sources | Official statements, original documents, direct media, first-party archives | Provenance record and relevant extract | `source-verification-analyst` |
| Media | Original images, video, audio, archives, publication history | Artifact ledger and manipulation/context findings | `geolocation-chronolocation-analyst` or `source-verification-analyst` |
| Public social platforms | Public accounts, posts, links, hashtags, platform-visible metadata | Reproducible scope and aggregate behavior findings | `social-network-analyst` |
| Corporate and technical | Filings, domains, certificates, repositories, public infrastructure | Entity or technical linkage with stable identifiers | `public-records-researcher` or the relevant technical agent |
| Contradictory evidence | Competing primary sources, corrections, negative searches | Explicit alternatives and disconfirming evidence | `source-verification-analyst` |

## Source Quality Tiers

- Tier A: official record, original artifact, primary document, direct statement, or reproducible observation. Use for decision-grade factual claims while recording date and scope.
- Tier B: independent reporting, transparent research, or maintained specialist database. Use for corroboration and context after checking methods and incentives.
- Tier C: repost, forum claim, unattributed summary, lead database, or AI-generated synthesis. Use only to find better sources.

## Evidence Ledger

- Lane and bounded question:
- Source owner, URL or identifier, and date checked:
- Source tier, provenance, and incentive:
- Relevant extract, frame, page, or record number:
- Fact, inference, allegation, or lead:
- Identity, entity, time, and jurisdiction checks:
- Corroboration and contradiction status:
- Confidence and what would change it:
- Personal data retained, redacted, or excluded:
- Next action or completion reason:

## Synthesis Review

- Answer only the stated intelligence question.
- Separate confirmed findings, supported inferences, unresolved allegations, and collection gaps.
- Include material negative searches and source-access limits.
- Remove personal data that does not change the decision.
- Stop or escalate any lane that crosses the approved harm boundary.
