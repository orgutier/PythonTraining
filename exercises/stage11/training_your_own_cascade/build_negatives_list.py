"""
Build a negatives.txt file for opencv_traincascade's -bg argument.

Usage:
    python build_negatives_list.py --images-dir path/to/backgrounds --output negatives.txt

Every image in --images-dir should contain NO instance of the thing you're
training a detector for (no hands, if you're following the hand-cascade
guide in this folder's README.md). No annotation needed -- just a plain
list of paths, one per line.
"""
import argparse
import os

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".pgm"}


def build_negatives_list(images_dir: str) -> list:
    """Return the path of every image file directly inside images_dir, sorted."""
    paths = []
    for name in sorted(os.listdir(images_dir)):
        if os.path.splitext(name)[1].lower() in IMAGE_EXTENSIONS:
            paths.append(os.path.join(images_dir, name))
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images-dir", required=True, help="Directory of background images with no hands in them")
    parser.add_argument("--output", default="negatives.txt", help="Where to write the list file")
    args = parser.parse_args()

    paths = build_negatives_list(args.images_dir)
    with open(args.output, "w") as f:
        f.write("\n".join(paths) + "\n")
    print(f"Wrote {len(paths)} negative image paths to {args.output}")


if __name__ == "__main__":
    main()
