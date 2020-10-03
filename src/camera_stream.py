import cv2
import os

# Open the device at the Id 0
camera = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.
if not (camera.isOpened()):
    print('Could not open video device')

#To set the resolution
# camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
# camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

while True:
# Capture frame-by-frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv2.imshow('Cámara',frame)

    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()