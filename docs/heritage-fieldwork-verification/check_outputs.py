"""Check retained synthetic outputs and their evidence hashes without model calls.

These assertions cover record preservation, arithmetic, and provenance. The
three prose-only review scenarios still require the recorded manual assessment.
"""
import argparse
import csv
import hashlib
import json
import re
from decimal import Decimal
from pathlib import Path


EVIDENCE = Path(__file__).resolve().parent
ROOT = EVIDENCE.parents[1]


def read_json(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table(case, filename, key, delimiter=','):
    with (EVIDENCE/'cases'/case/'outputs'/filename).open(newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter=delimiter))
    assert rows and all(None not in row and None not in row.values() for row in rows)
    indexed = {row[key]: row for row in rows}
    assert len(indexed) == len(rows), (case, filename, 'duplicate key')
    return indexed


def check_evidence():
    results = read_json(EVIDENCE/'live-results.json')['cases']
    fixtures = read_json(EVIDENCE/'fixtures.json')
    assert len(results) == len(fixtures) == 8
    assert {case['case'] for case in results} == set(fixtures)
    for case in results:
        folder = EVIDENCE/'cases'/case['case']
        run = read_json(folder/'run.json')
        assert case['result'] == 'accepted' and run['exit'] == 0
        assert run['inputs_unchanged']
        assert run['input_hashes_before'] == run['input_hashes_after']
        for path, source in fixtures[case['case']]['files'].items():
            assert (folder/path).read_text() == source
            assert digest(folder/path) == run['input_hashes_before'][path]
        assert run['output_hashes'] == case['output_hashes']
        actual_outputs = {
            str(path.relative_to(folder)): digest(path)
            for path in (folder/'outputs').rglob('*') if path.is_file()
        }
        assert actual_outputs == run['output_hashes'], case['case']
        for path, sha in case['relevant_final_sources'].items():
            assert digest(ROOT/path) == sha == run['source_hashes'][path], path
        assert digest(folder/'response.md') == run['response_sha256'] == case['response_sha256']
        if run['sandbox'] == 'read-only':
            assert not actual_outputs, case['case']
    review = read_json(EVIDENCE/'asset-review.json')
    assert len(review['source_hashes']) == 71
    for path, sha in review['source_hashes'].items():
        assert digest(ROOT/path) == sha, path


def check_archaeology():
    records = table('archaeology_records', 'contexts.csv', 'context_id')
    assert set(records) == {'C101', 'C102', 'C103'}
    expected = [
        ('C101', 'brown sandy layer', 'C102', 'N1:1'),
        ('C102', 'grey silty fill', 'C103', 'N1:2'),
        ('C103', 'pale clay', '', 'N1:3'),
    ]
    for key, description, related, anchor in expected:
        row = records[key]
        assert row['observed_description'] == description
        assert row['related_context_id'] == related
        assert anchor in row['source_anchor']
        assert all(not row[field] for field in ('easting', 'northing', 'elevation', 'coordinate_reference'))
    assert records['C102']['inferred_interpretation'] == "possible pit fill, recorder's proposal"
    items = table('archaeology_records', 'find-links.csv', 'item_id')
    assert set(items) == {'F01', 'F02', 'S01'}
    for key, kind, context, quantity, anchor in [
        ('F01', 'find', 'C102', '3', 'F1:1'),
        ('F02', 'find', 'C103', '1', 'F1:2'),
        ('S01', 'sample', 'C102', '', 'S1:1'),
    ]:
        row = items[key]
        assert (row['item_type'], row['context_id'], row['quantity_value']) == (kind, context, quantity)
        assert context in records and anchor in row['source_anchor']


def check_language():
    segments = table('language_annotation', 'segments.tsv', 'segment_id', '\t')
    assert set(segments) == {'U1', 'U2', 'U3'}
    for key, start, end, form in [
        ('U1', '1.0', '2.5', 'na ki tu'),
        ('U2', '3.0', '4.2', 'na lo tu'),
        ('U3', '5.0', '6.4', 'tu ki na'),
    ]:
        row = segments[key]
        assert (row['start_s'], row['end_s'], row['source_form']) == (start, end, form)
    assert segments['U1']['translation'] == 'I see a bird'
    assert segments['U3']['translation'] == 'A bird sees me'
    assert 'UNRESOLVED' in segments['U2']['gloss']
    assert 'unresolved' in segments['U2']['translation']
    entries = table('language_lexicon', 'lexicon.tsv', 'entry_id', '\t')
    assert set(entries) == {'E1', 'E2', 'E3', 'E4'}
    for key, form, meaning, variety, utterance in [
        ('E1', 'tal', 'stone', 'V1', 'U10'),
        ('E2', 'tal', 'count', 'V1', 'U11'),
        ('E3', 'tál', 'mountain', 'V2', 'U12'),
        ('E4', 'talan', 'not supplied', 'V1', 'U99'),
    ]:
        row = entries[key]
        assert row['original_entry_id'] == key
        assert (row['original_form'], row['supplied_meaning'], row['variety'], row['utterance_id']) == (form, meaning, variety, utterance)
        assert row['analytical_segmentation'] == 'not supplied'
    assert 'research-only' in entries['E3']['derivative_access_assessment']
    assert entries['E4']['attestation_status'].startswith('unattested in C1')


def check_transcript():
    folder = EVIDENCE/'cases/oral_transcript'
    source = (folder/'inputs/packet.md').read_text()
    edited = (folder/'outputs/transcript.md').read_text()
    original_turns = re.findall(r'^L(\d+) \[([^]]+)\] (Interviewer|Narrator): (.+)$', source, re.M)
    edited_turns = re.findall(r'^\[L(\d+) \| ([^]]+)\] \*\*(Interviewer|Narrator):\*\* (.+)$', edited, re.M)
    assert len(original_turns) == len(edited_turns) == 8
    expected = [(key, time, speaker, words.removeprefix('Um, ') if key == '2' else words)
                for key, time, speaker, words in original_turns]
    assert edited_turns == expected
    assert 'Later correction annotation — RN2, referring to L2' in edited
    assert 'I now think it was July.' in edited
    assert all('July' not in words for _, _, _, words in edited_turns)


def check_monitoring():
    rows = table('conservation_monitoring', 'monitoring.csv', 'observation_id')
    assert set(rows) == {f'M{i}' for i in range(1, 8)}
    for baseline, followup, difference, label in [('M1', 'M2', '4', 'percentage points'), ('M4', 'M5', '0.2', 'mm')]:
        old, new = rows[baseline], rows[followup]
        assert Decimal(new['observed_value']) - Decimal(old['observed_value']) == Decimal(difference)
        assert new['calculated_change'] == f'+{difference} {label}'
        assert new['baseline_reference'] == baseline
        assert new['comparison_status'] == 'comparable'
        assert new['trigger_status'] == 'crossed; review required'
    assert rows['M1']['trigger_status'] == 'not crossed'
    assert rows['M4']['trigger_status'] == 'not assessable'
    assert not rows['M1']['calculated_change'] and not rows['M4']['calculated_change']
    assert rows['M3']['observed_value'] == 'missing' and not rows['M3']['calculated_change']
    assert rows['M3']['trigger_status'] == 'not assessable'
    assert 'No dated scheduling evidence supplied' in rows['M3']['limits_of_inference']
    assert rows['M7']['comparison_status'] == 'not comparable' and not rows['M7']['calculated_change']
    tasks = table('conservation_monitoring', 'maintenance.csv', 'task_id')
    assert set(tasks) == {'T1', 'T2'}
    assert tasks['T1']['status'].startswith('unverified completion') and not tasks['T1']['completion_date']
    assert 'not confirmed non-performance' in tasks['T1']['limits_of_inference']
    assert tasks['T2']['status'] == 'completed' and tasks['T2']['completion_date'] == '2026-09-03'
    assert 'CN2' in tasks['T2']['completion_evidence']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    check_evidence()
    check_archaeology()
    check_language()
    check_transcript()
    check_monitoring()
    report = dict(result='passed', accepted_case_provenance_checks=8,
                  reviewed_asset_hashes=71, structured_output_scenarios=5,
                  prose_review_judgments='manual; see live-results.json')
    if args.report:
        args.report.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
