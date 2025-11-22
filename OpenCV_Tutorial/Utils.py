import cv2 as cv


def show(img):
    cv.imshow("Image", img)
    cv.waitKey(0)


def get_execution_time_in_seconds(func, args):
    time_1 = cv.getTickCount()
    func(*args)
    time_2 = cv.getTickCount()
    t = (time_1 - time_2) / cv.getTickFrequency()
    return t


def insert_image(destination_image, source_image, image_position, image_resolution):
    destination_image[
        image_position[0] : image_resolution[0] + image_position[0],
        image_position[1] : image_resolution[1] + image_position[1],
    ] = source_image
