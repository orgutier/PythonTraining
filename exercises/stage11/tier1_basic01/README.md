# Image I/O, Shape, and NumPy Arrays

An OpenCV image *is* a NumPy array -- `.shape` is a plain array attribute, not something OpenCV adds, and cropping is just array slicing. Implement:

- `load_image(path: str)` -- `cv2.imread(path)` (returns a NumPy array in BGR order, or `None` if the file can't be read).
- `save_image(path: str, image) -> bool` -- `cv2.imwrite(path, image)`.
- `get_dimensions(image) -> tuple` -- `image.shape[:2]`, i.e. `(height, width)` -- note **height first**, which trips up everyone coming from `(width, height)` conventions elsewhere.
- `get_channel_count(image) -> int` -- `image.shape[2]` if `image` has 3 dimensions (color), else `1` (grayscale images have no third dimension at all).
- `create_blank_image(height: int, width: int, channels: int)` -- `np.zeros((height, width, channels), dtype=np.uint8)`.
- `crop_image(image, y1: int, y2: int, x1: int, x2: int)` -- `image[y1:y2, x1:x2]` -- ordinary NumPy array slicing, rows (`y`) before columns (`x`), since that's the array's `(height, width, ...)` layout. There's no separate "crop function" in OpenCV, because the image is just an array.

See the Study Reference presentation, Topic 11 (Basic tier), for the theory.
