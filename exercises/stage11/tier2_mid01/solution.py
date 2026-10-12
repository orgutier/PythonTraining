"""
OpenCV: Hand Posture & Face Gesture Recognition -- Skin-Tone Thresholding for Hand Segmentation
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_tier2_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/tier2_mid01/ and import it as a submodule (e.g.
`from exercises.stage11.tier2_mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2
import numpy as np

SKIN_HSV_LOWER = np.array([0, 20, 70], dtype=np.uint8)
SKIN_HSV_UPPER = np.array([20, 255, 255], dtype=np.uint8)


def to_hsv(frame):
    """cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)."""
    raise NotImplementedError


def segment_skin(frame, lower, upper):
    """cv2.inRange(to_hsv(frame), lower, upper)."""
    raise NotImplementedError


def refine_mask(mask):
    """cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]."""
    raise NotImplementedError
