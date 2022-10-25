# In this part, we learn how to box moving objects in a specific viewing space

import cv2

# define video and object detection objects
cap = cv2.VideoCapture("sample.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(100, 40)

while True:
    # read video frame
    frame = cap.read()[1]

    # define viewing space
    zone = frame[340:640, 500:800]

    # detect object(s)
    mask = object_detector.apply(zone)
    mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)[1]

    # use mask to define contours of movement
    contours= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

    # create a box around countours with sufficient area
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(zone, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # display frame and mask
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # exit condition (esc key)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()