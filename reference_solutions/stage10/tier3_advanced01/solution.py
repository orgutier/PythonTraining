import io
import pandas as pd


def capture_info(df: pd.DataFrame) -> str:
    buf = io.StringIO()
    df.info(buf=buf)
    return buf.getvalue()


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    return df.groupby(["region", "product"])["sales"].mean()


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="count")
