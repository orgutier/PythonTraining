"""
OpenCV -- NumPy Arrays and Cascade Classifiers
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week11.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week11/exercise06/ and import it as a submodule (e.g.
`from exercises.week11.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2
import numpy as np


def create_blank_image(height: int, width: int, channels: int):
    """np.zeros((height, width, channels), dtype=np.uint8)."""
    raise NotImplementedError


def crop_image(image, y1: int, y2: int, x1: int, x2: int):
    """image[y1:y2, x1:x2] -- rows (y) before columns (x)."""
    raise NotImplementedError


def paste_region(image, region, y: int, x: int):
    """Paste region into a COPY of image at (y, x); return the copy."""
    raise NotImplementedError


def load_default_face_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")."""
    raise NotImplementedError


def load_cascade_from_path(path: str):
    """cv2.CascadeClassifier(path)."""
    raise NotImplementedError


def is_cascade_loaded(cascade) -> bool:
    """not cascade.empty()."""
    raise NotImplementedError
