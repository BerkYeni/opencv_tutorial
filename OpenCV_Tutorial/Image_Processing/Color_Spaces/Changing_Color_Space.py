# "For HSV, hue range is [0,179], saturation range is [0,255],
# and value range is [0,255]. Different software use different scales.
# So if you are comparing OpenCV values with them,
# you need to normalize these ranges."

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while 1:

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # get green in opencv's hsv scale
    green = 120 / 360
    g_in_cv_hsv = green * 179
    # define range of blue color in HSV
    lower_blue = np.array([g_in_cv_hsv - 20, 50, 50])
    upper_blue = np.array([g_in_cv_hsv + 20, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    # use a solid green image to make the color more apparent
    solid_green = np.zeros(frame.shape, np.uint8)
    solid_green[:] = (0, 255, 0)
    green_img = cv.bitwise_and(solid_green, solid_green, mask=mask)

    # get the rest of the img (background) and make it grayscale
    grayed = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    background = cv.bitwise_and(grayed, grayed, mask=cv.bitwise_not(mask))
    same_channel_sized_gray = cv.cvtColor(grayed, cv.COLOR_GRAY2BGR)

    # combine the foreground and background
    fun = cv.add(same_channel_sized_gray, green_img)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("green_img", green_img)
    cv.imshow("fun", fun)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
