import cv2

# define video and object detection objects
cap = cv2.VideoCapture("sample.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    # read video frame
    frame = cap.read()[1]

    # detect object(s)
    mask = object_detector.apply(frame)

    # display frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # exit condition (esc key)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()