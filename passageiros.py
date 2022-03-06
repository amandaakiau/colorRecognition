#1/usr/bin/python3.7.3
#OpenCV 4.2, Raspberry pi 3/3b+, 4b, Buster ver 10
#Date 30th January, 2020

import cv2 as cv

face_cascade = cv.CascadeClassifier('.\haarcascade\haarcascade_frontalface_default.xml')

cap = cv.VideoCapture('.\src\passageiros5.jpg')
font = cv.FONT_HERSHEY_SIMPLEX
org = (5, 25)
color = (255, 0, 0)

while True:

    # reads frames
    _, img = cap.read()

    # convert to gray scale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Detects faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    #print("Number of {0} faces!".format(len(faces)))
    cv.putText(img, "Number of {0} faces!".format(len(faces)), org, font, 1, color, 2)

    cv.imshow('img',img)

    # Wait for Esc key to stop
    k = cv.waitKey(0)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()