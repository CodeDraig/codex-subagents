# AI Eval Case Template

## Case Fields

- ID:
- Input:
- Context or retrieval:
- Tool availability:
- Expected behavior:
- Must include:
- Must not include:
- Score rule:
- Rationale:

## Dataset Mix

- Normal user request.
- Ambiguous request.
- Empty or missing context.
- Malformed input.
- Adversarial or injection attempt.
- Tool failure.
- Boundary policy case.

## Judge Rubric Rules

- Score task success, not style preference.
- Include disqualifiers.
- Require evidence for claims.
- Keep labels stable across model versions.
