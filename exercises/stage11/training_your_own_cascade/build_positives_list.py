"""
Build a positives.txt description file for opencv_createsamples.

Usage:
    python build_positives_list.py --images-dir path/to/cropped_hands --output positives.txt

Assumes every image in --images-dir is ALREADY cropped tightly to just the
hand (so the annotated bounding box is the whole image). If your images
aren't pre-cropped, annotate them with a bounding-box tool of your own
first, then adapt the "1 x y w h" line below to your actual coordinates.
"""
import argparse
import os

import cv2


def build_positives_list(images_dir: str) -> list:
    """Return one "path 1 x y w h" line per image in images_dir, with
    (x, y, w, h) covering the whole image (0, 0, width, height)."""
    lines = []
    for name in sorted(os.listdir(images_dir)):
        path = os.path.join(images_dir, name)
        image = cv2.imread(path)
        if image is None:
            continue
        height, width = image.shape[:2]
        lines.append(f"{path} 1 0 0 {width} {height}")
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images-dir", required=True, help="Directory of pre-cropped positive hand images")
    parser.add_argument("--output", default="positives.txt", help="Where to write the description file")
    args = parser.parse_args()

    lines = build_positives_list(args.images_dir)
    with open(args.output, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {len(lines)} positive image entries to {args.output}")


if __name__ == "__main__":
    main()
