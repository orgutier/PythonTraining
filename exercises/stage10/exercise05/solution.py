"""
Pandas -- Apply and Dtype Optimization
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage10_exercise05.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage10/exercise05/ and import it as a submodule (e.g.
`from exercises.stage10.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import pandas as pd


def _categorize_amount(x):
    if x < 100:
        return "low"
    if x < 300:
        return "medium"
    return "high"


def add_sales_tax_column(df: pd.DataFrame, rate: float) -> pd.DataFrame:
    """Copy of df with a "total" column: sales * (1 + rate), via .apply()."""
    raise NotImplementedError


def categorize_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Copy of df with a "tier" column: "low"/"medium"/"high", via .apply()."""
    raise NotImplementedError


def full_name_column(df: pd.DataFrame) -> pd.DataFrame:
    """Copy of df with a "full_name" column, via row-wise .apply(axis=1)."""
    raise NotImplementedError


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Copy of df with "region" cast to the "category" dtype."""
    raise NotImplementedError


def set_region_product_index(df: pd.DataFrame) -> pd.DataFrame:
    """df.set_index(["region", "product"])."""
    raise NotImplementedError
