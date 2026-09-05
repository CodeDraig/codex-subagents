import collections,hashlib,json,re,subprocess,tomllib
from pathlib import Path
from urllib.parse import unquote,urlsplit
import yaml
R=Path('/srv/data/code/codex-subagents');P=Path('/tmp/text-lifecycle-20260905')
data=json.loads((P/'catalog-data.json').read_text()); old=json.loads((P/'modified-existing-agents.json').read_text())
agents=list((R/'AGENTS/openai').glob('*.toml'));gateways=list((R/'SKILLS').glob('*/SKILL.md'))
assert len(agents)==133 and len(gateways)==26
required={'name','description','model','model_reasoning_effort','sandbox_mode','nickname_candidates','developer_instructions'}
models=collections.Counter(); refs=0;registry=(R/'REFERENCES/software-development-crew.md').read_text()
for p in agents:
 d=tomllib.loads(p.read_text());assert required<=d.keys(),p
 assert d['name']==p.stem and d['nickname_candidates'],p
 assert d['sandbox_mode'] in ['read-only','workspace-write'],p
 models[d['model'],d['model_reasoning_effort']]+=1
 for name in re.findall(r'\$([a-z][a-z0-9-]*)',d['developer_instructions']):
  assert (R/'SKILLS'/name/'SKILL.md').is_file(),(p,name);refs+=1
 assert '`'+p.stem+'`' in registry,p
for key,n in models.items():assert f'| `{key[0]}` | `{key[1]}` | {n} |' in registry,(key,n)
wfs=set();afs=set();links=0
for p in gateways:
 s=p.read_text();d=yaml.safe_load(s.split('---',2)[1]);assert d['name']==p.parent.name and d['description'],p
 side=yaml.safe_load((p.parent/'agents/openai.yaml').read_text())['interface']
 assert '$'+p.parent.name in side['default_prompt'],p
 assert '`$'+p.parent.name+'`' in registry,p
 for rel in re.findall(r'\]\((references/workflows/[^)]+)\)',s):wfs.add((p.parent/rel).resolve())
for p in [R/'README.md',*list((R/'REFERENCES').glob('*.md')),*list((R/'SKILLS').rglob('*.md'))]:
 for rel in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  u=urlsplit(rel)
  if u.scheme or rel.startswith('#'):continue
  target=(p.parent/unquote(u.path)).resolve();assert target.is_relative_to(R) and target.exists(),(p,rel)
  links+=1
  if '/references/artifacts/' in str(target):afs.add(target)
assert wfs=={p.resolve() for p in (R/'SKILLS').glob('*/references/workflows/*.md')}
assert afs=={p.resolve() for p in (R/'SKILLS').glob('*/references/artifacts/*.md')}
assert len(wfs)==104 and len(afs)==102
def sections(s):return re.findall(r'`([^`]+)`',next(l for l in s.splitlines() if l.startswith('Return exactly')))
aligned=[]
for a in data['agents']:
 ap=R/'AGENTS/openai'/f'{a["name"]}.toml'; wp=R/'SKILLS'/a['gateway']/'references/workflows'/f'{a["primary"]}.md'
 assert sections(tomllib.loads(ap.read_text())['developer_instructions'])==sections(wp.read_text()),a['name']
 aligned.append(a['name'])
for name,slug in old.items():
 gateway='text-revision' if name=='developmental-manuscript-editor' else 'publishing-editorial'
 assert sections(tomllib.loads((R/'AGENTS/openai'/f'{name}.toml').read_text())['developer_instructions'])==sections((R/'SKILLS'/gateway/'references/workflows'/f'{slug}.md').read_text()),name
 aligned.append(name)
for m in data['modes']:
 wf=R/'SKILLS'/m['gateway']/'references/workflows'/f'{m["slug"]}.md';art=R/'SKILLS'/m['gateway']/'references/artifacts'/f'{m["slug"]}-kit.md'
 assert all(h in wf.read_text() for h in ['## Intake','## Decision Rules','## Verification','## Output Contract','## Handoffs','## Boundaries']),wf
 assert all(h in art.read_text() for h in ['## Working Record','## Worked Example','## Failure Case']),art
for p in [R/'REFERENCES/software-development-crew.md',*gateways]:
 # Pipe rows without a header after a blank line are broken Markdown tables.
 lines=p.read_text().splitlines()
 for i,line in enumerate(lines):
  if line.startswith('|') and (i==0 or not lines[i-1].startswith('|')):
   assert i+1<len(lines) and re.match(r'^\|[ :|\-]+\|$',lines[i+1]),(p,i+1,'table lacks header separator')
subprocess.run(['git','diff','--check'],cwd=R,check=True)
before=json.loads((P/'before.json').read_text())
changed=[f for f,h in before.items() if hashlib.sha256((R/f).read_bytes()).hexdigest()!=h]
report={'agents':len(agents),'gateways':len(gateways),'workflows':len(wfs),'artifacts':len(afs),'skill_references':refs,'local_links':links,'aligned_new_or_modified_agent_contracts':aligned,'model_counts':{f'{k[0]}/{k[1]}':n for k,n in models.items()},'changed_existing_files':changed,'git_diff_check':'passed'}
(P/'catalog-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['changed_existing_files','aligned_new_or_modified_agent_contracts']},indent=2))
print('Aligned contracts:',len(aligned),'changed existing files:',len(changed))
