import pandas as pd


def sort_by_sales_desc(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("sales", ascending=False)


def sort_by_multiple(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(["region", "sales"], ascending=[True, False])


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region")["sales"].sum()


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    return df.groupby(["region", "product"])["sales"].mean()


def orders_per_region_sorted(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region").size().sort_values(ascending=False)
