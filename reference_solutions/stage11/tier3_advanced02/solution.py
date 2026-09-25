import cv2


def load_default_face_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def load_cascade_from_path(path: str):
    return cv2.CascadeClassifier(path)


def is_cascade_loaded(cascade) -> bool:
    return not cascade.empty()
