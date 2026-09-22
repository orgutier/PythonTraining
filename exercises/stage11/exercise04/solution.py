"""
OpenCV -- Thresholding and Blurring
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_exercise04.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/exercise04/ and import it as a submodule (e.g.
`from exercises.stage11.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2


def apply_threshold(gray_image, thresh_value: int):
    """cv2.threshold(gray_image, thresh_value, 255, cv2.THRESH_BINARY)[1]."""
    raise NotImplementedError


def apply_otsu_threshold(gray_image):
    """cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]."""
    raise NotImplementedError


def apply_adaptive_threshold(gray_image):
    """cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)."""
    raise NotImplementedError


def apply_gaussian_blur(image, ksize: int):
    """cv2.GaussianBlur(image, (ksize, ksize), 0)."""
    raise NotImplementedError


def apply_strong_blur(image):
    """cv2.GaussianBlur(image, (15, 15), 0)."""
    raise NotImplementedError
