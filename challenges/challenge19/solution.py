"""
Challenge 19 - Sales Data Analyzer
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge19.py / `python tools/cli.py test challenge19`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (pd.read_csv(), groupby()+sort_values() with zero explicit Python loops, boolean indexing, pivot_table(), and category-dtype memory optimization).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


import pandas as pd


def load_orders(path: str) -> pd.DataFrame:
    """pd.read_csv(path)."""
    raise NotImplementedError


def revenue_by_region(df: pd.DataFrame) -> pd.Series:
    """Total revenue per region, highest first."""
    raise NotImplementedError


def top_customers(df: pd.DataFrame, n: int) -> pd.Series:
    """The n customers with the highest total revenue, highest first."""
    raise NotImplementedError


def high_value_orders(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """Rows whose revenue exceeds threshold, via boolean indexing."""
    raise NotImplementedError


def region_product_pivot(df: pd.DataFrame) -> pd.DataFrame:
    """Regions x products, total revenue as values, via df.pivot_table()."""
    raise NotImplementedError


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """A copy of df with region/product/customer cast to "category"."""
    raise NotImplementedError
