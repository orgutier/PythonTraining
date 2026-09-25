# Inspecting, Pivoting, and Multi-Indexing

Implement:

- `capture_info(df: pd.DataFrame) -> str` -- `df.info()` prints straight to stdout and returns `None`, so to actually *get* the text back, redirect it: `buf = io.StringIO(); df.info(buf=buf); return buf.getvalue()`.
- `avg_sales_by_region_and_product(df) -> pd.Series` -- `df.groupby(["region", "product"])["sales"].mean()` -- grouping by *two* columns produces a result indexed by a **`MultiIndex`** of `(region, product)` pairs, instead of a single flat index.
- `sales_pivot_table(df) -> pd.DataFrame` -- `df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")` (regions as rows, products as columns, total sales as the cell values).
- `sales_pivot_count(df) -> pd.DataFrame` -- same shape, but `aggfunc="count"` instead of `"sum"` (how many orders per region/product, not their total).

See the Study Reference presentation, Topic 10 (Advanced tier), for the theory.
