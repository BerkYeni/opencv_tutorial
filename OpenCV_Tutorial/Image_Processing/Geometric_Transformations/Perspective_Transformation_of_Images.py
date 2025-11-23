import cv2 as cv
import numpy as np
from Utils import show

# To find this transformation matrix,
# you need 4 points on the input image and
# corresponding points on the output image

# Among these 4 points, 3 of them should NOT be collinear

# Straight lines will remain straight even after the transformation

img = cv.imread("OpenCV_Tutorial/Resources/sudoku.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols, ch = img.shape

points = [[70, 172], [310, 96], [242, 318], [495, 224]]
# showing the points for clarity
for pt in points:
    cv.circle(img, pt, 10, (0, 0, 255), -1)
cv.line(img, points[0], points[3], (0, 255, 0), 5)
cv.line(img, points[1], points[2], (0, 255, 0), 5)
show(img)

pts1 = np.float32([*points])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv.getPerspectiveTransform(pts1, pts2)

dst = cv.warpPerspective(img, M, (300, 300))

show(dst)
