# Design System Audit Checklist

## Component Quality

- Clear component purpose and API.
- Required states: default, hover, focus, active, disabled, loading, error.
- Stable layout dimensions.
- Keyboard and screen-reader behavior.
- Responsive behavior without text overlap.
- Screenshot evidence for default and edge states.

## Token Usage

- Colors use semantic tokens.
- Spacing and radius match system scale.
- Typography is consistent and readable.
- One-off values are justified.
- Motion and contrast are checked against the intended accessibility baseline.

## Adoption

- Duplicate components.
- Local styles replacing shared primitives.
- Consumers relying on private internals.
- Migration path for API changes.
- Document any intentional one-off that should not be generalized into the system.
