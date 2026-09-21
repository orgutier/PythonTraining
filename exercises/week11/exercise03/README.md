# Drawing on Images

Implement:

- `draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple)` -- work on **a copy** (`image.copy()`, since `cv2.rectangle` draws in place) and `cv2.rectangle(copy, pt1, pt2, color, thickness=2)`, returning the copy.
- `draw_filled_rectangle(image, pt1, pt2, color)` -- same, but `thickness=-1` (negative thickness means "filled", not "outline").
- `draw_bounding_boxes(image, boxes: list, color: tuple)` -- work on a copy; `cv2.rectangle(copy, (x1, y1), (x2, y2), color, 2)` once per `(x1, y1, x2, y2)` tuple in `boxes`, then return the copy.

Always drawing onto a copy (never the original `image` parameter) matters because `cv2.rectangle`/similar drawing functions mutate the array they're given -- without copying first, calling one of these twice on the same source image would compound, and the caller's original image would silently change too.

See the Study Reference presentation, Topic 11, for the theory.
