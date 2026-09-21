import pandas as pd


def filter_by_region(df: pd.DataFrame, region: str) -> pd.DataFrame:
    return df[df["region"] == region]


def filter_high_sales(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    return df[df["sales"] > threshold]


def filter_multiple_conditions(df: pd.DataFrame, region: str, threshold: float) -> pd.DataFrame:
    return df[(df["region"] == region) & (df["sales"] > threshold)]
