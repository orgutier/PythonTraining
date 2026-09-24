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
