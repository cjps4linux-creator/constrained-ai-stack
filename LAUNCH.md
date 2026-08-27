# Constrained AI Stack — Launch Readiness

**Date:** 2026-08-27
**Owner:** Conrad CJ Wilson
**Repo:** cjps4linux-creator/constrained-ai-stack
**Status:** Production-ready infrastructure prototype

---

## Readiness Snapshot

| Gate | Status | Evidence |
|---|---|---|
| CI passing | Pending | GitHub Actions workflow not yet present |
| Tests passing | Pending | No automated test suite; verification via `docker compose config` |
| Security scan | Pending | SECURITY.md in place |
| README complete | Complete | Architecture, resource budgets, ADRs, honest limitations |
| LICENSE | Complete | MIT — Conrad CJ Wilson |
| Docker build | Complete | Docker Compose validated with `docker compose config` |
| Documentation | Complete | Constraints doc, troubleshooting guide, monitoring config |

---

## Requirements

- Docker Compose v2+
- 3.5 GiB RAM minimum
- Linux host; tested on CachyOS/Arch
- 10 GiB disk

---

## Known Gaps

- No GitHub Actions CI workflow; validation is manual via `docker compose config` and `scripts/verify-install.sh`
- No automated test suite; production readiness is validated through infrastructure checks rather than application tests
- Prometheus retention is 7 days; longer retention requires additional disk and memory
- Memory shield script validates RAM at startup but does not continuously monitor resource usage during operation

---

## Actions Required Before Production

1. Add GitHub Actions CI workflow with lint, test, and security scan jobs
2. Add automated test suite for API endpoints and worker behavior
3. Enable GitHub secret scanning and vulnerability alerts
4. Configure branch protection with required status checks
5. Adjust PostgreSQL shared buffers and Prometheus retention for production data volumes

---

## Contact

Conrad CJ Wilson — conradcjwilson0@gmail.com
