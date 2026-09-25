import pandas as pd


def sort_by_sales_desc(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("sales", ascending=False)


def sort_by_multiple(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(["region", "sales"], ascending=[True, False])


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region")["sales"].sum()


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(customers_df, on="customer_id")


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(products_df, on="product_id", how="inner")
