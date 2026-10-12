"""
OpenCV: Hand Posture & Face Gesture Recognition -- Hand Posture via Contours and Convexity Defects
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
import numpy as np

MIN_DEFECT_DEPTH = 8.0


def preprocess_hand_mask(mask):
    """GaussianBlur(mask, (5, 5), 0), then an explicit binary threshold pass."""
    raise NotImplementedError


def find_hand_contour(binary_mask):
    """The largest contour from cv2.findContours(binary_mask, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)."""
    raise NotImplementedError


def count_extended_fingers(binary_mask) -> int:
    """Convex hull + convexity defects on find_hand_contour(...); count defects deeper than MIN_DEFECT_DEPTH."""
    raise NotImplementedError


def classify_hand_posture(binary_mask) -> str:
    """"fist" if count_extended_fingers == 0, "open_hand" if >= 4, else "partial"."""
    raise NotImplementedError
