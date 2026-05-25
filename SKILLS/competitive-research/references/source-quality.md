# Source Quality

## Quality Tiers

| Tier | Use for | Examples | Caveat |
| --- | --- | --- | --- |
| A | Decision-grade factual claims | Official docs, pricing pages, standards, release notes, status pages, contracts, public filings, reproducible trials | Still record date checked and product/version scope |
| B | Context and triangulation | Independent benchmarks, dated analyst reports, customer case studies, conference talks, maintained comparison repos | Check incentives, methodology, and freshness |
| C | Leads only | Blog posts, forums, social posts, sales decks, undated reviews, AI summaries with citations | Do not rely on alone for product, spend, security, or compliance decisions |

## Prefer

- Official documentation, standards, pricing pages, status pages, release notes.
- First-party demos or screenshots.
- Primary research artifacts: interviews, survey data, analytics, tickets.
- Reproducible experiments run locally.

## Treat Carefully

- Blog posts without dates.
- Vendor comparisons that favor the vendor.
- Social posts, forum comments, and old benchmarks.
- AI summaries without linked evidence.

## Currentness Rules

- Verify current pricing, package limits, licensing, supported regions, compliance claims, security features, and roadmap-dependent features on the day of use.
- Treat docs, screenshots, and benchmarks older than 12 months as stale unless the source explicitly says the behavior is unchanged.
- Record the source owner and incentive: vendor, competitor, independent reviewer, standards body, customer, or internal artifact.
- Separate observable product behavior from marketing claims and buyer sentiment.

## Comparable Set Rules

- Include products because they share the same user job, integration surface, budget category, deployment model, or compliance constraint.
- Exclude products explicitly when they solve a different job, require a different buyer, have incompatible deployment/security posture, or exceed the decision's cost/risk envelope.
- For procurement-facing work, separate capability score, commercial terms, contract risk, implementation burden, vendor risk, and exit cost.
- When a claim would affect a large spend, regulated workflow, security posture, or migration, require at least one Tier A source and one independent validation path.

## Local Validation Examples

- Run a small API spike to verify an integration surface instead of trusting a feature matrix.
- Capture screenshots or exported artifacts when UX behavior is the differentiator.
- Check SDK/package versions, changelogs, and issue trackers when ecosystem maturity matters.
- Compare trial behavior against acceptance criteria before recommending migration.

## Finding Format

- Claim:
- Source:
- Date checked:
- Source tier:
- Source owner/incentive:
- Confidence:
- Decision implication:
- Local validation needed:
