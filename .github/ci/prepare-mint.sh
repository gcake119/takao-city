#!/usr/bin/env bash
set -euo pipefail
case ${RUNNER_ENVIRONMENT:-} in
  github-hosted) exit 0 ;;
  self-hosted) ;;
  *) echo CI_RUNNER_ENVIRONMENT_INVALID >&2; exit 1 ;;
esac
[[ $(id -u) == 995 && ${GITHUB_REPOSITORY:-} == gcake119/takao-city && ${RUNNER_NAME:-} == mint-takao-city ]] || exit 1
[[ ${DOCKER_HOST:-} == unix:///run/user/995/docker.sock && -S /run/user/995/docker.sock ]] || exit 1
/usr/bin/docker info --format '{{range .SecurityOptions}}{{println .}}{{end}}' | grep -Fx name=rootless >/dev/null
for tool in /usr/local/bin/ci-resource-slot /usr/local/bin/ci-build-lock; do
  [[ -x $tool && ! -w $tool && $(stat -c '%u:%a' "$tool") == 0:755 ]] || exit 1
done
for protected in /home/yi-chun /media/yi-chun/DATA_2TB /media/yi-chun/BACKUP_4T1; do
  [[ ! -r $protected && ! -w $protected && ! -x $protected ]] || exit 1
done
[[ ! -w /var/run/docker.sock ]] || exit 1
python3 - <<'CHECK'
from pathlib import Path
root=Path('/sys/fs/cgroup/user.slice/user-995.slice')
q,p=(root/'cpu.max').read_text().split();assert int(q)/int(p)==3
for file,value in [('memory.high',16*1024**3),('memory.max',20*1024**3),('pids.max',4096)]:assert int((root/file).read_text())==value
assert '/user.slice/user-995.slice/' in Path('/proc/self/cgroup').read_text()
print('Shared CPU300%, MemoryHigh16GiB/Max20GiB, Tasks4096 verified')
CHECK
# Read fixed existing lock files; never replace or unlink their inode.
for lock in docker-build heavy light; do
  path=/var/lib/ci-build-lock/$lock.lock
  [[ -f $path && ! -L $path && -r $path && ! -w $path && $(stat -c '%u:%g:%a' "$path") == "0:$(id -g):640" ]] || exit 1
  stat -c 'Shared lock %n inode=%i owner=%u:%g mode=%a' "$path"
done
if [[ -n ${GITHUB_ENV:-} ]]; then
  echo RUNNER_TOOL_CACHE=/var/lib/github-runner/toolcache >> "$GITHUB_ENV"
  echo AGENT_TOOLSDIRECTORY=/var/lib/github-runner/toolcache >> "$GITHUB_ENV"
fi
