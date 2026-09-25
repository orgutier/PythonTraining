# Sorting, Grouping, and Merging

Implement:

- `sort_by_sales_desc(df) -> pd.DataFrame` -- `df.sort_values("sales", ascending=False)`.
- `sort_by_multiple(df) -> pd.DataFrame` -- `df.sort_values(["region", "sales"], ascending=[True, False])` (sort by `region` A-Z, and within each region by `sales` highest first).
- `total_sales_by_region(df) -> pd.Series` -- `df.groupby("region")["sales"].sum()`.
- `merge_customer_info(orders_df, customers_df) -> pd.DataFrame` -- `orders_df.merge(customers_df, on="customer_id")` (an inner join by default -- only matching rows survive).
- `inner_join_products(orders_df, products_df) -> pd.DataFrame` -- `orders_df.merge(products_df, on="product_id", how="inner")`.

See the Study Reference presentation, Topic 10 (Mid tier), for the theory.
