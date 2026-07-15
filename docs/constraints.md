# Design Constraints

This stack is engineered for constrained Linux hosts, typically 3–4 GiB RAM.

These constraints are not bugs. They are design inputs.

---

## Memory Budget

The total baseline target for all services is ~1.8 GiB, leaving headroom for batch jobs and OS overhead.

If a host has less than ~3.2 GiB usable RAM, reduce workers to 1, disable node-exporter, or remove prometheus retention.

## CPU Assumptions

Single-threaded or low-core CPUs are expected. The stack avoids CPU-bound parallelism by design.

Celery concurrency is set to 2, not host-count.

## Disk

PostgreSQL and Prometheus volumes will grow. Schedule backups and retention policies early.

## Failure Modes

- If Redis exhausts maxmemory, jobs may be rejected. Monitor queue depth.
- If PostgreSQL OOMs, the stack loses state. Use WAL archiving.
- If Prometheus retention fills disk, metrics are lost. Set retention size limits.

## Requirements

- Linux host with cgroups available
- At least one IPv4 interface
- `curl`, `wget`, and standard shell utilities installed on the host
- System clock is roughly accurate
