# OpenCV

Six exercises, two per tier: image I/O, shape, and NumPy array manipulation, plus color conversion/resizing/drawing, in Basic; thresholding and Canny edge detection in Mid; Gaussian blur with contour detection, plus Haar cascade classifiers, in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage11_<name>` (e.g. `python tools/cli.py test stage11_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- cv2.imread, cv2.imwrite, image.shape, numpy
- **`tier1_basic02/`** -- cv2.cvtColor, cv2.resize, cv2.rectangle
- **`tier2_mid01/`** -- thresholding
- **`tier2_mid02/`** -- cv2.Canny()
- **`tier3_advanced01/`** -- cv2.GaussianBlur(), cv2.findContours(), convolution filtering
- **`tier3_advanced02/`** -- cv2.CascadeClassifier
