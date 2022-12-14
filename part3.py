# In this part, we use the mask to identify areas of movement

import cv2

# define video and object detection objects
cap = cv2.VideoCapture("sample.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(100, 40)

while True:
    # read video frame
    frame = cap.read()[1]

    # create mask
    mask = object_detector.apply(frame)

    # use mask to define contours of movement
    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

    # draw contours with sufficient area onto frame
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

    # display frame and mask
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # exit condition (esc key)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()