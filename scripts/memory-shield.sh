#!/usr/bin/env bash
set -euo pipefail

TOTAL_MB=$(awk '/MemTotal/ {print int($2/1024)}' /proc/mem-info)
REQUIRED_MB=3200

echo "Host RAM: ${TOTAL_MB}MB"

if [ "$TOTAL_MB" -lt "$REQUIRED_MB" ]; then
  echo "BLOCKED: Constrained AI Stack requires at least ${REQUIRED_MB}MB RAM."
  echo "Detected ${TOTAL_MB}MB. Abort or override with FORCE_START=1."
  exit 1
fi

echo "OK: Memory check passed."
