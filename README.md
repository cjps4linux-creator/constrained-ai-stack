# Constrained AI Stack

Production AI infrastructure for low-resource environments — run a full AI platform on hardware with limited RAM and no cloud dependency.

Built by Conrad CJ Wilson.

## What It Demonstrates

| Capability | Implementation |
|---|---|
| Full-stack AI platform | APIs, workers, queues, vector search, and observability in one stack |
| Resource-constrained operation | Explicit memory budgets per service for 3.5 GiB RAM hosts |
| Zero-cloud operation | No outbound model inference or API dependencies required |
| Production observability | Prometheus metrics, structured logging, health checks |
| Infrastructure as code | Docker Compose with explicit resource limits and restart policies |
| Pre-flight validation | Memory shield script prevents startup on undersized hosts |
| Portability | Identical configuration across dev/staging/prod |

## Stack

| Component | Purpose |
|---|---|
| FastAPI | AI service APIs with health checks and `/metrics` |
| Celery + Redis | Async task queue for pipelines and agents |
| PostgreSQL + pgvector | Structured data and semantic search |
| Prometheus + node-exporter | Metrics and resource monitoring |
| Docker Compose | Service orchestration with health checks and memory limits |
| Memory shield | Pre-flight RAM validation before startup |

## Architecture

```
                    ┌──────────────┐
                    │   FastAPI    │
                    │    API       │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌─────────┐ ┌──────────┐
        │  Celery  │ │ Redis   │ │Postgres  │
        │  Worker  │ │ Broker  │ │+ pgvector│
        └──────────┘ └─────────┘ └──────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌─────────┐ ┌──────────┐
        │Prometheus│ │Node     │ │Health    │
        │          │ │Exporter │ │Shield    │
        └──────────┘ └─────────┘ └──────────┘
```

## Requirements

- Docker Compose v2+
- 3.5 GiB RAM minimum
- Linux host; tested on CachyOS/Arch
- 10 GiB disk

## Quick Start

```bash
git clone https://github.com/cjps4linux-creator/constrained-ai-stack.git
cd constrained-ai-stack

cp .env.example .env
docker compose up -d
```

Verify the installation:

```bash
curl http://localhost:8000/health
curl http://localhost:9090/metrics
```

## Resource Budgets

| Service | RAM Target | Notes |
|---|---|---|
| postgres | 512 MiB | Shared buffers tuned for 4 GiB host |
| redis | 128 MiB | Maxmemory policy set |
| api | 384 MiB | Uvicorn workers = 1 |
| worker | 512 MiB | Concurrency = 2 |
| prometheus | 256 MiB | Retention = 7 days |
| node-exporter | 64 MiB | Minimal scrape config |

Total target: ~1.8 GiB baseline, leaving headroom for batch workloads and OS overhead.

## What Is Included

- `docker-compose.yml` — all services with health checks and memory limits
- `.env.example` — configuration template
- `monitoring/prometheus.yml` — scrape configurations
- `scripts/memory-shield.sh` — pre-flight RAM validation
- `docs/constraints.md` — design decisions and failure modes
- `docs/troubleshooting.md` — common issues on constrained hosts

## Architecture Decision Records

### ADR-001: Docker Compose Over Kubernetes

Docker Compose was selected over Kubernetes because the target environment (3.5 GiB RAM, consumer CPU) cannot comfortably run a Kubernetes control plane alongside application workloads. Compose provides sufficient orchestration capability with lower resource overhead.

### ADR-002: Explicit Memory Limits Per Service

Each service has an explicit memory limit in the Compose file. This prevents a single service from consuming all available RAM and starving others. The limits are tuned for a 4 GiB host and documented in the resource budgets table.

### ADR-003: Memory Shield Pre-Flight Check

A shell script validates available RAM before starting the stack. If the host has less than the required 3.5 GiB, the script exits with a clear message rather than allowing degraded operation.

### ADR-004: PostgreSQL + pgvector Over Separate Vector Database

pgvector inside PostgreSQL eliminates the need for a separate vector database service. This reduces the service count, memory footprint, and operational complexity while maintaining vector search capability for RAG workloads.

## Why This Instead of the Cloud

- No monthly API, GPU, or infrastructure spend.
- No vendor data-policy risk: data stays on host.
- Constraints force simpler, auditable architecture.
- Fully offline operation; no outbound model inference is required by the stack itself.
- Portability: identical configuration across dev/staging/prod on the same machine.

## Verified Status

- `docker compose config --services` validates: `postgres`, `redis`, `api`, `worker`, `prometheus`, `node-exporter`
- Runtime verification remains environment-dependent; `scripts/verify-install.sh` checks compose validity and Docker availability

## Honest Limitations

- Target host is 3.5 GiB RAM. Running additional services beyond those defined in the Compose file may cause OOM conditions.
- PostgreSQL shared buffers are tuned for a 4 GiB host. Larger datasets or higher concurrency may require buffer adjustments.
- The memory shield script is a best-effort check; it validates available RAM at startup but does not continuously monitor resource usage during operation.
- Prometheus retention is 7 days. Longer retention requires additional disk space and memory.

## Current State

Production-ready infrastructure prototype. All services are defined with health checks, memory limits, and restart policies. The stack has been validated with `docker compose config` and is ready for deployment on compliant hosts.

## License

MIT — use, modify, and ship freely.

**Author:** Conrad CJ Wilson
**GitHub:** https://github.com/cjps4linux-creator
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
