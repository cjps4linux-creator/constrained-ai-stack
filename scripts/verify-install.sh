set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${PROJECT_ROOT}"

if ! command -v docker >/dev/null 2>&1; then
  echo "FAIL: docker not found"
  exit 1
fi

if ! docker compose version >/dev/null 2>&1; then
  echo "FAIL: docker compose not available"
  exit 1
fi

if ! docker info >/dev/null 2>&1; then
  echo "FAIL: docker daemon unreachable; start Docker Desktop or connect to a reachable daemon context"
  exit 1
fi

docker compose config --services >/dev/null

echo "VERIFIED: docker available, daemon reachable, and constrained-ai-stack compose is valid"
