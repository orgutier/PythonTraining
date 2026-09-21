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
