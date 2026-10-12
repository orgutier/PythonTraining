# Preparing Frames for Detection

Every detector in this stage (skin thresholding, Haar cascades) needs frames prepared first. Implement:

- `to_grayscale(frame)` -- `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)` -- Haar cascades run on grayscale, never color.
- `resize_for_processing(frame, width: int, height: int)` -- `cv2.resize(frame, (width, height))` -- note the argument order here **is** `(width, height)`, the opposite of `.shape`'s `(height, width)`. Real pipelines resize every incoming frame to a fixed size first, so detection runs at a predictable, controllable cost.
- `draw_detection_box(frame, box: tuple, color: tuple, thickness: int = 2)` -- `box` is `(x, y, w, h)`. Work on **a copy** (`frame.copy()`, since `cv2.rectangle` draws in place) and `cv2.rectangle(copy, (x, y), (x + w, y + h), color, thickness)`, returning the copy.
- `draw_multiple_boxes(frame, boxes: list, color: tuple)` -- work on a copy; call `draw_detection_box`'s underlying `cv2.rectangle` logic once per `(x, y, w, h)` box in `boxes`, then return the copy. Always drawing onto a copy (never the original `frame` parameter) matters because `cv2.rectangle` mutates the array it's given -- without copying first, drawing detections on the same source frame twice would compound, and the caller's original frame would silently change too.

See the Study Reference presentation, Topic 11 (Basic tier), for the theory.
