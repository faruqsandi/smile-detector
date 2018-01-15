import cv2
import numpy as np
import argparse
import os
import glob

argpar=argparse.ArgumentParser()
argpar.add_argument("-img", required=True, help="path to input image")
argpar.add_argument("-out",  action='store_true', help="path to output image")
argpar.add_argument("-scale", required=False, type=float, help="output scale")
args=vars(argpar.parse_args())
filename=glob.glob(pathname=args["img"]+str("/*"))
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
for f in filename:
    img=cv2.imread(f, 1)
    gray=cv2.imread(f, 0)
    gray2=cv2.resize(gray, (350, 350))
    mouths=mouth_cascade.detectMultiScale(gray, 1.2, 5, minSize=(100,100))
    mouthCount=0
    for (x,y,w,h) in mouths:
        mouthCount+=1
        roi_gray = gray[y:y+h, x:x+w]
        if(args["out"]):
            cv2.imwrite("out."+str(mouthCount)+str(os.path.basename(f)), roi_gray)
cv2.destroyAllWindows()
