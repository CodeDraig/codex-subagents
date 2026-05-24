# Test Matrix Template

| Risk | Impact | Layer | Test | Fixture | Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |

## Layer Selection

- Unit: pure logic and edge cases.
- Integration: database, service, filesystem, framework behavior.
- Contract: API, schema, event, SDK compatibility.
- E2E: critical user workflow only.
- Accessibility: keyboard, focus, semantics, contrast.
- Security: auth, injection, tenant boundaries.
- Performance: measured bottlenecks and budgets.
- AI eval: prompt, retrieval, tool, and safety behavior.
- Manual: one-time visual or operational checks.

## Flake Controls

- Avoid real time, real network, shared state, and order dependence.
- Use deterministic fixtures.
- Assert behavior, not implementation trivia.
