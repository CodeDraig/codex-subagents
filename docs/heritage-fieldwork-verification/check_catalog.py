"""Read-only catalog checks for this expansion; optionally save a JSON report."""
import argparse
import collections
import json
import re
import subprocess
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads((Path(__file__).parent/'manifest.json').read_text())
    registry = (root/'REFERENCES/software-development-crew.md').read_text()
    required = {'name','description','model','model_reasoning_effort','sandbox_mode','nickname_candidates','developer_instructions'}
    models = collections.Counter()
    agents = {}
    for path in sorted((root/'AGENTS/openai').glob('*.toml')):
        agent = tomllib.loads(path.read_text())
        assert required <= agent.keys(), path
        assert agent['name'] == path.stem and agent['description'] and agent['nickname_candidates'], path
        assert agent['sandbox_mode'] in {'read-only','workspace-write'}, path
        assert agent['name'] not in agents, path
        agents[agent['name']] = agent
        models[agent['model'],agent['model_reasoning_effort']] += 1
        for skill in re.findall(r'\$([a-z][a-z0-9-]*)', agent['developer_instructions']):
            assert (root/'SKILLS'/skill/'SKILL.md').is_file(), (path,skill)
        assert '`'+agent['name']+'`' in registry, path
    for (model,effort),count in models.items():
        assert f'| `{model}` | `{effort}` | {count} |' in registry, (model,effort,count)
    gateways = list((root/'SKILLS').glob('*/SKILL.md'))
    reached_workflows = set()
    reached_artifacts = set()
    new_gateways = {m['gateway'] for m in manifest}
    for path in gateways:
        text = path.read_text()
        front = yaml.safe_load(text.split('---',2)[1])
        assert front['name'] == path.parent.name and front['description'], path
        side = yaml.safe_load((path.parent/'agents/openai.yaml').read_text())['interface']
        assert '$'+front['name'] in side['default_prompt'], path
        assert '`$'+front['name']+'`' in registry, path
        if path.parent.name in new_gateways:
            assert 25 <= len(side['short_description']) <= 64, path
        for rel in re.findall(r'\]\((references/workflows/[^)]+)\)',text):
            reached_workflows.add((path.parent/rel).resolve())
    links = 0
    for path in [root/'README.md',*list((root/'REFERENCES').glob('*.md')),*list((root/'SKILLS').rglob('*.md'))]:
        for rel in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            url = urlsplit(rel)
            if url.scheme or not url.path:
                continue
            target = (path.parent/unquote(url.path)).resolve()
            assert target.is_relative_to(root) and target.exists(), (path,rel)
            links += 1
            if '/references/artifacts/' in str(target):
                reached_artifacts.add(target)
    workflows = {p.resolve() for p in (root/'SKILLS').glob('*/references/workflows/*.md')}
    artifacts = {p.resolve() for p in (root/'SKILLS').glob('*/references/artifacts/*.md')}
    assert reached_workflows == workflows, ('unreachable workflows', workflows-reached_workflows)
    assert reached_artifacts == artifacts, ('unreachable artifacts', artifacts-reached_artifacts)
    def sections(text):
        line = next(line for line in text.splitlines() if line.startswith('Return exactly these sections:'))
        return re.findall(r'`([^`]+)`',line)
    for item in manifest:
        name,gateway,mode = item['agent'],item['gateway'],item['mode']
        agent = agents[name]
        workflow = root/'SKILLS'/gateway/'references/workflows'/f'{mode}.md'
        kit = root/'SKILLS'/gateway/'references/artifacts'/f'{mode}-kit.md'
        text = workflow.read_text()
        assert sections(agent['developer_instructions']) == sections(text) == item['sections'], name
        assert (agent['model'],agent['model_reasoning_effort'],agent['sandbox_mode']) == (item['model'],item['reasoning'],item['sandbox']), name
        for heading in ['Intake','Workflow','Decision Rules','Verification','Output Contract','Handoffs','Boundaries','Practice References']:
            assert '## '+heading+'\n' in text, (workflow,heading)
        for heading in ['Working Record','Worked Example','Failure Case']:
            assert '## '+heading+'\n' in kit.read_text(), (kit,heading)
        handoffs = text.split('## Handoffs\n',1)[1].split('## Boundaries\n',1)[0]
        for target in re.findall(r'`([a-z][a-z0-9-]*)`',handoffs):
            assert target in agents, (name,target)
        for path in [workflow,kit,root/'AGENTS/openai'/f'{name}.toml']:
            assert all(line == line.rstrip() for line in path.read_text().splitlines()), path
    for path in [root/'REFERENCES/software-development-crew.md',*gateways]:
        lines = path.read_text().splitlines()
        for i,line in enumerate(lines):
            if line.startswith('|') and (i==0 or not lines[i-1].startswith('|')):
                assert i+1<len(lines) and re.fullmatch(r'[| :\-]+',lines[i+1]), (path,i+1,'broken table')
    readme = (root/'README.md').read_text()
    assert f'{len(agents)} OpenAI agent templates' in readme
    assert f'{len(gateways)} skill gateways' in readme and f'{len(workflows)} workflows' in readme
    assert f'{len(workflows)+len(artifacts)} selectively loaded' in readme
    assert (len(manifest),len(new_gateways)) == (21,4)
    subprocess.run(['git','diff','--check'],cwd=root,check=True)
    report = dict(agents=len(agents),gateways=len(gateways),workflows=len(workflows),artifacts=len(artifacts),local_links=links,new_aligned_contracts=len(manifest),model_counts={f'{k[0]}/{k[1]}':v for k,v in sorted(models.items())},git_diff_check='passed')
    if args.report:
        args.report.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
