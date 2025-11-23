import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("OpenCV_Tutorial/Resources/starry_night.jpg"))

if img is None:
    sys.exit("Couldn't read the image.")

cv.imshow("Display Window", img)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
