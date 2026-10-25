#!/usr/bin/env python3
"""Print a selective Codex installation plan without modifying any files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tomllib
from urllib.parse import quote, unquote, urlsplit


class PlanError(Exception):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise PlanError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True)
    if result.returncode:
        raise PlanError(result.stderr.decode(errors='replace').strip())
    return result.stdout


def absolute(path):
    # Do not resolve destination symlinks: comparison must detect them.
    return Path(os.path.abspath(os.path.expanduser(str(path))))


def path_blocker(path):
    for part in [*reversed(path.parents), path]:
        try:
            mode = part.lstat().st_mode
        except FileNotFoundError:
            return None
        except OSError as exc:
            return str(exc)
        if stat.S_ISLNK(mode):
            return f'symlink in path: {part}'
        if part != path and not stat.S_ISDIR(mode):
            return f'non-directory ancestor: {part}'
    return None


def markdown_links(text):
    """Yield destination spans outside fenced blocks (including reference definitions)."""
    fence = None
    offset = 0
    # Balanced parentheses are handled separately below; titles are not destinations.
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[marker.end():].strip():
                fence = None
            offset += len(line)
            continue
        if fence is not None:
            offset += len(line)
            continue
        starts = [m.end() for m in re.finditer(r'!?\[[^\]\n]*\]\(\s*', line)]
        definition = re.match(r'^ {0,3}\[[^\]\n]+\]:\s*', line)
        if definition:
            starts.append(definition.end())
        for start in sorted(set(starts)):
            if start >= len(line):
                continue
            if line[start] == '<':
                end = line.find('>', start + 1)
                if end < 0:
                    continue
                start += 1
            else:
                end, depth = start, 0
                while end < len(line):
                    char = line[end]
                    if char == '\\' and end + 1 < len(line):
                        end += 2
                        continue
                    if char.isspace() or (char == ')' and depth == 0):
                        break
                    depth += (char == '(') - (char == ')')
                    end += 1
            if end > start:
                yield offset + start, offset + end, line[start:end]
        offset += len(line)


class Planner:
    def __init__(self, root, agents_dir, skills_dir):
        self.root = root.resolve()
        self.agents_dir, self.skills_dir = agents_dir, skills_dir
        top = Path(git(self.root, 'rev-parse', '--show-toplevel').decode().strip()).resolve()
        if top != self.root:
            raise PlanError('--source-root must be the Git repository root')
        self.commit = git(self.root, 'rev-parse', 'HEAD').decode().strip()
        self.tracked = set(git(self.root, 'ls-files', '-z').decode().split('\0')) - {''}
        self.entries = {}
        self.dependencies = set()
        self.errors = []

    def read(self, rel):
        if rel not in self.tracked:
            raise PlanError(f'missing tracked source: {rel}')
        path = self.root / rel
        blocker = path_blocker(path)
        if blocker:
            raise PlanError(f'{rel}: {blocker}')
        try:
            if not stat.S_ISREG(path.stat().st_mode):
                raise PlanError(f'{rel}: source is not a regular file')
            return path.read_bytes()
        except OSError as exc:
            raise PlanError(f'{rel}: {exc}') from exc

    def add(self, rel, dest, reason, skill=None):
        key = str(dest)
        if key in self.entries:
            if self.entries[key]['source_relative'] != rel:
                raise PlanError(f'destination collision: {dest}')
            self.entries[key]['reasons'].add(reason)
            return
        for entry in self.entries.values():
            existing = entry['destination']
            if dest.is_relative_to(existing) or existing.is_relative_to(dest):
                raise PlanError(f'destination collision: {dest} and {existing}')
        raw = self.read(rel)
        self.entries[key] = dict(source_relative=rel, destination=dest, reasons={reason},
                                 raw=raw, proposed=raw, skill=skill, link_changes=[])

    def skill(self, name, reason):
        prefix = f'SKILLS/{name}/'
        if prefix + 'SKILL.md' not in self.tracked:
            raise PlanError(f'unknown or incomplete skill: {name}')
        for rel in sorted(p for p in self.tracked if p.startswith(prefix)):
            self.add(rel, self.skills_dir / name / rel[len(prefix):], reason, name)

    def transform(self, entry):
        rel, skill = entry['source_relative'], entry['skill']
        if not skill or not rel.endswith('.md'):
            return
        text = entry['raw'].decode('utf-8')
        replacements = []
        for start, end, link in markdown_links(text):
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (self.root / rel).parent / unquote(re.sub(r'\\([() ])', r'\1', url.path))
            target = Path(os.path.abspath(target))
            if not target.is_relative_to(self.root):
                raise PlanError(f'{rel}: link escapes source repository: {link}')
            target_rel = target.relative_to(self.root).as_posix()
            package = f'SKILLS/{skill}/'
            if target_rel.startswith(package):
                self.read(target_rel)
                destination = self.skills_dir / skill / target_rel[len(package):]
                new_path = os.path.relpath(destination, entry['destination'].parent)
            elif target_rel.startswith('REFERENCES/'):
                destination = self.skills_dir / skill / 'references/catalog' / target_rel[len('REFERENCES/'):]
                self.add(target_rel, destination, f'shared reference linked by {rel}', skill)
                new_path = os.path.relpath(destination, entry['destination'].parent)
            elif rel.startswith('REFERENCES/') and target_rel.startswith('docs/'):
                self.read(target_rel)
                self.dependencies.add(str(target))
                new_path = str(target)
            else:
                raise PlanError(f'{rel}: unresolved dependency: {link}')
            replacement = quote(new_path, safe='/.-_~')
            if url.query:
                replacement += '?' + url.query
            if url.fragment:
                replacement += '#' + url.fragment
            if replacement != link:
                replacements.append((start, end, replacement))
                entry['link_changes'].append(dict(before=link, after=replacement))
        for start, end, replacement in reversed(replacements):
            text = text[:start] + replacement + text[end:]
        entry['proposed'] = text.encode('utf-8')

    def report(self, agents, skills):
        needed = {}
        for name in agents:
            try:
                rel = f'AGENTS/openai/{name}.toml'
                raw = self.read(rel)
                cfg = tomllib.loads(raw.decode())
                for key in ('name', 'description', 'model', 'model_reasoning_effort', 'sandbox_mode', 'developer_instructions'):
                    if not isinstance(cfg.get(key), str) or not cfg[key]:
                        raise PlanError(f'{rel}: missing or invalid {key}')
                if cfg['name'] != name or not isinstance(cfg.get('nickname_candidates'), list) or not cfg['nickname_candidates'] or not all(isinstance(n, str) and n for n in cfg['nickname_candidates']):
                    raise PlanError(f'{rel}: invalid name or nickname_candidates')
                self.add(rel, self.agents_dir / f'{name}.toml', f'selected agent {name}')
                for dep in re.findall(r'\$([a-z][a-z0-9-]*)', cfg['developer_instructions']):
                    needed.setdefault(dep, set()).add(f'required by agent {name}')
            except (PlanError, ValueError) as exc:
                self.errors.append(str(exc))
        for name in skills:
            needed.setdefault(name, set()).add(f'selected skill {name}')
        for name, reasons in sorted(needed.items()):
            try:
                for reason in sorted(reasons):
                    self.skill(name, reason)
            except PlanError as exc:
                self.errors.append(str(exc))
        processed = set()
        while pending := sorted(set(self.entries) - processed):
            for key in pending:
                processed.add(key)
                try:
                    self.transform(self.entries[key])
                except (PlanError, ValueError) as exc:
                    self.errors.append(str(exc))
        files = []
        counts = dict.fromkeys(['missing', 'current', 'link-adaptation-needed', 'conflict', 'blocked'], 0)
        for _, entry in sorted(self.entries.items()):
            dest, raw, proposed = entry['destination'], entry['raw'], entry['proposed']
            blocker = path_blocker(dest)
            observed = None
            status = 'blocked' if blocker else 'missing'
            if not blocker:
                try:
                    mode = dest.stat().st_mode
                    if not stat.S_ISREG(mode):
                        raise OSError('destination is not a regular file')
                    observed = dest.read_bytes()
                    status = 'current' if observed == proposed else 'link-adaptation-needed' if observed == raw else 'conflict'
                except FileNotFoundError:
                    pass
                except OSError as exc:
                    status, blocker = 'blocked', str(exc)
            rel = entry['source_relative']
            original = subprocess.run(['git', '-C', str(self.root), 'show', f'{self.commit}:{rel}'], capture_output=True)
            files.append(dict(source=str(self.root / rel), destination=str(dest),
                              reasons=sorted(entry['reasons']), source_sha256=digest(raw),
                              proposed_sha256=digest(proposed), destination_sha256=digest(observed) if observed is not None else None,
                              differs_from_commit=original.returncode != 0 or original.stdout != raw,
                              status=status, detail=blocker, link_changes=entry['link_changes']))
            counts[status] += 1
        errors = sorted(set(self.errors))
        return dict(schema_version=1, source_root=str(self.root), source_commit=self.commit,
                    selected_sources_differ_from_commit=any(f['differs_from_commit'] for f in files),
                    selected_agents=agents, selected_skills=skills, required_skills=sorted(needed),
                    agents_dir=str(self.agents_dir), skills_dir=str(self.skills_dir),
                    source_checkout_dependencies=sorted(self.dependencies), files=files,
                    summary=counts, errors=errors,
                    exit_code=2 if errors else 1 if counts['conflict'] or counts['blocked'] else 0)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    parser = Parser(description=__doc__)
    parser.add_argument('--agent', action='append', default=[])
    parser.add_argument('--skill', action='append', default=[])
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument('--project', type=Path)
    target.add_argument('--personal', action='store_true')
    parser.add_argument('--agents-dir', type=Path)
    parser.add_argument('--skills-dir', type=Path)
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--format', choices=['text', 'json'], default='text')
    json_output = '--format=json' in argv or any(a == '--format' and i + 1 < len(argv) and argv[i+1] == 'json' for i, a in enumerate(argv))
    try:
        args = parser.parse_args(argv)
        if not args.agent and not args.skill:
            raise PlanError('select at least one --agent or --skill')
        if any(not re.fullmatch(r'[a-z][a-z0-9-]*', n) for n in args.agent + args.skill):
            raise PlanError('agent and skill names must use lowercase letters, digits, and hyphens')
        if args.project and (args.agents_dir or args.skills_dir):
            raise PlanError('directory overrides require --personal')
        agents_dir = absolute(args.agents_dir or (args.project / '.codex/agents' if args.project else Path.home() / '.codex/agents'))
        skills_dir = absolute(args.skills_dir or (args.project / '.agents/skills' if args.project else Path.home() / '.agents/skills'))
        report = Planner(args.source_root, agents_dir, skills_dir).report(sorted(set(args.agent)), sorted(set(args.skill)))
    except (PlanError, OSError, ValueError) as exc:
        report = dict(schema_version=1, files=[], errors=[str(exc)], exit_code=2)
    if json_output:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        if 'source_commit' in report:
            print(f"Source: {report['source_root']} @ {report['source_commit']}")
            print(f"Selected source changes: {report['selected_sources_differ_from_commit']}")
        for entry in report['files']:
            print(f"{entry['status']}: {entry['destination']}\n  source: {entry['source']}\n  reason: {', '.join(entry['reasons'])}")
            print(f"  hashes: source={entry['source_sha256']} proposed={entry['proposed_sha256']} destination={entry['destination_sha256']}")
            for change in entry['link_changes']:
                print(f"  link: {change['before']} -> {change['after']}")
            if entry['detail']:
                print(f"  {entry['detail']}", file=sys.stderr)
        for dependency in report.get('source_checkout_dependencies', []):
            print(f'Source-checkout dependency: {dependency}')
        if 'summary' in report:
            print('Summary: ' + ', '.join(f'{k}={v}' for k, v in report['summary'].items()))
        for error in report['errors']:
            print(f'error: {error}', file=sys.stderr)
    return report['exit_code']


if __name__ == '__main__':
    sys.exit(main())
