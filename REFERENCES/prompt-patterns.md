# Prompt Patterns

Use these as compact starting points. Fill in concrete paths, commands, and outputs before sending.

## Explorer

```text
Inspect the codebase to answer this specific question: <question>.

Scope:
- Read-only.
- Focus on <paths/modules>.
- Do not modify files.

Return:
- Direct answer first.
- Relevant file references.
- Any uncertainty or missing context.
```

## Worker

```text
Implement <bounded change>.

Ownership:
- You own <files/modules>.
- You are not alone in the codebase. Do not revert edits made by others; adapt to concurrent changes.

Constraints:
- Follow existing project patterns.
- Keep changes limited to the ownership scope unless a small adjacent edit is required; report any such edit.

Verification:
- Run <commands> if available.
- If a command cannot run, explain why.

Return:
- Summary of behavior changed.
- Files changed.
- Commands run and results.
- Blockers or integration notes.
```

## Validator

```text
Validate <artifact/change/workflow> against this task: <user-like task>.

Inputs:
- <raw artifact paths or links>

Rules:
- Treat this as an independent pass.
- Do not assume the intended answer.
- Do not modify source files unless explicitly asked.

Return:
- Pass/fail or findings ordered by severity.
- Evidence with file references, logs, or screenshots.
- Recommended next action.
```

## Forward-Test

```text
Use $<skill-name> at <skill-path> to solve this task: <realistic user request>.

Work as if this is the user's request. Use only the skill and the artifacts provided. Return the result, files changed if any, and any points where the skill lacked enough guidance.
```

## Catalog Asset Builder

```text
Create or revise <Skill|Agent> <name> for <domain>.

Read first:
- REFERENCES/quality-rubric.md
- Existing adjacent assets: <paths>
- Registry entries: REFERENCES/software-development-crew.md

Quality bar:
- Do not produce a generic workflow that would apply to most domains.
- Include domain-specific intake, checks, evidence, validation guidance, output contract, handoffs, and stop conditions.
- Add or update a supporting reference file when the skill would benefit from a checklist, template, decision table, or examples.
- Score the result against all seven rubric criteria before returning.

Return:
- Files changed.
- Rubric scores with evidence.
- Validation commands run.
- Any remaining `Useful but Thin` gaps.
```
