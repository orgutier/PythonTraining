# Going Further: Training Your Own Hand Cascade

**This folder is not a graded exercise.** There's no `solution.py`, no
`tests/test_stage11_...py` for it, and `python tools/cli.py test stage11`
never touches it. It exists for anyone who finishes Stage 11's algorithmic
hand-posture exercise (`tier3_advanced01`) and wants to go one step
further: training a *real* `cv2.CascadeClassifier` for hand/palm
detection, the same kind of file `tier3_advanced02` loads for faces.

## Why this isn't a bundled, ready-to-use file

Stage 11's `tier3_advanced02` exercise loads face/eye/smile cascades
straight out of `cv2.data.haarcascades` -- files that ship **inside the
`opencv-python` package itself**, under OpenCV's own BSD-3 license.
There is no equivalent official hand/palm cascade. Every "hand.xml" /
"palm.xml" / "fist.xml" file that turns up in a search is a
community-tutorial file with **no LICENSE file at all**, which under
default copyright law means "all rights reserved" -- not something this
repository (or any repository) can legally vendor and redistribute. That's
why `tier3_advanced01` uses a purely algorithmic approach (skin-color
thresholding + convexity defects) instead of a trained hand cascade: it
needs no model file, so there's nothing to license.

If you want a *trained* hand cascade of your own, you have to train it
yourself, on images you have the rights to use. This guide walks through
how.

## A tooling gap worth knowing about upfront

The classic Haar cascade training pipeline uses two command-line tools,
`opencv_createsamples` and `opencv_traincascade`. **Neither ships in the
`opencv-python` / `opencv-python-headless` pip packages** -- those wheels
contain only the compiled Python *bindings* (the `cv2` module), not
OpenCV's standalone C++ command-line apps. To get the training tools
themselves, you need one of:

- Build OpenCV from source with `-DBUILD_opencv_apps=ON` (the tools live
  in OpenCV's `apps` module).
- Install a distribution that bundles them -- e.g. conda-forge's
  `libopencv` package (`conda install -c conda-forge libopencv opencv`)
  often includes `opencv_createsamples`/`opencv_traincascade` on your
  `PATH`; check with `opencv_traincascade --help` after installing.
- Use a prebuilt Docker image that already has a full OpenCV build with
  apps enabled.

If none of that is available to you, skip straight to "A more modern
alternative" below -- it uses only `opencv-python-headless`, already in
this repo's `requirements.txt`.

## The classic Haar cascade workflow

1. **Collect positive images.** Several hundred to a few thousand images
   of the hand posture you want to detect (e.g. an open palm), cropped
   tightly to just the hand, varied in lighting/rotation/background/skin
   tone. Quality and variety matter far more than raw count.
2. **Collect negative images.** A larger set (1,000-3,000+) of images
   that do **not** contain the posture -- any scenery, objects, or other
   body parts. These teach the classifier what to reject.
3. **Build a positives description file** (`positives.txt`), one line per
   positive image: `path/to/image.jpg 1 x y w h` (the `1` is how many
   objects are annotated in that image, followed by one bounding box per
   object). `build_positives_list.py` below generates this automatically
   for a directory of already-cropped images.
4. **Build a negatives list file** (`negatives.txt`), one image path per
   line, no annotations needed. `build_negatives_list.py` below does
   this.
5. **Pack the positives into a `.vec` file:**
   ```bash
   opencv_createsamples -info positives.txt -num 800 -w 24 -h 24 -vec positives.vec
   ```
6. **Train the cascade** (this is the slow part -- can take from tens of
   minutes to many hours depending on data size and `-numStages`):
   ```bash
   opencv_traincascade -data cascade_output/ -vec positives.vec -bg negatives.txt \
       -numPos 720 -numNeg 1400 -numStages 15 -w 24 -h 24 -featureType HAAR
   ```
   (`-numPos` should be somewhat less than the total positives you packed,
   since `opencv_traincascade` discards some at each stage; a common rule
   of thumb is ~90% of what you fed `opencv_createsamples`.)
7. **Use it exactly like a bundled cascade:**
   ```python
   cascade = cv2.CascadeClassifier("cascade_output/cascade.xml")
   assert not cascade.empty()
   detections = cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
   ```
   `verify_cascade.py` below automates that sanity check.

## A more modern alternative (no legacy tools required)

Haar cascades are a technique from the early 2000s. If you don't have
access to `opencv_createsamples`/`opencv_traincascade` and don't want to
build OpenCV from source just for this, `cv2.HOGDescriptor` + a linear SVM
(both fully available in plain `opencv-python-headless`) is a more modern,
still-classical (pre-deep-learning) alternative that trains from pure
Python with no external command-line tools at all -- worth exploring if
you want to keep going without the tooling detour above.

## Helper scripts in this folder

- **`build_positives_list.py`** -- given a directory of already-cropped
  positive images (each image *is* the hand, filling the frame), writes
  `positives.txt` in the format `opencv_createsamples -info` expects.
- **`build_negatives_list.py`** -- given a directory of background
  images with no hand in them, writes `negatives.txt`.
- **`verify_cascade.py`** -- loads a trained (or any) `cascade.xml`,
  confirms it actually loaded (`not cascade.empty()`), and reports how
  many detections it finds across a directory of test images. Run this
  right after training to sanity-check the result before trusting it.

Each script is a plain, runnable Python file -- `python
build_positives_list.py --help` for its exact arguments.
