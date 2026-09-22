# Apply and Dtype Optimization

Implement:

- `add_sales_tax_column(df, rate: float) -> pd.DataFrame` -- return a copy with a new `"total"` column: `df["sales"].apply(lambda x: round(x * (1 + rate), 2))`.
- `categorize_sales(df) -> pd.DataFrame` -- return a copy with a new `"tier"` column via `df["sales"].apply(categorize_amount)`, where `categorize_amount(x)` returns `"low"` (`x < 100`), `"medium"` (`100 <= x < 300`), or `"high"` (`x >= 300`).
- `full_name_column(df) -> pd.DataFrame` -- return a copy with a new `"full_name"` column via **row-wise** apply: `df.apply(lambda row: f"{row['first']} {row['last']}", axis=1)` (`axis=1` runs the function once per *row* instead of once per column -- the other common shape of `.apply()`).
- `optimize_dtypes(df) -> pd.DataFrame` -- return a copy with `region` cast to the `"category"` dtype (`df.astype({"region": "category"})`) -- a column with few distinct repeated string values takes far less memory as a `category` than as `object`.
- `set_region_product_index(df) -> pd.DataFrame` -- `df.set_index(["region", "product"])` -- another way to get a `MultiIndex`, this time explicitly instead of as a side effect of `groupby`.

See the Study Reference presentation, Topic 10, for the theory.
