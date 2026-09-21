"""
Local API Endpoints -- Dependency Injection
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week13_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week13/exercise03/ and import it as a submodule (e.g.
`from exercises.week13.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


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
