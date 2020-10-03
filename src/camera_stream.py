import cv2
import os
import time

# Open the device at the Id 0
camera = cv2.VideoCapture(0)
time.sleep(1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

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

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    faces = face_cascade.detectMultiScale(gray, 1.3, 5);

    for(top, right, bottom, left) in faces:
        #add frame from face
        cv2.rectangle(frame,(top,right),(top+bottom,right+left),(0,0,255),2)

    fpsInfo = "FPS: " + str(1.0/(time.time() - start_time))
    print(fpsInfo)
    cv2.putText(frame, fpsInfo, (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))

    # Display the resulting frame
    cv2.imshow('Detección de rostros',frame)

    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()