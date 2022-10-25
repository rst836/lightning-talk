import cv2

# define video and object detection objects
cap = cv2.VideoCapture("sample.mp4")

while True:
    # read video frame
    frame = cap.read()[1]

    # display frame
    cv2.imshow("Frame", frame)

    # exit condition (esc key)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()