import cv2

# Open the device at the Id 0
video = cv2.VideoCapture('test.mp4')

while (video.isOpened()):
    # Capture frame-by-frame
    ret, frame = video.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Video para pruebas',video)

    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()