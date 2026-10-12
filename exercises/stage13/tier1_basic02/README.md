# Running the App

A second small app, plus the piece that actually serves it outside of tests. Implement:

- `@app.get("/health")` `health()` -- return `{"status": "ok"}`.
- `@app.post("/notes")` `create_note(payload: dict)` -- return `payload` unchanged.
- `run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None` -- `uvicorn.run(app, host=host, port=port)`. `uvicorn` is the actual server that runs a FastAPI app outside of tests; `uvicorn.run(...)` blocks forever serving requests, so the test for this one **mocks** `uvicorn.run` to check it was called correctly, instead of actually starting a server.

See the Study Reference presentation, Topic 13 (Basic tier), for the theory.
