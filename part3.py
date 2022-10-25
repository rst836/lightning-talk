import cv2

# define video and object detection objects
cap = cv2.VideoCapture("sample.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    # read video frame
    frame = cap.read()[1]

    # define viewing space
    zone = frame[340:640, 500:800]

    # detect object(s)
    mask = object_detector.apply(zone)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:

        # calculate area and remove small items
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(zone, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # display frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # exit condition (esc key)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()