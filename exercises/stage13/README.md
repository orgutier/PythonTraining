# Local API Endpoints

Six exercises, two per tier: routing with path/query parameters plus running the app via uvicorn.run in Basic; pydantic request models plus dependency injection and the auto-generated /docs in Mid; async def endpoints plus TestClient-driven app testing in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage13_<name>` (e.g. `python tools/cli.py test stage13_basic01`). Work through them in order.

- **`basic01/`** -- FastAPI(), @app.get, @app.post, path & query parameters
- **`basic02/`** -- FastAPI(), @app.get, @app.post, uvicorn.run
- **`mid01/`** -- pydantic.BaseModel
- **`mid02/`** -- Depends, dependency injection, automatic interactive docs (/docs)
- **`advanced01/`** -- async def endpoints
- **`advanced02/`** -- TestClient()
