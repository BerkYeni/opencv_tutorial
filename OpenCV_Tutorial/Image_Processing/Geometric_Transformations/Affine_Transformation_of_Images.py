import cv2 as cv
import numpy as np
from Utils import show

img = cv.imread("OpenCV_Tutorial/Resources/starry_night.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols, ch = img.shape

# To find the transformation matrix,
# we need three points from the input image and
# their corresponding locations in the output image.

pts = [50, 50], [200, 50], [50, 200]
# showing the points for clarity
for pt in pts:
    cv.circle(img, pt, 10, (0, 0, 255), -1)
show(img)

pts1 = np.float32([*pts])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pts1, pts2)

dst = cv.warpAffine(img, M, (cols, rows))

show(dst)
