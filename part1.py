# In this part, we import OpenCV and use it to play our sample.mp4 video

import cv2

# define video object
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