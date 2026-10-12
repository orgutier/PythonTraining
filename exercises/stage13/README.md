# Local API Endpoints

Six exercises, two per tier: routing with path/query parameters plus running the app via uvicorn.run in Basic; pydantic request models plus dependency injection and the auto-generated /docs in Mid; async def endpoints plus TestClient-driven app testing in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage13_<name>` (e.g. `python tools/cli.py test stage13_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- FastAPI(), @app.get, @app.post, path & query parameters
- **`tier1_basic02/`** -- FastAPI(), @app.get, @app.post, uvicorn.run
- **`tier2_mid01/`** -- pydantic.BaseModel
- **`tier2_mid02/`** -- Depends, dependency injection, automatic interactive docs (/docs)
- **`tier3_advanced01/`** -- async def endpoints
- **`tier3_advanced02/`** -- TestClient()
