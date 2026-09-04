![Codex Subagents banner](https://github.com/CodeDraig/codex-subagents/blob/55f38c5763dc0cfcf7280b3523d11ca2f4eee56b/codex-subagents.jpg)

# Codex Subagents

Reusable Codex custom-agent templates, skill packages, and quality references for building focused multi-agent workflows.

This repository is a catalog, not an application. It provides copyable OpenAI/Codex agent TOML files, progressively disclosed skill packages, and shared quality references.

## Current Inventory

- 96 OpenAI agent templates in `AGENTS/openai/`.
- 19 skill gateways in `SKILLS/` covering 58 established workflows.
- 19 skill-sidecar files at `SKILLS/*/agents/openai.yaml`.
- 120 selectively loaded workflow and artifact references under `SKILLS/*/references/`.

## Repository Layout

```text
AGENTS/openai/                 Reusable OpenAI custom-agent TOML templates
SKILLS/<skill-name>/           Reusable Codex skill packages
SKILLS/<skill-name>/SKILL.md   Concise trigger, mode router, and shared boundaries
SKILLS/<skill-name>/agents/    Skill sidecar metadata
SKILLS/<skill-name>/references/workflows/ Mode-specific execution guidance
SKILLS/<skill-name>/references/artifacts/  Conditional checklists and templates
REFERENCES/                    Shared catalog references and quality rules
AGENTS.md                      Repository-wide asset placement and catalog rules
```

Use `AGENTS.md` as the source of truth for where new catalog assets belong.

## Key References

- `REFERENCES/software-development-crew.md`: lifecycle map, routing rules, model coverage, intentional overlap, and implemented skill registry.
- `REFERENCES/quality-rubric.md`: readiness rubric for skills and agents.
- `REFERENCES/subagent-toml.md`: TOML format guidance for custom-agent files.
- `REFERENCES/prompt-patterns.md`: prompt patterns for delegating work to subagents.
- `SKILLS/codex-subagent-designer/SKILL.md`: workflow for designing or reviewing subagent systems.

## Validation

Review every changed gateway mode against `REFERENCES/quality-rubric.md`; the weakest mode determines gateway readiness. Confirm that TOML and YAML parse, each `$skill` resolves, workflow and artifact links exist, no reference is orphaned, and no router eagerly loads sibling guidance. Run `git diff --check` before relying on the catalog.

## Using Agent Templates

1. Pick the role from `REFERENCES/software-development-crew.md`.
2. Copy the matching file from `AGENTS/openai/<agent-name>.toml` into a project's `.codex/agents/` directory.
3. Keep only the agents that are useful for that project; this catalog is not meant to be installed wholesale into every repo.
4. Review each copied agent's `sandbox_mode`, model, reasoning effort, and handoffs against the target project's risk profile.

Most agent files reference skills with `$skill-name`. If a copied agent depends on a skill, install or copy that skill too, or include the skill's workflow in the parent prompt.

## Using Skill Packages

Each skill package lives under `SKILLS/<skill-name>/` and normally includes:

```text
SKILL.md
agents/openai.yaml
references/workflows/<mode>.md
references/artifacts/<focused-checklist-or-template>.md
```

Invoke the gateway and name the intended mode, for example `$interface-design-review` in `accessibility-audit` mode. The router chooses one primary workflow and loads additional modes or artifacts only when the request explicitly needs them.

When copying a skill outside this repo, preserve its workflow references, artifact references, and sidecar metadata. For `SKILLS/codex-subagent-designer/`, also preserve the top-level references linked by its mode workflows.

## Adding Or Changing Assets

Before adding a new skill or agent:

1. Read `REFERENCES/quality-rubric.md`.
2. Place the asset in the canonical directory defined in `AGENTS.md`.
3. Make the asset specific enough to change future agent behavior; do not add generic prompt advice.
4. Update `REFERENCES/software-development-crew.md` when the asset affects routing, lifecycle coverage, or implemented skill coverage.
5. Review every affected mode; do not infer gateway readiness from a sample.
6. Perform the validation checks above.

An asset is catalog-ready only when it has concrete domain checks, boundaries, validation guidance, handoffs, and an owner-facing output contract.

## What This Repo Does Not Provide

- No packaged application or runtime service.
- No package-manager install workflow.
- No Docker or CI configuration.
- No guarantee that model names or runtime fields remain valid forever; check the target Codex/OpenAI environment before broad installation.

## Maintenance Notes

The catalog is intentionally broad. Keep future changes narrow, scored against the rubric, and backed by validation evidence. If an asset only passes structurally, treat it as unfinished until the rubric says it is useful enough to reuse.
