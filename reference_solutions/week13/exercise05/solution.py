from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


def get_health_status(app) -> dict:
    client = TestClient(app)
    return client.get("/health").json()


def get_openapi_schema(app) -> dict:
    client = TestClient(app)
    return client.get("/openapi.json").json()


def docs_page_status(app) -> int:
    client = TestClient(app)
    return client.get("/docs").status_code


def run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None:
    uvicorn.run(app, host=host, port=port)
