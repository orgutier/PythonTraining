import pandas as pd


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(customers_df, on="customer_id")


def merge_with_suffixes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.merge(df2, on="id", how="left", suffixes=("_left", "_right"))


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(products_df, on="product_id", how="inner")


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="count")
