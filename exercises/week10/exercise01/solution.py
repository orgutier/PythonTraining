"""
Pandas -- Reading and Inspecting
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week10_exercise01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week10/exercise01/ and import it as a submodule (e.g.
`from exercises.week10.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import io
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """pd.read_csv(path)."""
    raise NotImplementedError


def preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """df.head(n)."""
    raise NotImplementedError


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """df.describe()."""
    raise NotImplementedError


def capture_info(df: pd.DataFrame) -> str:
    """df.info() redirected into a string via io.StringIO()."""
    raise NotImplementedError
