import cv2 as cv

# get the time difference
time_at_start = cv.getTickCount()

# some code

time_at_end = cv.getTickCount()

duration_in_seconds = (time_at_end - time_at_end) / cv.getTickFrequency()
print(duration_in_seconds)


# practical example
img1 = cv.imread("starry_night.jpg")
assert img1 is not None, "file could not be read, check with os.path.exists()"

e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)
