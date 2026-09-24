"""
Stage 11 -- OpenCV.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. All exercises are function-based, using small
synthetic images built with numpy (no external image files needed), since
images are just NumPy arrays -- that's the whole point of this stage.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    cv2.imread, cv2.imwrite, cv2.cvtColor, cv2.resize,
            cv2.rectangle, image.shape, numpy
  Mid:      cv2.Canny(), thresholding
  Advanced: cv2.findContours(), cv2.GaussianBlur(), cv2.CascadeClassifier,
            convolution filtering
"""

STAGE = "stage11"
TOPIC = "OpenCV"
OVERVIEW = (
    "Six exercises, two per tier: image I/O, shape, and NumPy array "
    "manipulation, plus color conversion/resizing/drawing, in Basic; "
    "thresholding and Canny edge detection in Mid; Gaussian blur with "
    "contour detection, plus Haar cascade classifiers, in Advanced."
)

EXERCISES = [
    {
        "name": "basic01",
        "title": "Image I/O, Shape, and NumPy Arrays",
        "summary": "cv2.imread, cv2.imwrite, image.shape, numpy",
        "readme": (
            "An OpenCV image *is* a NumPy array -- `.shape` is a plain "
            "array attribute, not something OpenCV adds, and cropping is "
            "just array slicing. Implement:\n\n"
            "- `load_image(path: str)` -- `cv2.imread(path)` (returns a "
            "NumPy array in BGR order, or `None` if the file can't be "
            "read).\n"
            "- `save_image(path: str, image) -> bool` -- "
            "`cv2.imwrite(path, image)`.\n"
            "- `get_dimensions(image) -> tuple` -- `image.shape[:2]`, "
            "i.e. `(height, width)` -- note **height first**, which "
            "trips up everyone coming from `(width, height)` conventions "
            "elsewhere.\n"
            "- `get_channel_count(image) -> int` -- `image.shape[2]` if "
            "`image` has 3 dimensions (color), else `1` (grayscale "
            "images have no third dimension at all).\n"
            "- `create_blank_image(height: int, width: int, channels: "
            "int)` -- `np.zeros((height, width, channels), "
            "dtype=np.uint8)`.\n"
            "- `crop_image(image, y1: int, y2: int, x1: int, x2: int)` "
            "-- `image[y1:y2, x1:x2]` -- ordinary NumPy array slicing, "
            "rows (`y`) before columns (`x`), since that's the array's "
            "`(height, width, ...)` layout. There's no separate \"crop "
            "function\" in OpenCV, because the image is just an array.\n\n"
            "See the Study Reference presentation, Topic 11 (Basic "
            "tier), for the theory."
        ),
        "stub": '''\
import cv2
import numpy as np


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


def create_blank_image(height: int, width: int, channels: int):
    """np.zeros((height, width, channels), dtype=np.uint8)."""
    raise NotImplementedError


def crop_image(image, y1: int, y2: int, x1: int, x2: int):
    """image[y1:y2, x1:x2] -- rows (y) before columns (x)."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2
import numpy as np


def load_image(path: str):
    return cv2.imread(path)


def save_image(path: str, image) -> bool:
    return cv2.imwrite(path, image)


def get_dimensions(image) -> tuple:
    return image.shape[:2]


def get_channel_count(image) -> int:
    return image.shape[2] if len(image.shape) == 3 else 1


def create_blank_image(height: int, width: int, channels: int):
    return np.zeros((height, width, channels), dtype=np.uint8)


def crop_image(image, y1: int, y2: int, x1: int, x2: int):
    return image[y1:y2, x1:x2]
''',
        "test": '''\
import numpy as np
from exercises.stage11.basic01.solution import (
    load_image,
    save_image,
    get_dimensions,
    get_channel_count,
    create_blank_image,
    crop_image,
)


def test_save_and_load_roundtrip(tmp_path):
    """save_image/load_image round-trip via cv2.imwrite/cv2.imread."""
    path = str(tmp_path / "img.png")
    original = np.zeros((20, 30, 3), dtype=np.uint8)
    original[:, :] = (0, 0, 255)
    assert save_image(path, original) is True
    loaded = load_image(path)
    assert loaded is not None
    assert loaded.shape == (20, 30, 3)


def test_load_missing_file_returns_none():
    """cv2.imread must return None (not raise) for a missing file."""
    assert load_image("/nonexistent/path/to/image.png") is None


def test_get_dimensions_is_height_then_width():
    """get_dimensions == image.shape[:2] -- height first, not (width, height)."""
    image = np.zeros((20, 30, 3), dtype=np.uint8)
    assert get_dimensions(image) == (20, 30)


def test_get_channel_count_color_vs_grayscale():
    """get_channel_count reads image.shape[2] for color, defaults to 1 for grayscale (2D)."""
    color = np.zeros((10, 10, 3), dtype=np.uint8)
    gray = np.zeros((10, 10), dtype=np.uint8)
    assert get_channel_count(color) == 3
    assert get_channel_count(gray) == 1


def test_create_blank_image():
    """create_blank_image == np.zeros((height, width, channels), dtype=np.uint8)."""
    image = create_blank_image(10, 20, 3)
    assert image.shape == (10, 20, 3)
    assert image.sum() == 0


def test_crop_image_is_plain_array_slicing():
    """crop_image must be image[y1:y2, x1:x2] -- rows before columns."""
    image = np.arange(100).reshape(10, 10).astype(np.uint8)
    cropped = crop_image(image, 2, 5, 3, 6)
    assert cropped.shape == (3, 3)
''',
    },
    {
        "name": "basic02",
        "title": "Color Conversion, Resizing, and Drawing",
        "summary": "cv2.cvtColor, cv2.resize, cv2.rectangle",
        "readme": (
            "Implement:\n\n"
            "- `to_grayscale(image)` -- `cv2.cvtColor(image, "
            "cv2.COLOR_BGR2GRAY)`.\n"
            "- `to_rgb(image)` -- `cv2.cvtColor(image, "
            "cv2.COLOR_BGR2RGB)` -- OpenCV reads/stores images in "
            "**BGR** order by default, not RGB; this is the conversion "
            "you need before handing an image to almost any other "
            "library (matplotlib, PIL, ...).\n"
            "- `resize_image(image, width: int, height: int)` -- "
            "`cv2.resize(image, (width, height))` -- note the argument "
            "order here **is** `(width, height)`, the opposite of "
            "`.shape`'s `(height, width)`.\n"
            "- `resize_by_scale(image, scale: float)` -- "
            "`cv2.resize(image, None, fx=scale, fy=scale)` (scale both "
            "dimensions by a factor instead of specifying exact "
            "pixels).\n"
            "- `draw_rectangle(image, pt1: tuple, pt2: tuple, color: "
            "tuple)` -- work on **a copy** (`image.copy()`, since "
            "`cv2.rectangle` draws in place) and `cv2.rectangle(copy, "
            "pt1, pt2, color, thickness=2)`, returning the copy.\n"
            "- `draw_bounding_boxes(image, boxes: list, color: tuple)` "
            "-- work on a copy; `cv2.rectangle(copy, (x1, y1), (x2, "
            "y2), color, 2)` once per `(x1, y1, x2, y2)` tuple in "
            "`boxes`, then return the copy. Always drawing onto a copy "
            "(never the original `image` parameter) matters because "
            "`cv2.rectangle` mutates the array it's given -- without "
            "copying first, calling this twice on the same source image "
            "would compound, and the caller's original image would "
            "silently change too.\n\n"
            "See the Study Reference presentation, Topic 11 (Basic "
            "tier), for the theory."
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


def draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    """Draw an outlined rectangle on a COPY of image; return the copy."""
    raise NotImplementedError


def draw_bounding_boxes(image, boxes: list, color: tuple):
    """Draw one rectangle per (x1, y1, x2, y2) in boxes, on a copy."""
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


def draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    result = image.copy()
    cv2.rectangle(result, pt1, pt2, color, thickness=2)
    return result


def draw_bounding_boxes(image, boxes: list, color: tuple):
    result = image.copy()
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(result, (x1, y1), (x2, y2), color, 2)
    return result
''',
        "test": '''\
import numpy as np
from exercises.stage11.basic02.solution import (
    to_grayscale,
    to_rgb,
    resize_image,
    resize_by_scale,
    draw_rectangle,
    draw_bounding_boxes,
)


def _bgr_image():
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    image[:, :] = (255, 0, 0)
    return image


def test_to_grayscale_drops_channel_dim():
    """to_grayscale must use cv2.COLOR_BGR2GRAY, producing a 2D array."""
    gray = to_grayscale(_bgr_image())
    assert gray.shape == (10, 10)


def test_to_rgb_swaps_channel_order():
    """to_rgb must use cv2.COLOR_BGR2RGB -- BGR (255,0,0) becomes RGB (0,0,255)."""
    rgb = to_rgb(_bgr_image())
    assert tuple(rgb[0, 0]) == (0, 0, 255)


def test_resize_image_uses_width_height_order():
    """resize_image passes (width, height) to cv2.resize -- the opposite of .shape's (height, width)."""
    resized = resize_image(_bgr_image(), 20, 5)
    assert resized.shape[:2] == (5, 20)


def test_resize_by_scale():
    """resize_by_scale == cv2.resize(image, None, fx=scale, fy=scale)."""
    resized = resize_by_scale(_bgr_image(), 2.0)
    assert resized.shape[:2] == (20, 20)


def test_draw_rectangle_does_not_mutate_original():
    """draw_rectangle must draw on image.copy(), leaving the original untouched."""
    image = np.zeros((20, 20, 3), dtype=np.uint8)
    result = draw_rectangle(image, (2, 2), (10, 10), (255, 255, 255))
    assert np.array_equal(image, np.zeros((20, 20, 3), dtype=np.uint8))
    assert result[2, 2].tolist() == [255, 255, 255]


def test_draw_bounding_boxes_draws_all_and_does_not_mutate():
    """draw_bounding_boxes draws every box from a copy, leaving the original image untouched."""
    image = np.zeros((30, 30, 3), dtype=np.uint8)
    boxes = [(1, 1, 5, 5), (10, 10, 15, 15)]
    result = draw_bounding_boxes(image, boxes, (255, 0, 0))
    assert result[1, 1].tolist() == [255, 0, 0]
    assert result[10, 10].tolist() == [255, 0, 0]
    assert image.sum() == 0
''',
    },
    {
        "name": "mid01",
        "title": "Thresholding",
        "summary": "thresholding",
        "readme": (
            "Implement three ways to binarize a grayscale image:\n\n"
            "- `apply_threshold(gray_image, thresh_value: int)` -- "
            "`cv2.threshold(gray_image, thresh_value, 255, "
            "cv2.THRESH_BINARY)[1]` (`cv2.threshold` returns "
            "`(used_threshold, result_image)` -- take `[1]`, the "
            "image).\n"
            "- `apply_otsu_threshold(gray_image)` -- "
            "`cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + "
            "cv2.THRESH_OTSU)[1]` -- Otsu's method picks the threshold "
            "value *automatically* from the image's histogram, so the "
            "`0` you pass for `thresh_value` is ignored.\n"
            "- `apply_adaptive_threshold(gray_image)` -- "
            "`cv2.adaptiveThreshold(gray_image, 255, "
            "cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)` -- "
            "picks a *different* threshold for each local neighborhood "
            "instead of one global value, useful when lighting is "
            "uneven across the image.\n\n"
            "See the Study Reference presentation, Topic 11 (Mid "
            "tier), for the theory."
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
''',
        "test": '''\
import numpy as np
from exercises.stage11.mid01.solution import (
    apply_threshold,
    apply_otsu_threshold,
    apply_adaptive_threshold,
)


def _half_bright_gray():
    image = np.zeros((20, 20), dtype=np.uint8)
    image[:, 10:] = 200
    return image


def test_apply_threshold():
    """apply_threshold binarizes at a fixed global value."""
    result = apply_threshold(_half_bright_gray(), 100)
    assert result[0, 0] == 0
    assert result[0, 15] == 255


def test_apply_otsu_threshold_separates_regions():
    """apply_otsu_threshold must pick its own threshold from the histogram and still separate the two regions."""
    result = apply_otsu_threshold(_half_bright_gray())
    assert result[0, 0] != result[0, 15]


def test_apply_adaptive_threshold_returns_binary_image():
    """apply_adaptive_threshold must return a same-shape image with only 0/255 values."""
    result = apply_adaptive_threshold(_half_bright_gray())
    assert result.shape == (20, 20)
    assert set(np.unique(result)).issubset({0, 255})
''',
    },
    {
        "name": "mid02",
        "title": "Edge Detection with Canny",
        "summary": "cv2.Canny()",
        "readme": (
            "Implement:\n\n"
            "- `detect_edges(gray_image, low: int, high: int)` -- "
            "`cv2.Canny(gray_image, low, high)`.\n"
            "- `detect_edges_default(gray_image)` -- "
            "`cv2.Canny(gray_image, 100, 200)` (commonly-used default "
            "thresholds).\n"
            "- `count_edge_pixels(gray_image, low: int, high: int) -> "
            "int` -- `int(np.count_nonzero(cv2.Canny(gray_image, low, "
            "high)))`.\n\n"
            "See the Study Reference presentation, Topic 11 (Mid "
            "tier), for the theory."
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
''',
        "test": '''\
import cv2
import numpy as np
from exercises.stage11.mid02.solution import detect_edges, detect_edges_default, count_edge_pixels


def _square_image():
    image = np.zeros((50, 50), dtype=np.uint8)
    cv2.rectangle(image, (10, 10), (30, 30), 255, -1)
    return image


def test_detect_edges_finds_something():
    """detect_edges must find edge pixels around the square's boundary."""
    edges = detect_edges(_square_image(), 50, 150)
    assert edges.sum() > 0


def test_detect_edges_default_uses_100_200():
    """detect_edges_default == cv2.Canny(gray_image, 100, 200), same output shape as input."""
    edges = detect_edges_default(_square_image())
    assert edges.shape == (50, 50)


def test_count_edge_pixels():
    """count_edge_pixels counts nonzero pixels in the Canny output."""
    assert count_edge_pixels(_square_image(), 50, 150) > 0
''',
    },
    {
        "name": "advanced01",
        "title": "Blurring and Contours",
        "summary": "cv2.GaussianBlur(), cv2.findContours(), convolution filtering",
        "readme": (
            "Implement:\n\n"
            "- `apply_gaussian_blur(image, ksize: int)` -- "
            "`cv2.GaussianBlur(image, (ksize, ksize), 0)` (`ksize` must "
            "be odd).\n"
            "- `apply_strong_blur(image)` -- same idea with a fixed, "
            "larger kernel: `cv2.GaussianBlur(image, (15, 15), 0)`. "
            "Blurring is **convolution filtering**: a small kernel "
            "window slides over every pixel, replacing it with a "
            "weighted average of its neighbors -- a bigger kernel (as "
            "here) averages over a wider neighborhood, producing a "
            "blurrier result.\n"
            "- `find_contours(binary_image) -> list` -- "
            "`cv2.findContours(binary_image, cv2.RETR_EXTERNAL, "
            "cv2.CHAIN_APPROX_SIMPLE)[0]` (the first element of the "
            "tuple is the list of contours; the second, ignored here, "
            "is the hierarchy).\n"
            "- `count_contours(binary_image) -> int` -- "
            "`len(find_contours(binary_image))`.\n"
            "- `largest_contour_area(binary_image) -> float` -- "
            "`max(cv2.contourArea(c) for c in "
            "find_contours(binary_image))`.\n\n"
            "See the Study Reference presentation, Topic 11 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import cv2


def apply_gaussian_blur(image, ksize: int):
    """cv2.GaussianBlur(image, (ksize, ksize), 0)."""
    raise NotImplementedError


def apply_strong_blur(image):
    """cv2.GaussianBlur(image, (15, 15), 0)."""
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


def apply_gaussian_blur(image, ksize: int):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)


def apply_strong_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)


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
from exercises.stage11.advanced01.solution import (
    apply_gaussian_blur,
    apply_strong_blur,
    find_contours,
    count_contours,
    largest_contour_area,
)


def test_apply_gaussian_blur_preserves_shape():
    """apply_gaussian_blur must preserve the image's shape."""
    image = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
    blurred = apply_gaussian_blur(image, 5)
    assert blurred.shape == image.shape


def test_apply_strong_blur_smooths_more_than_light_blur():
    """apply_strong_blur's larger (15,15) kernel must smooth a single bright pixel more than a small (3,3) kernel."""
    image = np.zeros((30, 30), dtype=np.uint8)
    image[15, 15] = 255
    light = apply_gaussian_blur(image, 3)
    strong = apply_strong_blur(image)
    assert strong[15, 15] < light[15, 15]


def _square_binary_image():
    image = np.zeros((50, 50), dtype=np.uint8)
    cv2.rectangle(image, (10, 10), (30, 30), 255, -1)
    return image


def test_find_and_count_contours():
    """find_contours/count_contours must find exactly one contour for one filled square."""
    contours = find_contours(_square_binary_image())
    assert len(contours) == 1
    assert count_contours(_square_binary_image()) == 1


def test_largest_contour_area():
    """largest_contour_area uses cv2.contourArea over all found contours."""
    area = largest_contour_area(_square_binary_image())
    assert 300 < area < 500
''',
    },
    {
        "name": "advanced02",
        "title": "Cascade Classifiers",
        "summary": "cv2.CascadeClassifier",
        "readme": (
            "Implement:\n\n"
            "- `load_default_face_cascade()` -- "
            "`cv2.CascadeClassifier(cv2.data.haarcascades + "
            "\"haarcascade_frontalface_default.xml\")`, one of the "
            "pretrained detectors OpenCV ships with.\n"
            "- `load_cascade_from_path(path: str)` -- "
            "`cv2.CascadeClassifier(path)` (the general form, for a "
            "cascade file you supply yourself).\n"
            "- `is_cascade_loaded(cascade) -> bool` -- `not "
            "cascade.empty()` -- `.empty()` is `True` when the "
            "classifier failed to load (e.g. a bad path), so this is "
            "how you check a load actually worked before trying to use "
            "it.\n\n"
            "See the Study Reference presentation, Topic 11 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import cv2


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


def load_default_face_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def load_cascade_from_path(path: str):
    return cv2.CascadeClassifier(path)


def is_cascade_loaded(cascade) -> bool:
    return not cascade.empty()
''',
        "test": '''\
import cv2
from exercises.stage11.advanced02.solution import (
    load_default_face_cascade,
    load_cascade_from_path,
    is_cascade_loaded,
)


def test_load_default_face_cascade_loads_successfully():
    """load_default_face_cascade must load one of OpenCV's built-in pretrained cascades."""
    cascade = load_default_face_cascade()
    assert is_cascade_loaded(cascade) is True


def test_load_cascade_from_bad_path_fails_to_load():
    """is_cascade_loaded must be False when the given path doesn't point to a real cascade file."""
    cascade = load_cascade_from_path("/nonexistent/cascade.xml")
    assert is_cascade_loaded(cascade) is False


def test_load_cascade_from_good_path():
    """load_cascade_from_path must work for a real path too, not just load_default_face_cascade's hardcoded one."""
    good_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    cascade = load_cascade_from_path(good_path)
    assert is_cascade_loaded(cascade) is True
''',
    },
]
