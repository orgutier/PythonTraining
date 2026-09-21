# Merging and Pivoting

Implement:

- `merge_customer_info(orders_df, customers_df) -> pd.DataFrame` -- `orders_df.merge(customers_df, on="customer_id")` (an inner join by default -- only matching rows survive).
- `merge_with_suffixes(df1, df2) -> pd.DataFrame` -- `df1.merge(df2, on="id", how="left", suffixes=("_left", "_right"))` -- `how="left"` keeps every row of `df1` even without a match; `suffixes` disambiguates any other same-named columns from each side.
- `inner_join_products(orders_df, products_df) -> pd.DataFrame` -- `orders_df.merge(products_df, on="product_id", how="inner")`.
- `sales_pivot_table(df) -> pd.DataFrame` -- `df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")` (regions as rows, products as columns, total sales as the cell values).
- `sales_pivot_count(df) -> pd.DataFrame` -- same shape, but `aggfunc="count"` instead of `"sum"` (how many orders per region/product, not their total).

See the Study Reference presentation, Topic 10, for the theory.
