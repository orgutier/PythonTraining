"""
OpenCV -- Image I/O, Shape, and NumPy Arrays
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/basic01/ and import it as a submodule (e.g.
`from exercises.stage11.basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2
import numpy as np


def load_image(path: str):
    """cv2.imread(path)."""
    raise NotImplementedError


def save_image(path: str, image) -> bool:
    """cv2.imwrite(path, image)."""
    raise NotImplementedError


def get_dimensions(image) -> tuple:
    """image.shape[:2] -- (height, width)."""
    raise NotImplementedError


def get_channel_count(image) -> int:
    """image.shape[2] if 3-dimensional, else 1."""
    raise NotImplementedError


def create_blank_image(height: int, width: int, channels: int):
    """np.zeros((height, width, channels), dtype=np.uint8)."""
    raise NotImplementedError


def crop_image(image, y1: int, y2: int, x1: int, x2: int):
    """image[y1:y2, x1:x2] -- rows (y) before columns (x)."""
    raise NotImplementedError
