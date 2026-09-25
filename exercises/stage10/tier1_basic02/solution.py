"""
Pandas -- Reading and Inspecting Employee Data
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage10_tier1_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage10/tier1_basic02/ and import it as a submodule (e.g.
`from exercises.stage10.tier1_basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import pandas as pd


def load_employees(path: str) -> pd.DataFrame:
    """pd.read_csv(path)."""
    raise NotImplementedError


def preview_employees(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """df.head(n)."""
    raise NotImplementedError


def salary_summary(df: pd.DataFrame) -> pd.DataFrame:
    """df.describe()."""
    raise NotImplementedError


def column_names(df: pd.DataFrame) -> list:
    """list(df.columns)."""
    raise NotImplementedError


def row_count(df: pd.DataFrame) -> int:
    """len(df)."""
    raise NotImplementedError
