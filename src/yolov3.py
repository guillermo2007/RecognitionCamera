import cv2
import os
import time
from yoloanalyzer import yoloV3_analyzer

# Open the device at the Id 0
camera = cv2.VideoCapture(0)
time.sleep(1)

ya = yoloV3_analyzer(0.5)

#Check whether user selected camera is opened successfully.
if not (camera.isOpened()):
    print('Could not open video device')

#To set the resolution
# camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
# camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

while True:
    start_time = time.time()
    # Capture frame-by-frame
    ret, frame = camera.read()

    frame = ya.ImageProcess(frame)

    fpsInfo = "FPS: " + str(1.0/(time.time() - start_time))
    print(fpsInfo)
    cv2.putText(frame, fpsInfo, (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))

    # Display the resulting frame
    cv2.imshow('Yolo V3',frame)

    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()