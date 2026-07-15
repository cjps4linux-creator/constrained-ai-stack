# Constrained AI Stack — Launch Documentation

## Launch Readiness Snapshot

| Field | Value |
| --- | --- |
| Repo | `constrained-ai-stack` |
| Default branch | `master` |
| License | MIT |
| Commercial baseline | CI, `CONTRIBUTING.md`, `SECURITY.md`, `LAUNCH.md`, `VERIFICATION.md` |
| Products | Community / Starter Support / Consulting / Done-for-you bundle |

## Verified
- Configured services verified via `docker compose config`
- Runtime verification remains environment-dependent; verify locally before launch
- Resource budgets documented in `README.md`
- Memory-shield pre-flight check included
- Hardened base-image and container controls make this repo publish-ready

## Launch Gates
- [ ] CI workflow green on `master` before release tag
- [ ] Branch protection enabled on `master`
- [ ] GitHub secret scanning and vulnerability alerts enabled
- [ ] `SECURITY.md` contact path validated before public exposure

## Post-Launch Actions
- Replace `.env.example` values with real production credentials in a secrets manager
- Maintain release notes in `CHANGELOG.md` or repository releases
- Enforce signed commits for maintainers if compliance requires provenance tracking

## Support
- Support contact: `conradcjwilson0@gmail.com`
