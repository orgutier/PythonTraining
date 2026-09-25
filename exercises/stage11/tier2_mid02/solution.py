"""
OpenCV: Hand Posture & Face Gesture Recognition -- Edge Detection on the Hand Silhouette
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


def detect_hand_edges(binary_mask, low: int, high: int):
    """cv2.Canny(binary_mask, low, high)."""
    raise NotImplementedError


def detect_hand_edges_default(binary_mask):
    """cv2.Canny(binary_mask, 50, 150)."""
    raise NotImplementedError


def count_edge_pixels(binary_mask, low: int, high: int) -> int:
    """int(np.count_nonzero(cv2.Canny(binary_mask, low, high)))."""
    raise NotImplementedError
