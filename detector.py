import cv2
import numpy as np
import argparse
import glob
import shutil
import os

def detect(filename):
    #mempersiapkan classifier
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eyes_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('./cascades/haarcascade_smile.xml')
    #membaca berkas gambar
    #dimuat dua kali agar tidak perlu repot konversi ke grayscale
    #img = cv2.imread(filename)
    #gray = cv2.imread(filename, 0)
    img = filename
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #praproses untuk mendapatkan kontras yang baik
    #gray = cv2.equalizeHist(gray)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    #mendeteksi wajah pada gambar
    faces=face_cascade.detectMultiScale(gray, 1.2, 5,minSize=(50,50))

    #inisiasi variabel untuk menghitung wajah dan senyum
    #print(faces)
    smileCount=0
    faceCount=0

    #untuk setiap wajah yang dideteksi, dicari senyum.
    for (x,y,w,h) in faces:
        #mencari mengambil segmen wajah dari gambar
        faceCount+=1
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        #mengubah ukuran wajah sebelum dicari senyumannya.
        windowed_gray = cv2.resize(roi_gray, (55, 55))

        #mendeteksi senyuman
        smiles=smile_cascade.detectMultiScale(image=windowed_gray,scaleFactor=1.1,minNeighbors=6)

        #untuk setiap senyuman yang dideteksi, maka wajah yang menjadi ROI ditandai
        for (mx,my,mw,mh) in smiles:
            smileCount+=1
            cv2.putText(img=windowed_gray,text="senyum",org=(mx,my),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
            cv2.rectangle(windowed_gray,(mx,my),(mx+mw,my+mh),(0,0,255),1)
            cv2.putText(img=img,text="wajah",org=(x,y),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)

        #menampilkan ROI sementara
        cv2.imshow("window", windowed_gray)
        #cv2.waitKey(100)
        #cv2.imshow('img',img)
        #cv2.waitKey(1)
        #cv2.destroyAllWindows()

    #membari label jumlah senyum dan jumlah wajah dan menampilkannya
    cv2.putText(img=img,text="Jumlah wajah= " + str(faceCount),org=(0,10),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
    cv2.putText(img=img,text="Jumlah senyum= " + str(smileCount),org=(0,20),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
    #img=cv2.resize(img, (0,0), fx=args["scale"], fy=args["scale"])
    cv2.imshow('img',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return smileCount
