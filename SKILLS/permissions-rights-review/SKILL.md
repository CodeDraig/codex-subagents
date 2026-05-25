---
name: permissions-rights-review
description: Use when tracking third-party content permissions, rights status, attribution, license scope, reuse limits, and clearance questions; not for final legal clearance or definitive fair-use opinions.
---

# Permissions Rights Review

## Overview

Organize permissions and rights evidence for third-party content. Do not provide legal clearance opinions or final rights approval.

## Workflow

1. Restate work, content item, source, intended use, territory, format, edition, platform, and schedule.
2. Inventory ownership, rights holder, license, permission request, attribution, restrictions, fees, exclusivity, term, and evidence path.
3. Match the requested use to license scope and publication requirements, including transformations, excerpts, translation, marketing, cover use, and digital distribution.
4. Flag missing permissions, unclear ownership, incompatible license terms, fair-use review boundaries, and legal-review needs.
5. Produce a rights tracker, blocker list, and owner questions.

Use `references/permissions-rights-checklist.md` for clearance tracking.

## Decision Rules

- Require a specific rights holder and evidence path before treating any permission as usable.
- A license must cover the actual medium, territory, term, edition, and distribution channel; partial coverage is a blocker until resolved.
- Transformations, excerpt length, marketing use, cover use, localization, and derivative formats each need explicit coverage or a separate permission.
- Fair-use analysis is a review boundary only; if final legal clearance is needed, escalate rather than guessing.

## Output Contract

Return exactly: `Rights Scope`, `Content Inventory`, `Permission Status`, `License Restrictions`, `Attribution Needs`, `Risks`, `Owner Questions`.
Include the evidence path and the exact reuse boundaries that were checked.

## Stop Conditions

Stop when asked to provide legal clearance, ignore license limits, remove attribution, use content without permission, or fabricate rights evidence.
