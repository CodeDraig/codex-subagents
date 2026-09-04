# Subagent Prompting

## Workflow

1. State one concrete goal and the exact scope the agent owns.
2. Supply only the context needed to start: relevant files, interfaces, constraints, and known evidence.
3. Name prohibited actions, concurrent-edit rules, authority boundaries, and required validation.
4. Require a predictable return containing the direct result, evidence, changed paths when applicable, commands run, blockers, and confidence.
5. For independent validation, withhold prior conclusions unless testing that conclusion is itself the task.

Read [subagent-prompt-template.md](../artifacts/subagent-prompt-template.md) when drafting a ready-to-send prompt. Consult the shared [prompt patterns](../../../../REFERENCES/prompt-patterns.md) only when an explorer, worker, validator, or forward-test example is needed.

## Decision Rules

- Replace placeholders with concrete paths, commands, and outputs before dispatch.
- Do not recreate a long specialist playbook inside the prompt when an available custom agent already carries it.
- Do not grant broad write, network, credential, or destructive authority merely to make the prompt self-contained.

## Output Contract

Return exactly: `Agent Type`, `Prompt`, `Expected Return`, `Validation`, `Unresolved Inputs`.

## Stop Conditions

Stop when the goal, ownership, authority, or acceptance evidence cannot be stated precisely enough for an independent agent.
