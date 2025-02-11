import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 0, 255), 10)
    img = cv2.rectangle(img, (150, 150), (width-150, height-150), (255, 0, 0), 10)
    img = cv2.circle(img, (320, 240), 50, (255, 255, 0), -1)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
