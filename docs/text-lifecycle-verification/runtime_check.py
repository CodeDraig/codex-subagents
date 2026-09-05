import json, os, selectors, subprocess, time
from pathlib import Path
p=Path(__file__).parent
project=p/'project'
exe=p/'bin/codex-x86_64-unknown-linux-musl'
env=dict(os.environ,CODEX_HOME=str(p/'home'))
log=(p/'app-server.stderr').open('w')
proc=subprocess.Popen([str(exe),'--strict-config','-C',str(project),'app-server','--stdio'],env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=log,text=True,bufsize=1)
sel=selectors.DefaultSelector();sel.register(proc.stdout,selectors.EVENT_READ)
messages=[]
def send(data):
 proc.stdin.write(json.dumps(data)+'\n');proc.stdin.flush()
def request(i,method,params):
 send({'id':i,'method':method,'params':params})
 deadline=time.monotonic()+20
 while time.monotonic()<deadline:
  if not sel.select(max(0,deadline-time.monotonic())):break
  line=proc.stdout.readline()
  if not line:raise RuntimeError('Server exited')
  msg=json.loads(line);messages.append(msg)
  if msg.get('id')==i:
   if 'error' in msg:raise RuntimeError(msg['error'])
   return msg['result']
 raise TimeoutError(method)
try:
 init=request(1,'initialize',{'clientInfo':{'name':'catalog-verification','version':'1'},'capabilities':{'experimentalApi':True}})
 send({'method':'initialized'})
 conf=request(2,'config/read',{'cwd':str(project),'includeLayers':True})
 skills=request(3,'skills/list',{'cwds':[str(project)],'forceReload':True})
 (p/'config-read.json').write_text(json.dumps(conf,indent=2)+'\n')
 (p/'skills-list.json').write_text(json.dumps(skills,indent=2)+'\n')
 print('Initialize:',init.get('userAgent','ok'))
 print('Agent settings:',json.dumps(conf['config'].get('agents')))
 print('Layer count:',len(conf.get('layers',[])))
 print('Skill response keys:',list(skills))
 for group in skills.get('data',[]):
  local=[s for s in group.get('skills',[]) if str(project/'.agents/skills') in str(s.get('path',''))]
  print('Local skills:',len(local),'errors:',group.get('errors',[]))
  assert len(local)==26
  assert not group.get('errors')
finally:
 proc.stdin.close()
 try:proc.wait(timeout=5)
 except subprocess.TimeoutExpired:proc.terminate();proc.wait(timeout=5)
 log.close();sel.close()
 (p/'rpc-messages.json').write_text(json.dumps(messages,indent=2)+'\n')
