import cv2 as cv
from Utils import show

# transformation matrix for rotation:
# |cos(a)  -sin(a)|
# |sin(a)   cos(a)|

img = cv.imread("starry_night.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols = img.shape

# cols-1 and rows-1 are the coordinate limits.
center = ((cols - 1) / 2.0, (rows - 1) / 2.0)
matrix = cv.getRotationMatrix2D(center, 90, 1)
reesult = cv.warpAffine(img, matrix, (cols, rows))
show(reesult)
