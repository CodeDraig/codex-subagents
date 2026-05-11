# Design System Audit Checklist

## Component Quality

- Clear component purpose and API.
- Required states: default, hover, focus, active, disabled, loading, error.
- Stable layout dimensions.
- Keyboard and screen-reader behavior.
- Responsive behavior without text overlap.

## Token Usage

- Colors use semantic tokens.
- Spacing and radius match system scale.
- Typography is consistent and readable.
- One-off values are justified.

## Adoption

- Duplicate components.
- Local styles replacing shared primitives.
- Consumers relying on private internals.
- Migration path for API changes.
