---
name: competitive-research
description: Use when researching competitors, product categories, ecosystem norms, standards, pricing, buying criteria, technology comparisons, user expectations, market conventions, or external evidence that affects product or architecture decisions.
---

# Competitive Research

## Overview

Research external context to inform decisions without pretending weak evidence is certainty. Prefer primary sources, record source dates, and translate findings into product, architecture, procurement, and validation implications.

## Workflow

1. State the research question, decision deadline, buyer or user context, and what would change if the answer is different.
2. Gather sources: official docs, product pages, standards, pricing, changelogs, demos, public filings, reviews, or direct competitor evidence.
3. Score source quality using `references/source-quality.md`; record source owner, date checked, evidence type, and incentive bias.
4. Extract findings and separate stable facts from time-sensitive claims such as price, availability, roadmap, security posture, or policy.
5. Compare options only on decision-relevant dimensions: workflow fit, integration cost, operating cost, compliance burden, migration risk, ecosystem maturity, and evidence strength.
6. Convert findings into product, UX, architecture, procurement, compliance, or validation implications.

Browse or verify when facts are current, commercial, legal, security-sensitive, or likely changed recently.

## Decision Rules

- Treat current pricing, packaging, limits, supported platforms, certifications, and security claims as volatile; verify from primary sources on the day of the recommendation.
- Do not rank products by popularity alone. State the comparable set, inclusion reason, and which alternatives were intentionally excluded.
- For procurement or spend decisions, separate capability fit from commercial terms, contract risk, vendor risk, and implementation switching cost.
- Prefer reproducible local trials or screenshots over vendor comparison pages when the decision depends on feature behavior.
- Mark any recommendation as provisional when evidence is older than 12 months, source dates are missing, or the claim comes from a party with a direct incentive.

## Validation Guidance

- Use primary sources first: official docs, pricing pages, release notes, standards, status pages, filings, support policies, and direct product trials.
- For software comparisons, validate claims with API docs, SDK examples, changelogs, issue trackers, package metadata, or small local spikes when possible.
- For market or buyer claims, distinguish anecdote, survey, analyst report, sales collateral, and first-party customer evidence.
- When browsing is unavailable, state that current facts were not live-verified and avoid recommendations that depend on recent market conditions.

## Output Contract

Return exactly: `Question`, `Decision Context`, `Sources Checked`, `Comparable Set`, `Findings`, `Implications`, `Options`, `Uncertainty`, `Recommended Local Validation`.

## Stop Conditions

Stop when no reliable source supports a claim that would materially affect product, architecture, procurement, legal, security, or compliance decisions. Hand procurement scoring to `vendor-scorecard-analyst`, vendor risk to `vendor-risk-reviewer`, architecture tradeoffs to `systems-architect`, and implementation planning to `technical-planner`.
