"""
Challenge 22 - Face-Region Redactor
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge22.py / `python tools/cli.py test challenge22`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (cv2.CascadeClassifier for detection, cv2.imread()/imwrite() for I/O, cv2.adaptiveThreshold() for the binary output, and image.shape-based box clipping).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import cv2


def load_default_face_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")."""
    raise NotImplementedError


def load_grayscale(path: str):
    """cv2.imread(path, cv2.IMREAD_GRAYSCALE)."""
    raise NotImplementedError


def detect_faces(gray_image, cascade) -> list:
    """cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5), normalized to a list."""
    raise NotImplementedError


def redact_regions(image, boxes: list):
    """A copy of image with every (clipped) box filled solid black."""
    raise NotImplementedError


def adaptive_binary(gray_image):
    """cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)."""
    raise NotImplementedError


def save_redacted(image, path: str) -> bool:
    """cv2.imwrite(path, image)."""
    raise NotImplementedError
