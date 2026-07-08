#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [ -d ".venv" ]; then
  PYTHON=".venv/bin/python"
else
  PYTHON="python"
fi
exec "$PYTHON" -m app.celery_app
