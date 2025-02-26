import cv2 as cv
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if(not ret):
        break

    gray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    edges = cv.Canny(gray, threshold1=100, threshold2=200)
    cv.imshow('orginal',frame)
    cv.imshow('edges', edges)
    if(cv.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv.destroyAllWindows()


