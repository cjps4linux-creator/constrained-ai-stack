from fastapi import FastAPI


app = FastAPI(title="constrained-api", version="0.2.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
