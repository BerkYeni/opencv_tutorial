import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if "EVENT" in i]
# print(events)

drawing = False
mode = "Rectangle"
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        # cv.circle(img, (x, y), 100, (255, 0, 0), -1)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == "Rectangle":
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == "Rectangle":
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("Image")
cv.setMouseCallback("Image", draw_circle)

while 1:
    cv.imshow("Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord("m"):
        mode = "Circle" if mode == "Rectangle" else "Rectangle"
    elif key == 27:
        break

cv.destroyAllWindows()
