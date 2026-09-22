# TestClient, Docs, and uvicorn.run

Implement:

- `app = FastAPI()` with one route, `@app.get("/health")` `health()` returning `{"status": "ok"}` (already fully written in the stub -- the rest of this exercise is about *using* the app, not adding more routes).
- `get_health_status(app) -> dict` -- `client = TestClient(app)`; `return client.get("/health").json()`.
- `get_openapi_schema(app) -> dict` -- `client = TestClient(app)`; `return client.get("/openapi.json").json()` -- this auto-generated JSON schema is what powers the interactive docs UI at `/docs`.
- `docs_page_status(app) -> int` -- `client = TestClient(app)`; `return client.get("/docs").status_code` -- every FastAPI app gets a working `/docs` page for free, no extra code required.
- `run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None` -- `uvicorn.run(app, host=host, port=port)`. `uvicorn` is the actual server that runs a FastAPI app outside of tests; `uvicorn.run(...)` blocks forever serving requests, so the test for this one **mocks** `uvicorn.run` to check it was called correctly, instead of actually starting a server.

See the Study Reference presentation, Topic 13, for the theory.
