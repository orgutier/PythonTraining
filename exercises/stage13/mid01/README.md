# Pydantic Models

Implement three `pydantic.BaseModel` request bodies and their routes:

- `Item(BaseModel)` -- fields `name: str`, `price: float`, `in_stock: bool = True`. `@app.post("/items")` `create_item(item: Item)` -- return `item.model_dump()`.
- `User(BaseModel)` -- fields `username: str`, `age: int`. `@app.post("/users")` `create_user(user: User)` -- return `{"username": user.username, "age": user.age}`.
- `LoginRequest(BaseModel)` -- fields `username: str`, `password: str`. `@app.post("/login")` `login(req: LoginRequest)` -- return `{"ok": True, "username": req.username}` (never echo the password back).

A `BaseModel` subclass is both documentation and validation: FastAPI parses the JSON body, checks every field against its type hint, and rejects the request (with a detailed error) before your function body even runs if something doesn't match -- there's no manual `if "name" not in data` checking to write.

See the Study Reference presentation, Topic 13 (Mid tier), for the theory.
