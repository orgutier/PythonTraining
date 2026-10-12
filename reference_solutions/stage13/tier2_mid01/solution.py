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
