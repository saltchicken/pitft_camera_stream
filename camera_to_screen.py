import cv2
from picamera2 import Picamera2
import time


picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (320, 240)})
picam2.configure(config)

picam2.start()
time.sleep(2)

cv2.namedWindow("Video Stream", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Video Stream", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

try:
    while True:
        frame = picam2.capture_array()
        cv2.imshow("Video Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    picam2.stop()
    cv2.destroyAllWindows()
