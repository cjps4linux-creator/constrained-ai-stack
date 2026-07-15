# Constrained AI Stack — Launch Documentation

## Launch Readiness Snapshot
- Repo: `constrained-ai-stack`
- Default branch: `master`
- License: MIT
- Purchase tiers: Community / Starter Support / Consulting / Done-for-you bundle
- Support contact: `conradcjwilson0@gmail.com`

## Evidence
- Configured services verified via `docker compose config`
- Runtime verification is environment-dependent; verify locally before launch
- Resource budgets documented in README
- Memory-shield pre-flight check included

## Requirements
- Docker Compose v2+
- 3.5 GiB RAM baseline
- Linux host tested; WSL2 supported on Windows 11 Pro

## Post-Launch Actions
- Replace `.env.example` values with real production credentials in a secrets manager
- Enable GitHub secret scanning and vulnerability alerts
- Add branch protection before public exposure
- Run `scripts/verify-install.sh` on target hardware before customer delivery
