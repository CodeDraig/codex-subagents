# Full Catalog Uplift Design

Date: 2026-05-24

## Purpose

Upgrade every existing Codex subagent catalog asset so the repository no longer contains reusable Skills or Agents that are merely structurally valid but behaviorally thin.

The uplift covers all current `SKILLS/` packages and all current `AGENTS/openai/*.toml` templates. Success is measured against `REFERENCES/quality-rubric.md`, not by prose volume or asset count.

## Baseline

The current quality audit at `docs/reviews/2026-05-24-skills-agents-quality-audit.md` found:

- `48` skills reviewed.
- `4` skills rated `Ready`.
- `44` skills rated `Useful but Thin`.
- `91` agents reviewed.
- `61` agents rated `Ready`.
- `30` agents rated `Useful but Thin`.

The dominant weaknesses are:

- Skills often have a valid workflow but not enough domain heuristics, decision rules, validation guidance, examples, or supporting references.
- Tooling and validation guidance is the most common skill gap.
- Thin agents often lack explicit skill/reference grounding.
- Older agents often have weaker handoff boundaries than newer domain groups.
- Some output contracts need stronger evidence fields and validation status.

## Goals

- Bring every current skill to `Ready`: every required skill criterion scores at least `3`.
- Bring every current agent to `Ready`: every required agent criterion scores at least `3`.
- Preserve useful existing content while replacing shallow generic guidance with concrete behavior.
- Make each skill useful without requiring the parent agent to reconstruct the domain workflow from scratch.
- Make each agent distinct, dispatchable, bounded, and aligned with the skill/reference catalog.
- Produce an updated final audit proving all assets were re-reviewed after uplift.

## Non-Goals

- Do not add large new agent groups unless an existing asset cannot be made coherent without a missing adjacent specialist.
- Do not rewrite Ready assets for symmetry when targeted consistency fixes are enough.
- Do not treat longer files as inherently better.
- Do not install generated assets outside the repository until the repo version passes validation.
- Do not replace rubric scoring with subjective judgment.

## Approach

Use a rubric-led batch uplift organized by asset families. Each family gets shared improvement material, then each individual asset gets the tailored changes needed to satisfy the rubric on its own.

This is preferred over a purely asset-by-asset rewrite because the catalog is large enough that disconnected edits would drift in style, depth, and handoff conventions. It is preferred over a tooling-first rewrite because the immediate defect is catalog content quality, not missing automation alone.

## Asset Families

### 1. Software Engineering Core

Covers engineering execution, architecture, implementation planning, release, testing, observability, performance, security, privacy, API, data modeling, localization, dependency, and prompt-injection assets.

Expected improvements:

- Repository inspection heuristics.
- Validation command selection rules.
- Risk-based test depth rules.
- Handoffs among architecture, implementation, testing, security, release, and operations roles.
- Evidence requirements for changed files, commands, failures, residual risk, and owner decisions.

### 2. Data, Analytics, And ML

Covers analytics engineering, data science, ML engineering, MLOps, research data curation, metrics contracts, model delivery, and measurement guidance.

Expected improvements:

- Data lineage and metric-contract checks.
- Reproducibility, leakage, sampling, and evaluation heuristics.
- Model deployment and monitoring readiness checks.
- Handoffs among data science, ML engineering, MLOps, analytics engineering, and data platform roles.
- Evidence requirements for datasets, queries, notebooks, metrics, experiment tracking, and validation limits.

### 3. Research, News, Publishing, And Editorial

Covers literature review, citation integrity, research methods, journal submission, fact-checking, assignment/editing agents, copy/editing production, source verification, standards, OSINT, misinformation, and geolocation analysis.

Expected improvements:

- Source quality and provenance rules.
- Citation, quote, correction, uncertainty, and standards checks.
- Editorial handoffs across assignment, reporting, verification, copy editing, production, and ethics roles.
- Clear boundaries for public-source investigation and high-risk claims.
- Evidence requirements for source links, timestamps, excerpts, confidence levels, unresolved questions, and publication blockers.

### 4. Legal, Policy, Procurement, Finance, And Grants

Covers contract review, legal research, records retention, permissions, policy analysis, legislative tracking, public comments, procurement/vendor review, SOW/RFP, finance operations, invoices, audit evidence, grants, and sponsored project reporting.

Expected improvements:

- Authority, compliance, approval, and evidence hierarchy rules.
- Explicit non-legal-advice and owner-review boundaries where applicable.
- Handoffs across legal research, contract review, procurement, policy, grants, finance, and audit roles.
- Validation guidance for records, filings, statutes, policies, scorecards, budgets, invoices, and grant requirements.
- Evidence requirements for source authority, decision owners, exceptions, due dates, audit trail, and unresolved risk.

### 5. Product, UX, Design, Support, And Documentation

Covers product discovery, UX flow, design systems, accessibility, competitive research, documentation architecture, knowledge-base, customer support, escalation, diagnostics, and support automation.

Expected improvements:

- User/task segmentation and decision framing rules.
- Accessibility, design consistency, support impact, and docs information architecture checks.
- Handoffs among product, UX, design systems, documentation, customer support, diagnostics, escalation, and automation roles.
- Validation guidance for prototypes, UI states, docs navigation, support workflows, and customer communications.
- Evidence requirements for user problems, scenarios, screenshots or file paths where relevant, support impact, and owner decisions.

### 6. Meta-Catalog Assets

Covers `codex-subagent-designer`, catalog references, layout docs, rubric alignment, and final audit/reporting workflow.

Expected improvements:

- Ensure the designer skill continues to block shallow asset generation.
- Keep registry and layout guidance aligned with canonical `SKILLS/`, `AGENTS/`, and `REFERENCES/` homes.
- Improve repeatable scoring and validation procedure if needed.
- Produce final before/after audit evidence.

## Implementation Architecture

### Inventory

Create a working matrix for all current assets. For each asset, record:

- Asset path and family.
- Current rating and score vector.
- Required fixes from the audit.
- Referenced skills, references, and agent handoffs.
- Planned changes.
- New rating and validation evidence.

### Family Uplift Packets

For each family, define shared guidance before editing individual assets:

- Domain decision rules.
- Evidence and source standards.
- Validation commands, parser choices, or manual inspection checks.
- Output sections and required evidence fields.
- Handoff map.
- Common stop conditions and prohibited behavior.

Use shared packets to keep the family coherent, but do not let them substitute for individual asset readiness.

### Skill Uplift

Upgrade skills before agents. Each skill should include:

- Trigger guidance that names concrete task signals and exclusions.
- A repeatable domain workflow.
- Domain heuristics and decision rules.
- A meaningful referenced support asset where useful.
- Tooling or validation guidance, including when validation is impossible.
- A stable output contract.
- Domain-specific stop conditions and handoffs.

If detailed guidance would bloat `SKILL.md`, place it in `SKILLS/<skill>/references/` and link it from the skill.

### Agent Uplift

Upgrade agents after related skills are strong. Each agent should include:

- A distinct role with dispatch signals.
- Explicit `$skill-name` usage where a skill exists, or a concrete reason no skill applies.
- A fallback workflow summary if the skill is unavailable.
- Domain-specific intake, checks, artifacts, risks, and prohibitions.
- Runtime settings aligned to role risk and work mode.
- Handoffs to implemented agents, not future groups or vague teams.
- Exact return sections with evidence fields.

### Cross-Catalog Consistency

After each family and again at the end, verify:

- Agent-to-skill references resolve.
- Skill-to-agent registries resolve.
- Handoff targets exist.
- `REFERENCES/software-development-crew.md` coverage is current.
- No stale "future group" language remains.
- Adjacent roles have intentional overlap notes.
- Filenames, names, and registries match.

## Validation Gates

### Structural Validation

- All `SKILL.md` files retain valid frontmatter.
- All TOML agent files parse.
- All `agents/openai.yaml` files parse.
- Referenced local paths exist.
- No `.DS_Store` or local machine artifacts are introduced.

### Rubric Validation

- Every asset is scored against `REFERENCES/quality-rubric.md`.
- Any criterion below `3` is a blocking defect.
- Scores must cite concrete content in the asset or its referenced files.
- Generic platitudes fail even when structure passes.

### Content Quality Review

- Skills must include domain checks, decision rules, validation guidance, output contracts, and stop conditions.
- Agents must include task boundaries, skill/reference grounding, fallback behavior, handoffs, and exact output expectations.
- Already-Ready assets must not be degraded by broad rewrites.

### Final Audit

Update or replace `docs/reviews/2026-05-24-skills-agents-quality-audit.md` with final results that include:

- Total skills and agents reviewed.
- Before and after readiness counts.
- Final score table for every asset.
- Validation commands or scripts used.
- Any residual risk. The target residual risk is none for current assets below `Ready`.

## Execution Controls

- Work one family at a time.
- Complete skill upgrades before related agent upgrades.
- Keep a before/after matrix throughout implementation.
- Use subagents for independent family review lanes where helpful.
- Centralize final scoring to avoid rubric drift.
- Keep commits reviewable by family or validation milestone.
- Install generated or revised local skill copies only after the repository version passes validation.

## Acceptance Criteria

The work is complete when:

- Every current skill is rated `Ready`.
- Every current agent is rated `Ready`.
- No current asset has any required criterion below `3`.
- Structural validation passes.
- Cross-reference validation passes.
- Final audit evidence is committed.
- Any installed copies are synchronized from the validated repository state.
