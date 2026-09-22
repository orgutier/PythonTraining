# Challenge 02 — Identity, Equality, and a Login Prompt

**Do this after:** Stage 01 (Python Fundamentals)
**Correctness is pytest-tested:** `python tools/cli.py test challenge02` (or `pytest tests/test_challenge02.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

"Is this the *same* object, or just an *equal* one?" comes up constantly in
real debugging (duplicate detection, cache invalidation, `None` vs a
falsy-but-present default). This challenge builds a small identity/equality
auditor, plus a tiny login prompt that gets the `None`-vs-falsy distinction
right -- both squarely Stage 1 material.

Implement four functions:

```python
def classify_pairs(items: list) -> dict[str, int]:
    """Every (i, j) with i < j: classify as "same_object", "equal_but_different", or "different". Return the counts."""

def dedupe_by_identity(items: list) -> list:
    """Keep only the FIRST occurrence of each distinct OBJECT (by `is`), order preserved."""

def dedupe_by_equality(items: list) -> list:
    """Keep only the first occurrence of each distinct VALUE (by `==`), order preserved."""

def prompt_login(username: str = None) -> str:
    """See below."""
```

```python
a = [1, 2]
b = [1, 2]          # equal to a, but a DIFFERENT object
c = a                # the SAME object as a
classify_pairs([a, b, c])
# pairs: (a,b) equal_but_different, (a,c) same_object, (b,c) equal_but_different
# -> {"same_object": 1, "equal_but_different": 2, "different": 0}
```

`dedupe_by_identity([a, b, c])` keeps `a` and `b` (two *different* objects,
even though `a == b`) but drops `c` (the same object as `a`) -> `[a, b]`.
`dedupe_by_equality([a, b, c])` keeps only `a` (or whichever comes first;
`b` and `c` are both `== a`) -> `[a]`.

`prompt_login`: if `username` **is** `None` (not just falsy -- an empty
string `""` is a valid, *different* case meaning "a blank username was
explicitly passed in", not "no username given"), call
`input("Username: ")` to get one interactively. Either way, then call
`input(f"Password for {the_username}: ")` (the password itself is never
validated or returned -- this isn't a security exercise), `print(f"Welcome,
{the_username}!")`, and return the username.

## Constraints on HOW you write it

1. **Identity comparisons must use `is`/`is not` explicitly** in
   `classify_pairs` and `dedupe_by_identity` -- never `==` where the
   question is "same object", and never `==` combined with `id(x) ==
   id(y)` as a workaround.
2. **`prompt_login`'s missing-argument check must be `username is None`**,
   not `if not username:` -- the latter would also treat `""` (empty
   string) as "not provided," which is a different, real case this
   function has to keep distinct.
3. **No `set()`/`dict` keyed by the items themselves** in
   `dedupe_by_equality` for the general case -- items here aren't
   guaranteed hashable (e.g. a `list`, as in the example above). Compare
   with `==` against what's already been kept, in a loop.
4. **Full type hints**, matching the signatures shown above.
5. **A docstring on `classify_pairs`** listing edge cases: an empty list
   and a single-item list (both have zero pairs), a list where every item
   is the exact same object, and a list containing `None`.
