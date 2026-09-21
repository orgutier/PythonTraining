"""
Week 11 -- OpenCV.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: cv2.imread, cv2.imwrite, cv2.cvtColor, cv2.resize,
            cv2.rectangle, image.shape
  modules:  opencv-python (cv2), numpy
  methods:  cv2.Canny(), cv2.findContours(), cv2.GaussianBlur(),
            cv2.CascadeClassifier
  concepts: thresholding, convolution filtering

All test images are built synthetically with numpy (no external image files
needed), since images are just NumPy arrays -- that's the whole point of
this week.
"""

WEEK = "week11"
TOPIC = "OpenCV"
OVERVIEW = (
    "Six exercises covering every OpenCV function and image-array concept "
    "from Topic 11 at least three times each, using small synthetic images "
    "built with numpy so nothing here depends on an external image file."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Image I/O and Shape",
        "summary": "cv2.imread, cv2.imwrite, image.shape x2",
        "readme": (
            "Implement:\n\n"
            "- `load_image(path: str)` -- `cv2.imread(path)` (returns a "
            "NumPy array in BGR order, or `None` if the file can't be read).\n"
            "- `save_image(path: str, image) -> bool` -- "
            "`cv2.imwrite(path, image)`.\n"
            "- `get_dimensions(image) -> tuple` -- `image.shape[:2]`, i.e. "
            "`(height, width)` -- note **height first**, which trips up "
            "everyone coming from `(width, height)` conventions elsewhere.\n"
            "- `get_channel_count(image) -> int` -- `image.shape[2]` if "
            "`image` has 3 dimensions (color), else `1` (grayscale images "
            "have no third dimension at all).\n\n"
            "An OpenCV image *is* a NumPy array -- `.shape` is a plain "
            "array attribute, not something OpenCV adds.\n\n"
            "See the Study Reference presentation, Topic 11, for the theory."
        ),
        "stub": '''\
import cv2


def load_image(path: str):
    """cv2.imread(path)."""
    raise NotImplementedError


def save_image(path: str, image) -> bool:
    """cv2.imwrite(path, image)."""
    raise NotImplementedError


def get_dimensions(image) -> tuple:
    """image.shape[:2] -- (height, width)."""
    raise NotImplementedError


def get_channel_count(image) -> int:
    """image.shape[2] if 3-dimensional, else 1."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2


def load_image(path: str):
    return cv2.imread(path)


def save_image(path: str, image) -> bool:
    return cv2.imwrite(path, image)


def get_dimensions(image) -> tuple:
    return image.shape[:2]


def get_channel_count(image) -> int:
    return image.shape[2] if len(image.shape) == 3 else 1
''',
        "test": '''\
import numpy as np
from exercises.week11.exercise01.solution import (
    load_image,
    save_image,
    get_dimensions,
    get_channel_count,
)


def test_save_and_load_roundtrip(tmp_path):
    path = str(tmp_path / "img.png")
    original = np.zeros((20, 30, 3), dtype=np.uint8)
    original[:, :] = (0, 0, 255)
    assert save_image(path, original) is True
    loaded = load_image(path)
    assert loaded is not None
    assert loaded.shape == (20, 30, 3)


def test_load_missing_file_returns_none():
    assert load_image("/nonexistent/path/to/image.png") is None


def test_get_dimensions():
    image = np.zeros((20, 30, 3), dtype=np.uint8)
    assert get_dimensions(image) == (20, 30)


def test_get_channel_count_color():
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    assert get_channel_count(image) == 3


def test_get_channel_count_grayscale():
    image = np.zeros((10, 10), dtype=np.uint8)
    assert get_channel_count(image) == 1
''',
    },
    {
        "name": "exercise02",
        "title": "Color Conversion and Resizing",
        "summary": "cv2.cvtColor x2, cv2.resize x2, image.shape",
        "readme": (
            "Implement:\n\n"
            "- `to_grayscale(image)` -- `cv2.cvtColor(image, "
            "cv2.COLOR_BGR2GRAY)`.\n"
            "- `to_rgb(image)` -- `cv2.cvtColor(image, cv2.COLOR_BGR2RGB)` "
            "-- OpenCV reads/stores images in **BGR** order by default, not "
            "RGB; this is the conversion you need before handing an image "
            "to almost any other library (matplotlib, PIL, ...).\n"
            "- `resize_image(image, width: int, height: int)` -- "
            "`cv2.resize(image, (width, height))` -- note the argument "
            "order here **is** `(width, height)`, the opposite of "
            "`.shape`'s `(height, width)`.\n"
            "- `resize_by_scale(image, scale: float)` -- "
            "`cv2.resize(image, None, fx=scale, fy=scale)` (scale both "
            "dimensions by a factor instead of specifying exact pixels).\n"
            "- `get_shape_after_resize(image, width: int, height: int) -> tuple` "
            "-- resize with `resize_image`, then return the result's "
            "`.shape[:2]`.\n\n"
            "See the Study Reference presentation, Topic 11, for the theory."
        ),
        "stub": '''\
import cv2


def to_grayscale(image):
    """cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)."""
    raise NotImplementedError


def to_rgb(image):
    """cv2.cvtColor(image, cv2.COLOR_BGR2RGB)."""
    raise NotImplementedError


def resize_image(image, width: int, height: int):
    """cv2.resize(image, (width, height))."""
    raise NotImplementedError


def resize_by_scale(image, scale: float):
    """cv2.resize(image, None, fx=scale, fy=scale)."""
    raise NotImplementedError


def get_shape_after_resize(image, width: int, height: int) -> tuple:
    """resize_image(image, width, height).shape[:2]."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2


def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def resize_image(image, width: int, height: int):
    return cv2.resize(image, (width, height))


def resize_by_scale(image, scale: float):
    return cv2.resize(image, None, fx=scale, fy=scale)


def get_shape_after_resize(image, width: int, height: int) -> tuple:
    return resize_image(image, width, height).shape[:2]
''',
        "test": '''\
import numpy as np
from exercises.week11.exercise02.solution import (
    to_grayscale,
    to_rgb,
    resize_image,
    resize_by_scale,
    get_shape_after_resize,
)


def _bgr_image():
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    image[:, :] = (255, 0, 0)
    return image


def test_to_grayscale_drops_channel_dim():
    gray = to_grayscale(_bgr_image())
    assert gray.shape == (10, 10)


def test_to_rgb_swaps_channel_order():
    rgb = to_rgb(_bgr_image())
    assert tuple(rgb[0, 0]) == (0, 0, 255)


def test_resize_image():
    resized = resize_image(_bgr_image(), 20, 5)
    assert resized.shape[:2] == (5, 20)


def test_resize_by_scale():
    resized = resize_by_scale(_bgr_image(), 2.0)
    assert resized.shape[:2] == (20, 20)


def test_get_shape_after_resize():
    assert get_shape_after_resize(_bgr_image(), 40, 30) == (30, 40)
''',
    },
    {
        "name": "exercise03",
        "title": "Drawing on Images",
        "summary": "cv2.rectangle x3",
        "readme": (
            "Implement:\n\n"
            "- `draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple)` "
            "-- work on **a copy** (`image.copy()`, since `cv2.rectangle` "
            "draws in place) and `cv2.rectangle(copy, pt1, pt2, color, "
            "thickness=2)`, returning the copy.\n"
            "- `draw_filled_rectangle(image, pt1, pt2, color)` -- same, but "
            "`thickness=-1` (negative thickness means \"filled\", not "
            "\"outline\").\n"
            "- `draw_bounding_boxes(image, boxes: list, color: tuple)` -- "
            "work on a copy; `cv2.rectangle(copy, (x1, y1), (x2, y2), color, "
            "2)` once per `(x1, y1, x2, y2)` tuple in `boxes`, then return "
            "the copy.\n\n"
            "Always drawing onto a copy (never the original `image` "
            "parameter) matters because `cv2.rectangle`/similar drawing "
            "functions mutate the array they're given -- without copying "
            "first, calling one of these twice on the same source image "
            "would compound, and the caller's original image would silently "
            "change too.\n\n"
            "See the Study Reference presentation, Topic 11, for the theory."
        ),
        "stub": '''\
import cv2


def draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    """Draw an outlined rectangle on a COPY of image; return the copy."""
    raise NotImplementedError


def draw_filled_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    """Draw a FILLED rectangle (thickness=-1) on a copy; return the copy."""
    raise NotImplementedError


def draw_bounding_boxes(image, boxes: list, color: tuple):
    """Draw one rectangle per (x1, y1, x2, y2) in boxes, on a copy."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2


def draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    result = image.copy()
    cv2.rectangle(result, pt1, pt2, color, thickness=2)
    return result


def draw_filled_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    result = image.copy()
    cv2.rectangle(result, pt1, pt2, color, thickness=-1)
    return result


def draw_bounding_boxes(image, boxes: list, color: tuple):
    result = image.copy()
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(result, (x1, y1), (x2, y2), color, 2)
    return result
''',
        "test": '''\
import numpy as np
from exercises.week11.exercise03.solution import (
    draw_rectangle,
    draw_filled_rectangle,
    draw_bounding_boxes,
)


def test_draw_rectangle_does_not_mutate_original():
    image = np.zeros((20, 20, 3), dtype=np.uint8)
    result = draw_rectangle(image, (2, 2), (10, 10), (255, 255, 255))
    assert np.array_equal(image, np.zeros((20, 20, 3), dtype=np.uint8))
    assert result[2, 2].tolist() == [255, 255, 255]


def test_draw_filled_rectangle_fills_interior():
    image = np.zeros((20, 20, 3), dtype=np.uint8)
    result = draw_filled_rectangle(image, (2, 2), (10, 10), (255, 255, 255))
    assert result[5, 5].tolist() == [255, 255, 255]


def test_draw_bounding_boxes_draws_all():
    image = np.zeros((30, 30, 3), dtype=np.uint8)
    boxes = [(1, 1, 5, 5), (10, 10, 15, 15)]
    result = draw_bounding_boxes(image, boxes, (255, 0, 0))
    assert result[1, 1].tolist() == [255, 0, 0]
    assert result[10, 10].tolist() == [255, 0, 0]
''',
    },
    {
        "name": "exercise04",
        "title": "Thresholding and Blurring",
        "summary": "thresholding x3, cv2.GaussianBlur() x2, convolution filtering",
        "readme": (
            "Implement:\n\n"
            "- `apply_threshold(gray_image, thresh_value: int)` -- "
            "`cv2.threshold(gray_image, thresh_value, 255, "
            "cv2.THRESH_BINARY)[1]` (`cv2.threshold` returns "
            "`(used_threshold, result_image)` -- take `[1]`, the image).\n"
            "- `apply_otsu_threshold(gray_image)` -- "
            "`cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + "
            "cv2.THRESH_OTSU)[1]` -- Otsu's method picks the threshold "
            "value *automatically* from the image's histogram, so the "
            "`0` you pass for `thresh_value` is ignored.\n"
            "- `apply_adaptive_threshold(gray_image)` -- "
            "`cv2.adaptiveThreshold(gray_image, 255, "
            "cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)` -- "
            "picks a *different* threshold for each local neighborhood "
            "instead of one global value, useful when lighting is uneven "
            "across the image.\n"
            "- `apply_gaussian_blur(image, ksize: int)` -- "
            "`cv2.GaussianBlur(image, (ksize, ksize), 0)` (`ksize` must be "
            "odd).\n"
            "- `apply_strong_blur(image)` -- same idea with a fixed, larger "
            "kernel: `cv2.GaussianBlur(image, (15, 15), 0)`.\n\n"
            "Blurring is **convolution filtering**: a small kernel window "
            "slides over every pixel, replacing it with a weighted average "
            "of its neighbors -- a bigger kernel (as in `apply_strong_blur`) "
            "averages over a wider neighborhood, producing a blurrier "
            "result.\n\n"
            "See the Study Reference presentation, Topic 11, for the theory."
        ),
        "stub": '''\
import cv2


def apply_threshold(gray_image, thresh_value: int):
    """cv2.threshold(gray_image, thresh_value, 255, cv2.THRESH_BINARY)[1]."""
    raise NotImplementedError


def apply_otsu_threshold(gray_image):
    """cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]."""
    raise NotImplementedError


def apply_adaptive_threshold(gray_image):
    """cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)."""
    raise NotImplementedError


def apply_gaussian_blur(image, ksize: int):
    """cv2.GaussianBlur(image, (ksize, ksize), 0)."""
    raise NotImplementedError


def apply_strong_blur(image):
    """cv2.GaussianBlur(image, (15, 15), 0)."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2


def apply_threshold(gray_image, thresh_value: int):
    return cv2.threshold(gray_image, thresh_value, 255, cv2.THRESH_BINARY)[1]


def apply_otsu_threshold(gray_image):
    return cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def apply_adaptive_threshold(gray_image):
    return cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )


def apply_gaussian_blur(image, ksize: int):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)


def apply_strong_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)
''',
        "test": '''\
import numpy as np
from exercises.week11.exercise04.solution import (
    apply_threshold,
    apply_otsu_threshold,
    apply_adaptive_threshold,
    apply_gaussian_blur,
    apply_strong_blur,
)


def _half_bright_gray():
    image = np.zeros((20, 20), dtype=np.uint8)
    image[:, 10:] = 200
    return image


def test_apply_threshold():
    result = apply_threshold(_half_bright_gray(), 100)
    assert result[0, 0] == 0
    assert result[0, 15] == 255


def test_apply_otsu_threshold_separates_regions():
    result = apply_otsu_threshold(_half_bright_gray())
    assert result[0, 0] != result[0, 15]


def test_apply_adaptive_threshold_returns_binary_image():
    result = apply_adaptive_threshold(_half_bright_gray())
    assert result.shape == (20, 20)
    assert set(np.unique(result)).issubset({0, 255})


def test_apply_gaussian_blur_preserves_shape():
    image = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
    blurred = apply_gaussian_blur(image, 5)
    assert blurred.shape == image.shape


def test_apply_strong_blur_smooths_more_than_light_blur():
    image = np.zeros((30, 30), dtype=np.uint8)
    image[15, 15] = 255
    light = apply_gaussian_blur(image, 3)
    strong = apply_strong_blur(image)
    assert strong[15, 15] < light[15, 15]
''',
    },
    {
        "name": "exercise05",
        "title": "Edges and Contours",
        "summary": "cv2.Canny() x3, cv2.findContours() x3",
        "readme": (
            "Implement:\n\n"
            "- `detect_edges(gray_image, low: int, high: int)` -- "
            "`cv2.Canny(gray_image, low, high)`.\n"
            "- `detect_edges_default(gray_image)` -- "
            "`cv2.Canny(gray_image, 100, 200)` (commonly-used default "
            "thresholds).\n"
            "- `count_edge_pixels(gray_image, low: int, high: int) -> int` "
            "-- `int(np.count_nonzero(cv2.Canny(gray_image, low, high)))`.\n"
            "- `find_contours(binary_image) -> list` -- "
            "`cv2.findContours(binary_image, cv2.RETR_EXTERNAL, "
            "cv2.CHAIN_APPROX_SIMPLE)[0]` (the first element of the tuple "
            "is the list of contours; the second, ignored here, is the "
            "hierarchy).\n"
            "- `count_contours(binary_image) -> int` -- "
            "`len(find_contours(binary_image))`.\n"
            "- `largest_contour_area(binary_image) -> float` -- "
            "`max(cv2.contourArea(c) for c in find_contours(binary_image))`.\n\n"
            "See the Study Reference presentation, Topic 11, for the theory."
        ),
        "stub": '''\
import cv2
import numpy as np


def detect_edges(gray_image, low: int, high: int):
    """cv2.Canny(gray_image, low, high)."""
    raise NotImplementedError


def detect_edges_default(gray_image):
    """cv2.Canny(gray_image, 100, 200)."""
    raise NotImplementedError


def count_edge_pixels(gray_image, low: int, high: int) -> int:
    """int(np.count_nonzero(cv2.Canny(gray_image, low, high)))."""
    raise NotImplementedError


def find_contours(binary_image) -> list:
    """cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]."""
    raise NotImplementedError


def count_contours(binary_image) -> int:
    """len(find_contours(binary_image))."""
    raise NotImplementedError


def largest_contour_area(binary_image) -> float:
    """max(cv2.contourArea(c) for c in find_contours(binary_image))."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2
import numpy as np


def detect_edges(gray_image, low: int, high: int):
    return cv2.Canny(gray_image, low, high)


def detect_edges_default(gray_image):
    return cv2.Canny(gray_image, 100, 200)


def count_edge_pixels(gray_image, low: int, high: int) -> int:
    return int(np.count_nonzero(cv2.Canny(gray_image, low, high)))


def find_contours(binary_image) -> list:
    return cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]


def count_contours(binary_image) -> int:
    return len(find_contours(binary_image))


def largest_contour_area(binary_image) -> float:
    return max(cv2.contourArea(c) for c in find_contours(binary_image))
''',
        "test": '''\
import cv2
import numpy as np
from exercises.week11.exercise05.solution import (
    detect_edges,
    detect_edges_default,
    count_edge_pixels,
    find_contours,
    count_contours,
    largest_contour_area,
)


def _square_image():
    image = np.zeros((50, 50), dtype=np.uint8)
    cv2.rectangle(image, (10, 10), (30, 30), 255, -1)
    return image


def test_detect_edges_finds_something():
    edges = detect_edges(_square_image(), 50, 150)
    assert edges.sum() > 0


def test_detect_edges_default():
    edges = detect_edges_default(_square_image())
    assert edges.shape == (50, 50)


def test_count_edge_pixels():
    assert count_edge_pixels(_square_image(), 50, 150) > 0


def test_find_and_count_contours():
    contours = find_contours(_square_image())
    assert len(contours) == 1
    assert count_contours(_square_image()) == 1


def test_largest_contour_area():
    area = largest_contour_area(_square_image())
    assert 300 < area < 500
''',
    },
    {
        "name": "exercise06",
        "title": "NumPy Arrays and Cascade Classifiers",
        "summary": "numpy x3, images as arrays, cv2.CascadeClassifier x3",
        "readme": (
            "Implement:\n\n"
            "- `create_blank_image(height: int, width: int, channels: int)` "
            "-- `np.zeros((height, width, channels), dtype=np.uint8)`.\n"
            "- `crop_image(image, y1: int, y2: int, x1: int, x2: int)` -- "
            "`image[y1:y2, x1:x2]` -- ordinary NumPy array slicing, rows "
            "(`y`) before columns (`x`), since that's the array's "
            "`(height, width, ...)` layout. This *is* how you crop in "
            "OpenCV -- there's no separate \"crop function\", because the "
            "image is just an array.\n"
            "- `paste_region(image, region, y: int, x: int)` -- copy "
            "`region` into `image` (a copy of it, so the original isn't "
            "mutated) starting at row `y`, column `x`: "
            "`result[y:y + region.shape[0], x:x + region.shape[1]] = "
            "region`; return `result`.\n"
            "- `load_default_face_cascade()` -- "
            "`cv2.CascadeClassifier(cv2.data.haarcascades + "
            "\"haarcascade_frontalface_default.xml\")`, one of the "
            "pretrained detectors OpenCV ships with.\n"
            "- `load_cascade_from_path(path: str)` -- "
            "`cv2.CascadeClassifier(path)` (the general form, for a "
            "cascade file you supply yourself).\n"
            "- `is_cascade_loaded(cascade) -> bool` -- `not cascade.empty()` "
            "-- `.empty()` is `True` when the classifier failed to load "
            "(e.g. a bad path), so this is how you check a load actually "
            "worked before trying to use it.\n\n"
            "See the Study Reference presentation, Topic 11, for the theory."
        ),
        "stub": '''\
import cv2
import numpy as np


def create_blank_image(height: int, width: int, channels: int):
    """np.zeros((height, width, channels), dtype=np.uint8)."""
    raise NotImplementedError


def crop_image(image, y1: int, y2: int, x1: int, x2: int):
    """image[y1:y2, x1:x2] -- rows (y) before columns (x)."""
    raise NotImplementedError


def paste_region(image, region, y: int, x: int):
    """Paste region into a COPY of image at (y, x); return the copy."""
    raise NotImplementedError


def load_default_face_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")."""
    raise NotImplementedError


def load_cascade_from_path(path: str):
    """cv2.CascadeClassifier(path)."""
    raise NotImplementedError


def is_cascade_loaded(cascade) -> bool:
    """not cascade.empty()."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2
import numpy as np


def create_blank_image(height: int, width: int, channels: int):
    return np.zeros((height, width, channels), dtype=np.uint8)


def crop_image(image, y1: int, y2: int, x1: int, x2: int):
    return image[y1:y2, x1:x2]


def paste_region(image, region, y: int, x: int):
    result = image.copy()
    result[y:y + region.shape[0], x:x + region.shape[1]] = region
    return result


def load_default_face_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def load_cascade_from_path(path: str):
    return cv2.CascadeClassifier(path)


def is_cascade_loaded(cascade) -> bool:
    return not cascade.empty()
''',
        "test": '''\
import cv2
import numpy as np
from exercises.week11.exercise06.solution import (
    create_blank_image,
    crop_image,
    paste_region,
    load_default_face_cascade,
    load_cascade_from_path,
    is_cascade_loaded,
)


def test_create_blank_image():
    image = create_blank_image(10, 20, 3)
    assert image.shape == (10, 20, 3)
    assert image.sum() == 0


def test_crop_image():
    image = np.arange(100).reshape(10, 10).astype(np.uint8)
    cropped = crop_image(image, 2, 5, 3, 6)
    assert cropped.shape == (3, 3)


def test_paste_region_does_not_mutate_original():
    image = np.zeros((10, 10), dtype=np.uint8)
    region = np.full((3, 3), 255, dtype=np.uint8)
    result = paste_region(image, region, 2, 2)
    assert image.sum() == 0
    assert result[2, 2] == 255


def test_load_default_face_cascade_loads_successfully():
    cascade = load_default_face_cascade()
    assert is_cascade_loaded(cascade) is True


def test_load_cascade_from_bad_path_fails_to_load():
    cascade = load_cascade_from_path("/nonexistent/cascade.xml")
    assert is_cascade_loaded(cascade) is False


def test_load_cascade_from_good_path():
    good_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    cascade = load_cascade_from_path(good_path)
    assert is_cascade_loaded(cascade) is True
''',
    },
]
