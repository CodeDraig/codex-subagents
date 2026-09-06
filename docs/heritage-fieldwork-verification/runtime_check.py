import json
import os
import selectors
import shutil
import subprocess
import time
from pathlib import Path

P = Path(__file__).parent/'runtime'
R = Path('/srv/data/code/codex-subagents')
P.mkdir()
project = P/'project';project.mkdir()
home = P/'home';home.mkdir(mode=0o700)
shutil.copytree(R/'SKILLS',project/'.agents/skills')
shutil.copytree(R/'REFERENCES',project/'.agents/REFERENCES')
manifest = json.loads((R/'docs/heritage-fieldwork-verification/manifest.json').read_text())
(project/'.codex/agents').mkdir(parents=True)
config = '[agents]\nmax_concurrent_threads_per_session = 2\n'
for item in manifest:
    name = item['agent']
    shutil.copy2(R/'AGENTS/openai'/f'{name}.toml',project/'.codex/agents'/f'{name}.toml')
    config += '\n[agents.'+name+']\nconfig_file = "agents/'+name+'.toml"\n'
(project/'.codex/config.toml').write_text(config)
(home/'config.toml').write_text('[projects.'+json.dumps(str(project))+']\ntrust_level = "trusted"\n')
env = dict(os.environ, CODEX_HOME=str(home))
messages = []
log = (P/'stderr.txt').open('w')
proc = subprocess.Popen(['codex','--strict-config','-C',str(project),'app-server','--stdio'],env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=log,text=True,bufsize=1)
selector = selectors.DefaultSelector();selector.register(proc.stdout,selectors.EVENT_READ)
pending_output = b''
def request(number,method,params,timeout=25):
    global pending_output
    proc.stdin.write(json.dumps(dict(id=number,method=method,params=params))+'\n');proc.stdin.flush()
    deadline = time.monotonic()+timeout
    while time.monotonic()<deadline:
        # Drain complete frames before waiting; TextIOWrapper can prefetch replies
        # invisible to select(). Decode only after a whole byte frame arrives.
        if b'\n' not in pending_output:
            if not selector.select(max(0,deadline-time.monotonic())): break
            chunk = os.read(proc.stdout.fileno(),65536)
            if not chunk: raise RuntimeError('app-server exited')
            pending_output += chunk
            continue
        line,pending_output = pending_output.split(b'\n',1)
        msg = json.loads(line);messages.append(msg)
        if msg.get('id')==number:
            if 'error' in msg: raise RuntimeError(msg['error'])
            return msg['result']
    raise TimeoutError(method)
try:
    init = request(1,'initialize',{'clientInfo':{'name':'heritage-catalog-check','version':'1'},'capabilities':{'experimentalApi':True}})
    proc.stdin.write('{"method":"initialized"}\n');proc.stdin.flush()
    conf = request(2,'config/read',{'cwd':str(project),'includeLayers':True})
    skills = request(3,'skills/list',{'cwds':[str(project)],'forceReload':True})
    (P/'config-read.json').write_text(json.dumps(conf,indent=2)+'\n')
    (P/'skills-list.json').write_text(json.dumps(skills,indent=2)+'\n')
    entries = conf['config']['agents']
    for item in manifest:
        entry = entries[item['agent']]
        candidate = Path(entry['config_file'])
        if not candidate.is_absolute(): candidate = project/'.codex'/candidate
        assert candidate.is_file(), candidate
    discovered = [s['name'] for g in skills.get('data',[]) for s in g.get('skills',[]) if str(project/'.agents/skills') in str(s.get('path',''))]
    errors = [e for g in skills.get('data',[]) for e in g.get('errors',[])]
    assert len(discovered)==30 and not errors,(len(discovered),errors)
    summary = dict(runtime=init.get('userAgent'),registered_new_agents=len(manifest),discovered_project_skills=len(discovered),new_gateways_discovered=sorted(set(m['gateway'] for m in manifest)&set(discovered)),skill_errors=errors,native_agent_dispatch_tested=False)
    (P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
finally:
    proc.stdin.close()
    try: proc.wait(timeout=5)
    except subprocess.TimeoutExpired: proc.terminate();proc.wait(timeout=5)
    selector.close();log.close()
    (P/'rpc-messages.json').write_text(json.dumps(messages,indent=2)+'\n')
