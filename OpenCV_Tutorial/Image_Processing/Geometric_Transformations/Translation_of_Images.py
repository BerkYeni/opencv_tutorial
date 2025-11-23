import numpy as np
import cv2 as cv

img = cv.imread("OpenCV_Tutorial/Resources/starry_night.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols = img.shape

matrix = np.float32([[1, 0, 100], [0, 1, 50]])
#  |1 0 100|
#  |0 1  50|

dst = cv.warpAffine(img, matrix, (cols, rows))
#  1.x + 0.y + 100.1  =  x + 100
#  0.x + 1.y + 50.1   =  y + 50

# dsize is because: width = columns, height = rows


cv.imshow("img", dst)
cv.waitKey(0)
cv.destroyAllWindows()
