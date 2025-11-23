import cv2 as cv
from Utils.Utils import show

img = cv.imread("starry_night.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"
show(img)

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
show(res)

# OR

height, width = img.shape[:2]
res = cv.resize(img, (2 * width, 2 * height), interpolation=cv.INTER_CUBIC)
show(res)
