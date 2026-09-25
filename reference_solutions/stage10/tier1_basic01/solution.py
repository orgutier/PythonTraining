import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.head(n)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()
