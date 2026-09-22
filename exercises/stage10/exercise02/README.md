# Boolean Indexing

Implement three filters on a sales DataFrame (columns `region`, `product`, `sales`):

- `filter_by_region(df, region: str) -> pd.DataFrame` -- `df[df["region"] == region]`.
- `filter_high_sales(df, threshold: float) -> pd.DataFrame` -- `df[df["sales"] > threshold]`.
- `filter_multiple_conditions(df, region: str, threshold: float) -> pd.DataFrame` -- both at once: `df[(df["region"] == region) & (df["sales"] > threshold)]` (note `&`, not `and` -- pandas boolean masks need the element-wise operator, and each condition needs its own parentheses).

`df[boolean_series]` -- indexing a DataFrame with a same-length `Series` of `True`/`False` -- keeps only the rows where it's `True`. This is **boolean indexing**, the pandas equivalent of a list comprehension's `if` filter.

See the Study Reference presentation, Topic 10, for the theory.
