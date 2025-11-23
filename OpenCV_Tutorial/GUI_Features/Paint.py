import cv2 as cv
import numpy as np


def nothing(x):
    pass


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, rg, gg, bg
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        # cv.circle(img, (x, y), 100, (255, 0, 0), -1)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == "Rectangle":
                cv.rectangle(img, (ix, iy), (x, y), (bg, gg, rg), -1)
            else:
                cv.circle(img, (x, y), 5, (bg, gg, rg), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == "Rectangle":
            cv.rectangle(img, (ix, iy), (x, y), (bg, gg, rg), -1)
        else:
            cv.circle(img, (x, y), 5, (bg, gg, rg), -1)


drawing = False
mode = "Rectangle"
ix, iy = -1, -1
rg, gg, bg = 0, 0, 0


img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("Image")
cv.setMouseCallback("Image", draw_circle)

cv.createTrackbar("R", "Image", 0, 255, nothing)
cv.createTrackbar("G", "Image", 0, 255, nothing)
cv.createTrackbar("B", "Image", 0, 255, nothing)


while True:
    cv.imshow("Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord("m"):
        mode = "Circle" if mode == "Rectangle" else "Rectangle"

    r = cv.getTrackbarPos("R", "Image")
    g = cv.getTrackbarPos("G", "Image")
    b = cv.getTrackbarPos("B", "Image")

    rg, gg, bg = r, g, b

    # img[:] = [b, g, r]

cv.destroyAllWindows()
