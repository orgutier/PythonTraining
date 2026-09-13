from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
def say_hello(name: str) -> dict:
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def add(a: int, b: int) -> dict:
    return {"result": a + b}
