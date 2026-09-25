import cv2
import numpy as np


def load_frame(path: str):
    return cv2.imread(path)


def save_frame(path: str, frame) -> bool:
    return cv2.imwrite(path, frame)


def get_frame_dimensions(frame) -> tuple:
    return frame.shape[:2]


def create_blank_frame(height: int, width: int):
    return np.zeros((height, width, 3), dtype=np.uint8)


def crop_to_roi(frame, y1: int, y2: int, x1: int, x2: int):
    return frame[y1:y2, x1:x2]
