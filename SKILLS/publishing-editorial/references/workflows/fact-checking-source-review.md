# Fact Checking Source Review

## Purpose

Verify manuscript claims by mapping them to sources, assessing source quality, documenting uncertainty, and returning author queries without overstating certainty.

## Intake

Identify manuscript/version, claims and coverage requested, available source versions, source-access limits, publication date, and whether external research is authorized. Distinguish full checking from spot-checking.

## Workflow

1. Restate manuscript type, claim scope, source packet availability, date sensitivity, publication risk, citation style, and whether the task is spot-checking or full claim review.
2. Build a claim inventory for names, dates, titles, numbers, quotations, paraphrases, chronology, causal claims, allegations, legal or medical statements, and source-dependent descriptions.
3. Match each claim to evidence using source class, source date, location, quote/page reference, confidence, contradiction search, and unresolved caveats.
4. Flag unsupported, overstated, stale, ambiguous, privacy-sensitive, defamatory, legally sensitive, or source-mismatched claims, then assign author or specialist queries.
5. Produce a claim log with status, evidence path, recommended wording changes, and handoffs to citation integrity, legal review, permissions, standards, or methods review.

Read [fact-checking-source-checklist.md](../artifacts/fact-checking-source-checklist.md) when you need claim-log fields and risk flags.

## Decision Rules

- Do not convert weak support into certainty; qualify claims or query the author when source support is partial.
- Treat quotes, numbers, dates, titles, names, allegations, causal claims, and legal or medical assertions as high-risk checks.
- Prefer primary or authoritative sources when available; label secondary summaries, author memory, and AI-generated material as insufficient unless corroborated.
- Track source date and manuscript date for time-sensitive claims, especially statistics, leadership roles, laws, prices, rankings, and scientific consensus.
- Separate fact-checking from legal clearance, medical advice, research-integrity certification, and publisher approval.

## Verification

- Check quotations against source context and compare numbers with their denominators, units, dates, and population.
- Record a status for every assigned claim: supported, contradicted, partly supported, unverifiable from supplied material, or not yet checked.
- Re-read recommended revisions against evidence so a repair does not introduce a stronger claim. Report partial coverage explicitly.

## Output Contract

Return exactly: `Claim Scope`, `Source Inventory`, `Verified Claims`, `Open Queries`, `Risk Flags`, `Recommended Revisions`, `Handoffs`.
For each material issue, include claim text or location, source path or citation, status, confidence, and owner question.

## Stop Conditions

Stop short of claiming a full check when sources are unavailable. Continue with the supplied evidence and a located gap log. Do not fabricate sources or citations, access private records without authorization, or provide definitive legal, medical, or reputational clearance.
