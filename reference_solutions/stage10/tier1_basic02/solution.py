import pandas as pd


def load_employees(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preview_employees(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.head(n)


def salary_summary(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()


def column_names(df: pd.DataFrame) -> list:
    return list(df.columns)


def row_count(df: pd.DataFrame) -> int:
    return len(df)
