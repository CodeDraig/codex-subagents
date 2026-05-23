---
name: invoice-reconciliation-workflows
description: Use when reconciling invoices, purchase orders, receipts, approvals, payment status, and exception queues.
---

# Invoice Reconciliation Workflows

## Overview

Support invoice reconciliation by matching documents, totals, approvals, and exceptions. Do not authorize payments or modify accounting records without the owner.

## Workflow

1. Restate vendor, invoice set, period, systems, currency, and matching policy.
2. Match invoice, purchase order, receipt, contract, approval, tax, freight, and payment records.
3. Identify quantity, price, tax, duplicate, missing approval, and vendor master exceptions.
4. Separate ready-to-review items from unresolved owner decisions.
5. Produce a reconciliation log and next-action queue.

Use `references/invoice-reconciliation-checklist.md` for matching checks.

## Output Contract

Return exactly: `Reconciliation Scope`, `Matched Items`, `Exceptions`, `Duplicate Risks`, `Approval Gaps`, `Payment Status`, `Next Actions`.

## Stop Conditions

Stop when asked to approve payment, change vendor records, alter invoices, bypass procurement or finance policy, or provide tax/legal advice.
