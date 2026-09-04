# Agent Template Review

## Workflow

1. Read the canonical [subagent TOML reference](../../../../REFERENCES/subagent-toml.md) and inspect the agent's referenced skills and handoff targets.
2. Verify filename and `name`, required fields, TOML parsing, model and reasoning support, sandbox fit, and non-empty nickname candidates.
3. Check that the role has distinct dispatch signals, domain-specific instructions, fallback behavior for unavailable skills, exact return sections, and bounded authority.
4. Resolve every `$skill` reference and every named handoff against the target runtime or catalog.
5. Use the [crew registry](../../../../REFERENCES/software-development-crew.md) only when reviewing lifecycle coverage, overlap, model coverage, or catalog routing.
6. Score the template with the quality rubric and distinguish structural validity from operational usefulness.

## Decision Rules

- Read-only analysis and high-stakes review roles should not receive write authority unless file mutation is central to the role.
- Runtime overrides must express a real capability, latency, or risk need; otherwise inherit defaults.
- A generic agent that can be replaced by a short task prompt is not catalog-ready.

## Output Contract

Return exactly: `Template`, `Dispatch Fit`, `Runtime Fit`, `Skill Resolution`, `Handoffs`, `Rubric Scores`, `Required Fixes`.

## Stop Conditions

Stop before claiming runtime support that was not verified, granting unnecessary authority, or retaining unresolved skill and handoff targets.
