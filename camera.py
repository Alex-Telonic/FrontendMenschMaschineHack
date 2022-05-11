import numpy as np
import cv2

cap = cv2.VideoCapture(0)


#cap.set(3, 640) # set width as 640
#cap.set(4, 480) # set height as 480

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
