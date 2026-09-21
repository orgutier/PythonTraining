import cv2


def load_image(path: str):
    return cv2.imread(path)


def save_image(path: str, image) -> bool:
    return cv2.imwrite(path, image)


def get_dimensions(image) -> tuple:
    return image.shape[:2]


def get_channel_count(image) -> int:
    return image.shape[2] if len(image.shape) == 3 else 1
