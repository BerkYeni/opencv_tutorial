import cv2 as cv
import numpy as np


def nothing(x):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("Image")

cv.createTrackbar("R", "Image", 0, 255, nothing)
cv.createTrackbar("G", "Image", 0, 255, nothing)
cv.createTrackbar("B", "Image", 0, 255, nothing)

switch = "0 : OFF \n1 : ON"
cv.createTrackbar(switch, "Image", 0, 1, nothing)

while True:
    cv.imshow("Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

    r = cv.getTrackbarPos("R", "Image")
    g = cv.getTrackbarPos("G", "Image")
    b = cv.getTrackbarPos("B", "Image")
    s = cv.getTrackbarPos(switch, "Image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()
