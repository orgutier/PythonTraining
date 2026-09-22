"""
OpenCV -- Edges and Contours
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_exercise05.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/exercise05/ and import it as a submodule (e.g.
`from exercises.stage11.exercise05 import helpers`) -- solution.py just has to
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


def find_contours(binary_image) -> list:
    """cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]."""
    raise NotImplementedError


def count_contours(binary_image) -> int:
    """len(find_contours(binary_image))."""
    raise NotImplementedError


def largest_contour_area(binary_image) -> float:
    """max(cv2.contourArea(c) for c in find_contours(binary_image))."""
    raise NotImplementedError
