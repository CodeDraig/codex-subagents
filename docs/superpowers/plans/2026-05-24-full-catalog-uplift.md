# Full Catalog Uplift Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade every existing `SKILLS/` package and `AGENTS/openai/` template to `Ready` under `REFERENCES/quality-rubric.md`.

**Architecture:** Use a rubric-led, family-based uplift. Build validation and inventory support first, upgrade skills before related agents in each family, then run a centralized cross-catalog scoring and audit pass.

**Tech Stack:** Markdown, TOML, YAML, Python standard library (`tomllib`, `pathlib`, `re`, `json`, `csv`), `rg`, `find`, `git`.

---

## Source Documents

- Design spec: `docs/superpowers/specs/2026-05-24-full-catalog-uplift-design.md`
- Current audit: `docs/reviews/2026-05-24-skills-agents-quality-audit.md`
- Rubric: `REFERENCES/quality-rubric.md`
- Agent format reference: `REFERENCES/subagent-toml.md`
- Crew registry: `REFERENCES/software-development-crew.md`
- Layout reference: `docs/migration/current-layout.md`

## File Structure

Create these planning and validation files:

- `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv` — working before/after matrix for every skill and agent.
- `docs/reviews/2026-05-24-skills-agents-quality-audit.md` — update with final all-Ready audit evidence.
- `scripts/catalog_quality/inventory.py` — generate the current skill/agent inventory.
- `scripts/catalog_quality/validate_catalog.py` — parse TOML/YAML/frontmatter, validate references, and detect local artifacts.
- `scripts/catalog_quality/score_audit.py` — summarize the matrix and fail if any asset is below `Ready`.

Modify assets in these existing locations:

- `SKILLS/*/SKILL.md`
- `SKILLS/*/references/*.md`
- `SKILLS/*/agents/openai.yaml`
- `AGENTS/openai/*.toml`
- `REFERENCES/software-development-crew.md`
- `REFERENCES/quality-rubric.md` only if scoring instructions need clarification discovered during implementation.
- `SKILLS/codex-subagent-designer/SKILL.md` only if the uplift reveals missing safeguards in the generator skill.

Do not install revised skills outside the repository until Task 9 passes.

## Family Ownership

Use these family boundaries to avoid file conflicts:

### Software Engineering Core

Skills:

- `SKILLS/accessibility-audit/`
- `SKILLS/ai-evals/`
- `SKILLS/api-contract-review/`
- `SKILLS/architecture-decision-records/`
- `SKILLS/data-modeling/`
- `SKILLS/dependency-risk-triage/`
- `SKILLS/design-system-audit/`
- `SKILLS/docs-information-architecture/`
- `SKILLS/engineering-execution/`
- `SKILLS/implementation-planning/`
- `SKILLS/incident-postmortems/`
- `SKILLS/localization-readiness/`
- `SKILLS/observability-runbooks/`
- `SKILLS/performance-profiling/`
- `SKILLS/privacy-review/`
- `SKILLS/prompt-injection-defense/`
- `SKILLS/release-readiness/`
- `SKILLS/test-matrix-design/`
- `SKILLS/threat-modeling/`
- `SKILLS/ux-flow-mapping/`

Agents:

- `AGENTS/openai/accessibility-reviewer.toml`
- `AGENTS/openai/ai-feature-engineer.toml`
- `AGENTS/openai/api-contract-architect.toml`
- `AGENTS/openai/backend-domain-engineer.toml`
- `AGENTS/openai/build-release-engineer.toml`
- `AGENTS/openai/code-reviewer.toml`
- `AGENTS/openai/data-platform-engineer.toml`
- `AGENTS/openai/database-modeler.toml`
- `AGENTS/openai/dependency-maintenance-engineer.toml`
- `AGENTS/openai/design-system-engineer.toml`
- `AGENTS/openai/developer-experience-engineer.toml`
- `AGENTS/openai/devops-platform-engineer.toml`
- `AGENTS/openai/documentation-engineer.toml`
- `AGENTS/openai/frontend-experience-engineer.toml`
- `AGENTS/openai/implementation-finisher.toml`
- `AGENTS/openai/localization-engineer.toml`
- `AGENTS/openai/observability-incident-engineer.toml`
- `AGENTS/openai/performance-investigator.toml`
- `AGENTS/openai/performance-optimizer.toml`
- `AGENTS/openai/privacy-compliance-reviewer.toml`
- `AGENTS/openai/prompt-evaluation-engineer.toml`
- `AGENTS/openai/rapid-prototype-scout.toml`
- `AGENTS/openai/refactor-surgeon.toml`
- `AGENTS/openai/security-fix-engineer.toml`
- `AGENTS/openai/security-threat-modeler.toml`
- `AGENTS/openai/software-engineering-lead.toml`
- `AGENTS/openai/systems-architect.toml`
- `AGENTS/openai/technical-planner.toml`
- `AGENTS/openai/test-automation-engineer.toml`
- `AGENTS/openai/test-strategy-architect.toml`
- `AGENTS/openai/triage-router.toml`
- `AGENTS/openai/ux-flow-architect.toml`

### Data, Analytics, And ML

Skills:

- `SKILLS/analytics-engineering/`
- `SKILLS/data-science-workflows/`
- `SKILLS/ml-engineering/`
- `SKILLS/mlops-readiness/`

Agents:

- `AGENTS/openai/analytics-engineer.toml`
- `AGENTS/openai/data-scientist.toml`
- `AGENTS/openai/ml-engineer.toml`
- `AGENTS/openai/mlops-engineer.toml`
- `AGENTS/openai/research-data-curator.toml`

### Research, News, Publishing, And Editorial

Skills:

- `SKILLS/academic-literature-review/`
- `SKILLS/citation-integrity-review/`
- `SKILLS/journal-submission-workflows/`
- `SKILLS/permissions-rights-review/`
- `SKILLS/publishing-production-workflows/`
- `SKILLS/research-methods-review/`

Agents:

- `AGENTS/openai/assignment-editor.toml`
- `AGENTS/openai/audience-seo-editor.toml`
- `AGENTS/openai/breaking-news-reporter.toml`
- `AGENTS/openai/citation-integrity-checker.toml`
- `AGENTS/openai/copy-desk-editor.toml`
- `AGENTS/openai/developmental-manuscript-editor.toml`
- `AGENTS/openai/geolocation-chronolocation-analyst.toml`
- `AGENTS/openai/indexing-coordinator.toml`
- `AGENTS/openai/journal-submission-specialist.toml`
- `AGENTS/openai/literature-reviewer.toml`
- `AGENTS/openai/misinformation-risk-analyst.toml`
- `AGENTS/openai/news-fact-checker.toml`
- `AGENTS/openai/osint-research-lead.toml`
- `AGENTS/openai/peer-review-prep-editor.toml`
- `AGENTS/openai/permissions-reviewer.toml`
- `AGENTS/openai/production-editor.toml`
- `AGENTS/openai/public-records-researcher.toml`
- `AGENTS/openai/social-network-analyst.toml`
- `AGENTS/openai/source-verification-analyst.toml`
- `AGENTS/openai/standards-ethics-editor.toml`

### Legal, Policy, Procurement, Finance, And Grants

Skills:

- `SKILLS/audit-evidence-management/`
- `SKILLS/contract-review-operations/`
- `SKILLS/finance-operations-review/`
- `SKILLS/grant-budget-justification/`
- `SKILLS/grant-proposal-compliance/`
- `SKILLS/invoice-reconciliation-workflows/`
- `SKILLS/legal-research-workflows/`
- `SKILLS/legislative-tracking/`
- `SKILLS/policy-analysis-workflows/`
- `SKILLS/procurement-vendor-review/`
- `SKILLS/public-comment-drafting/`
- `SKILLS/records-retention-operations/`
- `SKILLS/rfp-response-workflows/`
- `SKILLS/sow-review-workflows/`
- `SKILLS/sponsored-projects-reporting/`

Agents:

- `AGENTS/openai/accounting-controls-reviewer.toml`
- `AGENTS/openai/audit-evidence-organizer.toml`
- `AGENTS/openai/budget-justification-writer.toml`
- `AGENTS/openai/budget-variance-analyst.toml`
- `AGENTS/openai/contract-review-specialist.toml`
- `AGENTS/openai/financial-model-reviewer.toml`
- `AGENTS/openai/grant-opportunity-scout.toml`
- `AGENTS/openai/grant-reporting-specialist.toml`
- `AGENTS/openai/impact-assessment-writer.toml`
- `AGENTS/openai/invoice-reconciliation-specialist.toml`
- `AGENTS/openai/legal-ops-coordinator.toml`
- `AGENTS/openai/legal-research-analyst.toml`
- `AGENTS/openai/legislative-tracker.toml`
- `AGENTS/openai/policy-analyst.toml`
- `AGENTS/openai/procurement-compliance-specialist.toml`
- `AGENTS/openai/proposal-compliance-reviewer.toml`
- `AGENTS/openai/public-comment-drafter.toml`
- `AGENTS/openai/records-retention-advisor.toml`
- `AGENTS/openai/regulatory-monitor.toml`
- `AGENTS/openai/rfp-response-analyst.toml`
- `AGENTS/openai/sow-reviewer.toml`
- `AGENTS/openai/sponsored-projects-coordinator.toml`
- `AGENTS/openai/stakeholder-map-analyst.toml`
- `AGENTS/openai/vendor-risk-reviewer.toml`
- `AGENTS/openai/vendor-scorecard-analyst.toml`

### Product, UX, Design, Support, And Documentation

Skills:

- `SKILLS/competitive-research/`
- `SKILLS/product-discovery/`

Agents:

- `AGENTS/openai/customer-communications-specialist.toml`
- `AGENTS/openai/customer-diagnostics-engineer.toml`
- `AGENTS/openai/escalation-support-engineer.toml`
- `AGENTS/openai/knowledge-base-author.toml`
- `AGENTS/openai/market-researcher.toml`
- `AGENTS/openai/product-discovery-strategist.toml`
- `AGENTS/openai/support-automation-engineer.toml`
- `AGENTS/openai/support-triage-specialist.toml`

### Meta-Catalog

Skills:

- `SKILLS/codex-subagent-designer/`

References and docs:

- `REFERENCES/quality-rubric.md`
- `REFERENCES/software-development-crew.md`
- `REFERENCES/subagent-toml.md`
- `REFERENCES/prompt-patterns.md`
- `docs/migration/current-layout.md`
- `docs/reviews/2026-05-24-skills-agents-quality-audit.md`

## Task 1: Add Catalog Inventory And Validation Scripts

**Files:**

- Create: `scripts/catalog_quality/inventory.py`
- Create: `scripts/catalog_quality/validate_catalog.py`
- Create: `scripts/catalog_quality/score_audit.py`
- Create: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`

- [ ] **Step 1: Create the scripts directory**

Run:

```bash
mkdir -p scripts/catalog_quality
```

Expected: directory exists at `scripts/catalog_quality/`.

- [ ] **Step 2: Write `inventory.py`**

Create `scripts/catalog_quality/inventory.py` with this behavior:

```python
#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "SKILLS"
AGENTS = ROOT / "AGENTS" / "openai"
OUTPUT = ROOT / "docs" / "reviews" / "2026-05-24-full-catalog-uplift-matrix.csv"

FAMILIES = {
    "software-engineering-core": {
        "skills": {
            "accessibility-audit", "ai-evals", "api-contract-review",
            "architecture-decision-records", "data-modeling",
            "dependency-risk-triage", "design-system-audit",
            "docs-information-architecture", "engineering-execution",
            "implementation-planning", "incident-postmortems",
            "localization-readiness", "observability-runbooks",
            "performance-profiling", "privacy-review",
            "prompt-injection-defense", "release-readiness",
            "test-matrix-design", "threat-modeling", "ux-flow-mapping",
        },
        "agents": {
            "accessibility-reviewer", "ai-feature-engineer",
            "api-contract-architect", "backend-domain-engineer",
            "build-release-engineer", "code-reviewer",
            "data-platform-engineer", "database-modeler",
            "dependency-maintenance-engineer", "design-system-engineer",
            "developer-experience-engineer", "devops-platform-engineer",
            "documentation-engineer", "frontend-experience-engineer",
            "implementation-finisher", "localization-engineer",
            "observability-incident-engineer", "performance-investigator",
            "performance-optimizer", "privacy-compliance-reviewer",
            "prompt-evaluation-engineer", "rapid-prototype-scout",
            "refactor-surgeon", "security-fix-engineer",
            "security-threat-modeler", "software-engineering-lead",
            "systems-architect", "technical-planner",
            "test-automation-engineer", "test-strategy-architect",
            "triage-router", "ux-flow-architect",
        },
    },
    "data-analytics-ml": {
        "skills": {"analytics-engineering", "data-science-workflows", "ml-engineering", "mlops-readiness"},
        "agents": {"analytics-engineer", "data-scientist", "ml-engineer", "mlops-engineer", "research-data-curator"},
    },
    "research-news-publishing-editorial": {
        "skills": {
            "academic-literature-review", "citation-integrity-review",
            "journal-submission-workflows", "permissions-rights-review",
            "publishing-production-workflows", "research-methods-review",
        },
        "agents": {
            "assignment-editor", "audience-seo-editor", "breaking-news-reporter",
            "citation-integrity-checker", "copy-desk-editor",
            "developmental-manuscript-editor", "geolocation-chronolocation-analyst",
            "indexing-coordinator", "journal-submission-specialist",
            "literature-reviewer", "misinformation-risk-analyst",
            "news-fact-checker", "osint-research-lead",
            "peer-review-prep-editor", "permissions-reviewer",
            "production-editor", "public-records-researcher",
            "social-network-analyst", "source-verification-analyst",
            "standards-ethics-editor",
        },
    },
    "legal-policy-procurement-finance-grants": {
        "skills": {
            "audit-evidence-management", "contract-review-operations",
            "finance-operations-review", "grant-budget-justification",
            "grant-proposal-compliance", "invoice-reconciliation-workflows",
            "legal-research-workflows", "legislative-tracking",
            "policy-analysis-workflows", "procurement-vendor-review",
            "public-comment-drafting", "records-retention-operations",
            "rfp-response-workflows", "sow-review-workflows",
            "sponsored-projects-reporting",
        },
        "agents": {
            "accounting-controls-reviewer", "audit-evidence-organizer",
            "budget-justification-writer", "budget-variance-analyst",
            "contract-review-specialist", "financial-model-reviewer",
            "grant-opportunity-scout", "grant-reporting-specialist",
            "impact-assessment-writer", "invoice-reconciliation-specialist",
            "legal-ops-coordinator", "legal-research-analyst",
            "legislative-tracker", "policy-analyst",
            "procurement-compliance-specialist", "proposal-compliance-reviewer",
            "public-comment-drafter", "records-retention-advisor",
            "regulatory-monitor", "rfp-response-analyst", "sow-reviewer",
            "sponsored-projects-coordinator", "stakeholder-map-analyst",
            "vendor-risk-reviewer", "vendor-scorecard-analyst",
        },
    },
    "product-ux-design-support-docs": {
        "skills": {"competitive-research", "product-discovery"},
        "agents": {
            "customer-communications-specialist", "customer-diagnostics-engineer",
            "escalation-support-engineer", "knowledge-base-author",
            "market-researcher", "product-discovery-strategist",
            "support-automation-engineer", "support-triage-specialist",
        },
    },
    "meta-catalog": {
        "skills": {"codex-subagent-designer"},
        "agents": set(),
    },
}


def family_for(kind: str, name: str) -> str:
    bucket = "skills" if kind == "skill" else "agents"
    matches = [family for family, assets in FAMILIES.items() if name in assets[bucket]]
    if len(matches) != 1:
        raise SystemExit(f"{kind} {name!r} matched {len(matches)} families: {matches}")
    return matches[0]


def main() -> None:
    rows: list[dict[str, str]] = []
    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        name = skill_file.parent.name
        rows.append({
            "kind": "skill",
            "family": family_for("skill", name),
            "name": name,
            "path": str(skill_file.relative_to(ROOT)),
            "before_rating": "",
            "before_scores": "",
            "required_fixes": "",
            "planned_changes": "",
            "after_rating": "",
            "after_scores": "",
            "validation_evidence": "",
        })
    for agent_file in sorted(AGENTS.glob("*.toml")):
        name = agent_file.stem
        rows.append({
            "kind": "agent",
            "family": family_for("agent", name),
            "name": name,
            "path": str(agent_file.relative_to(ROOT)),
            "before_rating": "",
            "before_scores": "",
            "required_fixes": "",
            "planned_changes": "",
            "after_rating": "",
            "after_scores": "",
            "validation_evidence": "",
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {OUTPUT.relative_to(ROOT)} rows={len(rows)}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Write `validate_catalog.py`**

Create `scripts/catalog_quality/validate_catalog.py` with checks for TOML parsing, skill frontmatter, YAML-like registry presence, `$skill` references, handoff names, and `.DS_Store` artifacts.

```python
#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "SKILLS"
AGENTS = ROOT / "AGENTS" / "openai"
REGISTRY = ROOT / "REFERENCES" / "software-development-crew.md"

REQUIRED_TOML_KEYS = {
    "name",
    "description",
    "model",
    "model_reasoning_effort",
    "developer_instructions",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def skill_names() -> set[str]:
    return {path.parent.name for path in SKILLS.glob("*/SKILL.md")}


def agent_names() -> set[str]:
    return {path.stem for path in AGENTS.glob("*.toml")}


def validate_skill_frontmatter(failures: list[str]) -> None:
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        text = path.read_text()
        if not text.startswith("---\n"):
            fail(f"{path.relative_to(ROOT)} missing opening frontmatter", failures)
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            fail(f"{path.relative_to(ROOT)} missing closing frontmatter", failures)
            continue
        frontmatter = text[4:end]
        if "name:" not in frontmatter:
            fail(f"{path.relative_to(ROOT)} frontmatter missing name", failures)
        if "description:" not in frontmatter:
            fail(f"{path.relative_to(ROOT)} frontmatter missing description", failures)


def validate_toml(failures: list[str]) -> None:
    names = agent_names()
    for path in sorted(AGENTS.glob("*.toml")):
        try:
            data = tomllib.loads(path.read_text())
        except tomllib.TOMLDecodeError as exc:
            fail(f"{path.relative_to(ROOT)} TOML parse failed: {exc}", failures)
            continue
        missing = sorted(REQUIRED_TOML_KEYS - set(data))
        if missing:
            fail(f"{path.relative_to(ROOT)} missing keys {missing}", failures)
        if data.get("name") != path.stem:
            fail(f"{path.relative_to(ROOT)} name {data.get('name')!r} does not match filename", failures)
        instructions = str(data.get("developer_instructions", ""))
        for target in re.findall(r"`([a-z0-9-]+)`", instructions):
            if target.endswith("-engineer") or target.endswith("-reviewer") or target.endswith("-analyst") or target.endswith("-editor") or target.endswith("-specialist") or target.endswith("-architect") or target.endswith("-lead") or target.endswith("-author") or target.endswith("-strategist") or target.endswith("-coordinator") or target.endswith("-drafter") or target.endswith("-writer") or target.endswith("-scout"):
                if target not in names:
                    fail(f"{path.relative_to(ROOT)} references unknown agent `{target}`", failures)


def validate_skill_refs(failures: list[str]) -> None:
    names = skill_names()
    for path in sorted(AGENTS.glob("*.toml")):
        text = path.read_text()
        for skill in re.findall(r"\$([a-z0-9-]+)", text):
            if skill not in names:
                fail(f"{path.relative_to(ROOT)} references missing skill ${skill}", failures)


def validate_registries(failures: list[str]) -> None:
    registry = REGISTRY.read_text()
    for agent in sorted(agent_names()):
        if agent not in registry:
            fail(f"{REGISTRY.relative_to(ROOT)} missing agent {agent}", failures)
    for skill in sorted(skill_names()):
        if skill not in registry and skill != "codex-subagent-designer":
            fail(f"{REGISTRY.relative_to(ROOT)} missing skill {skill}", failures)
    for path in sorted(SKILLS.glob("*/agents/openai.yaml")):
        text = path.read_text()
        if "models:" not in text and "agents:" not in text:
            fail(f"{path.relative_to(ROOT)} missing models or agents key", failures)


def validate_artifacts(failures: list[str]) -> None:
    for path in ROOT.rglob(".DS_Store"):
        fail(f"local artifact present: {path.relative_to(ROOT)}", failures)


def main() -> int:
    failures: list[str] = []
    validate_skill_frontmatter(failures)
    validate_toml(failures)
    validate_skill_refs(failures)
    validate_registries(failures)
    validate_artifacts(failures)
    if failures:
        print("catalog validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("catalog validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Write `score_audit.py`**

Create `scripts/catalog_quality/score_audit.py` to enforce the working matrix after reviewers fill in scores.

```python
#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "docs" / "reviews" / "2026-05-24-full-catalog-uplift-matrix.csv"


def parse_scores(value: str) -> list[int]:
    pieces = [piece.strip() for piece in value.split("/") if piece.strip()]
    if len(pieces) != 7:
        raise ValueError(f"score vector must have 7 values, got {value!r}")
    scores = [int(piece) for piece in pieces]
    if any(score < 0 or score > 4 for score in scores):
        raise ValueError(f"score vector has value outside 0..4: {value!r}")
    return scores


def main() -> int:
    failures: list[str] = []
    with MATRIX.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 139:
        failures.append(f"expected 139 assets, found {len(rows)}")
    for row in rows:
        name = f"{row['kind']}:{row['name']}"
        if row["after_rating"] != "Ready":
            failures.append(f"{name} after_rating is {row['after_rating']!r}")
        try:
            scores = parse_scores(row["after_scores"])
        except ValueError as exc:
            failures.append(f"{name} invalid after_scores: {exc}")
            continue
        low = [str(score) for score in scores if score < 3]
        if low:
            failures.append(f"{name} has scores below 3: {'/'.join(map(str, scores))}")
        if not row["validation_evidence"].strip():
            failures.append(f"{name} missing validation_evidence")
    if failures:
        print("score audit failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("score audit passed: all assets Ready")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Generate the initial matrix**

Run:

```bash
python3 scripts/catalog_quality/inventory.py
```

Expected output:

```text
wrote docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv rows=139
```

- [ ] **Step 6: Run structural validation**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
```

Expected: either `catalog validation passed` or a concrete defect list to fix before family work begins.

- [ ] **Step 7: Commit validation scaffolding**

Run:

```bash
git add scripts/catalog_quality docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv
git commit -m "chore: add catalog quality validation tools"
```

## Task 2: Uplift Software Engineering Core

**Files:**

- Modify the Software Engineering Core skill and agent files listed in Family Ownership.
- Modify: `REFERENCES/software-development-crew.md`
- Modify: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`

- [ ] **Step 1: Review current deficiencies**

Run:

```bash
rg -n "engineering-execution|architecture-decision-records|data-modeling|design-system-audit|observability-runbooks|release-readiness|ux-flow-mapping|backend-domain-engineer|frontend-experience-engineer|performance-optimizer|rapid-prototype-scout|implementation-finisher" docs/reviews/2026-05-24-skills-agents-quality-audit.md
```

Expected: rows showing the required fixes for this family.

- [ ] **Step 2: Upgrade skills first**

For each Software Engineering Core skill, edit `SKILL.md` and referenced files so the package includes:

- concrete repository inspection heuristics;
- risk-based validation command selection;
- expected evidence fields;
- stop conditions for unsafe edits, unverified tests, missing repo context, or high-stakes domains;
- output sections tied to the skill's workflow.

Required minimum changes for previously thin skills:

- `engineering-execution`: add execution sequencing, user-change preservation, conflict boundaries, and verification escalation.
- `architecture-decision-records`: add decision fitness rules, reversibility checks, alternatives table guidance, and ADR validation.
- `data-modeling`: add entity ownership, migration safety, index/query-shape, retention/deletion, and backfill checks.
- `design-system-audit`: add token/component inventory rules, state coverage, contrast/motion/accessibility checks, and screenshot evidence.
- `observability-runbooks`: add log/metric/trace/alert/runbook evidence rules and alert actionability checks.
- `release-readiness`: add rollout, rollback, migration, feature flag, package, and release-note validation.
- `ux-flow-mapping`: add entry/exit states, empty/error/loading/recovery paths, permission states, and task completion checks.
- All other skills in the family: score against the rubric and make targeted changes if any criterion is below `3`.

- [ ] **Step 3: Upgrade agents after skills**

For each Software Engineering Core agent, update `developer_instructions` so the agent:

- references the relevant `$skill-name` when one exists;
- includes a fallback workflow if the skill is unavailable;
- names concrete handoffs to implemented agents;
- contains exact output sections with evidence fields;
- keeps runtime settings aligned with review versus implementation responsibility.

Required minimum changes for previously thin agents:

- `backend-domain-engineer`: reference `$engineering-execution`, `$api-contract-review`, or `$data-modeling` based on task; add handoffs to `database-modeler`, `api-contract-architect`, `security-fix-engineer`, and `test-automation-engineer`.
- `frontend-experience-engineer`: reference `$engineering-execution`, `$ux-flow-mapping`, `$accessibility-audit`, and `$design-system-audit`; add handoffs to `design-system-engineer`, `accessibility-reviewer`, and `test-automation-engineer`.
- `implementation-finisher`: reference `$implementation-planning`, `$release-readiness`, and `$test-matrix-design`; add stop conditions for broad redesign and missing validation.
- `performance-optimizer`: reference `$performance-profiling`; hand off unmeasured bottlenecks to `performance-investigator`.
- `rapid-prototype-scout`: reference `$product-discovery` or `$engineering-execution`; add boundaries that prototypes must not become production changes without owner approval.
- `refactor-surgeon`, `security-fix-engineer`, `support-automation-engineer`, `test-automation-engineer`, and other thin software agents: add skill grounding and handoffs shown by the rubric audit.

- [ ] **Step 4: Update registry and matrix**

Update `REFERENCES/software-development-crew.md` so new or strengthened skill references and handoffs appear in lifecycle, routing, model coverage, and intentional overlap sections.

Update matrix rows for this family:

- `planned_changes`: one sentence naming the actual added behavior.
- `after_rating`: `Ready`.
- `after_scores`: seven slash-separated values, each at least `3`.
- `validation_evidence`: commands run plus files inspected.

- [ ] **Step 5: Validate and commit**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Expected:

```text
catalog validation passed
```

Then commit:

```bash
git add SKILLS AGENTS/openai REFERENCES/software-development-crew.md docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv
git commit -m "docs: uplift software engineering catalog assets"
```

## Task 3: Uplift Data, Analytics, And ML

**Files:**

- Modify the Data, Analytics, And ML skill and agent files listed in Family Ownership.
- Modify: `REFERENCES/software-development-crew.md`
- Modify: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`

- [ ] **Step 1: Review current deficiencies**

Run:

```bash
rg -n "analytics-engineering|data-science-workflows|ml-engineering|mlops-readiness|analytics-engineer|data-scientist|ml-engineer|mlops-engineer|research-data-curator" docs/reviews/2026-05-24-skills-agents-quality-audit.md
```

- [ ] **Step 2: Upgrade skills first**

Add domain heuristics and validation guidance:

- `analytics-engineering`: metric contract checks, grain/aggregation rules, lineage, freshness, backfill, null semantics, and dashboard/query validation.
- `data-science-workflows`: hypothesis framing, dataset provenance, sampling, leakage, baselines, evaluation metrics, reproducibility, and uncertainty reporting.
- `ml-engineering`: training/inference contract, feature ownership, model packaging, evaluation handoff, deployment constraints, and failure-mode checks.
- `mlops-readiness`: model registry, monitoring, drift, rollback, inference SLO, data dependency, alerting, and approval-gate checks.

- [ ] **Step 3: Upgrade agents after skills**

Ensure:

- `analytics-engineer` references `$analytics-engineering` and names handoffs to `data-platform-engineer`, `data-scientist`, and `documentation-engineer`.
- `data-scientist` references `$data-science-workflows` and names handoffs to `analytics-engineer`, `ml-engineer`, and `research-data-curator`.
- `ml-engineer` references `$ml-engineering` and names handoffs to `mlops-engineer`, `data-platform-engineer`, and `performance-investigator`.
- `mlops-engineer` references `$mlops-readiness`, `$observability-runbooks`, and `$release-readiness`.
- `research-data-curator` references `$data-science-workflows` or adds a fallback curation workflow with provenance, schema, retention, and reproducibility evidence.

- [ ] **Step 4: Update registry and matrix**

Update registry handoffs and matrix rows for this family with all `after_scores` at least `3`.

- [ ] **Step 5: Validate and commit**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Commit:

```bash
git add SKILLS AGENTS/openai REFERENCES/software-development-crew.md docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv
git commit -m "docs: uplift data analytics and ml catalog assets"
```

## Task 4: Uplift Research, News, Publishing, And Editorial

**Files:**

- Modify the Research, News, Publishing, And Editorial skill and agent files listed in Family Ownership.
- Modify: `REFERENCES/software-development-crew.md`
- Modify: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`

- [ ] **Step 1: Review current deficiencies**

Run:

```bash
rg -n "academic-literature-review|citation-integrity-review|journal-submission-workflows|permissions-rights-review|publishing-production-workflows|research-methods-review|assignment-editor|audience-seo-editor|copy-desk-editor|geolocation-chronolocation-analyst|news-fact-checker|osint-research-lead|source-verification-analyst|standards-ethics-editor" docs/reviews/2026-05-24-skills-agents-quality-audit.md
```

- [ ] **Step 2: Upgrade skills first**

Add source-quality, provenance, validation, and output guidance:

- `academic-literature-review`: search strategy, inclusion/exclusion criteria, evidence grading, synthesis patterns, citation integrity, and uncertainty.
- `citation-integrity-review`: bibliographic matching, quote verification, page/section evidence, retraction/correction checks, and fabricated-source stops.
- `journal-submission-workflows`: scope fit, author instructions, files checklist, metadata, cover letter, ethics declarations, and submission blockers.
- `permissions-rights-review`: rights holder, use type, territory, term, exclusivity, fair-use review boundary, and clearance evidence.
- `publishing-production-workflows`: copy flow, proof stages, metadata, assets, indexing, accessibility, and publication hold criteria.
- `research-methods-review`: design validity, sampling, controls, measurement, bias, reproducibility, and ethics review boundaries.

- [ ] **Step 3: Upgrade agents after skills**

Ensure previously thin editorial and investigation agents reference available skills or state why no skill exists:

- `assignment-editor`, `breaking-news-reporter`, `news-fact-checker`, `source-verification-analyst`, and `standards-ethics-editor`: add source provenance, timestamp discipline, correction, allegation, and publication-risk handoffs.
- `copy-desk-editor`, `audience-seo-editor`, `production-editor`, `indexing-coordinator`, and `knowledge-base-author` where applicable: add production and metadata handoffs.
- `geolocation-chronolocation-analyst`, `osint-research-lead`, `misinformation-risk-analyst`, and `social-network-analyst`: add public-source safety boundaries, confidence levels, non-targeting rules, and evidence treatment.
- `literature-reviewer`, `citation-integrity-checker`, `journal-submission-specialist`, `peer-review-prep-editor`, and `research-methods-reviewer`: align to strengthened research skills.

- [ ] **Step 4: Update registry and matrix**

Update registry handoffs and matrix rows for this family with all `after_scores` at least `3`.

- [ ] **Step 5: Validate and commit**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Commit:

```bash
git add SKILLS AGENTS/openai REFERENCES/software-development-crew.md docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv
git commit -m "docs: uplift research editorial and publishing assets"
```

## Task 5: Uplift Legal, Policy, Procurement, Finance, And Grants

**Files:**

- Modify the Legal, Policy, Procurement, Finance, And Grants skill and agent files listed in Family Ownership.
- Modify: `REFERENCES/software-development-crew.md`
- Modify: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`

- [ ] **Step 1: Review current deficiencies**

Run:

```bash
rg -n "audit-evidence-management|finance-operations-review|grant-budget-justification|grant-proposal-compliance|invoice-reconciliation-workflows|legal-research-workflows|legislative-tracking|policy-analysis-workflows|procurement-vendor-review|public-comment-drafting|records-retention-operations|rfp-response-workflows|sow-review-workflows|sponsored-projects-reporting" docs/reviews/2026-05-24-skills-agents-quality-audit.md
```

- [ ] **Step 2: Upgrade skills first**

Strengthen evidence, authority, and owner-review guidance:

- `audit-evidence-management`: evidence chain, sufficiency, sampling, control mapping, retention, and exception handling.
- `finance-operations-review`: reconciliation, variance, approval, policy exception, source document, and financial-advice boundaries.
- `grant-budget-justification`: funder rules, allowability, allocation basis, matching, personnel, indirects, and narrative evidence.
- `grant-proposal-compliance`: eligibility, required attachments, page limits, due dates, certifications, budget alignment, and submission blockers.
- `invoice-reconciliation-workflows`: purchase order, receipt, duplicate, tax, approval, exception, and payment-status checks.
- `legal-research-workflows`: authority hierarchy, jurisdiction, currency, procedural posture, non-advice boundary, and counsel questions.
- `legislative-tracking`: bill status, chamber, committee, amendments, sponsors, effective dates, and source links.
- `policy-analysis-workflows`: stakeholder impact, implementation feasibility, tradeoffs, affected parties, and evidence limits.
- `procurement-vendor-review`: scoring criteria, conflict checks, risk, references, compliance, and award rationale.
- `public-comment-drafting`: docket source, standing, evidence, requested action, tone, and submission constraints.
- `records-retention-operations`: schedule authority, record class, legal hold, privacy, disposition, and audit trail.
- `rfp-response-workflows`: compliance matrix, win themes, evidence, assumptions, pricing handoff, and no-bid triggers.
- `sow-review-workflows`: scope, deliverables, acceptance, dependencies, assumptions, change control, and commercial handoffs.
- `sponsored-projects-reporting`: award terms, reporting period, expenses, deliverables, certifications, and sponsor evidence.

- [ ] **Step 3: Upgrade agents after skills**

Align agents with strengthened skills and concrete handoffs:

- Contract/legal agents hand off procurement scoring to `vendor-scorecard-analyst`, vendor risk to `vendor-risk-reviewer`, SOW issues to `sow-reviewer`, and records questions to `records-retention-advisor`.
- Policy agents hand off public comments to `public-comment-drafter`, stakeholder mapping to `stakeholder-map-analyst`, legislative status to `legislative-tracker`, and impact analysis to `impact-assessment-writer`.
- Finance and grant agents hand off invoice evidence to `invoice-reconciliation-specialist`, audit packets to `audit-evidence-organizer`, budget variance to `budget-variance-analyst`, and proposal compliance to `proposal-compliance-reviewer`.
- Every high-stakes agent names owner/counsel/finance review gates and avoids final legal, financial, procurement-award, or compliance determinations.

- [ ] **Step 4: Update registry and matrix**

Update registry handoffs and matrix rows for this family with all `after_scores` at least `3`.

- [ ] **Step 5: Validate and commit**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Commit:

```bash
git add SKILLS AGENTS/openai REFERENCES/software-development-crew.md docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv
git commit -m "docs: uplift legal finance procurement and policy assets"
```

## Task 6: Uplift Product, UX, Design, Support, And Documentation

**Files:**

- Modify the Product, UX, Design, Support, And Documentation skill and agent files listed in Family Ownership.
- Modify: `REFERENCES/software-development-crew.md`
- Modify: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`

- [ ] **Step 1: Review current deficiencies**

Run:

```bash
rg -n "competitive-research|product-discovery|customer-communications-specialist|customer-diagnostics-engineer|escalation-support-engineer|knowledge-base-author|market-researcher|product-discovery-strategist|support-automation-engineer|support-triage-specialist" docs/reviews/2026-05-24-skills-agents-quality-audit.md
```

- [ ] **Step 2: Upgrade skills first**

Strengthen:

- `competitive-research`: competitor selection, buyer criteria, source quality, pricing/currentness caveats, comparison axes, and recommendation limits.
- `product-discovery`: user problem framing, opportunity sizing, constraints, non-goals, acceptance criteria, success metrics, and decision gates.

Also review cross-family skills used by this family:

- `accessibility-audit`
- `design-system-audit`
- `docs-information-architecture`
- `ux-flow-mapping`

Do not edit those cross-family skills in this task unless Task 2 left a documented gap.

- [ ] **Step 3: Upgrade agents after skills**

Ensure:

- `product-discovery-strategist` references `$product-discovery` and hands off flow details to `ux-flow-architect`, visual systems to `design-system-engineer`, and implementation planning to `technical-planner`.
- `market-researcher` references `$competitive-research` and requires source dates, comparable selection rationale, and spend/time-risk caveats.
- `knowledge-base-author` references `$docs-information-architecture` when structuring KB content and hands off support triage gaps to `support-triage-specialist`.
- `customer-communications-specialist`, `customer-diagnostics-engineer`, `escalation-support-engineer`, `support-automation-engineer`, and `support-triage-specialist` include impact/urgency, reproducibility, customer-safe language, privacy boundaries, and engineering handoff evidence.

- [ ] **Step 4: Update registry and matrix**

Update registry handoffs and matrix rows for this family with all `after_scores` at least `3`.

- [ ] **Step 5: Validate and commit**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Commit:

```bash
git add SKILLS AGENTS/openai REFERENCES/software-development-crew.md docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv
git commit -m "docs: uplift product support and documentation assets"
```

## Task 7: Uplift Meta-Catalog Assets

**Files:**

- Modify: `SKILLS/codex-subagent-designer/SKILL.md`
- Modify: `SKILLS/codex-subagent-designer/references/*` if present.
- Modify: `REFERENCES/quality-rubric.md`
- Modify: `REFERENCES/subagent-toml.md`
- Modify: `REFERENCES/prompt-patterns.md`
- Modify: `docs/migration/current-layout.md`
- Modify: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`

- [ ] **Step 1: Re-review the generator failure mode**

Read:

```bash
sed -n '1,240p' SKILLS/codex-subagent-designer/SKILL.md
sed -n '1,280p' REFERENCES/quality-rubric.md
sed -n '1,220p' REFERENCES/subagent-toml.md
```

Confirm the designer skill requires:

- rubric review before asset creation;
- domain-specific guidance before structural validation;
- explicit `Ready` versus scaffold labeling;
- rejection of generic workflow platitudes;
- complete coverage when the user asks for complete coverage.

- [ ] **Step 2: Add required safeguards**

Add or verify these safeguards in the designer skill and references:

- Add an example of a failing shallow skill and a passing skill pattern.
- Add an example of a failing broad agent and a passing specialist agent pattern.
- Add a checklist requiring supporting references, validation guidance, output contracts, and handoff targets.
- Add a note that installing copied skills must preserve bundled references and agent examples.

- [ ] **Step 3: Update matrix**

Set `codex-subagent-designer` to `Ready` with after scores at least `3`, citing the exact safeguards in `validation_evidence`.

- [ ] **Step 4: Validate and commit**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Commit:

```bash
git add SKILLS/codex-subagent-designer REFERENCES docs/migration/current-layout.md docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv
git commit -m "docs: reinforce catalog design safeguards"
```

## Task 8: Central Scoring And Final Audit

**Files:**

- Modify: `docs/reviews/2026-05-24-skills-agents-quality-audit.md`
- Modify: `docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv`
- Modify: `scripts/catalog_quality/score_audit.py` only if the matrix schema changed during implementation.

- [ ] **Step 1: Verify matrix completeness**

Run:

```bash
python3 scripts/catalog_quality/score_audit.py
```

Expected:

```text
score audit passed: all assets Ready
```

If it fails, fix the listed matrix or asset defects before continuing.

- [ ] **Step 2: Run structural validation**

Run:

```bash
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Expected:

```text
catalog validation passed
```

- [ ] **Step 3: Update final audit**

Rewrite `docs/reviews/2026-05-24-skills-agents-quality-audit.md` so it includes:

- summary counts with `48` skills reviewed, `48` skills Ready, `91` agents reviewed, and `91` agents Ready;
- before/after counts from the original audit;
- final score table for every skill;
- final score table for every agent;
- validation evidence listing the exact commands run;
- residual risk statement.

The residual risk statement should be:

```text
Residual risk: no current catalog asset remains below Ready. Future additions still require rubric review before catalog inclusion.
```

- [ ] **Step 4: Validate final audit and commit**

Run:

```bash
python3 scripts/catalog_quality/score_audit.py
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
```

Commit:

```bash
git add docs/reviews scripts/catalog_quality
git commit -m "docs: finalize full catalog quality audit"
```

## Task 9: Install Verified Local Skill Copy

**Files:**

- Source: `SKILLS/codex-subagent-designer/`
- Destination: `/Users/thomasjones/.codex/skills/codex-subagent-designer/`

- [ ] **Step 1: Confirm repository validation passes**

Run:

```bash
python3 scripts/catalog_quality/score_audit.py
python3 scripts/catalog_quality/validate_catalog.py
git status --short
```

Expected:

```text
score audit passed: all assets Ready
catalog validation passed
```

`git status --short` should be clean or show only intentional install-note changes that will be committed before install.

- [ ] **Step 2: Install the validated designer skill**

Run with permission to write `/Users/thomasjones/.codex/skills/codex-subagent-designer/`:

```bash
rsync -a --delete --exclude .DS_Store SKILLS/codex-subagent-designer/ /Users/thomasjones/.codex/skills/codex-subagent-designer/
mkdir -p /Users/thomasjones/.codex/skills/codex-subagent-designer/references
rsync -a --delete --exclude .DS_Store REFERENCES/ /Users/thomasjones/.codex/skills/codex-subagent-designer/references/
mkdir -p /Users/thomasjones/.codex/skills/codex-subagent-designer/agents/examples/openai
rsync -a --delete --exclude .DS_Store AGENTS/openai/ /Users/thomasjones/.codex/skills/codex-subagent-designer/agents/examples/openai/
```

- [ ] **Step 3: Adjust installed links if needed**

Inspect:

```bash
rg -n "../../REFERENCES|AGENTS/openai|references/quality-rubric|agents/examples/openai" /Users/thomasjones/.codex/skills/codex-subagent-designer/SKILL.md
```

If repo-relative links remain in the installed copy, replace them in the installed copy only:

```bash
perl -pi -e 's#\\]\\(\\.\\./\\.\\./REFERENCES/#](references/#g; s#`AGENTS/openai/`#`agents/examples/openai/`#g' /Users/thomasjones/.codex/skills/codex-subagent-designer/SKILL.md
```

- [ ] **Step 4: Validate installed copy**

Run:

```bash
test -f /Users/thomasjones/.codex/skills/codex-subagent-designer/SKILL.md
test -f /Users/thomasjones/.codex/skills/codex-subagent-designer/references/quality-rubric.md
test -d /Users/thomasjones/.codex/skills/codex-subagent-designer/agents/examples/openai
find /Users/thomasjones/.codex/skills/codex-subagent-designer -name .DS_Store -print
```

Expected: the first three commands exit `0`; the final command prints nothing.

## Task 10: Final Review And Handoff

**Files:**

- Review all changed files from Tasks 1 through 9.

- [ ] **Step 1: Run all final checks**

Run:

```bash
python3 scripts/catalog_quality/score_audit.py
python3 scripts/catalog_quality/validate_catalog.py
git diff --check
git status --short
```

Expected:

```text
score audit passed: all assets Ready
catalog validation passed
```

- [ ] **Step 2: Inspect final history**

Run:

```bash
git log --oneline -10
```

Expected: recent commits show validation tooling, one or more family uplift commits, final audit, and any installed-copy synchronization note if represented in repo docs.

- [ ] **Step 3: Prepare review summary**

Final response should include:

- count of skills upgraded and final Ready count;
- count of agents upgraded and final Ready count;
- validation commands run;
- installed skill path if Task 9 was performed;
- any residual risk from the final audit.
