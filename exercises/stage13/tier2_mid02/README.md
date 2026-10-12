# Dependency Injection and Automatic Docs

Implement three routes, each using `Depends()` to pull shared logic out of the route function itself:

- `get_pagination(page: int = 1, size: int = 10) -> dict` -- return `{"page": page, "size": size}` (a plain function, not a route). `@app.get("/paginated")` `paginated(params: dict = Depends(get_pagination))` -- return `params`.
- `get_db() -> dict` -- return `{"connected": True}`. `@app.get("/status")` `status(db: dict = Depends(get_db))` -- return `db`.
- `verify_token(token: str = "") -> bool` -- return `token == "secret"`. `@app.get("/protected")` `protected(authorized: bool = Depends(verify_token))` -- return `{"data": "secret data"}` if `authorized`, else `{"error": "unauthorized"}`.

`Depends(some_function)` tells FastAPI to call `some_function` for you before your route runs, and hand you its return value as an argument -- **dependency injection**: the route declares what it needs, and doesn't have to know how to build it.

Then, two functions about what you get *for free* on every FastAPI app, no extra code required:

- `get_openapi_schema(app) -> dict` -- `app.openapi()` -- the auto-generated JSON schema describing every route, which is what powers the **interactive docs UI at `/docs`**.
- `has_docs_route(app) -> bool` -- `"/docs" in [route.path for route in app.routes]` -- confirms the `/docs` page itself is registered as a real route on the app.

See the Study Reference presentation, Topic 13 (Mid tier), for the theory.
