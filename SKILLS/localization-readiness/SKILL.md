---
name: localization-readiness
description: Use when preparing UI, copy, forms, dates, times, numbers, currency, pluralization, right-to-left layouts, translation keys, layout expansion, locale-sensitive sorting, or internationalization before shipping.
---

# Localization Readiness

## Overview

Prepare software for translation and locale variation before copy and layout harden. Focus on meaning, formatting, expansion, plural rules, and directionality.

## Workflow

1. Inventory user-visible strings and dynamic values.
2. Check dates, times, numbers, currency, names, addresses, sorting, casing, and pluralization.
3. Check layout expansion, truncation, wrapping, and right-to-left behavior.
4. Add translator context and stable keys where implementation is in scope.
5. Identify copy that must be approved before translation.

Use `references/i18n-checklist.md` for detailed review.

## Output Contract

Return exactly: `Scope`, `Strings And Formats`, `Files Changed`, `Translator Notes`, `Layout Risks`, `Validation`, `Open Questions`.

## Stop Conditions

Stop when requested copy changes alter product meaning, legal terms, pricing, or user commitments without owner approval.
