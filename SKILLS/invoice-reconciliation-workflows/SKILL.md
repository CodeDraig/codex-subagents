---
name: invoice-reconciliation-workflows
description: Use when reconciling invoices, purchase orders, receipts, approvals, payment status, and exception queues before payment authorization.
---

# Invoice Reconciliation Workflows

## Overview

Support invoice reconciliation by matching documents, totals, approvals, tax treatment, and exceptions. Do not authorize payments or modify accounting records without the owner.

## Workflow

1. Restate vendor, invoice set, period, systems, currency, matching policy, and approval threshold.
2. Match invoice, purchase order, receipt, contract, approval, tax, freight, coding, and payment records, then verify date, quantity, unit price, and total logic.
3. Identify quantity, price, tax, duplicate, missing approval, vendor master, payment-status, and policy-exception issues.
4. Separate ready-to-review items from unresolved owner decisions, and note whether each exception is informational, corrective, or blocking payment.
5. Produce a reconciliation log, exception queue, and next-action list for procurement, AP, or business-owner follow-up.

Use `references/invoice-reconciliation-checklist.md` for matching checks.

## Output Contract

Return exactly: `Reconciliation Scope`, `Matched Items`, `Exceptions`, `Duplicate Risks`, `Approval Gaps`, `Payment Status`, `Next Actions`.

## Stop Conditions

Stop when asked to approve payment, change vendor records, alter invoices, bypass procurement or finance policy, or provide tax/legal advice.
