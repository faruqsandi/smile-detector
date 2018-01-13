import cv2
import numpy as np
import argparse
from detector import detect

argpar=argparse.ArgumentParser()
argpar.add_argument("-img", "--input-image", required=True, help="path to input image")
args=vars(argpar.parse_args())
filename=args["input_image"]

img=cv2.imread(filename, 1)
markedImage, smileCount, cropSmile=detect(img)
cv2.imshow("markedImage", markedImage)
print(smileCount)
cv2.imshow("cropSmile", cropSmile)
cv2.waitKey(0)
cv2.destroyAllWindows()
