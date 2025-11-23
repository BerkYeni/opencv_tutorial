# "For HSV, hue range is [0,179], saturation range is [0,255],
# and value range is [0,255]. Different software use different scales.
# So if you are comparing OpenCV values with them,
# you need to normalize these ranges."

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)


def nothing(x):
    pass


# add trackbar to change which color to be tracked
color_window = "Color"
color_display_img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow(color_window)
cv.createTrackbar("H", color_window, 0, 179, nothing)

while 1:

    # Take each frame
    _, frame = cap.read()

    # get hue value from trackbar
    h = cv.getTrackbarPos("H", color_window)
    hsv_value = [h, 255, 255]
    bgr_value = cv.cvtColor(np.uint8([[hsv_value]]), cv.COLOR_HSV2BGR)

    # Convert frame from BGR to HSV
    hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    error_margin = 20

    lower_color_value = np.array([h - error_margin, 50, 50])
    upper_color_value = np.array([h + error_margin, 255, 255])

    # Threshold the HSV image to get only the selected color
    mask = cv.inRange(hsv_img, lower_color_value, upper_color_value)

    # Bitwise-AND mask and original image
    # use a solid color image to make the color more apparent
    solid_color = np.zeros(frame.shape, np.uint8)
    solid_color[:] = bgr_value
    green_img = cv.bitwise_and(solid_color, solid_color, mask=mask)

    # get the rest of the img (background) and make it grayscale
    grayed = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    background = cv.bitwise_and(grayed, grayed, mask=cv.bitwise_not(mask))
    same_channel_sized_gray = cv.cvtColor(grayed, cv.COLOR_GRAY2BGR)

    # combine the foreground and background
    fun = cv.add(same_channel_sized_gray, green_img)

    color_display_img[:] = bgr_value
    cv.imshow(color_window, color_display_img)
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("green_img", green_img)
    cv.imshow("fun", fun)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
