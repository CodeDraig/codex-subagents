"""Isolated acceptance tests; no installed Codex files or model calls."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'tools/plan_install.py'
spec = importlib.util.spec_from_file_location('planner', SCRIPT)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'source'
        self.root.mkdir()
        self.dest = self.base / 'destination'
        self.git('init', '-q')
        self.write('AGENTS/openai/author.toml', '''name = "author"
description = "An author"
model = "example"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
nickname_candidates = ["Author"]
developer_instructions = "Use $writing. Hand off to reviewer."
''')
        self.write('AGENTS/openai/reviewer.toml', 'not selected')
        self.write('SKILLS/writing/SKILL.md', '''# Writing
[workflow](references/workflows/write.md#steps)
[shared]: ../../REFERENCES/guide.md#guide
```
[not a dependency](missing-code.md)
```
[external](https://example.org)
[fragment](#writing)
''')
        self.write('SKILLS/writing/agents/openai.yaml', 'interface: {}\n')
        self.write('SKILLS/writing/references/workflows/write.md', '# Steps\n[kit](../kit.md)\n')
        self.write('SKILLS/writing/references/kit.md', '# Kit\n')
        self.write('SKILLS/other/SKILL.md', '# Other\n')
        self.write('REFERENCES/guide.md', '[rules](rules.md)\n[record](../docs/evidence.md#checks)\nMentions $other without requiring it.\n')
        self.write('REFERENCES/rules.md', '[guide](guide.md#guide)\n')
        self.write('docs/evidence.md', '# Checks\n')
        self.git('add', '.')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture')
        self.write('SKILLS/writing/__pycache__/ignored.pyc', 'untracked')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.root), *args], check=True, capture_output=True)

    def write(self, rel, content):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def run_plan(self, *args, code=0, default=True):
        command = [sys.executable, '-B', str(SCRIPT), '--source-root', str(self.root), '--format', 'json']
        if default:
            command += ['--project', str(self.dest)]
        result = subprocess.run(command + list(args), capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report['exit_code'], code)
        return report

    def snapshot(self):
        return {str(p.relative_to(self.base)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.base.rglob('*') if p.is_file() and not p.is_symlink()}

    def test_dependencies_and_preservation(self):
        before = self.snapshot()
        report = self.run_plan('--agent', 'author', '--agent', 'author')
        self.assertEqual(report['selected_agents'], ['author'])
        self.assertEqual(report['required_skills'], ['writing'])
        self.assertEqual(len(report['files']), 7)
        self.assertEqual(report['summary']['missing'], 7)
        self.assertFalse(report['selected_sources_differ_from_commit'])
        self.assertFalse(self.dest.exists())
        self.assertEqual(before, self.snapshot())
        self.assertEqual(report, self.run_plan('--agent', 'author'))
        self.assertEqual(report['source_checkout_dependencies'], [str(self.root / 'docs/evidence.md')])
        links = [link for f in report['files'] for link in f['link_changes']]
        self.assertIn({'before': '../../REFERENCES/guide.md#guide', 'after': 'references/catalog/guide.md#guide'}, links)
        self.assertIn({'before': '../docs/evidence.md#checks', 'after': str(self.root / 'docs/evidence.md') + '#checks'}, links)
        names = [f['source'] for f in report['files']]
        self.assertFalse(any('__pycache__' in p or 'reviewer' in p or 'other/' in p for p in names))

    def test_skill_and_mixed_selection(self):
        report = self.run_plan('--skill', 'other')
        self.assertEqual(len(report['files']), 1)
        mixed = self.run_plan('--agent', 'author', '--skill', 'writing', '--skill', 'other')
        self.assertEqual(mixed['required_skills'], ['other', 'writing'])
        self.assertEqual(len(mixed['files']), 8)
        writing = next(f for f in mixed['files'] if f['source'].endswith('writing/SKILL.md'))
        self.assertEqual(writing['reasons'], ['required by agent author', 'selected skill writing'])

    def test_personal_and_overrides(self):
        report = self.run_plan('--skill', 'other', '--personal', default=False)
        self.assertEqual(report['skills_dir'], str(Path.home() / '.agents/skills'))
        report = self.run_plan('--agent', 'author', '--personal', '--agents-dir', str(self.base / 'agents'), '--skills-dir', str(self.base / 'skills'), default=False)
        self.assertEqual(report['agents_dir'], str(self.base / 'agents'))
        self.assertEqual(report['skills_dir'], str(self.base / 'skills'))
        self.assertFalse((self.base / 'skills').exists())

    def test_all_comparison_states(self):
        p = planner.Planner(self.root, self.dest / '.codex/agents', self.dest / '.agents/skills')
        p.report(['author'], [])
        for entry in p.entries.values():
            path = entry['destination']
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(entry['proposed'])
        report = self.run_plan('--agent', 'author')
        self.assertEqual(report['summary']['current'], 7)
        package = self.dest / '.agents/skills/writing'
        (package / 'SKILL.md').write_bytes((self.root / 'SKILLS/writing/SKILL.md').read_bytes())
        (package / 'references/kit.md').write_text('local changes')
        (package / 'agents/openai.yaml').unlink()
        target = self.dest / '.codex/agents/author.toml'
        target.unlink()
        target.mkdir()
        before = self.snapshot()
        report = self.run_plan('--agent', 'author', code=1)
        self.assertEqual(report['summary'], dict(blocked=1, conflict=1, current=3, **{'link-adaptation-needed': 1, 'missing': 1}))
        self.assertEqual(before, self.snapshot())

    def test_symlink_and_ancestor_collision(self):
        self.dest.symlink_to(self.base / 'missing')
        report = self.run_plan('--skill', 'other', code=1)
        self.assertEqual(report['summary']['blocked'], 1)
        self.dest.unlink()
        self.dest.write_text('file instead of directory')
        report = self.run_plan('--skill', 'other', code=1)
        self.assertEqual(report['summary']['blocked'], 1)

    def test_unreadable_destination(self):
        target = self.dest / '.agents/skills/other/SKILL.md'
        target.parent.mkdir(parents=True)
        target.write_text('# Other\n')
        original = Path.read_bytes
        def denied(path):
            if path == target:
                raise PermissionError('unreadable test destination')
            return original(path)
        with patch.object(Path, 'read_bytes', denied):
            report = planner.Planner(self.root, self.dest / '.codex/agents', self.dest / '.agents/skills').report([], ['other'])
        self.assertEqual(report['exit_code'], 1)
        self.assertEqual(report['summary']['blocked'], 1)

    def test_source_changes(self):
        self.write('SKILLS/other/SKILL.md', 'changed')
        report = self.run_plan('--skill', 'other')
        self.assertTrue(report['selected_sources_differ_from_commit'])
        self.assertTrue(report['files'][0]['differs_from_commit'])

    def test_source_symlink_is_rejected(self):
        path = self.root / 'SKILLS/other/SKILL.md'
        path.unlink()
        path.symlink_to(self.root / 'docs/evidence.md')
        report = self.run_plan('--skill', 'other', code=2)
        self.assertIn('symlink', report['errors'][0])

    def test_bundled_reference_collision(self):
        self.write('SKILLS/writing/references/catalog/guide.md', 'local package guide')
        self.git('add', 'SKILLS/writing/references/catalog/guide.md')
        report = self.run_plan('--skill', 'writing', code=2)
        self.assertTrue(any('destination collision' in e for e in report['errors']))

    def test_ignored_unrelated_destination(self):
        self.dest.mkdir()
        unrelated = self.dest / 'unrelated.txt'
        unrelated.write_text('preserve this')
        before = self.snapshot()
        report = self.run_plan('--skill', 'other')
        self.assertEqual(len(report['files']), 1)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(sorted(p.name for p in self.dest.iterdir()), ['unrelated.txt'])

    def test_planned_ancestor_collisions_in_both_orders(self):
        ancestor = self.dest / 'file'
        descendant = ancestor / 'child'
        before = self.snapshot()
        for first, second in [(ancestor, descendant), (descendant, ancestor)]:
            with self.subTest(first=first):
                p = planner.Planner(self.root, self.dest / 'agents', self.dest / 'skills')
                p.add('SKILLS/other/SKILL.md', first, 'first')
                with self.assertRaises(planner.PlanError) as caught:
                    p.add('SKILLS/writing/SKILL.md', second, 'second')
                self.assertIn(str(ancestor), str(caught.exception))
                self.assertIn(str(descendant), str(caught.exception))
        self.assertFalse(self.dest.exists())
        self.assertEqual(before, self.snapshot())

    def test_similar_sibling_paths_are_valid(self):
        p = planner.Planner(self.root, self.dest / 'agents', self.dest / 'skills')
        for name in ['file', 'file-other', 'files/child']:
            p.add('SKILLS/other/SKILL.md', self.dest / name, name)
        self.assertEqual(len(p.entries), 3)
        self.assertFalse(self.dest.exists())

    def test_overlapping_personal_overrides(self):
        self.dest.mkdir()
        (self.dest / 'unrelated.txt').write_text('preserve this')
        ancestor = self.dest / 'writing/SKILL.md'
        before = self.snapshot()
        report = self.run_plan('--agent', 'author', '--skill', 'writing', '--personal',
                               '--agents-dir', str(ancestor), '--skills-dir', str(self.dest),
                               code=2, default=False)
        errors = '\n'.join(report['errors'])
        self.assertIn(str(ancestor), errors)
        self.assertIn(str(ancestor / 'author.toml'), errors)
        self.assertEqual(before, self.snapshot())
        self.assertFalse(ancestor.parent.exists())

    def test_invalid_inputs(self):
        for args in [[], ['--agent', 'absent'], ['--skill', 'absent'], ['--skill', '../other'], ['--skill', 'other', '--agents-dir', '/tmp/unused']]:
            with self.subTest(args=args):
                self.assertTrue(self.run_plan(*args, code=2)['errors'])
        self.run_plan('--skill', 'other', code=2, default=False)
        self.run_plan('--skill', 'other', '--personal', code=2)
        self.write('AGENTS/openai/author.toml', 'invalid = [')
        self.run_plan('--agent', 'author', code=2)
        self.write('AGENTS/openai/author.toml', 'name = "author"')
        self.run_plan('--agent', 'author', code=2)

    def test_broken_and_outside_links(self):
        for content in ['[bad](missing.md)', '[outside](../../docs/evidence.md)', '[escape](../../../outside.md)', '[other](../other/SKILL.md)']:
            with self.subTest(content=content):
                self.write('SKILLS/writing/SKILL.md', content)
                self.assertTrue(self.run_plan('--skill', 'writing', code=2)['errors'])

    def test_missing_dependency_and_tracked_file(self):
        (self.root / 'SKILLS/writing/SKILL.md').unlink()
        self.run_plan('--agent', 'author', code=2)
        self.write('SKILLS/writing/SKILL.md', '# Recreated')
        (self.root / 'REFERENCES/rules.md').unlink()
        self.write('SKILLS/writing/SKILL.md', '[guide](../../REFERENCES/guide.md)')
        self.run_plan('--skill', 'writing', code=2)

    def test_markdown_scanner(self):
        text = '[a](folder/a(b).md#x "title")\n[r]: <file%20name.md#y> "title"\n~~~\n[x](ignore.md)\n~~~\n![i](image.png)\n'
        self.assertEqual([x[2] for x in planner.markdown_links(text)], ['folder/a(b).md#x', 'file%20name.md#y', 'image.png'])

    def test_text_errors_stderr(self):
        result = subprocess.run([sys.executable, '-B', str(SCRIPT), '--project', str(self.dest)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('select at least one', result.stderr)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
