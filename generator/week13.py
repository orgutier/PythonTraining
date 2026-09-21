"""
Week 13 -- Local API Endpoints (FastAPI).

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: FastAPI(), @app.get, @app.post, Depends, uvicorn.run
  modules:  fastapi, pydantic, uvicorn
  methods:  TestClient(), BaseModel (pydantic)
  concepts: path & query parameters, dependency injection,
            async def endpoints, automatic interactive docs (/docs)
"""

WEEK = "week13"
TOPIC = "Local API Endpoints"
OVERVIEW = (
    "Five exercises, each its own small FastAPI app tested in-process with "
    "TestClient (no real server or port needed), covering routing, "
    "pydantic request/response models, dependency injection, async "
    "endpoints, and the /docs + uvicorn.run side of things at least three "
    "times each."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Basic Routes",
        "summary": "FastAPI(), @app.get x3, @app.post, path/query parameters",
        "readme": (
            "Implement a small app, `app = FastAPI()` (already in the stub), "
            "with four routes:\n\n"
            "- `@app.get(\"/\")` `read_root()` -- return `{\"message\": "
            "\"hello\"}`.\n"
            "- `@app.get(\"/items/{item_id}\")` `read_item(item_id: int)` -- "
            "return `{\"item_id\": item_id}`. `{item_id}` in the route "
            "string is a **path parameter**: FastAPI extracts it from the "
            "URL and passes it as an argument, converting it to `int` "
            "automatically because of the type hint.\n"
            "- `@app.get(\"/search\")` `search(q: str = \"\")` -- return "
            "`{\"q\": q}`. `q` is a **query parameter** instead "
            "(`?q=...` in the URL) because it's *not* named in the route "
            "path.\n"
            "- `@app.post(\"/echo\")` `echo(payload: dict)` -- return "
            "`payload` unchanged (whatever JSON body was posted).\n\n"
            "See the Study Reference presentation, Topic 13, for the theory."
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
from exercises.week13.exercise01.solution import app as basic_routes_app

basic_routes_client = TestClient(basic_routes_app)


def test_read_root():
    assert basic_routes_client.get("/").json() == {"message": "hello"}


def test_read_item_path_parameter():
    assert basic_routes_client.get("/items/42").json() == {"item_id": 42}


def test_search_query_parameter():
    assert basic_routes_client.get("/search?q=python").json() == {"q": "python"}


def test_search_default_query_parameter():
    assert basic_routes_client.get("/search").json() == {"q": ""}


def test_echo_post():
    assert basic_routes_client.post("/echo", json={"a": 1}).json() == {"a": 1}
''',
    },
    {
        "name": "exercise02",
        "title": "Pydantic Models",
        "summary": "pydantic.BaseModel x3, @app.post x2 more",
        "readme": (
            "Implement three `pydantic.BaseModel` request bodies and their "
            "routes:\n\n"
            "- `Item(BaseModel)` -- fields `name: str`, `price: float`, "
            "`in_stock: bool = True`. `@app.post(\"/items\")` "
            "`create_item(item: Item)` -- return `item.model_dump()`.\n"
            "- `User(BaseModel)` -- fields `username: str`, `age: int`. "
            "`@app.post(\"/users\")` `create_user(user: User)` -- return "
            "`{\"username\": user.username, \"age\": user.age}`.\n"
            "- `LoginRequest(BaseModel)` -- fields `username: str`, "
            "`password: str`. `@app.post(\"/login\")` "
            "`login(req: LoginRequest)` -- return `{\"ok\": True, "
            "\"username\": req.username}` (never echo the password back).\n\n"
            "A `BaseModel` subclass is both documentation and validation: "
            "FastAPI parses the JSON body, checks every field against its "
            "type hint, and rejects the request (with a detailed error) "
            "before your function body even runs if something doesn't "
            "match -- there's no manual `if \"name\" not in data` checking "
            "to write.\n\n"
            "See the Study Reference presentation, Topic 13, for the theory."
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
from exercises.week13.exercise02.solution import app as models_app

models_client = TestClient(models_app)


def test_create_item_defaults_in_stock_true():
    response = models_client.post("/items", json={"name": "Widget", "price": 9.99})
    assert response.json() == {"name": "Widget", "price": 9.99, "in_stock": True}


def test_create_item_validation_rejects_missing_field():
    response = models_client.post("/items", json={"name": "Widget"})
    assert response.status_code == 422


def test_create_user():
    response = models_client.post("/users", json={"username": "ada", "age": 30})
    assert response.json() == {"username": "ada", "age": 30}


def test_login_never_echoes_password():
    response = models_client.post("/login", json={"username": "ada", "password": "secret"})
    data = response.json()
    assert data == {"ok": True, "username": "ada"}
    assert "password" not in data
''',
    },
    {
        "name": "exercise03",
        "title": "Dependency Injection",
        "summary": "Depends x3, dependency injection concept",
        "readme": (
            "Implement three routes, each using `Depends()` to pull shared "
            "logic out of the route function itself:\n\n"
            "- `get_pagination(page: int = 1, size: int = 10) -> dict` -- "
            "return `{\"page\": page, \"size\": size}` (a plain function, "
            "not a route). `@app.get(\"/paginated\")` "
            "`paginated(params: dict = Depends(get_pagination))` -- return "
            "`params`.\n"
            "- `get_db() -> dict` -- return `{\"connected\": True}`. "
            "`@app.get(\"/status\")` `status(db: dict = Depends(get_db))` "
            "-- return `db`.\n"
            "- `verify_token(token: str = \"\") -> bool` -- return "
            "`token == \"secret\"`. `@app.get(\"/protected\")` "
            "`protected(authorized: bool = Depends(verify_token))` -- "
            "return `{\"data\": \"secret data\"}` if `authorized`, else "
            "`{\"error\": \"unauthorized\"}`.\n\n"
            "`Depends(some_function)` tells FastAPI to call `some_function` "
            "for you before your route runs, and hand you its return value "
            "as an argument -- **dependency injection**: the route declares "
            "what it needs, and doesn't have to know how to build it.\n\n"
            "See the Study Reference presentation, Topic 13, for the theory."
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
''',
        "test": '''\
from fastapi.testclient import TestClient
from exercises.week13.exercise03.solution import app as di_app

di_client = TestClient(di_app)


def test_paginated_defaults():
    assert di_client.get("/paginated").json() == {"page": 1, "size": 10}


def test_paginated_custom_values():
    assert di_client.get("/paginated?page=3&size=20").json() == {"page": 3, "size": 20}


def test_status_depends_on_get_db():
    assert di_client.get("/status").json() == {"connected": True}


def test_protected_without_token():
    assert di_client.get("/protected").json() == {"error": "unauthorized"}


def test_protected_with_correct_token():
    response = di_client.get("/protected?token=secret")
    assert response.json() == {"data": "secret data"}
''',
    },
    {
        "name": "exercise04",
        "title": "Async Endpoints",
        "summary": "async def endpoints x3",
        "readme": (
            "Implement three routes as `async def` instead of plain `def`:\n\n"
            "- `@app.get(\"/async-hello\")` `async def async_hello()` -- "
            "return `{\"message\": \"hello async\"}`.\n"
            "- `@app.get(\"/async-items/{item_id}\")` "
            "`async def async_get_item(item_id: int)` -- return "
            "`{\"item_id\": item_id}`.\n"
            "- `@app.post(\"/async-echo\")` `async def async_echo(payload: "
            "dict)` -- return `payload` unchanged.\n\n"
            "None of these actually `await` anything here, so they'd behave "
            "identically as plain `def` routes -- the point of this "
            "exercise is just the syntax and where it matters: FastAPI runs "
            "an `async def` route directly on its event loop, while a plain "
            "`def` route is run in a background thread pool so it can't "
            "block everything else. `async def` only pays off once the body "
            "actually does `await` an async operation (a database call, "
            "another HTTP request, ...).\n\n"
            "See the Study Reference presentation, Topic 13, for the theory."
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
from exercises.week13.exercise04.solution import app as async_app

async_client = TestClient(async_app)


def test_async_hello():
    assert async_client.get("/async-hello").json() == {"message": "hello async"}


def test_async_get_item():
    assert async_client.get("/async-items/7").json() == {"item_id": 7}


def test_async_echo():
    assert async_client.post("/async-echo", json={"x": 1}).json() == {"x": 1}
''',
    },
    {
        "name": "exercise05",
        "title": "TestClient, Docs, and uvicorn.run",
        "summary": "TestClient() x3, automatic interactive docs, uvicorn.run",
        "readme": (
            "Implement:\n\n"
            "- `app = FastAPI()` with one route, `@app.get(\"/health\")` "
            "`health()` returning `{\"status\": \"ok\"}` (already fully "
            "written in the stub -- the rest of this exercise is about "
            "*using* the app, not adding more routes).\n"
            "- `get_health_status(app) -> dict` -- `client = "
            "TestClient(app)`; `return client.get(\"/health\").json()`.\n"
            "- `get_openapi_schema(app) -> dict` -- `client = "
            "TestClient(app)`; `return client.get(\"/openapi.json\").json()` "
            "-- this auto-generated JSON schema is what powers the "
            "interactive docs UI at `/docs`.\n"
            "- `docs_page_status(app) -> int` -- `client = TestClient(app)`; "
            "`return client.get(\"/docs\").status_code` -- every FastAPI "
            "app gets a working `/docs` page for free, no extra code "
            "required.\n"
            "- `run_server(app, host: str = \"127.0.0.1\", port: int = 8000) "
            "-> None` -- `uvicorn.run(app, host=host, port=port)`. "
            "`uvicorn` is the actual server that runs a FastAPI app outside "
            "of tests; `uvicorn.run(...)` blocks forever serving requests, "
            "so the test for this one **mocks** `uvicorn.run` to check it "
            "was called correctly, instead of actually starting a server.\n\n"
            "See the Study Reference presentation, Topic 13, for the theory."
        ),
        "stub": '''\
from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


def get_health_status(app) -> dict:
    """TestClient(app).get("/health").json()."""
    raise NotImplementedError


def get_openapi_schema(app) -> dict:
    """TestClient(app).get("/openapi.json").json()."""
    raise NotImplementedError


def docs_page_status(app) -> int:
    """TestClient(app).get("/docs").status_code."""
    raise NotImplementedError


def run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None:
    """uvicorn.run(app, host=host, port=port)."""
    raise NotImplementedError
''',
        "reference": '''\
from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


def get_health_status(app) -> dict:
    client = TestClient(app)
    return client.get("/health").json()


def get_openapi_schema(app) -> dict:
    client = TestClient(app)
    return client.get("/openapi.json").json()


def docs_page_status(app) -> int:
    client = TestClient(app)
    return client.get("/docs").status_code


def run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None:
    uvicorn.run(app, host=host, port=port)
''',
        "test": '''\
from unittest.mock import patch
from exercises.week13.exercise05.solution import (
    app,
    get_health_status,
    get_openapi_schema,
    docs_page_status,
    run_server,
)


def test_get_health_status():
    assert get_health_status(app) == {"status": "ok"}


def test_get_openapi_schema_has_health_path():
    schema = get_openapi_schema(app)
    assert "/health" in schema["paths"]


def test_docs_page_status():
    assert docs_page_status(app) == 200


def test_run_server_calls_uvicorn_run_without_starting_a_server():
    with patch("uvicorn.run") as mock_run:
        run_server(app, host="0.0.0.0", port=9000)
    mock_run.assert_called_once_with(app, host="0.0.0.0", port=9000)
''',
    },
]
