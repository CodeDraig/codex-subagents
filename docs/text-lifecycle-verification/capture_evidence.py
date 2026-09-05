import ast,hashlib,json,re,shutil,tomllib,zipfile
from pathlib import Path
R=Path('/srv/data/code/codex-subagents');P=Path('/tmp/text-lifecycle-20260905');D=R/'docs/text-lifecycle-verification';project=P/'project'
cases=json.loads((P/'fixtures.json').read_text())
acceptance={
'planning':'Produced a four-receipt brief and drafting handoff; explicitly separated the plan from text not yet drafted.',
'fiction':'Delivered the complete four-receipt story from the actual planning output, without an outside narrator in the story; 248 whitespace-delimited words.',
'nonfiction':'Delivered 272 words excluding title; retained 18/30, entrance recruitment, one Saturday, comparison limits, and a labeled hypothetical example. No unsupported recency or inference about omitted study questions remains.',
'essay':'Delivered a 232-word complete reflective essay using supplied memories, recurring repair/listening material, and an open ending.',
'poetry':'Delivered exactly eight free-verse lines, each beginning Still; retained the refrain and changed the final significance of waiting.',
'drama':'Delivered a complete 268-word scene with Mina, Sol, one table, coherent key movement, and an altered final relationship; timing remained approximate.',
'professional':'Delivered a complete proposal memo preserving all supplied facts and no approved staffing/budget commitment. The final run executed wc -w and accurately reported 160 words including headers.',
'academic':'Delivered a complete abstract retaining 24 volunteers, two weeks, self-report, 3 minutes/day, no control group, and absent uncertainty information. The final run executed wc -w and accurately reported 178 words excluding metadata.',
'revision':'Applied the requested date discrepancy to the actual preceding fiction draft; wrote the complete four-receipt revision with a responsive final receipt and unresolved memory origin.',
'feedback':'Wrote the complete revised passage; retained all three I remember openings, shortened the explanation, and accounted for the accepted and declined comments.',
'rhetoric':'Delivered the revised passage with all three We waited openings and the clerk\'s uncertainty preserved.',
'continuity':'Reported the paired Tuesday/Wednesday bridge contradiction; distinguished an identified lie and explicitly limited conclusions to supplied excerpts.',
'readers':'Located undefined concepts and action-order problems; separated predicted effects from absent reader-study evidence and did not modify source files.',
'adaptation':'Delivered a complete community notice within the 90-130-word range, preserving sampling limits and the unapproved extended-hours proposal without adding unsupported survey duration or recency.',
'translation':'Translated both source sentences with singular they, preserved negation and might, and retained the two-day interval.',
 'translation_review':'Compared the actual preceding translation and a deliberately faulty alternative; accepted defensible A and located B\'s gender, negation, modality/reported-speech, and time-interval errors without applying changes.',
'scholarship':'Wrote witness descriptions, diplomatic transcriptions, collation, edited text, apparatus, and policy. Preserved A\'s unreadable span and historical spelling, distinguished B variants, and made no physical-source or stemma claim.',
'proof':'Returned exact public-access and note-number corrections, identified the missed prior correction, and left visual proof coverage unverified.',
'format':'Inspected the actual EPUB ZIP/XML and found the seeded missing ending anchor. Also reported missing XHTML language attributes. Distinguished those checks from unavailable EPUBCheck, rendering, and accessibility certification.',
'index':'Wrote a provisional concept index with only supplied anchors, substantive headings, and resolving see-references; did not invent print pages.',
'submission':'Wrote complete separate cover note and nine-word biography. Preserved residence and occupation as separate facts, did not invent credentials, and left the absent anonymous story and metadata unverified.',
'edition':'Wrote the corrected source and log. Independent comparison confirms that the sole source change is table-label 2018 to 2019; caption/discussion agree and unavailable PDF/EPUB updates remain pending.'}
fail_notes={
'adaptation-before-measured-count':'Length/reporting failure: after the qualifier correction, the next notice was 83 whitespace-delimited words including title while claiming 91; this missed the 90-word minimum. Added measured hard-limit checks and reran.',
'adaptation-before-qualifier-check':'Content failure: the notice called the survey brief although no duration was supplied. Added a factual-qualifier check and reran.',
'nonfiction-before-evidence-rule':'Content failure: inferred that the underlying survey did not ask a question from absence of details in the packet. Added an explicit missing-packet-evidence rule and reran.',
'nonfiction-before-recency-check':'Content failure: described an undated survey as recent. Added unsupported-specificity and relationship checks and reran.',
'drama-before-action-check':'Content failure: a direction moved the table and then said it did not move. Added attempted-versus-completed-action checks and reran.',
'drama-completed-event-no-response-timeout':'Harness/runtime failure: a final agent message and turn.completed event exist, but the CLI did not create its response file before the 180-second process timeout. Preserved the final event, inspected output, and reran; not accepted as a clean run.',
'submission-before-fact-relationship-check':'Content failure: connective wording inferred employment in the author\'s city of residence. Added a check against relationships not supplied and reran.',
'nonfiction-network-delay':'Network/environment failure: repeated DNS/connection errors, no completed model turn, 300-second timeout. Retained and reran with network access.',
'submission-network-delay':'Network/environment failure: repeated DNS/connection errors, no completed model turn, 300-second timeout. Retained and reran with network access.',
 'translation_review-network-delay':'Interrupted attempt after sustained DNS/connection delay; connection had recovered and source reading had begun, but no completed review existed. Retained and reran. The interruption was not a content failure.',
'professional-before-measured-count':'Reporting failure: draft was within the 140-190 word limit, but claimed 158 words; independent whitespace counting found 149 including headers. Added measured-count guidance and reran.',
'academic-before-measured-count':'Reporting failure: abstract was within the 150-200 word limit, but claimed 159 words; independent whitespace counting found 173. Added measured-count guidance and reran.'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save_json(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def inspect_run(src,dest):
 es=[json.loads(line) for line in (src/'events.jsonl').read_text().splitlines() if line.strip()]
 cmds=[e['item'] for e in es if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution']
 data={'status':json.loads((src/'status.json').read_text()),'prompt':(src/'prompt.txt').read_text(),'invocation':json.loads((src/'invocation.json').read_text()),'turn_completed_events':sum(e['type']=='turn.completed' for e in es),'error_events':[e for e in es if e['type'] in ['error','turn.failed']],'commands':[{'command':c['command'],'exit_code':c['exit_code']} for c in cmds],'raw_evidence':[{'path':str(src/n),'sha256':sha(src/n)} for n in ['events.jsonl','stderr']]}
 dest.mkdir(parents=True,exist_ok=True)
 response=src/'response.md'
 if response.exists():
  shutil.copy2(response,dest/'response.md');data['response_sha256']=sha(response)
 elif data['turn_completed_events']:
  finals=[e['item']['text'] for e in es if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='agent_message']
  if finals:(dest/'completion-event.md').write_text(finals[-1]);data['completion_event_sha256']=sha(dest/'completion-event.md')
 return data
results=[]
for name,c in cases.items():
 src=P/'live'/name;dest=D/'cases'/name;record=inspect_run(src,dest)
 assert record['status']['exit']==0 and record['turn_completed_events']==1 and 'response_sha256' in record,name
 record.update({'case':name,'acceptance':'pass','manual_acceptance_evidence':acceptance[name],'fixture':c,'runtime_scope':'Ephemeral single Codex invocation using the named template settings; delegation disabled.' if c['agent'] else 'Direct gateway workflow invocation on Terra/high; no individual specialist-agent runtime claim.'})
 save_json(dest/'run.json',record)
 results.append({'case':name,'agent':c['agent'],'skill':c['skill'],'mode':c['mode'],'exit':0,'seconds':record['status']['seconds'],'acceptance':'pass','evidence':f'cases/{name}/run.json','response':f'cases/{name}/response.md','note':acceptance[name],'nonzero_commands':sum(x['exit_code']!=0 for x in record['commands']),'connection_error_events':len(record['error_events'])})
failed=[]
for name,note in fail_notes.items():
 record=inspect_run(P/'live/failed-attempts'/name,D/'failed-attempts'/name);record['disposition']=note
 save_json(D/'failed-attempts'/name/'run.json',record);failed.append({'attempt':name,'status':record['status'],'disposition':note,'evidence':f'failed-attempts/{name}/run.json'})
# Verify original textual fixtures directly against literal generator inputs; never rerun its mutations.
checked_inputs=[]
for n in ast.walk(ast.parse((P/'fixtures.py').read_text())):
 if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='write_text' and isinstance(n.func.value,ast.BinOp) and isinstance(n.func.value.left,ast.Name) and n.func.value.left.id=='I':
  name=ast.literal_eval(n.func.value.right);expected=ast.literal_eval(n.args[0]);assert (project/'inputs'/name).read_text()==expected,name;checked_inputs.append(name)
with zipfile.ZipFile(project/'inputs/book.epub') as z:
 assert 'chapter.xhtml#ending' in z.read('EPUB/nav.xhtml').decode() and 'id="ending"' not in z.read('EPUB/chapter.xhtml').decode()
for parent,name in [(project/'inputs','inputs'),(project/'outputs','outputs')]:
 (D/name).mkdir(exist_ok=True)
 for f in sorted(parent.iterdir()):
  if f.is_file():shutil.copy2(f,D/name/f.name)
# Preserve artifacts displaced during failed attempts separately.
failed_art=P/'live/failed-attempts/artifacts'
if failed_art.exists():
 shutil.copytree(failed_art,D/'failed-attempts/artifacts',dirs_exist_ok=True)
checks={}
for name,start,end,lower,upper in [('fiction','## Draft','## Craft Decisions',220,320),('essay','## Essay','## Form And Voice Notes',220,300),('drama','## Dramatic Text','## Character And Action Notes',220,320),('professional','## Draft','Exact word count:',140,190),('academic','## Manuscript Draft','Exact word count:',150,200),('adaptation','## Adapted Text','## Source To Target Map',90,130)]:
 s=(P/'live'/name/'response.md').read_text();span=s.split(start,1)[1].split(end,1)[0].strip();span=re.sub(r'(?m)^#{1,6} +','',span);count=len(span.split());assert lower<=count<=upper,(name,count)
 checks[name]={'word_count':count,'method':'Python str.split over delivered artifact span, excluding Markdown heading markers; headers/title retained where supplied','range':[lower,upper]}
assert checks['professional']['word_count']==160 and checks['academic']['word_count']==178
s=(P/'live/poetry/response.md').read_text();poem=re.split(r'(?m)^#{0,2} ?Poem\s*$',s,maxsplit=1)[1];poem=re.split(r'(?m)^#{0,2} ?Form And Sound Notes\s*$',poem,maxsplit=1)[0];lines=[x.strip() for x in poem.splitlines() if x.strip()];assert len(lines)==8 and all(x.startswith('Still') for x in lines)
checks['poetry']={'lines':8,'all_start_with':'Still'}
old=(project/'inputs/edition-source.md').read_text();new=(project/'outputs/edition-source-corrected.md').read_text();assert new==old.replace('Table label: 2018 respondents','Table label: 2019 respondents')
assert (project/'outputs/feedback-revision.md').read_text().count('I remember')==3
assert len((project/'outputs/rowan-hale-biography.md').read_text().split())==9
copies=0
for source,target in [(R/'SKILLS',project/'.agents/skills'),(R/'AGENTS/openai',project/'.codex/agents')]:
 for f in source.rglob('*'):
  if f.is_file():assert f.read_bytes()==(target/f.relative_to(source)).read_bytes(),f;copies+=1
save_json(D/'live-results.json',{'date':'2026-09-05','cli_version':'0.153.4','cases':results,'failed_attempts':failed,'independent_artifact_checks':checks,'input_integrity':{'original_text_fixtures_match_generator':checked_inputs,'seeded_epub_target_verified':True},'guidance_integrity':{'files_matching_final_catalog':copies},'limits':['Representative bounded fixtures, not full-length-book or every-agent runtime coverage.','Feedback integration and scholarship were direct gateway tests; scholarship exercised four workflows in one invocation, not four independently spawned agents.','CLI turns completed, but some recovered nonzero tool commands and connection retries occurred; raw evidence and compact command outcomes are retained.','Most runs predate the later router link-resolution sentence. Nonfiction, submission, translation review, professional, academic, and adaptation exercised the clarified router; no claim that every role was rerun for that navigation clarification.','No publication, submission, global installation, real external-document transfer, or changes to the host Codex installation.']})
# Store reproducible source and verification helpers without bundling binaries, account data, or raw transient stores.
for name in ['fixtures.py','fixtures.json','run_live.py','check_catalog.py','runtime_check.py']:
 shutil.copy2(P/name,D/name)
for name in ['catalog-check.json','config-read.json','skills-list.json','rpc-messages.json']:
 shutil.copy2(P/name,D/name)
print('Retained',len(results),'passing cases and',len(failed),'prior attempts; guidance copies match:',copies)
print('Independent artifact checks:',json.dumps(checks))
