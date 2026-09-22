# NumPy Arrays and Cascade Classifiers

Implement:

- `create_blank_image(height: int, width: int, channels: int)` -- `np.zeros((height, width, channels), dtype=np.uint8)`.
- `crop_image(image, y1: int, y2: int, x1: int, x2: int)` -- `image[y1:y2, x1:x2]` -- ordinary NumPy array slicing, rows (`y`) before columns (`x`), since that's the array's `(height, width, ...)` layout. This *is* how you crop in OpenCV -- there's no separate "crop function", because the image is just an array.
- `paste_region(image, region, y: int, x: int)` -- copy `region` into `image` (a copy of it, so the original isn't mutated) starting at row `y`, column `x`: `result[y:y + region.shape[0], x:x + region.shape[1]] = region`; return `result`.
- `load_default_face_cascade()` -- `cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")`, one of the pretrained detectors OpenCV ships with.
- `load_cascade_from_path(path: str)` -- `cv2.CascadeClassifier(path)` (the general form, for a cascade file you supply yourself).
- `is_cascade_loaded(cascade) -> bool` -- `not cascade.empty()` -- `.empty()` is `True` when the classifier failed to load (e.g. a bad path), so this is how you check a load actually worked before trying to use it.

See the Study Reference presentation, Topic 11, for the theory.
