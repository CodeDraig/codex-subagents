## Review Scope

Reviewed the complete bounded evidence supplied in [packet.md](/tmp/heritage-fieldwork-20260906/live/archaeology_sequence/attempt-2/project/inputs/packet.md:5):

- Inventory `INV1`: five contexts, `C201–C205`.
- Relationship table `R1`: five asserted later-than relations.
- Dating note `D1`: one potentially residual sherd from `C203`.
- No equivalence decisions, proposed phases, original context sheets, or wider site matrix were supplied.

Source files were left unchanged.

## Relationship Model

Graph direction is **later context → earlier context**. Chronological sequences below are written **earliest < latest**.

| Source | Supplied edge | Temporal meaning |
|---|---|---|
| `R1:1` | `C201 → C202` | `C202 < C201` |
| `R1:2` | `C202 → C203` | `C203 < C202` |
| `R1:3` | `C203 → C201` | `C201 < C203` |
| `R1:4` | `C204 → C205` | `C205 < C204` |
| `R1:5` | `C205 → C999` | `C999 < C205`, conditional on resolving `C999` |

All five relations are presented as temporal assertions. No merely spatial contacts or interpretive associations were supplied. No contexts were collapsed: similar attributes are not reported, and the packet explicitly states that no equivalence decisions exist.

## Sequence Findings

- **Blocking cycle:** `R1:1`, `R1:2`, and `R1:3` form:

  `C201 → C202 → C203 → C201`

  This simultaneously asserts `C202 < C201 < C203 < C202`. No consistent temporal ordering exists for `C201`, `C202`, and `C203` while all three observations remain established.

- I manually inspected each conflicting source row at [R1:1–R1:3](/tmp/heritage-fieldwork-20260906/live/archaeology_sequence/attempt-2/project/inputs/packet.md:9). Nothing in the packet supports selecting one edge for deletion.

- **Missing reference:** `R1:5` names `C999`, which is absent from `INV1`. The relationship remains a supplied observation but cannot be validated against the supplied context inventory.

- **Usable relation:** `R1:4` supports `C205 < C204`.

- There is no path connecting the `C201–C203` component to the `C204–C205` component. Their relative order is unresolved, not contemporary.

- No phases or equivalences can be supported from this evidence.

## Supported Order And Alternatives

Supported inventory-only partial order:

`C205 < C204`

Conditional extension if `C999` is confirmed as a valid context and `R1:5` is confirmed:

`C999 < C205 < C204`

The cyclic component has no supported total order. If later source review establishes that exactly one cycle edge is erroneous, the corresponding hypothetical alternatives would be:

- If `R1:1` is rejected: `C201 < C203 < C202`
- If `R1:2` is rejected: `C202 < C201 < C203`
- If `R1:3` is rejected: `C203 < C202 < C201`

These are repair scenarios, not recommended corrections; the supplied evidence does not distinguish among them.

## Dating Limits

[D1](/tmp/heritage-fieldwork-20260906/live/archaeology_sequence/attempt-2/project/inputs/packet.md:15) records:

- Supplied context: `C203`
- Object: sherd
- Provisional object date: `1200–1300`
- Interpretation: possibly residual

The date applies provisionally to the object, not to deposition of `C203`. No depositional date, terminus, phase date, or absolute chronology was assigned. The cycle also prevents propagation of any future date through `C201–C203` until the contradiction is resolved.

## Checks And Limits

Checks actually performed:

- Parsed the Markdown relationship table into a read-only directed graph.
- Confirmed the declared counts: five inventory nodes and five relationship rows.
- Found six distinct referenced graph nodes: the five inventory contexts plus `C999`.
- Found one missing inventory reference: `C999`.
- Confirmed every inventory context appears in at least one relationship.
- Found zero self-links, duplicate directed edges, or direct reciprocal pairs.
- Cycle/SCC check found one cyclic component: `{C201, C202, C203}`.
- Topological check over all six named nodes failed because of that cycle. It processed only `C204, C205, C999` in later→earlier edge order before stalling: 3 of 6 nodes.
- Manually checked all three reported cycle edges against their source rows.

Only the synthetic packet was inspected. Original sheets, field observations, context descriptions, and a full-site matrix were unavailable, so this is a partial-matrix review rather than a full-site sequence.

## Owner Questions

1. Is `C999` a valid context omitted from `INV1`, a transcription error, or an external reference?
2. Can the original records underlying `R1:1–R1:3` be checked to determine whether any relationship direction or context identifier was entered incorrectly?
3. Is the `D1` sherd securely linked to `C203`, and what evidence supports the residual interpretation?
4. Are there additional relationships, equivalence proposals, or phase proposals outside this packet?

## Handoffs

- **`archaeological-recording-specialist`:** reconcile `C999` with `INV1` and inspect the original records for `R1:1–R1:3`. Preserve all current observations while recording any correction separately.
- **`archaeological-finds-coordinator`:** verify the sherd-to-`C203` association and clarify the basis and confidence of the residual interpretation and provisional object date.
- **`archaeological-report-author`:** receive the supported partial chain and any synthesis only after the missing reference and cycle have been resolved or explicitly retained as unresolved.