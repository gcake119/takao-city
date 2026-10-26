import hashlib,json,os,re,subprocess,urllib.parse
from pathlib import Path

def git(*args):return subprocess.check_output(['git',*args],text=True).strip()
root=Path.cwd().resolve();config=json.loads(Path('.ci/repository-baseline.json').read_text());repo=os.environ['GITHUB_REPOSITORY'];assert config['schemaVersion']==1 and config['repository']==repo
roles={'takao-city':'coordination','takao-city-frontend':'frontend','takao-document-engine':'document-engine','takao-city-backend':'backend'}
name=repo.removeprefix('gcake119/');assert repo.startswith('gcake119/') and roles[name]==config['role']
assert config['coordination']=='https://github.com/gcake119/takao-city'
assert config['verificationScope']=='repository-baseline-only' and config['applicationVerification']=='not-implemented-not-tested'
assert config['applicationStatus']==('not-applicable-documentation-only' if name=='takao-city' else 'not-initialized')
files=git('ls-files','-z').split('\0');files=[x for x in files if x]
for file in files:
 p=Path(file);assert not p.is_absolute() and '..' not in p.parts and not p.is_symlink(),'UNSAFE_TRACKED_PATH'
 assert file in ('README.md','.gitignore','LICENSE') or file.startswith(('.github/','.ci/','docs/')),'APPLICATION_CI_REQUIRED: '+file
 assert p.name not in ('.env','.env.local') and not re.search(r'\.(db|sqlite\d*|pem|key)$',file,re.I),'PRIVATE_DATA_FORBIDDEN'
assert 'README.md' in files and '.gitignore' in files
ignore=Path('.gitignore').read_text()
for pattern in ('.env','*.db','*.sqlite*','node_modules/','dist/','data/'):
 assert pattern in ignore.splitlines(),'MISSING_PRIVATE_DATA_IGNORE: '+pattern
readme=Path('README.md').read_text();assert config['coordination'] in readme
local_links=0
for raw in re.findall(r'\]\(([^)]+)\)',readme):
 target=raw.strip().strip('<>');parsed=urllib.parse.urlsplit(target)
 if parsed.scheme or target.startswith('#'):continue
 relative=urllib.parse.unquote(parsed.path)
 if not relative:continue
 path=(root/relative).resolve();assert path.is_relative_to(root) and path.exists(),'BROKEN_OR_ESCAPING_README_LINK';local_links+=1
sha=git('rev-parse','HEAD');assert sha==os.environ['GITHUB_SHA'];subprocess.check_call(['git','diff','--quiet']);subprocess.check_call(['git','diff','--cached','--quiet'])
receipt={'sourceSha':sha,'sourceTree':git('rev-parse','HEAD^{tree}'),'repository':repo,'runner':os.environ['RUNNER_NAME'],'scope':'repository-baseline-only','role':config['role'],'trackedFiles':len(files),'readmeLocalLinks':local_links,'ownershipAndPrivacyBaseline':'passed','applicationVerification':'not-implemented-not-tested','deployment':'not-run','humanAcceptance':'not-run'}
Path('ci-verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'baseline':'passed','applicationVerification':receipt['applicationVerification'],'localLinks':local_links}))
