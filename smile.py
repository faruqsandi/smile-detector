#NOTES:
# fix, ukuran ROI wajah harus sekitar 50x50
#

 #dont code here
import cv2
import numpy as np
import argparse
import glob
import shutil
import os

argpar=argparse.ArgumentParser()
argpar.add_argument("-img", "--input-image", required=True, help="path to input image")
argpar.add_argument("-mark", "--mark-image", required=False, help="mark a smile?")
#ap.add_argument("-out", "--output-image", required=True, help="path to output image")
args=vars(argpar.parse_args())

files=glob.glob(args["input_image"]+"/*")
#filename=args["input_image"]


def detect(filename):
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eyes_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('./cascades/haarcascade_smile.xml')

    img = cv2.imread(filename)
    gray = cv2.imread(filename, 0)

    #gray = cv2.equalizeHist(gray)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    #img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    #gray = cv2.resize(gray, (0,0), fx=0.5, fy=0.5)
    faces=face_cascade.detectMultiScale(gray, 1.2, 5)
    #print(faces)
    smileCount=0
    for (x,y,w,h) in faces:
        #print("face" + str(faces.shape[0]))
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        windowed_gray = cv2.resize(roi_gray, (55, 55))
        smiles=smile_cascade.detectMultiScale(image=windowed_gray,scaleFactor=1.1,minNeighbors=6)
        cv2.imshow('img',img)
        cv2.waitKey(10)
        for (mx,my,mw,mh) in smiles:
            smileCount+=1
            cv2.putText(img=windowed_gray,text="senyum",org=(mx,my),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
            cv2.rectangle(windowed_gray,(mx,my),(mx+mw,my+mh),(0,0,255),1)
        cv2.imshow("window", windowed_gray)
        cv2.waitKey(10)
        if args["input_image"]=="1":
            cv2.putText(img=img,text="wajah",org=(x,y),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(255,0,0),thickness=1)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
        #smiles=smile_cascade.detectMultiScale(image=roi_gray,scaleFactor=1.1,minNeighbors=6)
        #for (mx,my,mw,mh) in smiles:
        #    cv2.putText(img=roi_color,text="senyum",org=(mx,my),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
        #    cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),1)
    cv2.destroyAllWindows()
    return smileCount
#print(detect(filename))
for f in files:
    #print(detect(f))
    print("processing: "+str(os.path.basename(f)))
    if detect(f) != 0:
        print(str(os.path.basename(f))+" ada")
        shutil.copyfile(f, "./senyum/"+str(os.path.basename(f)))
    else:
        print(str(os.path.basename(f))+" tidakada")
        shutil.copyfile(f, "./nonsenyum/"+str(os.path.basename(f)))
