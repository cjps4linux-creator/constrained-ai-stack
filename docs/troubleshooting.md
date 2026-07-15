# Troubleshooting

## Services fail to start

1. Run `scripts/memory-shield.sh`
2. Check `docker compose ps`
3. Inspect logs with `docker compose logs <service>`
4. If the container is `OOMKilled`, lower memory limits in Compose

## PostgreSQL connection refused

- Confirm container health with `docker compose ps postgres`
- Check for port conflicts with `ss -ltnp | grep 5432`
- Verify credentials in `.env` match Compose expectations

## Redis maxmemory evictions

- Monitor with `redis-cli info memory`
- Reduce worker concurrency or batch sizes
- Increase maxmemory only if RAM allows

## Prometheus disk full

- Retention is set to 7 days / 1GB
- For smaller disks, lower retention in the command args
- Move prometheus_data volume to larger disk if available

## Worker not consuming jobs

- Confirm broker reachable: `docker compose exec worker celery -A app.celery inspect ping`
- Check queue names match producer/consumer
- Review worker logs for import or config errors
