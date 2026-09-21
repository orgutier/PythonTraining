import cv2


def preprocess_for_scan(image) -> dict:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return {"gray": gray, "blurred": blurred, "edges": edges}


def find_document_contour(edges):
    """
    The largest-area contour in edges.

    Edge cases handled:
      - No contours at all -> returns None.
      - Multiple contours of very different sizes -> only the single
        largest (by cv2.contourArea) is returned.
    """
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    return max(contours, key=cv2.contourArea)


def bounding_box_of_contour(contour) -> tuple:
    return cv2.boundingRect(contour)


def draw_document_outline(image, contour):
    result = image.copy()
    x, y, w, h = bounding_box_of_contour(contour)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return result


def resize_to_fit(image, max_dimension: int):
    height, width = image.shape[:2]
    scale = max_dimension / max(height, width)
    new_width = int(round(width * scale))
    new_height = int(round(height * scale))
    return cv2.resize(image, (new_width, new_height))
