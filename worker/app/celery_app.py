from celery import Celery
from app.config import settings

celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.REDIS_URL,
)
celery_app.conf.update(
    task_serialization="json",
    accept_content=["json"],
    result_serialization="json",
    task_track_started=True,
    worker_prefetch_multiplier=1,
)

@celery_app.task
def healthcheck() -> dict:
    return {"status": "ok", "worker": "constrained-worker"}
