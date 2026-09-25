"""
Sanity-check a trained (or any) Haar cascade file.

Usage:
    python verify_cascade.py --cascade cascade_output/cascade.xml --images-dir path/to/test_images

Confirms the cascade file actually loaded, then runs detectMultiScale
across every image in --images-dir and reports how many detections it
found in each -- a quick way to eyeball whether training worked before
wiring the cascade into a real pipeline.
"""
import argparse
import os

import cv2


def load_and_check(cascade_path: str) -> cv2.CascadeClassifier:
    """Load cascade_path and raise a clear error if it failed to load."""
    cascade = cv2.CascadeClassifier(cascade_path)
    if cascade.empty():
        raise ValueError(
            f"{cascade_path} failed to load as a cascade -- check the path, "
            "and that training actually produced a cascade.xml there."
        )
    return cascade


def run_on_directory(cascade: cv2.CascadeClassifier, images_dir: str, scale_factor: float = 1.1, min_neighbors: int = 5) -> dict:
    """Return {image_path: detection_count} for every image in images_dir."""
    results = {}
    for name in sorted(os.listdir(images_dir)):
        path = os.path.join(images_dir, name)
        image = cv2.imread(path)
        if image is None:
            continue
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        detections = cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)
        results[path] = len(detections)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cascade", required=True, help="Path to the cascade.xml to verify")
    parser.add_argument("--images-dir", required=True, help="Directory of test images to run detection on")
    parser.add_argument("--scale-factor", type=float, default=1.1)
    parser.add_argument("--min-neighbors", type=int, default=5)
    args = parser.parse_args()

    cascade = load_and_check(args.cascade)
    print(f"{args.cascade} loaded successfully.")

    results = run_on_directory(cascade, args.images_dir, args.scale_factor, args.min_neighbors)
    total_detections = sum(results.values())
    images_with_a_hit = sum(1 for count in results.values() if count > 0)
    for path, count in results.items():
        print(f"  {path}: {count} detection(s)")
    print(
        f"\n{images_with_a_hit}/{len(results)} images had at least one detection, "
        f"{total_detections} detections total."
    )


if __name__ == "__main__":
    main()
