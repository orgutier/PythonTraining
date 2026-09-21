"""
Local API Endpoints -- Pydantic Models
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week13.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week13/exercise02/ and import it as a submodule (e.g.
`from exercises.week13.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


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
