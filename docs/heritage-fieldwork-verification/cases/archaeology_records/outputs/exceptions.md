# Derived desk-record exceptions — AR1 / T1

## Scope and source inventory

Derived from `inputs/packet.md` only; source register version: **1** (line 5). These outputs are transcriptions and normalized links, not field inspection records. The source packet remains unmodified.

| Supplied record or reference | Source anchor | Coverage in derived outputs | Status |
| --- | --- | --- | --- |
| Context observation N1:1 / C101 | `inputs/packet.md:9` | `contexts.csv` row AR1/T1/C101 | transcribed |
| Context observation N1:2 / C102 | `inputs/packet.md:10` | `contexts.csv` row AR1/T1/C102 | transcribed |
| Context observation N1:3 / C103 | `inputs/packet.md:11` | `contexts.csv` row AR1/T1/C103 | transcribed |
| Find F1:1 / F01 | `inputs/packet.md:17` | `find-links.csv` row AR1/T1/F01 | transcribed |
| Find F1:2 / F02 | `inputs/packet.md:18` | `find-links.csv` row AR1/T1/F02 | transcribed |
| Sample S1:1 / S01 | `inputs/packet.md:20` | `find-links.csv` row AR1/T1/S01 | transcribed |
| Plan references P1, P2 | `inputs/packet.md:9-11,20` | retained in `contexts.csv` | references only; no plan attached |
| Photograph references PH1, PH2, PH3 | `inputs/packet.md:9-11,20` | retained in `contexts.csv` | references only; no image attached |

## Exceptions and follow-up checks

| ID | Affected record(s) | Issue | Treatment in derived record | Follow-up needed |
| --- | --- | --- | --- | --- |
| EX-01 | C101, C102, C103 | No context coordinates, coordinate reference, units, or precision are supplied. T1 is explicitly not a measured location. | Spatial fields are blank; no location was derived. | Obtain measured context locations and spatial-reference metadata, with coordinate access terms before any coordinate export. |
| EX-02 | P1, P2 | No plan files or plan index are attached. | IDs retained as source references only; plan content and placement not verified. | Supply plans/index and confirm each context-to-plan reference. |
| EX-03 | PH1, PH2, PH3 | No photograph files or photo index are attached. | IDs retained as source references only; image content not inspected or verified. | Supply images/index and verify depicted context, view, and any scale/location information. |
| EX-04 | C103 | The source says “no temporal relation recorded.” | No relationship term or target was entered. | Check the original record or a stratigraphic review only if a relationship is later proposed. |
| EX-05 | C102 | “possible pit fill, recorder's proposal” is an interpretation, not an observed cut/fill/contact description. | Stored only in `inferred_interpretation`, with its source status. | Confirm against the field sheet, section/plan, or later specialist review before using as function or chronology. |
| EX-06 | F01, F02 | Both identifications are explicitly provisional. | Verbatim descriptions and quantities retained; no identification normalized. | Send to archaeological-finds-coordinator if identification, quantity, container, or context reconciliation is required. |
| EX-07 | S01 | No analysis or dating report is supplied. | No analytical result or date entered. | Link any future sample-analysis/dating report by source anchor. |
| EX-08 | All records | Observer names, field dates, record owner, and coordinate access terms are not supplied. | Values marked not supplied or left blank where no value exists. | Owner to provide record custody/ownership and any access restrictions. |

## Normalization notes

- `above` is the only transcribed temporal relationship term; it is retained verbatim as the normalized term for C101 → C102 and C102 → C103.
- Context, find, sample, container, plan, and photo identifiers are preserved exactly as supplied. No new identifiers, merges, or collision resolutions were proposed because no collision is present within the packet.
- Quantity values were split from the supplied expressions `3 fragments` and `1 fragment`; the original expression remains in `quantity_verbatim`.
