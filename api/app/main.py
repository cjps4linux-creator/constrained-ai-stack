from fastapi import FastAPI
from app.config import settings


app = FastAPI(title="constrained-api", version="0.2.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
