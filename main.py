import cv2
from util import get_limits
from PIL import Image

cap = cv2.VideoCapture(0)

yellow = [0, 255, 255]

while True:
    ret, frame = cap.read()
   
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlimit, upperlimit = get_limits(color=yellow)

    mask = cv2.inRange(hsv_frame, lowerlimit, upperlimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    bbox = mask_.getbbox()

    if bbox is not None:
        x, y, w, h = bbox
        frame = cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 5)

    cv2.imshow('Frame', frame)   
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    