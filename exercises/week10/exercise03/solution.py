"""
Pandas -- Sorting and Grouping
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week10_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week10/exercise03/ and import it as a submodule (e.g.
`from exercises.week10.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import pandas as pd


def sort_by_sales_desc(df: pd.DataFrame) -> pd.DataFrame:
    """df.sort_values("sales", ascending=False)."""
    raise NotImplementedError


def sort_by_multiple(df: pd.DataFrame) -> pd.DataFrame:
    """df.sort_values(["region", "sales"], ascending=[True, False])."""
    raise NotImplementedError


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    """df.groupby("region")["sales"].sum()."""
    raise NotImplementedError


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    """df.groupby(["region", "product"])["sales"].mean() -- a MultiIndex result."""
    raise NotImplementedError


def orders_per_region_sorted(df: pd.DataFrame) -> pd.Series:
    """df.groupby("region").size().sort_values(ascending=False)."""
    raise NotImplementedError
