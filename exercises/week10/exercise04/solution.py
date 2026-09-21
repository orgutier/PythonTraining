"""
Pandas -- Merging and Pivoting
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week10.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week10/exercise04/ and import it as a submodule (e.g.
`from exercises.week10.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import pandas as pd


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(customers_df, on="customer_id")."""
    raise NotImplementedError


def merge_with_suffixes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """df1.merge(df2, on="id", how="left", suffixes=("_left", "_right"))."""
    raise NotImplementedError


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(products_df, on="product_id", how="inner")."""
    raise NotImplementedError


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    """df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")."""
    raise NotImplementedError


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    """Same shape as sales_pivot_table, but aggfunc="count"."""
    raise NotImplementedError
