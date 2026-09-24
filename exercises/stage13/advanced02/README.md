# Testing Apps with TestClient

A tiny app, `app = FastAPI()` with `@app.get("/ping")` `ping()` returning `{"pong": True}` and `@app.post("/echo2")` `echo2(payload: dict)` returning `payload` unchanged (both already given). Implement three small, reusable `TestClient` helpers around it:

- `client_get_json(app, path: str) -> dict` -- `TestClient(app).get(path).json()`.
- `client_post_json(app, path: str, payload: dict) -> dict` -- `TestClient(app).post(path, json=payload).json()`.
- `client_status_code(app, path: str) -> int` -- `TestClient(app).get(path).status_code`.

`TestClient` runs the app **in-process**, with no real network socket or port involved -- exactly how every test in this stage exercises a FastAPI app, including the ones you wrote in the earlier exercises.

See the Study Reference presentation, Topic 13 (Advanced tier), for the theory.
