#NOTES:
# #fix, ukuran ROI wajah harus sekitar 50x50
#dont code here

 #TODO:
 # 1. autoscale

#CHANGES:


#penggunaan
#python smile.py -img <gambar>

import cv2
import numpy as np
import argparse
from detector import detect

argpar=argparse.ArgumentParser()
argpar.add_argument("-img", "--input-image", required=False, help="path to input image")
argpar.add_argument("-scale", required=False, type=float, help="output scale")
args=vars(argpar.parse_args())
filename=args["input_image"]

cap = cv2.VideoCapture("./girl.mp4")
ds_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', frame)
    detect(frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
