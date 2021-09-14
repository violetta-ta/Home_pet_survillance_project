import numpy as np
import cv2 as cv
import time


index = 0
cap = cv.VideoCapture(0)
scaleFactor=0.5


if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame

    ret, frame1 = cap.read()  # first image
    time.sleep(1/25)          # slight delay
    ret, frame2 = cap.read()  # second image

    difference = np.mean(cv.absdiff(frame1,frame2) ) # image difference
    print("difference", difference)
    frameSmall=cv.resize(frame2,(0,0),fx=scaleFactor,fy=scaleFactor)
    print("printing", index)
    # if frame is read correctly ret is True
    if not ret:
        print("No frame. Exiting ...")
        break

    if difference > 2.5:

        cv.imshow('frame', frameSmall)
        print("showing", index)
        cv.imwrite('image{}.png'.format(index),frameSmall)
        print("saving", index)
    index =index + 1
    time.sleep(1)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
