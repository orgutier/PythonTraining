# Sorting and Grouping

Implement:

- `sort_by_sales_desc(df) -> pd.DataFrame` -- `df.sort_values("sales", ascending=False)`.
- `sort_by_multiple(df) -> pd.DataFrame` -- `df.sort_values(["region", "sales"], ascending=[True, False])` (sort by `region` A-Z, and within each region by `sales` highest first).
- `total_sales_by_region(df) -> pd.Series` -- `df.groupby("region")["sales"].sum()`.
- `avg_sales_by_region_and_product(df) -> pd.Series` -- `df.groupby(["region", "product"])["sales"].mean()` -- grouping by *two* columns produces a result indexed by a **`MultiIndex`** of `(region, product)` pairs, instead of a single flat index.
- `orders_per_region_sorted(df) -> pd.Series` -- `df.groupby("region").size().sort_values(ascending=False)` (how many rows per region, busiest region first).

See the Study Reference presentation, Topic 10, for the theory.
