import cv2
import time


# Open the device at the Id 0
video = cv2.VideoCapture('./data/video/test.mp4')

while (video.isOpened()):
    start_time = time.time()
    # Capture frame-by-frame
    ret, frame = video.read()

    # calculate FPS >> FPS = 1 / time to process loop
    fpsInfo = "FPS: " + str(1.0/(time.time() - start_time))
    print(fpsInfo)
    cv2.putText(frame, fpsInfo, (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Video para pruebas',frame)

    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()