import numpy as np
import cv2 as cv
import math

img = np.zeros((512, 512, 3), np.uint8)


def the_thing(center, color, rotation=0):
    cv.ellipse(
        img, center, (50, 50), 0, 0 + rotation, 300 + rotation, color, -1, cv.LINE_AA
    )
    cv.circle(img, center, 25, 0, -1, cv.LINE_AA)


radius = 62
center_x = 256
center_y = 256

top_coords = (center_x, center_y - radius)
left_coords = (int(center_x - (radius / 2) * (3**0.5)), center_y + (radius // 2))
right_coords = (int(center_x + (radius / 2) * (3**0.5)), center_y + (radius // 2))

the_thing(left_coords, (0, 256, 0))
the_thing(right_coords, (256, 0, 0), -60)
the_thing(top_coords, (0, 0, 256), 120)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow("Shapes", img)
k = cv.waitKey(0)
