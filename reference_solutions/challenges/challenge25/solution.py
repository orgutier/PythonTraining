import secrets
from fastapi import FastAPI, Depends, HTTPException, Query, Header
from pydantic import BaseModel, HttpUrl

app = FastAPI()

_store = {}


class ShortenRequest(BaseModel):
    url: HttpUrl


class ShortenResponse(BaseModel):
    code: str
    short_url: str


def get_api_key(x_api_key: str = Header(default="")) -> str:
    if x_api_key == "":
        raise HTTPException(status_code=401, detail="missing API key")
    return x_api_key


def _find_existing_code(url: str):
    for code, entry in _store.items():
        if entry["url"] == url:
            return code
    return None


def _generate_code() -> str:
    code = secrets.token_urlsafe(6)[:6]
    while code in _store:
        code = secrets.token_urlsafe(6)[:6]
    return code


@app.post("/shorten")
def shorten(req: ShortenRequest, api_key: str = Depends(get_api_key)) -> ShortenResponse:
    url_str = str(req.url)
    existing = _find_existing_code(url_str)
    if existing:
        return ShortenResponse(code=existing, short_url=f"/{existing}")
    code = _generate_code()
    _store[code] = {"url": url_str, "clicks": 0}
    return ShortenResponse(code=code, short_url=f"/{code}")


@app.get("/search")
def search(prefix: str = "", limit: int = Query(default=10, le=100)):
    matches = [code for code in _store if code.startswith(prefix)]
    return {"codes": matches[:limit]}


@app.get("/stats/{code}")
def stats(code: str):
    if code not in _store:
        raise HTTPException(status_code=404, detail="not found")
    entry = _store[code]
    return {"code": code, "url": entry["url"], "clicks": entry["clicks"]}


@app.get("/{code}")
async def redirect(code: str):
    if code not in _store:
        raise HTTPException(status_code=404, detail="not found")
    _store[code]["clicks"] += 1
    return {"redirect_to": _store[code]["url"]}
