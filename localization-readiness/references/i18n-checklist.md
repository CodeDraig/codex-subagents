# Localization Readiness Checklist

## Text

- No hard-coded user-visible strings.
- Variables are named and contextualized.
- Plural rules are locale-aware.
- Gender, tone, and formality assumptions are noted.
- Error and empty states are included.

## Formats

- Date, time, number, currency, unit, address, and name formats use locale-aware APIs.
- Sorting and case conversion are locale-aware where visible.

## Layout

- Text can expand by 30-50%.
- Long words wrap.
- Buttons and labels do not clip.
- Right-to-left layout is not blocked by hard-coded directions.
