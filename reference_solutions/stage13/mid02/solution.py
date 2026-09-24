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
