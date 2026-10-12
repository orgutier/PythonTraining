# Challenge 22 — Face-Region Redactor

**Do this after:** Stage 11 (OpenCV)
**Correctness is pytest-tested:** `python tools/cli.py test challenge22` (or `pytest tests/test_challenge22.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 21: a small privacy tool that detects faces with
a Haar cascade classifier and blacks them out, plus a thresholded
"redaction-ready" binary version of the image -- the file I/O and
thresholding half of Stage 11 that Challenge 21 didn't need.

Implement:

```python
def load_default_face_cascade():
    """A cv2.CascadeClassifier loaded from OpenCV's bundled haarcascade_frontalface_default.xml."""

def load_grayscale(path: str):
    """cv2.imread(path, cv2.IMREAD_GRAYSCALE)."""

def detect_faces(gray_image, cascade) -> list:
    """Every (x, y, w, h) box cascade.detectMultiScale finds in gray_image (scaleFactor=1.1, minNeighbors=5)."""

def redact_regions(image, boxes: list):
    """A COPY of image with every box filled solid black (cv2.rectangle, thickness=-1) -- boxes are clipped to stay inside image's own bounds first."""

def adaptive_binary(gray_image):
    """cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)."""

def save_redacted(image, path: str) -> bool:
    """cv2.imwrite(path, image)."""
```

```python
cascade = load_default_face_cascade()
gray = load_grayscale("photo.jpg")
boxes = detect_faces(gray, cascade)
redacted = redact_regions(photo, boxes)
save_redacted(redacted, "photo_redacted.jpg")
```

## Constraints on HOW you write it

1. **`load_default_face_cascade` must use `cv2.data.haarcascades +
   "haarcascade_frontalface_default.xml"`** as the path passed to
   `cv2.CascadeClassifier(...)` -- OpenCV ships this cascade, no external
   download needed.
2. **`detect_faces` must call `cascade.detectMultiScale(gray_image,
   scaleFactor=1.1, minNeighbors=5)`** and return it as a plain `list` of
   `(x, y, w, h)` tuples (the raw return value is a NumPy array, or an
   empty tuple when nothing's found -- normalize both into a `list`).
3. **`redact_regions` must clip every box to `image`'s own bounds
   first**, using `image.shape[:2]` -- a box that a detector reports
   slightly outside the frame must not crash `cv2.rectangle`, just get
   clamped.
4. **`redact_regions` must draw filled (`thickness=-1`), solid black
   (`(0, 0, 0)`) rectangles**, on a copy -- never mutate the caller's
   `image`.
5. **`adaptive_binary` must use `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`**
   specifically (not `..._MEAN_C`), with a block size of `11` and `C` of
   `2`.
6. **A docstring on `detect_faces`** listing edge cases: an image with no
   detectable faces at all (returns `[]`, not an error -- this is the
   expected, common case for a plain synthetic test image), and
   confirming the return type is always a `list`, never the raw NumPy
   array `detectMultiScale` returns internally.
