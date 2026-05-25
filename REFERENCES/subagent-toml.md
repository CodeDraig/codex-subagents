# Codex Subagent TOML

Use this reference when creating or reviewing Codex custom subagent files and related `config.toml` entries.

Use `REFERENCES/quality-rubric.md` alongside this file when deciding whether an agent template is complete enough for reusable catalog inclusion.

## Locations

- Project-scoped custom agents: `.codex/agents/<name>.toml`
- Personal custom agents: `~/.codex/agents/<name>.toml`
- Global or project runtime limits: `config.toml` under `[agents]`

Prefer one custom agent per TOML file. Match the filename to `name` for readability, but treat the `name` field as the source of truth.

## Custom Agent File

Required fields:

- `name`: stable identifier used to reference the agent.
- `description`: capability statement that helps the parent decide when to use the agent.
- `developer_instructions`: standing instructions for the agent.

Reusable catalog agents should also include operational content in `developer_instructions`:

- Intake fields the parent should provide.
- Domain-specific checks, artifacts, evidence, and failure modes.
- `$skill-name` references when a relevant skill exists, plus fallback behavior if the skill is unavailable.
- Specific handoffs to implemented agents for adjacent work.
- Exact return sections aligned to downstream use.
- Stop conditions for unsafe, unauthorized, high-stakes, or evidence-poor work.

Common optional fields:

- `model`: override model for this role; omit to inherit.
- `model_reasoning_effort`: reasoning setting such as `"low"`, `"medium"`, `"high"`, or `"xhigh"` when supported by the configured model.
- `sandbox_mode`: for example `"read-only"` for review/exploration roles, or omit to inherit.
- `nickname_candidates`: non-empty display names for multiple instances of the same role.
- `mcp_servers`: role-specific MCP server configuration when needed.
- `skills.config`: role-specific skill configuration when supported by the runtime.

Example:

```toml
name = "reviewer"
description = "Reviews code for correctness, security, behavior regressions, and missing tests."
model = "gpt-5.4-mini"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
nickname_candidates = ["Atlas", "Delta", "Echo"]

developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings and file references.
Do not implement fixes unless explicitly asked.
"""
```

For implementation roles, use a writable sandbox only when edits are expected:

```toml
name = "payments-worker"
description = "Implements bounded changes in the payments module and runs targeted validation."
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"

developer_instructions = """
Implement only the assigned payments-module task.
You are not alone in the codebase. Do not revert edits made by others; adapt to concurrent changes.
Keep changes scoped, follow existing patterns, and report files changed plus commands run.
"""
```

## Runtime Agent Limits

Use `[agents]` in `config.toml` for concurrency and nesting limits:

```toml
[agents]
max_threads = 6
max_depth = 1
job_max_runtime_seconds = 1800
```

Current config schema also supports role entries with `config_file`, `description`, and `nickname_candidates`:

```toml
[agents.reviewer]
config_file = ".codex/agents/reviewer.toml"
description = "Read-only reviewer for code quality and regression risks."
nickname_candidates = ["Atlas", "Delta", "Echo"]
```

Use `max_depth = 1` unless there is a strong reason to allow subagents to spawn their own subagents.

## Practical Caveats

- Tool-backed Codex sessions may expose only generic `default`, `worker`, and `explorer` spawning even when custom TOML files exist. In that case, read the TOML and inject the role's `developer_instructions` into a generic spawned agent prompt.
- Agent-local `skills.config` behavior has changed across releases. Verify it in the target runtime before relying on per-agent skill enable/disable overrides.
- Keep agent files narrow. Broad "do everything" agents usually perform worse than explicit prompts plus built-in `worker` or `explorer` roles.
- Do not accept generic developer instructions that only say to be careful, communicate clearly, follow best practices, or consider edge cases. Reusable agents need domain-specific intake, checks, artifacts, boundaries, handoffs, and output contracts.
- Before installing a generated agent, parse the TOML, check every `$skill` reference, confirm every named handoff target exists, and score it with `quality-rubric.md`.
