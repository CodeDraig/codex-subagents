---
name: docs-information-architecture
description: Use when organizing documentation sets, choosing doc types, improving navigation, separating concept/task/reference/tutorial content, reducing stale docs, designing docs for audiences, or planning developer/user/operator documentation.
---

# Docs Information Architecture

## Overview

Structure docs around audience tasks and maintenance cost. Good docs make the next action obvious and keep volatile details easy to update.

## Workflow

1. Identify audiences: new user, power user, developer, operator, reviewer, support, or maintainer.
2. Classify docs: concept, task, reference, tutorial, troubleshooting, runbook, changelog.
3. Map navigation and ownership.
4. Remove duplication and stale paths.
5. Define freshness policy and verification points.

Use `references/docs-map.md` for larger sets.

## Output Contract

Return exactly: `Audience`, `Current Structure`, `Problems`, `Recommended Structure`, `Content Types`, `Freshness Policy`, `Migration Steps`, `Open Questions`.

## Stop Conditions

Stop when docs depend on behavior, commands, or policies that cannot be verified from the provided code or sources.
