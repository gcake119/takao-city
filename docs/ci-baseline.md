# Repository CI baseline

Repository: gcake119/takao-city. Coordination: https://github.com/gcake119/takao-city

The user authorized main and CI initialization for the empty application repositories, with application delivery accepted separately. This check verifies the repository ownership metadata, a documentation/infrastructure-only tracked-file boundary, private-data ignores, local README links, and exact Git SHA/tree. It is not an application build/test, OCR quality, API/database verification, deployment or human acceptance.

The baseline intentionally fails if application files are added without replacing this infrastructure-only gate with real application CI. No placeholder application pass is emitted. CI evidence explicitly says applicationVerification=not-implemented-not-tested.

The dedicated Mint runner reuses ci-runner UID995/GID984, rootless Docker and shared CPU300%/MemoryHigh16GiB/Max20GiB/Tasks4096. Light admission remains one slot with a900-second wait; all original heavy/light/Docker lock inodes are preserved. No sudo/rootful/backup permissions or APT packages are added. Fork verification uses hosted Ubuntu24.04.

For an initially empty repository, the first main commit contains only README and ignore rules; this unavoidable bootstrap is explicitly authorized. The CI baseline is then proposed through a separate branch/PR and ordinarily merged only after its checks and independent review. The existing coordination README and plans are preserved; this repo has no product runtime.

Platform results, real-main evidence and central closeout remain pending. No application deployment, GHCR publication, provider call or Spectra archive is authorized by this baseline.
