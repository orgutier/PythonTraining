"""
Challenge 02 - Identity, Equality, and a Login Prompt
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge02.py / `python tools/cli.py test challenge02`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (explicit `is`/`is not` for identity, `is None` (not truthiness) for a missing argument, and input()/print() for the login prompt).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


def classify_pairs(items: list) -> dict:
    """Classify every (i, j), i < j pair; return counts. See README."""
    raise NotImplementedError


def dedupe_by_identity(items: list) -> list:
    """Keep only the first occurrence of each distinct OBJECT (`is`), order preserved."""
    raise NotImplementedError


def dedupe_by_equality(items: list) -> list:
    """Keep only the first occurrence of each distinct VALUE (`==`), order preserved."""
    raise NotImplementedError


def prompt_login(username: str = None) -> str:
    """If username is None, input() one; then input() a password; print a welcome; return the username."""
    raise NotImplementedError
