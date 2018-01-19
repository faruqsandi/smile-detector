import cv2
import numpy as np
import argparse
from detector import detect
import os
import glob

#inisialisasi parameter command line
argpar=argparse.ArgumentParser()
argpar.add_argument("-img", required=True, help="path to input image")
argpar.add_argument("-out",  action='store_true', help="path to output image")
argpar.add_argument("-scale", required=False, type=float, help="output scale")
args=vars(argpar.parse_args())
filename=glob.glob(pathname=args["img"]+str("/*"))

#untuk setiap file yang ditemukan di folder, lakukan operasi pendeteksian
for f in filename:
    img=cv2.imread(f, 1)
    result, smileCount=detect(img)
    if(args["out"]):
        cv2.imwrite("out"+str(os.path.basename(f)), img)
cv2.destroyAllWindows()
