# Constrained AI Stack — Setup Checklist

## Before you run
- [ ] Docker Desktop is installed and the daemon is running
- [ ] Docker Compose v2+ is installed
- [ ] Host has 3.5 GiB RAM or more
- [ ] `.env` is copied from `.env.example` and verified

## First run
- [ ] `docker compose config --services` runs without errors
- [ ] `docker compose up -d` starts all services
- [ ] `curl http://localhost:8000/health` returns `{"status":"ok"}`
- [ ] `curl http://localhost:9090/metrics` returns Prometheus metrics output
- [ ] Health checks pass in `docker compose ps`

## Verification
- [ ] `scripts/verify-install.sh` passes
- [ ] `scripts/memory-shield.sh` shows headroom is acceptable

## Support
- [ ] Community support: open a GitHub issue
- [ ] Starter Support: purchase via the product listing for setup review
- [ ] Consulting: message via LinkedIn

## Notes

- If a deployment fails, do not ship customer-facing code until you can reproduce the failure in staging or a throwaway clone.
- If the stack runs locally but not on a buyer environment, capture `/etc/host` state and container version information before publishing.