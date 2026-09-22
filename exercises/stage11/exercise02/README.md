# Color Conversion and Resizing

Implement:

- `to_grayscale(image)` -- `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`.
- `to_rgb(image)` -- `cv2.cvtColor(image, cv2.COLOR_BGR2RGB)` -- OpenCV reads/stores images in **BGR** order by default, not RGB; this is the conversion you need before handing an image to almost any other library (matplotlib, PIL, ...).
- `resize_image(image, width: int, height: int)` -- `cv2.resize(image, (width, height))` -- note the argument order here **is** `(width, height)`, the opposite of `.shape`'s `(height, width)`.
- `resize_by_scale(image, scale: float)` -- `cv2.resize(image, None, fx=scale, fy=scale)` (scale both dimensions by a factor instead of specifying exact pixels).
- `get_shape_after_resize(image, width: int, height: int) -> tuple` -- resize with `resize_image`, then return the result's `.shape[:2]`.

See the Study Reference presentation, Topic 11, for the theory.
