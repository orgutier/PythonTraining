# Cascade Classifiers

Implement:

- `load_default_face_cascade()` -- `cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")`, one of the pretrained detectors OpenCV ships with.
- `load_cascade_from_path(path: str)` -- `cv2.CascadeClassifier(path)` (the general form, for a cascade file you supply yourself).
- `is_cascade_loaded(cascade) -> bool` -- `not cascade.empty()` -- `.empty()` is `True` when the classifier failed to load (e.g. a bad path), so this is how you check a load actually worked before trying to use it.

See the Study Reference presentation, Topic 11 (Advanced tier), for the theory.
