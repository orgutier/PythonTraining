import pandas as pd


def load_sales_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region")["sales"].sum()


def top_n_products(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.sort_values("sales", ascending=False).head(n)
