"""
Pandas -- Inspecting, Pivoting, and Multi-Indexing
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage10_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage10/advanced01/ and import it as a submodule (e.g.
`from exercises.stage10.advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import io
import pandas as pd


def capture_info(df: pd.DataFrame) -> str:
    """df.info() redirected into a string via io.StringIO()."""
    raise NotImplementedError


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    """df.groupby(["region", "product"])["sales"].mean() -- a MultiIndex result."""
    raise NotImplementedError


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    """df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")."""
    raise NotImplementedError


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    """Same shape as sales_pivot_table, but aggfunc="count"."""
    raise NotImplementedError
