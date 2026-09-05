# Delegation Design

## Workflow

1. Restate the concrete result and identify the main agent's immediate critical path.
2. Delegate only independent work that can be bounded by inputs, ownership, output, and validation.
3. Prefer an exposed named custom agent when its domain and standing contract fit; otherwise use the active tool's supported fallback mechanism. Use `explorer`, `worker`, or `default` only when those types are exposed. Validation is an assignment, not a guaranteed built-in `validator` type; give that assignment to an available agent.
4. Give each coding worker a disjoint write set and warn it not to revert concurrent edits. Keep dependent, tightly coupled, trivial, secret-bearing, or destructive work local.
5. Define integration order, conflict ownership, review gates, and the evidence required before accepting each result.
6. Obey the active session's delegation limits and approval rules. If delegation is unavailable or unauthorized, return the same design as a plan without spawning agents.

When a reusable plan artifact is useful, read [delegation-plan-template.md](../artifacts/delegation-plan-template.md). Consult the [crew registry](../../../../REFERENCES/software-development-crew.md) only when choosing among catalog agents.

## Decision Rules

- Parallelize independent questions, disjoint implementation slices, or validation that can run beside local work.
- Keep work local when the next step depends on the answer, ownership overlaps, or integration would require continuous shared judgment.
- A validator receives the user-like request and raw artifacts, not the intended answer or suspected defect.
- A subagent result is evidence to review, not automatic proof of completion.

## Output Contract

Return exactly: `Main Agent`, `Subagents`, `Ownership`, `Integration Order`, `Verification`, `Constraints`, `Fallbacks`.

## Stop Conditions

Stop before delegating work that lacks a bounded outcome, safe authority, compatible ownership, or a reviewable return contract.
