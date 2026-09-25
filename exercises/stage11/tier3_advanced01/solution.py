"""
OpenCV -- Blurring and Contours
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_tier3_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/tier3_advanced01/ and import it as a submodule (e.g.
`from exercises.stage11.tier3_advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2


def apply_gaussian_blur(image, ksize: int):
    """cv2.GaussianBlur(image, (ksize, ksize), 0)."""
    raise NotImplementedError


def apply_strong_blur(image):
    """cv2.GaussianBlur(image, (15, 15), 0)."""
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
