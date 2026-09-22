"""
Pandas -- Boolean Indexing
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage10_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage10/exercise02/ and import it as a submodule (e.g.
`from exercises.stage10.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import pandas as pd


def filter_by_region(df: pd.DataFrame, region: str) -> pd.DataFrame:
    """df[df["region"] == region]."""
    raise NotImplementedError


def filter_high_sales(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """df[df["sales"] > threshold]."""
    raise NotImplementedError


def filter_multiple_conditions(df: pd.DataFrame, region: str, threshold: float) -> pd.DataFrame:
    """df[(df["region"] == region) & (df["sales"] > threshold)]."""
    raise NotImplementedError
