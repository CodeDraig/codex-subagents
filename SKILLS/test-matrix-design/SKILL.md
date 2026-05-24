---
name: test-matrix-design
description: Use when designing test strategy, mapping risks to unit/integration/contract/e2e/accessibility/security/performance/AI eval/manual checks, choosing fixtures, reducing flaky tests, or deciding what must be verified before release.
---

# Test Matrix Design

## Overview

Design tests from risk and behavior, not coverage percentage. The goal is a practical matrix that catches important regressions without creating brittle noise.

## Workflow

1. List requirements, workflows, contracts, and failure modes.
2. Rank risk by impact and likelihood.
3. Assign each risk to the cheapest reliable validation layer.
4. Define fixtures, mocks, data setup, and flake controls.
5. Name commands and gaps.

Use `references/matrix-template.md` for larger features.

## Output Contract

Return exactly: `Risk Matrix`, `Test Layers`, `Priority Order`, `Fixtures`, `Commands`, `Flake Risks`, `Coverage Gaps`.

## Stop Conditions

Stop when acceptance criteria are missing or the system has no controllable validation surface for the claimed behavior.
