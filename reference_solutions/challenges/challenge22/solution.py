import cv2


def load_default_face_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def load_grayscale(path: str):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def detect_faces(gray_image, cascade) -> list:
    """
    Every face box cascade finds in gray_image.

    Edge cases handled:
      - No detectable faces -> returns [] (the common case for a plain
        synthetic test image, not an error).
      - The return type is always a list of plain tuples, never the raw
        NumPy array detectMultiScale returns internally.
    """
    boxes = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
    return [tuple(box) for box in boxes]


def redact_regions(image, boxes: list):
    result = image.copy()
    height, width = image.shape[:2]
    for x, y, w, h in boxes:
        x1 = max(0, x)
        y1 = max(0, y)
        x2 = min(width, x + w)
        y2 = min(height, y + h)
        cv2.rectangle(result, (x1, y1), (x2, y2), (0, 0, 0), -1)
    return result


def adaptive_binary(gray_image):
    return cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )


def save_redacted(image, path: str) -> bool:
    return cv2.imwrite(path, image)
