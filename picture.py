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
import os

argpar=argparse.ArgumentParser()
argpar.add_argument("-img", required=True, help="path to input image")
argpar.add_argument("-out",  action='store_true', help="path to output image")
argpar.add_argument("-scale", required=False, type=float, help="output scale")
args=vars(argpar.parse_args())
filename=args["img"]

img=cv2.imread(filename, 1)
result=detect(img)
if(args["out"]):
    cv2.imwrite("out"+os.path.basename(filename), img)
cv2.waitKey(0)
cv2.destroyAllWindows()
