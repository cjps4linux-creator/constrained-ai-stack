# Constrained AI Stack — Verification Record

## Local Verification
- `docker compose config --services` validates: postgres, redis, api, worker, prometheus, node-exporter
- Runtime verification remains environment-dependent
- `scripts/verify-install.sh` checks compose validity and Docker availability

## Assumptions
- 3.5 GiB RAM target host
- Linux or WSL2 backend
- Ports 8000, 5432, 6379, 9090 available

## Gaps
- No pytest suite present in repo; product validation depends on runtime smoke tests
