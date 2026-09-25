# Color Conversion, Resizing, and Drawing

Implement:

- `to_grayscale(image)` -- `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`.
- `to_rgb(image)` -- `cv2.cvtColor(image, cv2.COLOR_BGR2RGB)` -- OpenCV reads/stores images in **BGR** order by default, not RGB; this is the conversion you need before handing an image to almost any other library (matplotlib, PIL, ...).
- `resize_image(image, width: int, height: int)` -- `cv2.resize(image, (width, height))` -- note the argument order here **is** `(width, height)`, the opposite of `.shape`'s `(height, width)`.
- `resize_by_scale(image, scale: float)` -- `cv2.resize(image, None, fx=scale, fy=scale)` (scale both dimensions by a factor instead of specifying exact pixels).
- `draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple)` -- work on **a copy** (`image.copy()`, since `cv2.rectangle` draws in place) and `cv2.rectangle(copy, pt1, pt2, color, thickness=2)`, returning the copy.
- `draw_bounding_boxes(image, boxes: list, color: tuple)` -- work on a copy; `cv2.rectangle(copy, (x1, y1), (x2, y2), color, 2)` once per `(x1, y1, x2, y2)` tuple in `boxes`, then return the copy. Always drawing onto a copy (never the original `image` parameter) matters because `cv2.rectangle` mutates the array it's given -- without copying first, calling this twice on the same source image would compound, and the caller's original image would silently change too.

See the Study Reference presentation, Topic 11 (Basic tier), for the theory.
