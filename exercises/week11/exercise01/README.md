# Image I/O and Shape

Implement:

- `load_image(path: str)` -- `cv2.imread(path)` (returns a NumPy array in BGR order, or `None` if the file can't be read).
- `save_image(path: str, image) -> bool` -- `cv2.imwrite(path, image)`.
- `get_dimensions(image) -> tuple` -- `image.shape[:2]`, i.e. `(height, width)` -- note **height first**, which trips up everyone coming from `(width, height)` conventions elsewhere.
- `get_channel_count(image) -> int` -- `image.shape[2]` if `image` has 3 dimensions (color), else `1` (grayscale images have no third dimension at all).

An OpenCV image *is* a NumPy array -- `.shape` is a plain array attribute, not something OpenCV adds.

See the Study Reference presentation, Topic 11, for the theory.
