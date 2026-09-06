# Curation Context

Input inspected: `inputs/packet.md`, a synthetic verification packet. Requested deliverables: a TSV lexicon and a curation/source-link report. The corpus is `C1`; its version is not supplied. Source utterances are `U10`, `U11`, `U12`, and the supplied but unresolved reference `U99`. No participant metadata is supplied. Variety labels are `V1` (E1, E2, E4) and `V2` (E3). No segmentation or inflectional analysis is supplied.

Original record IDs, forms, and supplied meanings are retained in `lexicon.tsv`. `search_key` is intentionally an exact copy of each recorded form because no normalization convention is supplied. It is not an instruction to remove diacritics. The recorded diacritic in `tál` is retained.

# Lexicon Or Corpus Index

| Entry / sense | Recorded form | Supplied meaning | Variety | Corpus result |
| --- | --- | --- | --- | --- |
| E1 / E1-S1 | tal | stone | V1 | Attested: C1 U10, C1:10 |
| E2 / E2-S1 | tal | count | V1 | Attested: C1 U11, C1:11 |
| E3 / E3-S1 | tál | mountain | V2 | Attested: C1 U12, C1:12 |
| E4 / E4-S1 | talan | not supplied | V1 | Unattested in C1; supplied U99 reference does not resolve in C1 |

`E1-S1` through `E4-S1` are curator-assigned working sense IDs, each mapped to its original entry ID. They do not assert a complete sense inventory or a linguistic analysis.

# Attestation Links

| Lexicon record | Supplied corpus relationship | Checked result | Access evidence |
| --- | --- | --- | --- |
| E1 / E1-S1 | C1 U10, C1:10, `tal` ‘stone’ | Resolved and meaning agrees with the supplied attestation | P1 permits a public example; entry-level release scope is not separately supplied |
| E2 / E2-S1 | C1 U11, C1:11, `tal` ‘count’ | Resolved and meaning agrees with the supplied attestation | P1 permits a public example; entry-level release scope is not separately supplied |
| E3 / E3-S1 | C1 U12, C1:12, `tál` ‘mountain’ | Resolved and meaning agrees with the supplied attestation | A12 identifies U12 and derivatives as research-only |
| E4 / E4-S1 | C1 U99 | Unmatched: the packet states C1 contains no U99 | No access terms supplied |

No corpus version identifier beyond `C1` is available, so the links resolve only to the corpus and anchors stated in the packet.

# Merge And Variant Decisions

No entries were merged, deleted, or re-keyed. The reversible change map is identity-only: E1 → E1/E1-S1, E2 → E2/E2-S1, E3 → E3/E3-S1, E4 → E4/E4-S1.

- E1 and E2 remain separate: identical spelling (`tal`) does not establish one lexical item, and their supplied meanings and distinct C1 utterances differ. Their homography/lexical relationship is unresolved.
- E3 remains separate from the V1 entries: `tál` retains its recorded diacritic, is attested in V2, and no cross-variety equivalence or variant relationship is supplied.
- E4 remains an incomplete source record. Its unattested status in C1 does not establish that `talan` is impossible or absent from the language.

The proposed X1 public export is not accepted as a blanket release decision. E3 cannot be public while A12 remains controlling; no supplied supersession resolves A12 against X1. E4 lacks access terms and a resolved source link. P1 supports public examples for E1 and E2, but the packet does not separately define entry-level release scope.

# Unresolved Analyses

- Whether E1 and E2 are homographs, distinct lexical entries, or related senses is not supplied.
- Whether V1 and V2 forms are equivalent, comparable, or variant-related is not supplied.
- No analytical segmentation, inflectional analysis, grammatical category, or paradigm is supplied for any entry.
- E4 has no supplied meaning, no resolved attestation, and no access terms.
- Community spelling preferences and a normalized-search convention are not supplied.

# Checks And Limits

Performed: compared every supplied record against the C1 statements in the packet; checked that E1–E4 and E1-S1–E4-S1 are unique; resolved U10–U12 and identified U99 as unmatched; compared the three supplied meanings against the stated attestations; preserved all original entry IDs and forms; reviewed A12, P1, and X1 for the stated export decision.

The TSV has one header and four data rows. Its fields retain original forms, separate search keys, segmentation status, evidence status, source references, variety, access evidence, and reversible change notes. This structural check does not establish linguistic correctness beyond the supplied packet. No audio, transcript, corpus file, agreement text, export sheet, source-version metadata, participant metadata, or release authorization beyond the packet was available for inspection.

# Owner Questions

1. Does an authorized decision supersede A12 for E3/U12 or should X1 be corrected to exclude it and its derivatives from public export?
2. What source should replace or clarify E4’s U99 reference, and what are E4’s meaning and access terms?
3. What relationship, if any, should be recorded between E1 and E2, and are there approved normalization and community-spelling conventions for search keys?
4. Does P1 authorize publication of only examples, or the complete E1/E2 lexical entries and their associated metadata?

# Files Changed

- `outputs/lexicon.tsv` — created a four-record source-linked working lexicon.
- `outputs/curation-decisions.md` — created this curation, source-link, access, and unresolved-analysis report.

# Handoffs

- `linguistic-annotation-editor`: resolve or correct the U99 source-tier reference and provide a verifiable C1 version/source representation if available.
- `linguistic-session-designer`: prepare review/elicitation questions for E4’s meaning and any E1/E2 relationship or V1/V2 comparison, if further work is authorized.
- `language-deposit-coordinator`: resolve A12 versus X1 and define release scope for P1 before any public export or deposit metadata is issued.
