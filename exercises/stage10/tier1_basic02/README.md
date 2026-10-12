# Reading and Inspecting Employee Data

Same three operations as the previous exercise, on a different dataset (columns `name`, `salary`), plus two more everyday DataFrame introspection helpers:

- `load_employees(path: str) -> pd.DataFrame` -- `pd.read_csv(path)`.
- `preview_employees(df: pd.DataFrame, n: int) -> pd.DataFrame` -- `df.head(n)`.
- `salary_summary(df: pd.DataFrame) -> pd.DataFrame` -- `df.describe()`.
- `column_names(df: pd.DataFrame) -> list` -- `list(df.columns)`.
- `row_count(df: pd.DataFrame) -> int` -- `len(df)`.

See the Study Reference presentation, Topic 10 (Basic tier), for the theory.
