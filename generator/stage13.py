"""
Stage 13 -- Local API Endpoints (FastAPI).

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. Every exercise is its own small FastAPI app
tested in-process with TestClient (no real server or port needed).

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    FastAPI(), @app.get, @app.post, uvicorn.run, path & query
            parameters
  Mid:      Depends, pydantic.BaseModel, dependency injection, automatic
            interactive docs (/docs)
  Advanced: TestClient(), async def endpoints
"""

STAGE = "stage13"
TOPIC = "Local API Endpoints"
OVERVIEW = (
    "Six exercises, two per tier: routing with path/query parameters plus "
    "running the app via uvicorn.run in Basic; pydantic request models "
    "plus dependency injection and the auto-generated /docs in Mid; async "
    "def endpoints plus TestClient-driven app testing in Advanced."
)

EXERCISES = [
    {
        "name": "tier1_basic01",
        "title": "Basic Routes",
        "summary": "FastAPI(), @app.get, @app.post, path & query parameters",
        "readme": (
            "Implement a small app, `app = FastAPI()` (already in the "
            "stub), with four routes:\n\n"
            "- `@app.get(\"/\")` `read_root()` -- return "
            "`{\"message\": \"hello\"}`.\n"
            "- `@app.get(\"/items/{item_id}\")` `read_item(item_id: "
            "int)` -- return `{\"item_id\": item_id}`. `{item_id}` in "
            "the route string is a **path parameter**: FastAPI extracts "
            "it from the URL and passes it as an argument, converting "
            "it to `int` automatically because of the type hint.\n"
            "- `@app.get(\"/search\")` `search(q: str = \"\")` -- return "
            "`{\"q\": q}`. `q` is a **query parameter** instead "
            "(`?q=...` in the URL) because it's *not* named in the "
            "route path.\n"
            "- `@app.post(\"/echo\")` `echo(payload: dict)` -- return "
            "`payload` unchanged (whatever JSON body was posted).\n\n"
            "See the Study Reference presentation, Topic 13 (Basic "
            "tier), for the theory."
        ),
        "stub": '''\
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """{"message": "hello"}."""
    raise NotImplementedError


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """{"item_id": item_id} -- item_id is a path parameter."""
    raise NotImplementedError


@app.get("/search")
def search(q: str = ""):
    """{"q": q} -- q is a query parameter."""
    raise NotImplementedError


@app.post("/echo")
def echo(payload: dict):
    """Return payload unchanged."""
    raise NotImplementedError
''',
        "reference": '''\
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "hello"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/search")
def search(q: str = ""):
    return {"q": q}


@app.post("/echo")
def echo(payload: dict):
    return payload
''',
        "test": '''\
from fastapi.testclient import TestClient
from exercises.stage13.tier1_basic01.solution import app as basic_routes_app

basic_routes_client = TestClient(basic_routes_app)


def test_read_root():
    """GET / returns {"message": "hello"}."""
    assert basic_routes_client.get("/").json() == {"message": "hello"}


def test_read_item_path_parameter():
    """{item_id} is a path parameter, auto-converted to int."""
    assert basic_routes_client.get("/items/42").json() == {"item_id": 42}


def test_search_query_parameter():
    """q is a query parameter (?q=...), not part of the route path."""
    assert basic_routes_client.get("/search?q=python").json() == {"q": "python"}


def test_search_default_query_parameter():
    """search's q defaults to "" when omitted."""
    assert basic_routes_client.get("/search").json() == {"q": ""}


def test_echo_post():
    """POST /echo returns the JSON body unchanged."""
    assert basic_routes_client.post("/echo", json={"a": 1}).json() == {"a": 1}
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Running the App",
        "summary": "FastAPI(), @app.get, @app.post, uvicorn.run",
        "readme": (
            "A second small app, plus the piece that actually serves it "
            "outside of tests. Implement:\n\n"
            "- `@app.get(\"/health\")` `health()` -- return "
            "`{\"status\": \"ok\"}`.\n"
            "- `@app.post(\"/notes\")` `create_note(payload: dict)` -- "
            "return `payload` unchanged.\n"
            "- `run_server(app, host: str = \"127.0.0.1\", port: int = "
            "8000) -> None` -- `uvicorn.run(app, host=host, "
            "port=port)`. `uvicorn` is the actual server that runs a "
            "FastAPI app outside of tests; `uvicorn.run(...)` blocks "
            "forever serving requests, so the test for this one "
            "**mocks** `uvicorn.run` to check it was called correctly, "
            "instead of actually starting a server.\n\n"
            "See the Study Reference presentation, Topic 13 (Basic "
            "tier), for the theory."
        ),
        "stub": '''\
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    """{"status": "ok"}."""
    raise NotImplementedError


@app.post("/notes")
def create_note(payload: dict):
    """Return payload unchanged."""
    raise NotImplementedError


def run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None:
    """uvicorn.run(app, host=host, port=port)."""
    raise NotImplementedError
''',
        "reference": '''\
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/notes")
def create_note(payload: dict):
    return payload


def run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None:
    uvicorn.run(app, host=host, port=port)
''',
        "test": '''\
from unittest.mock import patch
from fastapi.testclient import TestClient
from exercises.stage13.tier1_basic02.solution import app as running_app, run_server

running_client = TestClient(running_app)


def test_health():
    """GET /health returns {"status": "ok"}."""
    assert running_client.get("/health").json() == {"status": "ok"}


def test_create_note_post():
    """POST /notes returns the JSON body unchanged."""
    assert running_client.post("/notes", json={"text": "hi"}).json() == {"text": "hi"}


def test_run_server_calls_uvicorn_run_without_starting_a_server():
    """run_server must call uvicorn.run(app, host=host, port=port) -- mocked here so no real server starts."""
    with patch("uvicorn.run") as mock_run:
        run_server(running_app, host="0.0.0.0", port=9000)
    mock_run.assert_called_once_with(running_app, host="0.0.0.0", port=9000)
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Pydantic Models",
        "summary": "pydantic.BaseModel",
        "readme": (
            "Implement three `pydantic.BaseModel` request bodies and "
            "their routes:\n\n"
            "- `Item(BaseModel)` -- fields `name: str`, `price: float`, "
            "`in_stock: bool = True`. `@app.post(\"/items\")` "
            "`create_item(item: Item)` -- return `item.model_dump()`.\n"
            "- `User(BaseModel)` -- fields `username: str`, `age: int`. "
            "`@app.post(\"/users\")` `create_user(user: User)` -- return "
            "`{\"username\": user.username, \"age\": user.age}`.\n"
            "- `LoginRequest(BaseModel)` -- fields `username: str`, "
            "`password: str`. `@app.post(\"/login\")` "
            "`login(req: LoginRequest)` -- return `{\"ok\": True, "
            "\"username\": req.username}` (never echo the password "
            "back).\n\n"
            "A `BaseModel` subclass is both documentation and "
            "validation: FastAPI parses the JSON body, checks every "
            "field against its type hint, and rejects the request "
            "(with a detailed error) before your function body even "
            "runs if something doesn't match -- there's no manual "
            "`if \"name\" not in data` checking to write.\n\n"
            "See the Study Reference presentation, Topic 13 (Mid "
            "tier), for the theory."
        ),
        "stub": '''\
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


class User(BaseModel):
    username: str
    age: int


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/items")
def create_item(item: Item):
    """item.model_dump()."""
    raise NotImplementedError


@app.post("/users")
def create_user(user: User):
    """{"username": user.username, "age": user.age}."""
    raise NotImplementedError


@app.post("/login")
def login(req: LoginRequest):
    """{"ok": True, "username": req.username} -- never echo the password."""
    raise NotImplementedError
''',
        "reference": '''\
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


class User(BaseModel):
    username: str
    age: int


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/items")
def create_item(item: Item):
    return item.model_dump()


@app.post("/users")
def create_user(user: User):
    return {"username": user.username, "age": user.age}


@app.post("/login")
def login(req: LoginRequest):
    return {"ok": True, "username": req.username}
''',
        "test": '''\
from fastapi.testclient import TestClient
from exercises.stage13.tier2_mid01.solution import app as models_app

models_client = TestClient(models_app)


def test_create_item_defaults_in_stock_true():
    """Item.in_stock defaults to True when omitted from the request body."""
    response = models_client.post("/items", json={"name": "Widget", "price": 9.99})
    assert response.json() == {"name": "Widget", "price": 9.99, "in_stock": True}


def test_create_item_validation_rejects_missing_field():
    """pydantic must reject a request missing a required field (price) with a 422, before the route body runs."""
    response = models_client.post("/items", json={"name": "Widget"})
    assert response.status_code == 422


def test_create_user():
    """create_user returns username/age extracted from the validated User model."""
    response = models_client.post("/users", json={"username": "ada", "age": 30})
    assert response.json() == {"username": "ada", "age": 30}


def test_login_never_echoes_password():
    """login must never include the password in its response."""
    response = models_client.post("/login", json={"username": "ada", "password": "secret"})
    data = response.json()
    assert data == {"ok": True, "username": "ada"}
    assert "password" not in data
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Dependency Injection and Automatic Docs",
        "summary": "Depends, dependency injection, automatic interactive docs (/docs)",
        "readme": (
            "Implement three routes, each using `Depends()` to pull "
            "shared logic out of the route function itself:\n\n"
            "- `get_pagination(page: int = 1, size: int = 10) -> dict` "
            "-- return `{\"page\": page, \"size\": size}` (a plain "
            "function, not a route). `@app.get(\"/paginated\")` "
            "`paginated(params: dict = Depends(get_pagination))` -- "
            "return `params`.\n"
            "- `get_db() -> dict` -- return `{\"connected\": True}`. "
            "`@app.get(\"/status\")` `status(db: dict = "
            "Depends(get_db))` -- return `db`.\n"
            "- `verify_token(token: str = \"\") -> bool` -- return "
            "`token == \"secret\"`. `@app.get(\"/protected\")` "
            "`protected(authorized: bool = Depends(verify_token))` -- "
            "return `{\"data\": \"secret data\"}` if `authorized`, else "
            "`{\"error\": \"unauthorized\"}`.\n\n"
            "`Depends(some_function)` tells FastAPI to call "
            "`some_function` for you before your route runs, and hand "
            "you its return value as an argument -- **dependency "
            "injection**: the route declares what it needs, and "
            "doesn't have to know how to build it.\n\n"
            "Then, two functions about what you get *for free* on "
            "every FastAPI app, no extra code required:\n\n"
            "- `get_openapi_schema(app) -> dict` -- `app.openapi()` -- "
            "the auto-generated JSON schema describing every route, "
            "which is what powers the **interactive docs UI at "
            "`/docs`**.\n"
            "- `has_docs_route(app) -> bool` -- `\"/docs\" in [route.path "
            "for route in app.routes]` -- confirms the `/docs` page "
            "itself is registered as a real route on the app.\n\n"
            "See the Study Reference presentation, Topic 13 (Mid "
            "tier), for the theory."
        ),
        "stub": '''\
from fastapi import FastAPI, Depends

app = FastAPI()


def get_pagination(page: int = 1, size: int = 10) -> dict:
    """{"page": page, "size": size}."""
    raise NotImplementedError


def get_db() -> dict:
    """{"connected": True}."""
    raise NotImplementedError


def verify_token(token: str = "") -> bool:
    """token == "secret"."""
    raise NotImplementedError


@app.get("/paginated")
def paginated(params: dict = Depends(get_pagination)):
    """Return params."""
    raise NotImplementedError


@app.get("/status")
def status(db: dict = Depends(get_db)):
    """Return db."""
    raise NotImplementedError


@app.get("/protected")
def protected(authorized: bool = Depends(verify_token)):
    """{"data": "secret data"} if authorized, else {"error": "unauthorized"}."""
    raise NotImplementedError


def get_openapi_schema(app) -> dict:
    """app.openapi() -- the schema that powers the /docs page."""
    raise NotImplementedError


def has_docs_route(app) -> bool:
    """"/docs" in [route.path for route in app.routes]."""
    raise NotImplementedError
''',
        "reference": '''\
from fastapi import FastAPI, Depends

app = FastAPI()


def get_pagination(page: int = 1, size: int = 10) -> dict:
    return {"page": page, "size": size}


def get_db() -> dict:
    return {"connected": True}


def verify_token(token: str = "") -> bool:
    return token == "secret"


@app.get("/paginated")
def paginated(params: dict = Depends(get_pagination)):
    return params


@app.get("/status")
def status(db: dict = Depends(get_db)):
    return db


@app.get("/protected")
def protected(authorized: bool = Depends(verify_token)):
    if authorized:
        return {"data": "secret data"}
    return {"error": "unauthorized"}


def get_openapi_schema(app) -> dict:
    return app.openapi()


def has_docs_route(app) -> bool:
    return "/docs" in [route.path for route in app.routes]
''',
        "test": '''\
from fastapi.testclient import TestClient
from exercises.stage13.tier2_mid02.solution import app as di_app, get_openapi_schema, has_docs_route

di_client = TestClient(di_app)


def test_paginated_defaults():
    """paginated depends on get_pagination for its default page/size."""
    assert di_client.get("/paginated").json() == {"page": 1, "size": 10}


def test_paginated_custom_values():
    """Query parameters flow through the Depends()-injected get_pagination."""
    assert di_client.get("/paginated?page=3&size=20").json() == {"page": 3, "size": 20}


def test_status_depends_on_get_db():
    """status returns whatever the get_db dependency returns."""
    assert di_client.get("/status").json() == {"connected": True}


def test_protected_without_token():
    """verify_token's dependency-injected result gates the /protected response."""
    assert di_client.get("/protected").json() == {"error": "unauthorized"}


def test_protected_with_correct_token():
    """A correct token, via the same Depends()-injected verify_token, unlocks the protected data."""
    response = di_client.get("/protected?token=secret")
    assert response.json() == {"data": "secret data"}


def test_get_openapi_schema_has_paginated_path():
    """get_openapi_schema uses app.openapi(), which must describe every registered route."""
    schema = get_openapi_schema(di_app)
    assert "/paginated" in schema["paths"]


def test_has_docs_route():
    """Every FastAPI app gets a /docs route registered automatically, no extra code required."""
    assert has_docs_route(di_app) is True
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "Async Endpoints",
        "summary": "async def endpoints",
        "readme": (
            "Implement three routes as `async def` instead of plain "
            "`def`:\n\n"
            "- `@app.get(\"/async-hello\")` `async def async_hello()` "
            "-- return `{\"message\": \"hello async\"}`.\n"
            "- `@app.get(\"/async-items/{item_id}\")` "
            "`async def async_get_item(item_id: int)` -- return "
            "`{\"item_id\": item_id}`.\n"
            "- `@app.post(\"/async-echo\")` `async def "
            "async_echo(payload: dict)` -- return `payload` "
            "unchanged.\n\n"
            "None of these actually `await` anything here, so they'd "
            "behave identically as plain `def` routes -- the point of "
            "this exercise is just the syntax and where it matters: "
            "FastAPI runs an `async def` route directly on its event "
            "loop, while a plain `def` route is run in a background "
            "thread pool so it can't block everything else. `async "
            "def` only pays off once the body actually does `await` "
            "an async operation (a database call, another HTTP "
            "request, ...).\n\n"
            "See the Study Reference presentation, Topic 13 "
            "(Advanced tier), for the theory."
        ),
        "stub": '''\
from fastapi import FastAPI

app = FastAPI()


@app.get("/async-hello")
async def async_hello():
    """{"message": "hello async"}."""
    raise NotImplementedError


@app.get("/async-items/{item_id}")
async def async_get_item(item_id: int):
    """{"item_id": item_id}."""
    raise NotImplementedError


@app.post("/async-echo")
async def async_echo(payload: dict):
    """Return payload unchanged."""
    raise NotImplementedError
''',
        "reference": '''\
from fastapi import FastAPI

app = FastAPI()


@app.get("/async-hello")
async def async_hello():
    return {"message": "hello async"}


@app.get("/async-items/{item_id}")
async def async_get_item(item_id: int):
    return {"item_id": item_id}


@app.post("/async-echo")
async def async_echo(payload: dict):
    return payload
''',
        "test": '''\
from fastapi.testclient import TestClient
from exercises.stage13.tier3_advanced01.solution import app as async_app

async_client = TestClient(async_app)


def test_async_hello():
    """An async def route behaves like a normal GET route from the client's perspective."""
    assert async_client.get("/async-hello").json() == {"message": "hello async"}


def test_async_get_item():
    """async def routes still support path parameters."""
    assert async_client.get("/async-items/7").json() == {"item_id": 7}


def test_async_echo():
    """async def routes still support POST bodies."""
    assert async_client.post("/async-echo", json={"x": 1}).json() == {"x": 1}
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Testing Apps with TestClient",
        "summary": "TestClient()",
        "readme": (
            "A tiny app, `app = FastAPI()` with `@app.get(\"/ping\")` "
            "`ping()` returning `{\"pong\": True}` and "
            "`@app.post(\"/echo2\")` `echo2(payload: dict)` returning "
            "`payload` unchanged (both already given). Implement three "
            "small, reusable `TestClient` helpers around it:\n\n"
            "- `client_get_json(app, path: str) -> dict` -- "
            "`TestClient(app).get(path).json()`.\n"
            "- `client_post_json(app, path: str, payload: dict) -> "
            "dict` -- `TestClient(app).post(path, json=payload).json()`.\n"
            "- `client_status_code(app, path: str) -> int` -- "
            "`TestClient(app).get(path).status_code`.\n\n"
            "`TestClient` runs the app **in-process**, with no real "
            "network socket or port involved -- exactly how every test "
            "in this stage exercises a FastAPI app, including the ones "
            "you wrote in the earlier exercises.\n\n"
            "See the Study Reference presentation, Topic 13 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/ping")
def ping():
    return {"pong": True}


@app.post("/echo2")
def echo2(payload: dict):
    return payload


def client_get_json(app, path: str) -> dict:
    """TestClient(app).get(path).json()."""
    raise NotImplementedError


def client_post_json(app, path: str, payload: dict) -> dict:
    """TestClient(app).post(path, json=payload).json()."""
    raise NotImplementedError


def client_status_code(app, path: str) -> int:
    """TestClient(app).get(path).status_code."""
    raise NotImplementedError
''',
        "reference": '''\
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/ping")
def ping():
    return {"pong": True}


@app.post("/echo2")
def echo2(payload: dict):
    return payload


def client_get_json(app, path: str) -> dict:
    return TestClient(app).get(path).json()


def client_post_json(app, path: str, payload: dict) -> dict:
    return TestClient(app).post(path, json=payload).json()


def client_status_code(app, path: str) -> int:
    return TestClient(app).get(path).status_code
''',
        "test": '''\
from exercises.stage13.tier3_advanced02.solution import (
    app,
    client_get_json,
    client_post_json,
    client_status_code,
)


def test_client_get_json():
    """client_get_json must build its own TestClient(app) and GET the given path."""
    assert client_get_json(app, "/ping") == {"pong": True}


def test_client_post_json():
    """client_post_json must build its own TestClient(app) and POST the given payload."""
    assert client_post_json(app, "/echo2", {"a": 1}) == {"a": 1}


def test_client_status_code():
    """client_status_code returns the raw HTTP status code from a TestClient GET."""
    assert client_status_code(app, "/ping") == 200
    assert client_status_code(app, "/nonexistent") == 404
''',
    },
]
