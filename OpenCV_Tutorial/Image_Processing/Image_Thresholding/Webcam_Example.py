import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

titles = [
    "Original Image",
    "Global Thresholding (v = 127)",
    "Adaptive Mean Thresholding",
    "Adaptive Gaussian Thresholding",
]


def nothing(x):
    pass


values_window = "Values"
cv.namedWindow(values_window)
cv.createTrackbar("Threshold", values_window, 0, 255, nothing)
cv.createTrackbar("Blur", values_window, 1, 20, nothing)
cv.createTrackbar("Opening", values_window, 0, 1, nothing)
cv.createTrackbar("Kernel", values_window, 1, 20, nothing)


bl = 1
k = 5


while True:
    ret, frame = cap.read()
    th_value = cv.getTrackbarPos("Threshold", values_window)
    blur_value = cv.getTrackbarPos("Blur", values_window)
    opening = cv.getTrackbarPos("Opening", values_window)
    kernel_size = cv.getTrackbarPos("Kernel", values_window)

    if not ret:
        print("Can't receive frame")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # otsu
    # ret3, th3 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # gray = th3

    if blur_value % 2 == 1:
        bl = blur_value

    # median
    # blurred = cv.medianBlur(gray, bl)
    # gaussian
    if kernel_size % 2 == 1:
        k = kernel_size
    blurred = cv.GaussianBlur(gray, (k, k), 0)

    # blurred = gray
    ret, binary_thresh = cv.threshold(blurred, th_value, 255, cv.THRESH_BINARY)
    adaptive_mean = cv.adaptiveThreshold(
        blurred, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2
    )
    adaptive_gauss = cv.adaptiveThreshold(
        blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2
    )
    images = [blurred, binary_thresh, adaptive_mean, adaptive_gauss]

    if opening:
        images = map(lambda imag: cv.morphologyEx(imag, cv.MORPH_OPEN, kernel), images)
    # images = map(lambda imag: cv.erode(imag, kernel, iterations=1), images)

    # cv.imshow("Camera", gray)
    for title, image in zip(titles, images):
        cv.imshow(title, image)
    # cv.waitKey(0)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
