"""Constrained AI Stack packaging and compose sanity tests."""
from pathlib import Path
import subprocess

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_repo_required_files_exist():
    required = ["README.md", "LICENSE", "TOS.md", "docs/setup-checklist.md", "docs/README.md"]
    for rel in required:
        assert (REPO_ROOT / rel).exists(), f"Missing required file: {rel}"


def test_docker_compose_services_declared():
    compose = REPO_ROOT / "docker-compose.yml"
    assert compose.exists()
    text = compose.read_text(encoding="utf-8")
    for service in ["postgres", "redis", "api", "worker", "prometheus", "node-exporter"]:
        assert service in text, f"Missing service in compose: {service}"


def test_compose_config_validation(tmp_path):
    result = subprocess.run(
        ["docker", "compose", "config", "--services"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise AssertionError(f"docker compose config failed: {result.stderr}")
    for service in ["postgres", "redis", "api", "worker"]:
        assert service in result.stdout, f"Service missing from compose config: {service}"
