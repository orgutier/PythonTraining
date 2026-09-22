# Local API Endpoints

Five exercises, each its own small FastAPI app tested in-process with TestClient (no real server or port needed), covering routing, pydantic request/response models, dependency injection, async endpoints, and the /docs + uvicorn.run side of things at least three times each.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage13_exerciseXX`. Work through them in order.

- **`exercise01/`** -- FastAPI(), @app.get x3, @app.post, path/query parameters
- **`exercise02/`** -- pydantic.BaseModel x3, @app.post x2 more
- **`exercise03/`** -- Depends x3, dependency injection concept
- **`exercise04/`** -- async def endpoints x3
- **`exercise05/`** -- TestClient() x3, automatic interactive docs, uvicorn.run
