# Changelog

## 0.3.0
- Added real `api/` FastAPI minimum viable service with `/health`
- Added real `worker/` Celery app with `healthcheck` task
- Added `verify-install.sh` for environment validation
- Corrected worker startup target to `worker.app.celery_app:celery_app`
- Documented compose verification in README

## 0.2.0
- Refined pricing and troubleshooting docs
- Added product listing assets

## 0.1.0
- Initial docker-compose stack with API, worker, Postgres, Redis, Prometheus, node-exporter
- Memory shield script and metrics config
- Constraints and troubleshooting docs
