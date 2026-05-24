---
name: competitive-research
description: Use when researching competitors, product categories, ecosystem norms, standards, pricing, buying criteria, technology comparisons, user expectations, market conventions, or external evidence that affects product or architecture decisions.
---

# Competitive Research

## Overview

Research external context to inform decisions without pretending weak evidence is certainty. Prefer primary sources and translate findings into engineering implications.

## Workflow

1. State the research question and decision it supports.
2. Gather sources: official docs, product pages, standards, pricing, changelogs, demos, reviews, or direct competitor evidence.
3. Score source quality using `references/source-quality.md`.
4. Extract findings and separate stable facts from time-sensitive claims.
5. Convert findings into product, UX, architecture, compliance, or validation implications.

Browse or verify when facts are current, commercial, legal, security-sensitive, or likely changed recently.

## Output Contract

Return exactly: `Question`, `Sources Checked`, `Findings`, `Implications`, `Options`, `Uncertainty`, `Recommended Local Validation`.

## Stop Conditions

Stop when no reliable source supports a claim that would materially affect product, architecture, procurement, legal, security, or compliance decisions.
