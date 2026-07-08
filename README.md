# Constrained AI Stack

Production AI infrastructure for low-resource environments.

Run a full AI platform — APIs, workers, queues, vector search, and observability — on hardware with limited RAM and no cloud dependency.

| | |
|---|---|
| **Target environment** | 3–4 GiB RAM, consumer CPU, Linux |
| **Cost** | $0/month after hardware |
| **Use case** | prototyping, edge deployment, budget-constrained production, learning AI ops |

---

## What This Gives You

| Component | Purpose |
|-----------|---------|
| FastAPI backend | AI service APIs with health checks and `/metrics` |
| Celery + Redis | Async task queue for pipelines and agents |
| PostgreSQL + pgvector | Structured data and semantic search |
| Prometheus + node-exporter | Metrics and resource monitoring |
| Health checks | Service-level monitoring with restart policies |
| Memory shield | Pre-flight RAM check before startup |
| Compose profile | One-command startup with explicit resource limits |

---

## Why this instead of the cloud

- No monthly API/GPU/infrastructure spend.
- No vendor data-policy risk; data stays on host.
- Constraints force simpler, auditable architecture.
- Full offline operation; no outbound model inference required by the stack itself.
- Portability: identical config across dev/staging/prod on the same machine.

---

## Requirements

- Docker Compose v2+
- 3.5+ GiB RAM
- Linux host; tested on CachyOS/Arch
- 10+ GiB disk

---

## Quick Start

```bash
git clone https://github.com/cjps4linux-creator/constrained-ai-stack.git
cd constrained-ai-stack
cp .env.example .env
docker compose up -d
```

Verify:
```bash
curl http://localhost:8000/health
curl http://localhost:9090/metrics
```

---

## Resource Budgets

| Service | RAM Target | Notes |
|---------|-----------|-------|
| postgres | 512 MiB | Shared buffers tuned for 4GB host |
| redis | 128 MiB | Maxmemory policy set |
| api | 384 MiB | Uvicorn workers = 1 |
| worker | 512 MiB | Concurrency = 2 |
| prometheus | 256 MiB | Retention = 7 days |
| node-exporter | 64 MiB | Minimal scrape config |

Total target: ~1.8 GiB baseline. Headroom for batch jobs.

---

## What’s Included

- `docker-compose.yml` — all services with health checks and memory limits
- `.env.example` — config template
- `monitoring/prometheus.yml` — scrape configs
- `scripts/memory-shield.sh` — pre-flight RAM check
- `docs/constraints.md` — design decisions and failure modes
- `docs/troubleshooting.md` — common issues on constrained hosts

---

## Support

| Tier | Price | Deliverables |
|------|-------|--------------|
| Community | Free | Source-available, self-hosted |
| Starter Support | $97 | One-hour setup review, config audit, runbook |
| Consulting | Custom | Architecture review, implementation, training |

Terms: 50% upfront, 50% on delivery. Scope freeze required before start. Rush add-ons priced separately.

---

## Verified Status

- `docker compose config --services` validates: `postgres`, `redis`, `api`, `worker`, `prometheus`, `node-exporter`
- Runtime verification remains environment-dependent; `scripts/verify-install.sh` checks compose validity and Docker availability

---

## License

MIT — use, modify, and ship freely.  
**Author:** Conrad CJ Wilson  
**GitHub:** https://github.com/cjps4linux-creator  
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
