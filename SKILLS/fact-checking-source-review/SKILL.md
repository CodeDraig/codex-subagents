---
name: fact-checking-source-review
description: Use when checking nonfiction, long-form, or book-manuscript claims against source packets, interviews, datasets, public records, citations, and author notes; not for legal clearance, scholarly peer review, or unsupported web-only assertion chasing without sources.
---

# Fact Checking Source Review

## Overview

Verify manuscript claims by mapping them to sources, assessing source quality, documenting uncertainty, and returning author queries without overstating certainty.

## Workflow

1. Restate manuscript type, claim scope, source packet availability, date sensitivity, publication risk, citation style, and whether the task is spot-checking or full claim review.
2. Build a claim inventory for names, dates, titles, numbers, quotations, paraphrases, chronology, causal claims, allegations, legal or medical statements, and source-dependent descriptions.
3. Match each claim to evidence using source class, source date, location, quote/page reference, confidence, contradiction search, and unresolved caveats.
4. Flag unsupported, overstated, stale, ambiguous, privacy-sensitive, defamatory, legally sensitive, or source-mismatched claims, then assign author or specialist queries.
5. Produce a claim log with status, evidence path, recommended wording changes, and handoffs to citation integrity, legal review, permissions, standards, or methods review.

Use `references/fact-checking-source-checklist.md` for claim-log fields and risk flags.

## Decision Rules

- Do not convert weak support into certainty; qualify claims or query the author when source support is partial.
- Treat quotes, numbers, dates, titles, names, allegations, causal claims, and legal or medical assertions as high-risk checks.
- Prefer primary or authoritative sources when available; label secondary summaries, author memory, and AI-generated material as insufficient unless corroborated.
- Track source date and manuscript date for time-sensitive claims, especially statistics, leadership roles, laws, prices, rankings, and scientific consensus.
- Separate fact-checking from legal clearance, medical advice, research-integrity certification, and publisher approval.

## Output Contract

Return exactly: `Claim Scope`, `Source Inventory`, `Verified Claims`, `Open Queries`, `Risk Flags`, `Recommended Revisions`, `Handoffs`.
For each material issue, include claim text or location, source path or citation, status, confidence, and owner question.

## Stop Conditions

Stop when sources are unavailable for a requested full check, when asked to fabricate sources or citations, when verification requires private records without authorization, or when the user asks for definitive legal, medical, or reputational clearance.
