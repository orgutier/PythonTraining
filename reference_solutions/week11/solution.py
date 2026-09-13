import cv2


def to_grayscale(input_path: str, output_path: str) -> None:
    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, gray)


def resize_image(input_path: str, output_path: str, width: int, height: int) -> None:
    img = cv2.imread(input_path)
    resized = cv2.resize(img, (width, height))
    cv2.imwrite(output_path, resized)


def draw_rectangle(input_path: str, output_path: str, top_left: tuple, bottom_right: tuple) -> None:
    img = cv2.imread(input_path)
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imwrite(output_path, img)
