![Codex Subagents banner](https://github.com/CodeDraig/codex-subagents/blob/55f38c5763dc0cfcf7280b3523d11ca2f4eee56b/codex-subagents.jpg)

# Codex Subagents

Reusable Codex custom-agent templates, skill packages, and quality references for building focused multi-agent workflows.

This repository is a catalog, not an application. It provides copyable OpenAI/Codex agent TOML files, reusable skill packages, shared references, and local validation scripts that keep the catalog structurally consistent.

## Current Inventory

- 96 OpenAI agent templates in `AGENTS/openai/`.
- 53 skill packages in `SKILLS/`.
- 53 skill-sidecar files at `SKILLS/*/agents/openai.yaml`.
- 52 skill reference files under `SKILLS/*/references/`.
- 149 audited catalog assets tracked in `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`.

The latest full-catalog audit is in `docs/reviews/2026-05-24-skills-agents-quality-audit.md`.

## Repository Layout

```text
AGENTS/openai/                 Reusable OpenAI custom-agent TOML templates
SKILLS/<skill-name>/           Reusable Codex skill packages
SKILLS/<skill-name>/SKILL.md   Skill trigger, workflow, output, and boundaries
SKILLS/<skill-name>/agents/    Skill sidecar metadata
SKILLS/<skill-name>/references/ Supporting checklists, templates, and guides
REFERENCES/                    Shared catalog references and quality rules
docs/migration/                Canonical layout guidance
docs/reviews/                  Catalog audit and scoring matrix
docs/superpowers/              Design specs and implementation plans
docs/maestro/                  Historical implementation plans and records
scripts/catalog_quality/       Local catalog validation scripts
```

Use `docs/migration/current-layout.md` as the source of truth for where new catalog assets belong.

## Key References

- `REFERENCES/software-development-crew.md`: lifecycle map, routing rules, model coverage, intentional overlap, and implemented skill registry.
- `REFERENCES/quality-rubric.md`: readiness rubric for skills and agents.
- `REFERENCES/subagent-toml.md`: TOML format guidance for custom-agent files.
- `REFERENCES/prompt-patterns.md`: prompt patterns for delegating work to subagents.
- `SKILLS/codex-subagent-designer/SKILL.md`: workflow for designing or reviewing subagent systems.

## Validation

Run these commands from the repository root before relying on the catalog or after changing any asset:

```sh
python3.11 scripts/catalog_quality/validate_catalog.py
python3.11 scripts/catalog_quality/score_audit.py
git diff --check
```

`validate_catalog.py` checks TOML parseability, required agent fields, skill frontmatter, `$skill` references, registry coverage, skill sidecars, and `.DS_Store` files.

`score_audit.py` checks that the full-catalog audit matrix contains 149 rows and that every asset is rated `Ready` with complete score and evidence fields.

`scripts/catalog_quality/inventory.py` regenerates the review matrix and writes to `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`; use it intentionally, not as a read-only check.

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
references/<focused-supporting-file>.md
```

When copying a skill outside this repo, preserve its supporting references and sidecar metadata. For `SKILLS/codex-subagent-designer/`, also preserve the shared reference material and OpenAI agent examples described in `docs/migration/current-layout.md`.

## Adding Or Changing Assets

Before adding a new skill or agent:

1. Read `REFERENCES/quality-rubric.md`.
2. Place the asset in the canonical directory from `docs/migration/current-layout.md`.
3. Make the asset specific enough to change future agent behavior; do not add generic prompt advice.
4. Update `REFERENCES/software-development-crew.md` when the asset affects routing, lifecycle coverage, or implemented skill coverage.
5. Update the review matrix and audit docs when catalog readiness changes.
6. Run the validation commands above.

An asset is catalog-ready only when it has concrete domain checks, boundaries, validation guidance, handoffs, and an owner-facing output contract.

## What This Repo Does Not Provide

- No packaged application or runtime service.
- No package-manager install workflow.
- No Docker or CI configuration.
- No guarantee that model names or runtime fields remain valid forever; check the target Codex/OpenAI environment before broad installation.

## Maintenance Notes

The catalog is intentionally broad. Keep future changes narrow, scored against the rubric, and backed by validation evidence. If an asset only passes structurally, treat it as unfinished until the rubric says it is useful enough to reuse.
