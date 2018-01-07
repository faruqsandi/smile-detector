 #dont code here
import cv2

filename='./12.jpg'

def detect(filename):

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    cascade = cv2.CascadeClassifier('cascade.xml')
    img = cv2.imread(filename)
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    #for (x,y,w,h) in faces:
    #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #faces=mouth_cascade.detectMultiScale(gray, 1.3, 5)
    #for (x,y,w,h) in faces:
    #    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    faces=cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('img',img)
    cv2.imwrite("random.jpg", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

detect(filename)
