# Challenge 05 — URL Shortener API

**Do this after:** Week 13 (FastAPI)
**Not pytest-tested.** Grade it yourself against the constraints below.

## Problem

Build a minimal URL-shortener REST API -- "write me a URL shortener" is one
of the most common "design + code it live" interview exercises, because it
compresses routing, data modeling, validation, and a real design decision
(how do you generate a short code?) into something codeable in under an
hour.

## Required endpoints

| Method & path | Behavior |
|---|---|
| `POST /shorten` | Body: `{"url": "https://example.com/very/long/path"}`. Creates a short code for the URL (reusing the existing code if that exact URL was already shortened) and returns `{"code": "...", "short_url": "/abc123"}`. |
| `GET /{code}` | Redirects (HTTP 307) to the original URL if `code` exists; otherwise returns a 404. Each successful redirect increments that code's click count. |
| `GET /stats/{code}` | Returns `{"code": "...", "url": "...", "clicks": N}` if `code` exists; otherwise 404. |

Storage is **in-memory only** -- a plain Python dict at module scope is
fine. No database, no file persistence; state resets when the process
restarts.

## Constraints on HOW you write it

1. **Request and response bodies must be Pydantic `BaseModel` classes**,
   not raw dicts passed straight through -- define at least a
   `ShortenRequest` (the incoming `{"url": ...}`) and a `ShortenResponse`
   (the outgoing `{"code", "short_url"}`) model, matching Week 13's
   lesson on typed validation instead of untyped dicts.
2. **Reject invalid URLs with a proper 4xx response**, not a silent
   failure or a 500. Use Pydantic's URL validation on the request model
   (or explicit validation in the handler) so `POST /shorten` with
   `{"url": "not a url"}` returns a 422 with a useful error message.
3. **Submitting the same URL twice must return the same code** both times
   -- don't generate a new code (and waste one) for a URL you've already
   shortened. Document in a docstring how you detect "already shortened."
4. **A short code, once generated, must never collide with an existing
   one.** Document your code-generation strategy (length, character set,
   collision handling) in a docstring on the generation function.
5. **A docstring (module-level or per-function) with a comprehensive list
   of the edge cases your implementation handles:** an empty/missing `url`
   field, a URL submitted a second time, `GET` on a code that was never
   created, and `GET /stats` on a code that exists but has never been
   clicked (clicks should read 0, not error).

## Try it yourself

FastAPI's `TestClient` (Week 13) calls the app in-process -- use it in a
scratch script (not a pytest file, per this challenge's rules) to walk
through: shorten a URL, redirect through it twice, check `/stats` shows 2
clicks, submit the same URL again and confirm you get the same code back,
and confirm an invalid URL and an unknown code both come back as errors
instead of crashing the server.
