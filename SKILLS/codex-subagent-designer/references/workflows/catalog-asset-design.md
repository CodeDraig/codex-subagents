# Catalog Asset Design

## Workflow

1. Read the canonical [quality rubric](../../../../REFERENCES/quality-rubric.md) and inspect adjacent assets and registry entries.
2. Define the task signals, exclusion boundaries, domain decisions, evidence, validation, output artifact, and stop conditions that make the asset reusable.
3. For a skill, separate concise discovery metadata, shared routing, mode workflows, and conditionally loaded artifacts. For an agent, define a distinct role, exact handoffs, runtime posture, and return sections.
4. Reject generic workflow prose, unavailable tools, stale paths, fabricated authority, and scaffolds presented as ready assets.
5. Score every changed asset and every gateway mode. The weakest mode determines gateway readiness.
6. Run structural checks only after the usefulness review passes; report anything below `Ready` as a required fix.

## Decision Rules

- A reusable asset must change future behavior through domain checks, decision rules, artifacts, boundaries, or verification—not tone advice.
- Keep a gateway entrypoint small enough to route without loading sibling workflows; put mode-specific outputs and procedures in the selected workflow.
- A supporting artifact must be linked where its loading condition is clear and must not duplicate the workflow.
- Do not claim complete catalog coverage from a sampled review.

## Output Contract

Return exactly: `Assets`, `Behavior Added`, `Routing`, `Rubric Scores`, `Validation`, `Required Fixes`, `Registry Changes`.

## Stop Conditions

Stop before overwriting an existing asset without inspecting its callers, publishing a shallow scaffold as ready, or claiming validation that did not run.
