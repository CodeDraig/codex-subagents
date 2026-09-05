import concurrent.futures,hashlib,json,os,signal,subprocess,sys,time,tomllib
from pathlib import Path
P=Path('/tmp/text-lifecycle-20260905');project=P/'project'
cases=json.loads((P/'fixtures.json').read_text())
def run(name):
 c=cases[name];folder=P/'live'/name
 if folder.exists():raise RuntimeError('Case already has evidence; archive the completed attempt explicitly before a justified rerun: '+name)
 folder.mkdir(parents=True)
 for dep in c['depends']:
  status=json.loads((P/'live'/dep/'status.json').read_text());assert status['exit']==0
  (project/'inputs'/f'{dep}.md').write_text((P/'live'/dep/'response.md').read_text())
 prompt=f'Use ${c["skill"]} in {c["mode"]} mode from .agents/skills/{c["skill"]}/SKILL.md.\n\n'+c['prompt']
 (folder/'prompt.txt').write_text(prompt+'\n')
 settings={'model':'gpt-5.6-terra','model_reasoning_effort':'high'}
 sandbox='workspace-write'
 if c['agent']:
  cfg=tomllib.loads((project/'.codex/agents'/f'{c["agent"]}.toml').read_text())
  settings={k:cfg[k] for k in ['model','model_reasoning_effort','developer_instructions']};sandbox=cfg['sandbox_mode']
 args=[str(P/'bin/codex-x86_64-unknown-linux-musl'),'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox',sandbox,'--color','never','--json','-C',str(project),'-c','agents.enabled=false','--disable','multi_agent','--disable','multi_agent_v2','--disable','hooks','--disable','shell_snapshot','--disable','apps','--disable','remote_plugin','-c','web_search="disabled"','-c','history.persistence="none"','-c','log_dir='+json.dumps(str(folder/'log')),'-c','sqlite_home='+json.dumps(str(folder/'state')),'-o',str(folder/'response.md')]
 for k,v in settings.items():args+=['-c',k+'='+json.dumps(v)]
 args+=['-']
 (folder/'invocation.json').write_text(json.dumps({'args':args,'agent':c['agent'],'model':settings['model'],'reasoning':settings['model_reasoning_effort'],'sandbox':sandbox},indent=2)+'\n')
 start=time.monotonic()
 with (folder/'events.jsonl').open('w') as out,(folder/'stderr').open('w') as err:
  proc=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=out,stderr=err,text=True,start_new_session=True)
  (folder/'running.json').write_text(json.dumps({'pid':proc.pid,'case':name})+'\n')
  try:proc.communicate(prompt,timeout=300);code=proc.returncode
  except subprocess.TimeoutExpired:
   os.killpg(proc.pid,signal.SIGTERM)
   try:proc.wait(timeout=5)
   except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
   code='timeout'
 status={'case':name,'exit':code,'seconds':round(time.monotonic()-start,2)}
 (folder/'status.json').write_text(json.dumps(status,indent=2)+'\n')
 print(json.dumps(status),flush=True)
 return status
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for result in pool.map(run,sys.argv[1:]):pass
