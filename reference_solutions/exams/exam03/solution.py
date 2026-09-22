"""
Exam 3 -- Product Analytics & Photo Pipeline API (Stages 10-13). Reference solution.
"""
import concurrent.futures
import threading

import cv2
import numpy as np
import pandas as pd
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel


# --------------------------------------------------------------------------- Stage 10

def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .reset_index(drop=True)
    )


def pivot_revenue_by_region_and_month(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(values="revenue", index="region", columns="month", aggfunc="sum", fill_value=0)


def merge_with_targets(sales_df: pd.DataFrame, targets_df: pd.DataFrame) -> pd.DataFrame:
    summary = sales_by_category(sales_df)
    merged = summary.merge(targets_df, on="category")
    merged["pct_of_target"] = merged["revenue"] / merged["target"]
    return merged


def flag_underperforming(merged_df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    return merged_df[merged_df["pct_of_target"] < threshold].reset_index(drop=True)


# --------------------------------------------------------------------------- Stage 11

def preprocess_product_photo(image: np.ndarray) -> dict:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    return {"gray": gray, "blurred": blurred, "thresh": thresh}


def crop_to_largest_contour(image: np.ndarray) -> np.ndarray:
    thresh = preprocess_product_photo(image)["thresh"]
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return image
    largest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest)
    return image[y:y + h, x:x + w]


def compute_brightness(image: np.ndarray) -> float:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return float(np.mean(gray))


# --------------------------------------------------------------------------- Stage 12

class ThreadSafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._value = 0

    def increment(self):
        with self._lock:
            self._value += 1

    @property
    def value(self):
        with self._lock:
            return self._value


def fetch_all_metadata_concurrently(session, urls, counter, max_workers=4):
    def _fetch(url):
        response = session.get(url)
        response.raise_for_status()
        data = response.json()
        counter.increment()
        return data

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(_fetch, urls))


# --------------------------------------------------------------------------- Stage 13

class SalesSummary(BaseModel):
    category: str
    revenue: float


_sales_df = pd.DataFrame(columns=["category", "region", "month", "revenue"])
_targets_df = pd.DataFrame(columns=["category", "target"])
_photo_counter = ThreadSafeCounter()


def get_sales_dataframe() -> pd.DataFrame:
    return _sales_df


def get_targets_dataframe() -> pd.DataFrame:
    return _targets_df


def get_photo_counter() -> ThreadSafeCounter:
    return _photo_counter


app = FastAPI()


@app.get("/sales/summary", response_model=list[SalesSummary])
def sales_summary(df: pd.DataFrame = Depends(get_sales_dataframe)):
    return sales_by_category(df).to_dict("records")


@app.get("/sales/underperforming")
def underperforming(
    threshold: float = Query(0.5, ge=0, le=1),
    sales_df: pd.DataFrame = Depends(get_sales_dataframe),
    targets_df: pd.DataFrame = Depends(get_targets_dataframe),
):
    merged = merge_with_targets(sales_df, targets_df)
    flagged = flag_underperforming(merged, threshold)
    return flagged.to_dict("records")


@app.get("/photos/fetch-count")
def photo_fetch_count(counter: ThreadSafeCounter = Depends(get_photo_counter)):
    return {"count": counter.value}
