import concurrent.futures
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import tomllib
from pathlib import Path

P = Path(__file__).parent
R = Path('/srv/data/code/codex-subagents')
CASES = json.loads((P/'fixtures.json').read_text())
GATEWAYS = json.loads((P/'catalog-data.json').read_text())['gateways']

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(name):
    case = CASES[name]
    attempts = P/'live'/name
    attempts.mkdir(parents=True,exist_ok=True)
    folder = attempts/f'attempt-{len(list(attempts.glob("attempt-*")))+1}'
    folder.mkdir()
    project = folder/'project';project.mkdir()
    (project/'outputs').mkdir()
    for gateway in GATEWAYS:
        shutil.copytree(R/'SKILLS'/gateway, project/'.agents/skills'/gateway)
    agent_path = R/'AGENTS/openai'/f'{case["agent"]}.toml'
    local_agent = project/'.codex/agents'/agent_path.name
    local_agent.parent.mkdir(parents=True)
    shutil.copy2(agent_path,local_agent)
    source_hashes = {str(agent_path.relative_to(R)):digest(agent_path)}
    for gateway in GATEWAYS:
        for path in (R/'SKILLS'/gateway).rglob('*'):
            if path.is_file(): source_hashes[str(path.relative_to(R))] = digest(path)
    for rel,text in case['files'].items():
        path = project/rel;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
    before = {rel:digest(project/rel) for rel in case['files']}
    cfg = tomllib.loads(local_agent.read_text())
    prompt = f'Use ${case["gateway"]} in `{case["mode"]}` mode from .agents/skills/{case["gateway"]}/SKILL.md.\n\n'+case['request']
    (folder/'prompt.txt').write_text(prompt+'\n')
    args = ['codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox',cfg['sandbox_mode'],'--color','never','--json','-C',str(project),'-c','agents.enabled=false','--disable','multi_agent','--disable','multi_agent_v2','--disable','hooks','--disable','shell_snapshot','--disable','apps','--disable','remote_plugin','-c','web_search="disabled"','-c','approval_policy="never"','-c','history.persistence="none"','-c','log_dir='+json.dumps(str(folder/'log')),'-c','sqlite_home='+json.dumps(str(folder/'state')),'-o',str(folder/'response.md')]
    for key in ['model','model_reasoning_effort','developer_instructions']:
        args += ['-c',key+'='+json.dumps(cfg[key])]
    args += ['-']
    task_home = folder/'home'
    task_home.mkdir(mode=0o700)
    auth_source = Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'auth.json'
    if auth_source.is_file():
        (task_home/'auth.json').symlink_to(auth_source)
    env = dict(os.environ, CODEX_HOME=str(task_home))
    started = time.monotonic()
    with (folder/'events.jsonl').open('w') as out,(folder/'stderr.txt').open('w') as err:
        proc = subprocess.Popen(args,stdin=subprocess.PIPE,stdout=out,stderr=err,text=True,start_new_session=True,env=env)
        (folder/'running.json').write_text(json.dumps({'pid':proc.pid,'case':name})+'\n')
        try:
            proc.communicate(prompt,timeout=300)
            result = proc.returncode
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid,signal.SIGTERM)
            try: proc.wait(timeout=5)
            except subprocess.TimeoutExpired: os.killpg(proc.pid,signal.SIGKILL);proc.wait()
            result = 'timeout'
    after = {rel:digest(project/rel) if (project/rel).exists() else None for rel in case['files']}
    record = dict(case=name,attempt=folder.name,agent=case['agent'],gateway=case['gateway'],mode=case['mode'],model=cfg['model'],reasoning=cfg['model_reasoning_effort'],sandbox=cfg['sandbox_mode'],exit=result,seconds=round(time.monotonic()-started,2),prompt=prompt,args=args,source_hashes=source_hashes,input_hashes_before=before,input_hashes_after=after,inputs_unchanged=before==after,raw_log_hashes={p.name:digest(p) for p in [folder/'events.jsonl',folder/'stderr.txt']},output_hashes={str(p.relative_to(project)):digest(p) for p in (project/'outputs').rglob('*') if p.is_file()})
    if (folder/'response.md').exists(): record['response_sha256']=digest(folder/'response.md')
    (folder/'run.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['case','attempt','exit','seconds','inputs_unchanged']}),flush=True)

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    list(pool.map(run,sys.argv[1:] or list(CASES)))
