# Software Development Subagent Crew Design

## Goal

Build a reusable Codex subagent roster for software development that spans the full lifecycle from ambiguous idea to production shipping and long-term maintenance.

## Structure

The roster will live under `codex-subagent-designer/agents/examples/openai/` as one TOML file per agent. This makes each agent reusable by copying a single file into `.codex/agents/` or a personal Codex agent directory. A registry at `codex-subagent-designer/references/software-development-crew.md` will group the agents by lifecycle stage and record the model, reasoning effort, sandbox posture, overlapping domains, and future Skill references.

## Model Coverage

The roster will intentionally use `gpt-5.5` at `low`, `medium`, `high`, and `xhigh` reasoning levels. It will also include `gpt-5.4-mini`, `gpt-5.3-codex`, and `gpt-5.3-codex-spark`. Overlap is allowed when the model choice changes behavior, such as a high-reasoning reviewer paired with a fast implementation fixer in the same domain.

## Agent Behavior

Each TOML file will include meaningful `developer_instructions`, not short role blurbs. Instructions will define how the agent reasons, what it owns, how it collaborates with concurrent agents, what it refuses to do without approval, and what evidence it must return. Agents may reference future Skills that do not exist yet, but every referenced Skill must be listed in the registry so it can be developed later.

## Lifecycle Coverage

The crew will cover intake, product discovery, research, architecture, planning, UX, design systems, frontend, backend, APIs, data, AI features, security, compliance, performance, testing, code review, refactoring, documentation, developer experience, release, operations, incident response, accessibility, localization, and dependency maintenance.

## Verification

The implementation should keep TOML syntax valid and maintain a readable inventory. Since this workspace is not a git repository and has no test runner, validation will use local syntax parsing with Python `tomllib` and direct inspection of the generated references.
