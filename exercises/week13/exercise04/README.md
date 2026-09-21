# Async Endpoints

Implement three routes as `async def` instead of plain `def`:

- `@app.get("/async-hello")` `async def async_hello()` -- return `{"message": "hello async"}`.
- `@app.get("/async-items/{item_id}")` `async def async_get_item(item_id: int)` -- return `{"item_id": item_id}`.
- `@app.post("/async-echo")` `async def async_echo(payload: dict)` -- return `payload` unchanged.

None of these actually `await` anything here, so they'd behave identically as plain `def` routes -- the point of this exercise is just the syntax and where it matters: FastAPI runs an `async def` route directly on its event loop, while a plain `def` route is run in a background thread pool so it can't block everything else. `async def` only pays off once the body actually does `await` an async operation (a database call, another HTTP request, ...).

See the Study Reference presentation, Topic 13, for the theory.
