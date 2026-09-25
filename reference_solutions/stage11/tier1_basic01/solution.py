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
