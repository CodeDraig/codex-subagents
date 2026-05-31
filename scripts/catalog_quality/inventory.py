#!/usr/bin/env python3
"""Generate the full catalog uplift inventory matrix."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv"

FAMILIES = {
    "software-engineering-core": {
        "skills": {
            "accessibility-audit",
            "ai-evals",
            "api-contract-review",
            "architecture-decision-records",
            "data-modeling",
            "dependency-risk-triage",
            "design-system-audit",
            "docs-information-architecture",
            "engineering-execution",
            "implementation-planning",
            "incident-postmortems",
            "localization-readiness",
            "observability-runbooks",
            "performance-profiling",
            "privacy-review",
            "prompt-injection-defense",
            "release-readiness",
            "test-matrix-design",
            "threat-modeling",
            "ux-flow-mapping",
        },
        "agents": {
            "accessibility-reviewer",
            "ai-feature-engineer",
            "api-contract-architect",
            "backend-domain-engineer",
            "build-release-engineer",
            "code-reviewer",
            "data-platform-engineer",
            "database-modeler",
            "dependency-maintenance-engineer",
            "design-system-engineer",
            "developer-experience-engineer",
            "devops-platform-engineer",
            "documentation-engineer",
            "frontend-experience-engineer",
            "implementation-finisher",
            "localization-engineer",
            "observability-incident-engineer",
            "performance-investigator",
            "performance-optimizer",
            "privacy-compliance-reviewer",
            "prompt-evaluation-engineer",
            "rapid-prototype-scout",
            "refactor-surgeon",
            "security-fix-engineer",
            "security-threat-modeler",
            "software-engineering-lead",
            "systems-architect",
            "technical-planner",
            "test-automation-engineer",
            "test-strategy-architect",
            "triage-router",
            "ux-flow-architect",
        },
    },
    "data-analytics-ml": {
        "skills": {
            "analytics-engineering",
            "data-science-workflows",
            "ml-engineering",
            "mlops-readiness",
        },
        "agents": {
            "analytics-engineer",
            "data-scientist",
            "ml-engineer",
            "mlops-engineer",
            "research-data-curator",
        },
    },
    "research-news-publishing-editorial": {
        "skills": {
            "academic-literature-review",
            "book-metadata-packaging",
            "citation-integrity-review",
            "fact-checking-source-review",
            "fiction-development-workflows",
            "journal-submission-workflows",
            "line-copyediting-workflows",
            "nonfiction-manuscript-development",
            "permissions-rights-review",
            "publishing-production-workflows",
            "research-methods-review",
        },
        "agents": {
            "assignment-editor",
            "audience-seo-editor",
            "book-metadata-packaging-editor",
            "breaking-news-reporter",
            "citation-integrity-checker",
            "copy-desk-editor",
            "developmental-manuscript-editor",
            "fact-checking-editor",
            "fiction-development-editor",
            "geolocation-chronolocation-analyst",
            "indexing-coordinator",
            "journal-submission-specialist",
            "line-copy-editor",
            "literature-reviewer",
            "misinformation-risk-analyst",
            "news-fact-checker",
            "nonfiction-manuscript-editor",
            "osint-research-lead",
            "peer-review-prep-editor",
            "permissions-reviewer",
            "production-editor",
            "public-records-researcher",
            "social-network-analyst",
            "source-verification-analyst",
            "research-methods-reviewer",
            "standards-ethics-editor",
        },
    },
    "legal-policy-procurement-finance-grants": {
        "skills": {
            "audit-evidence-management",
            "contract-review-operations",
            "finance-operations-review",
            "grant-budget-justification",
            "grant-proposal-compliance",
            "invoice-reconciliation-workflows",
            "legal-research-workflows",
            "legislative-tracking",
            "policy-analysis-workflows",
            "procurement-vendor-review",
            "public-comment-drafting",
            "records-retention-operations",
            "rfp-response-workflows",
            "sow-review-workflows",
            "sponsored-projects-reporting",
        },
        "agents": {
            "accounting-controls-reviewer",
            "audit-evidence-organizer",
            "budget-justification-writer",
            "budget-variance-analyst",
            "contract-review-specialist",
            "financial-model-reviewer",
            "grant-opportunity-scout",
            "grant-reporting-specialist",
            "impact-assessment-writer",
            "invoice-reconciliation-specialist",
            "legal-ops-coordinator",
            "legal-research-analyst",
            "legislative-tracker",
            "policy-analyst",
            "procurement-compliance-specialist",
            "proposal-compliance-reviewer",
            "public-comment-drafter",
            "records-retention-advisor",
            "regulatory-monitor",
            "rfp-response-analyst",
            "sow-reviewer",
            "sponsored-projects-coordinator",
            "stakeholder-map-analyst",
            "vendor-risk-reviewer",
            "vendor-scorecard-analyst",
        },
    },
    "product-ux-design-support-docs": {
        "skills": {
            "competitive-research",
            "product-discovery",
        },
        "agents": {
            "customer-communications-specialist",
            "customer-diagnostics-engineer",
            "escalation-support-engineer",
            "knowledge-base-author",
            "market-researcher",
            "product-discovery-strategist",
            "support-automation-engineer",
            "support-triage-specialist",
        },
    },
    "meta-catalog": {
        "skills": {
            "codex-subagent-designer",
        },
        "agents": set(),
    },
}

FIELDNAMES = [
    "kind",
    "family",
    "name",
    "path",
    "before_rating",
    "before_scores",
    "required_fixes",
    "planned_changes",
    "after_rating",
    "after_scores",
    "validation_evidence",
]
REVIEW_FIELDNAMES = [
    field
    for field in FIELDNAMES
    if field not in {"kind", "family", "name", "path"}
]


def family_for(kind: str, name: str) -> str:
    matches = [
        family
        for family, assets in FAMILIES.items()
        if name in assets[f"{kind}s"]
    ]
    if len(matches) != 1:
        raise ValueError(f"{kind} {name!r} maps to {len(matches)} families")
    return matches[0]


def asset_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for path in sorted((ROOT / "SKILLS").glob("*/SKILL.md")):
        name = path.parent.name
        family = family_for("skill", name)
        rows.append(make_row("skill", family, name, path))
        seen.add(("skill", name))
    for path in sorted((ROOT / "AGENTS/openai").glob("*.toml")):
        name = path.stem
        family = family_for("agent", name)
        rows.append(make_row("agent", family, name, path))
        seen.add(("agent", name))

    expected = {
        (kind[:-1], name)
        for assets in FAMILIES.values()
        for kind in ("skills", "agents")
        for name in assets[kind]
    }
    missing = sorted(expected - seen)
    extra = sorted(seen - expected)
    if missing or extra:
        raise ValueError(f"inventory mapping mismatch missing={missing} extra={extra}")
    return rows


def make_row(kind: str, family: str, name: str, path: Path) -> dict[str, str]:
    rel_path = path.relative_to(ROOT).as_posix()
    return {
        "kind": kind,
        "family": family,
        "name": name,
        "path": rel_path,
        "before_rating": "",
        "before_scores": "",
        "required_fixes": "",
        "planned_changes": "",
        "after_rating": "",
        "after_scores": "",
        "validation_evidence": "",
    }


def load_existing_rows() -> dict[tuple[str, str], dict[str, str]]:
    if not OUTPUT.exists():
        return {}

    rows: dict[tuple[str, str], dict[str, str]] = {}
    with OUTPUT.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            key = (row.get("kind", ""), row.get("name", ""))
            if not all(key):
                raise ValueError(f"{OUTPUT.relative_to(ROOT).as_posix()}: row missing kind or name")
            if key in rows:
                raise ValueError(f"{OUTPUT.relative_to(ROOT).as_posix()}: duplicate row key {key!r}")
            rows[key] = row
    return rows


def merge_existing_review_data(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    existing_rows = load_existing_rows()
    merged_rows: list[dict[str, str]] = []
    for row in rows:
        existing = existing_rows.get((row["kind"], row["name"]))
        if existing:
            for field in REVIEW_FIELDNAMES:
                row[field] = existing.get(field, "")
        merged_rows.append(row)
    return merged_rows


def main() -> int:
    rows = merge_existing_review_data(asset_rows())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    rel_output = OUTPUT.relative_to(ROOT).as_posix()
    print(f"wrote {rel_output} rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
