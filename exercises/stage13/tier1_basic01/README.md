# Basic Routes

Implement a small app, `app = FastAPI()` (already in the stub), with four routes:

- `@app.get("/")` `read_root()` -- return `{"message": "hello"}`.
- `@app.get("/items/{item_id}")` `read_item(item_id: int)` -- return `{"item_id": item_id}`. `{item_id}` in the route string is a **path parameter**: FastAPI extracts it from the URL and passes it as an argument, converting it to `int` automatically because of the type hint.
- `@app.get("/search")` `search(q: str = "")` -- return `{"q": q}`. `q` is a **query parameter** instead (`?q=...` in the URL) because it's *not* named in the route path.
- `@app.post("/echo")` `echo(payload: dict)` -- return `payload` unchanged (whatever JSON body was posted).

See the Study Reference presentation, Topic 13 (Basic tier), for the theory.
