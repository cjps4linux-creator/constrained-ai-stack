# Constrained AI Stack — Listing Assets

## Product Name
Constrained AI Stack

## One-Line Pitch
Production AI infrastructure — APIs, workers, queues, and observability — on constrained hardware.

## Subtitle / Tagline
Full AI stack, zero cloud spend, zero dependency on specialized hardware.

## Who It's For
- Low-resource environments and retro/off-market hardware
- Engineers shipping on 3–4 GiB RAM without cloud spend
- Privacy-sensitive deployments that cannot outbound model calls
- Budget production stacks that must remain auditable and portable

## What They Get
### Self-Hosted Download
- `docker-compose.yml` — 6-service stack with health checks
- `api/` — FastAPI app with `/health`, structured config, env-driven settings
- `worker/` — Celery worker with `healthcheck` task and config
- `scripts/` — `verify-install.sh`, `memory-shield.sh`, `worker-run.sh`
- `docs/` — `constraints.md`, `troubleshooting.md`, `pricing.md`, `setup-checklist.md`
- `monitoring/` — Prometheus config
- MIT LICENSE

## Formats
- Docker Compose deployment
- Local no-Docker verification scripts
- Markdown runbooks

## Pricing
- Self-hosted download: free
- Starter Support: $97
- Consulting: custom

## Problem It Solves
Most stack guides require 8+ GiB RAM, cloud inference, or expensive GPU hosts. Buyers get a stack they can run on a 3.8 GB RAM PS4-class host with self-hosted persistence and observability.

## Outcomes
- Baseline stack under 2 GiB RAM
- FastAPI `/health` and `/metrics` exposed
- Async task queue separated from API process
- Verified install path without needing Docker locally to validate config
- One-hour setup review for Starter Support

## Offer Terms
- Community: source-available, self-hosted
- Starter Support: one-hour setup review, config audit, runbook
- Consulting: architecture review, implementation, training
- 50% upfront, 50% on delivery
- Scope freeze required before start
- Rush add-ons priced separately

## Channel Notes
- GitHub repo stays private until explicit approval
- Starter Support sold via LinkedIn DM
- Consulting scoped per request

## Sample Checkout Copy
```
Package: Constrained AI Stack — Starter Support $97
Includes:
 - Cloned private repo access
 - 1-hour live setup review over screen share
 - Config audit + runbook
Payment: 50% upfront via Stripe
Delivery: repo access + review scheduled within 24 hours
```

## Sample DM Opening
```
I built a constrained AI stack that runs a full FastAPI + Celery + PostgreSQL + Prometheus setup on a 3.8 GB host for under $0/month cloud spend.
If you want the repo + docs, share a private GitHub username and I’ll add access.
If you’re running into setup edge cases, the Starter Support review is $97 with a fixed runbook.
```

## No-Go Examples
- Public repo release without buyer qualification path
- Support tier sold without a written scope or deliverable list
- Promising SLA or uptime for self-hosted stack

## Author
Conrad CJ Wilson
LinkedIn: https://www.linkedin.com/in/conradcjwilson
GitHub: https://github.com/cjps4linux-creator
