import cv2 as cv

faceCascade = cv.CascadeClassifier(r"Resources\haarcascades\haarcascade_frontalface_default.xml") 
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if(not ret):
        break
    gray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces =  faceCascade.detectMultiScale(frame , 1.1 , 5) 
    for (x , y , w , h) in faces : 
    #Draws a rectangle around the face
     cv.rectangle(frame , (x , y) , (x + w , y + h) , (255 , 0 , 0) , 2)
    # edges = cv.Canny(gray, threshold1=100, threshold2=200)
    cv.imshow("Canny with Face Detection", frame)
    if(cv.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv.destroyAllWindows()


