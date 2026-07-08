set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${PROJECT_ROOT}"

MEM_MB="$(free -m 2>/dev/null | awk '/^Mem:/ {print $7} || sysctl -n hw.memsize 2>/dev/null | awk '{print int($1/1024/1024)}')"
MIN_MB=3200

if [ "${MEM_MB}" -lt "${MIN_MB}" ]; then
  echo "FAIL: available memory ${MEM_MB} MB is below minimum ${MIN_MB} MB"
  exit 1
fi

echo "VERIFIED: available memory ${MEM_MB} MB meets minimum ${MIN_MB} MB"
