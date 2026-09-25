"""
OpenCV -- Edge Detection with Canny
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_tier2_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/tier2_mid02/ and import it as a submodule (e.g.
`from exercises.stage11.tier2_mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2
import numpy as np


def detect_edges(gray_image, low: int, high: int):
    """cv2.Canny(gray_image, low, high)."""
    raise NotImplementedError


def detect_edges_default(gray_image):
    """cv2.Canny(gray_image, 100, 200)."""
    raise NotImplementedError


def count_edge_pixels(gray_image, low: int, high: int) -> int:
    """int(np.count_nonzero(cv2.Canny(gray_image, low, high)))."""
    raise NotImplementedError
