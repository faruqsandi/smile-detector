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

    #menyalin citra yang dilewatkan argumen
    img = filename
    try:
        #mengubah citra ke grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except IOError:
        gray=img

    #perbaikan kontras citra grayscale
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    #mendeteksi wajah pada citra grayscale dan menyimpannya sebagai list
    faces=face_cascade.detectMultiScale(gray, 1.2, 5,minSize=(50,50))

    #inisialisasi counter
    smileCount=0
    faceCount=0

    #untuk setiap wajah yang ditemukan, lakukan operasi pendeteksian senyum
    for (x,y,w,h) in faces:
        faceCount+=1

        #memotong ROI
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        #menyalin ROI ke citra terpisah, agar bisa diproses mandiri
        #di-resize ke ukuran 55*55 agar pendeteksian senyum lebih baik.
        #nilai 55*55 ditemukan secara tidak sengaja, dan berhasil
        windowed_gray = cv2.resize(roi_gray, (55, 55))

        #mendeteksi senyuman pada citra
        smiles=smile_cascade.detectMultiScale(image=windowed_gray,scaleFactor=1.1,minNeighbors=6)

        #menandai wajah dengan kotak biru
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

        #untuk semua senyuman yang ditemukan di wajah, lakukan operasi penandaan
        for (mx,my,mw,mh) in smiles:
            smileCount+=1

            #kode debug
            #cv2.putText(img=windowed_gray,text="senyum",org=(mx,my),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
            #cv2.rectangle(windowed_gray,(mx,my),(mx+mw,my+mh),(0,0,255),1)
            #cv2.putText(img=img,text="wajah",org=(x,y),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)

            #menandai senyuman dengan kotak hijau
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
            smileCrop=windowed_gray[my:my+mh, mx:mx+mw]
        #kode debug
        #cv2.imshow("window", windowed_gray)

    cv2.putText(img=img,text="Jumlah wajah= " + str(faceCount),org=(0,10),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
    cv2.putText(img=img,text="Jumlah senyum= " + str(smileCount),org=(0,20),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,255),thickness=1)
    cv2.imshow('img',img)

    # mereturn gambar yang terlabeli, jumlah senyum
    return img, smileCount
