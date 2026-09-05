from pathlib import Path
import hashlib,json,re,subprocess,yaml
from urllib.parse import urlsplit,unquote
R=Path('/srv/data/code/codex-subagents');P=Path('/tmp/text-lifecycle-20260905');D=R/'docs/text-lifecycle-verification'
review=json.loads((D/'asset-review.json').read_text());files={}
for group in ['modes','agents','gateways']:
 for row in review[group]:
  assert min(row['scores'].values())>=3
  for f in row['reviewed_files']:files[f['path']]=f['sha256']
for f in review['integration_files']:files[f['path']]=f['sha256']
assert len(files)==116
for f,h in files.items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h,f
status=subprocess.run(['git','status','--porcelain','--untracked-files=all'],cwd=R,capture_output=True,text=True,check=True).stdout
changes=[line[3:] for line in status.splitlines()]
assert set(changes)==set(files)|{p for p in changes if p.startswith('docs/')}
for name in ['text-composition','text-revision','text-translation','textual-scholarship','publishing-editorial']:
 d=yaml.safe_load((R/'SKILLS'/name/'agents/openai.yaml').read_text())['interface'];assert all(d.get(k) for k in ['display_name','short_description','default_prompt']);assert 25<=len(d['short_description'])<=64
 links=re.findall(r'\]\((references/workflows/[^)]+)\)',(R/'SKILLS'/name/'SKILL.md').read_text());assert len(links)==len(set(links))
for f in [R/'docs/text-lifecycle-verification.md',D/'asset-review.md',R/'docs/text-lifecycle-expansion-plan.md']:
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  u=urlsplit(link)
  if not u.scheme and not link.startswith('#'):assert (f.parent/unquote(u.path)).exists(),(f,link)
names={p.stem for p in (R/'AGENTS/openai').glob('*.toml')};targets=set()
for path in files:
 if not (path.startswith('AGENTS/') or path.startswith('SKILLS/')):continue
 for n in re.findall(r'\b[a-z][a-z0-9]*(?:-[a-z0-9]+){1,5}\b',(R/path).read_text()):
  if any(n.endswith(suffix) for suffix in ['-editor','-reviewer','-analyst','-writer','-specialist','-coordinator','-planner','-drafter','-transcriber','-collator','-translator','-engineer','-checker']):assert n in names,(path,n);targets.add(n)
shared=0
for f in (R/'REFERENCES').rglob('*'):
 if f.is_file():assert f.read_bytes()==(P/'project/.agents/REFERENCES'/f.relative_to(R/'REFERENCES')).read_bytes();shared+=1
for cat in ['cases','failed-attempts']:
 for f in (D/cat).glob('*/run.json'):
  data=json.loads(f.read_text())
  for raw in data['raw_evidence']:assert hashlib.sha256(Path(raw['path']).read_bytes()).hexdigest()==raw['sha256']
  if 'response_sha256' in data:assert hashlib.sha256((f.parent/'response.md').read_bytes()).hexdigest()==data['response_sha256']
live=json.loads((D/'live-results.json').read_text());assert len(live['cases'])==22 and all(c['exit']==0 and c['acceptance']=='pass' for c in live['cases'])
before=json.loads((P/'before.json').read_text());subprocess.run(['git','diff','--check'],cwd=R,check=True)
report={'reviewed_catalog_and_integration_files':len(files),'named_handoff_targets':len(targets),'shared_reference_copies_matching':shared,'changed_tracked_files':sum(not l.startswith('??') for l in status.splitlines()),'new_catalog_files':sum(p not in before and not p.startswith('docs/') for p in changes),'accepted_live_cases':len(live['cases']),'prior_attempts_retained':len(live['failed_attempts']),'git_diff_check':'passed','files':files}
(D/'final-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='files'},indent=2))
