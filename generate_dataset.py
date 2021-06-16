import os

import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)

# Load the cascade
total = 0
face_cascade = cv2.CascadeClassifier('face_detector.xml')
while True:

    ret, frame = cap.read()
    orig = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("k"):

        cv2.imwrite("dataset/dataset" + str(total) + ".png", orig)
        total += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
