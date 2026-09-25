"""
OpenCV: Hand Posture & Face Gesture Recognition -- Face Gesture and Gaze Direction (Driver-Camera Style)
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_tier3_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/tier3_advanced02/ and import it as a submodule (e.g.
`from exercises.stage11.tier3_advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2


def load_face_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")."""
    raise NotImplementedError


def load_eye_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")."""
    raise NotImplementedError


def load_smile_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")."""
    raise NotImplementedError


def is_cascade_loaded(cascade) -> bool:
    """not cascade.empty()."""
    raise NotImplementedError


def detect_smile(face_gray_region, smile_cascade) -> bool:
    """True if smile_cascade.detectMultiScale(face_gray_region, scaleFactor=1.7, minNeighbors=20) finds anything."""
    raise NotImplementedError


def estimate_gaze_direction(face_box: tuple, eye_boxes: list, off_axis_ratio: float = 0.15) -> str:
    """"looking_away" if no eyes; else "left"/"right"/"center" from the eye centroid vs. face center."""
    raise NotImplementedError
