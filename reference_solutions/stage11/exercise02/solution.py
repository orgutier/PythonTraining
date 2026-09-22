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
