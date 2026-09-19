import random
import string

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

app = FastAPI()

_CODE_ALPHABET = string.ascii_letters + string.digits
_CODE_LENGTH = 6

# In-memory storage only, per the challenge's constraints -- state resets
# when the process restarts.
_url_by_code: dict[str, str] = {}
_code_by_url: dict[str, str] = {}
_clicks_by_code: dict[str, int] = {}


class ShortenRequest(BaseModel):
    url: HttpUrl  # Pydantic validates this is a well-formed URL; an
    # invalid value (e.g. "not a url") fails validation automatically and
    # FastAPI turns that into a 422 response before our handler even runs.


class ShortenResponse(BaseModel):
    code: str
    short_url: str


def _generate_unique_code() -> str:
    """
    Generate a short code that does not already exist in `_url_by_code`.

    Strategy: 6 random alphanumeric characters (62 possible characters per
    position, so 62**6 -- about 56 billion -- possible codes), regenerated
    on the rare case of a collision with an existing code. At this codespace
    size, collisions are astronomically unlikely for any realistic number
    of stored URLs, but we check and retry anyway rather than assume it.
    """
    while True:
        code = "".join(random.choices(_CODE_ALPHABET, k=_CODE_LENGTH))
        if code not in _url_by_code:
            return code


@app.post("/shorten")
def shorten(request: ShortenRequest) -> ShortenResponse:
    """
    Create (or reuse) a short code for the given URL.

    Idempotency: URLs are looked up in `_code_by_url` first. Submitting
    the same URL twice returns the same code both times instead of
    minting a new one -- this is the whole reason a reverse (url -> code)
    index is kept alongside the forward (code -> url) one.
    """
    url = str(request.url)
    existing_code = _code_by_url.get(url)
    if existing_code is not None:
        return ShortenResponse(code=existing_code, short_url=f"/{existing_code}")

    code = _generate_unique_code()
    _url_by_code[code] = url
    _code_by_url[url] = code
    _clicks_by_code[code] = 0
    return ShortenResponse(code=code, short_url=f"/{code}")


@app.get("/{code}")
def redirect(code: str):
    """
    Redirect to the original URL for `code`, or 404 if it doesn't exist.
    Each successful redirect increments that code's click count.
    """
    url = _url_by_code.get(code)
    if url is None:
        raise HTTPException(status_code=404, detail="Unknown short code")
    _clicks_by_code[code] += 1
    return RedirectResponse(url=url, status_code=307)


@app.get("/stats/{code}")
def stats(code: str) -> dict:
    """
    Return click stats for `code`, or 404 if it doesn't exist. A code that
    exists but has never been visited reports clicks=0, not an error --
    `_clicks_by_code` is initialized to 0 the moment a code is created in
    shorten(), before any redirect has happened.
    """
    url = _url_by_code.get(code)
    if url is None:
        raise HTTPException(status_code=404, detail="Unknown short code")
    return {"code": code, "url": url, "clicks": _clicks_by_code[code]}
