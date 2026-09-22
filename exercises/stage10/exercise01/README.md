# Reading and Inspecting

Implement:

- `load_csv(path: str) -> pd.DataFrame` -- `pd.read_csv(path)`.
- `preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame` -- `df.head(n)`.
- `summarize(df: pd.DataFrame) -> pd.DataFrame` -- `df.describe()` (count/mean/std/min/max/quartiles for every numeric column).
- `capture_info(df: pd.DataFrame) -> str` -- `df.info()` prints straight to stdout and returns `None`, so to actually *get* the text back, redirect it: `buf = io.StringIO(); df.info(buf=buf); return buf.getvalue()`.

See the Study Reference presentation, Topic 10, for the theory.
