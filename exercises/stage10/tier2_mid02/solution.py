"""
Pandas -- Sorting, Grouping, and Merging
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage10_tier2_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage10/tier2_mid02/ and import it as a submodule (e.g.
`from exercises.stage10.tier2_mid02 import helpers`) -- solution.py just has to
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


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(customers_df, on="customer_id")."""
    raise NotImplementedError


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(products_df, on="product_id", how="inner")."""
    raise NotImplementedError
