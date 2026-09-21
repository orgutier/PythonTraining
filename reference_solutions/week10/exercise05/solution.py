import pandas as pd


def _categorize_amount(x):
    if x < 100:
        return "low"
    if x < 300:
        return "medium"
    return "high"


def add_sales_tax_column(df: pd.DataFrame, rate: float) -> pd.DataFrame:
    result = df.copy()
    result["total"] = df["sales"].apply(lambda x: round(x * (1 + rate), 2))
    return result


def categorize_sales(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["tier"] = df["sales"].apply(_categorize_amount)
    return result


def full_name_column(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["full_name"] = df.apply(lambda row: f"{row['first']} {row['last']}", axis=1)
    return result


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    return df.astype({"region": "category"})


def set_region_product_index(df: pd.DataFrame) -> pd.DataFrame:
    return df.set_index(["region", "product"])
