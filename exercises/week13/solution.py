"""
Week 13 - FastAPI
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week13.py
imports directly from here.
"""


from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
def say_hello(name: str) -> dict:
    raise NotImplementedError


@app.get("/add")
def add(a: int, b: int) -> dict:
    raise NotImplementedError
