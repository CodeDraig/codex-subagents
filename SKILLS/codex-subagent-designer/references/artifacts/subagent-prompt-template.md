# Subagent Prompt Template

```text
Goal: <one concrete result>

Scope:
- Own: <files, modules, questions, or artifacts>
- Read: <minimum context>

Constraints:
- <authority and prohibited actions>
- You are not alone in the codebase. Do not revert edits made by others; adapt to concurrent changes.

Verification:
- <commands, evidence, or review gates>

Return exactly:
- Direct result
- Evidence or files changed
- Commands run and results
- Blockers, integration notes, and confidence
```
