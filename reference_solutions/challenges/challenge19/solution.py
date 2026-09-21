import pandas as pd


def load_orders(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def revenue_by_region(df: pd.DataFrame) -> pd.Series:
    """
    Total revenue per region, highest first.

    Edge cases handled:
      - A region with only one order -> its sum is just that order's
        revenue.
      - Two regions tied for the same total -> both are returned; their
        relative order between ties is not asserted by the tests.
    """
    return df.groupby("region")["revenue"].sum().sort_values(ascending=False)


def top_customers(df: pd.DataFrame, n: int) -> pd.Series:
    return df.groupby("customer")["revenue"].sum().sort_values(ascending=False).head(n)


def high_value_orders(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    return df[df["revenue"] > threshold]


def region_product_pivot(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="revenue", aggfunc="sum")


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    return df.astype({"region": "category", "product": "category", "customer": "category"})
