#support url:
# http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/


import numpy as np
import argparse
from detector import detect
import os
import glob
import cv2

argpar=argparse.ArgumentParser()
argpar.add_argument("-img", required=True, help="path to input image")
argpar.add_argument("-out",  action='store_true', help="path to output image")
argpar.add_argument("-scale", required=False, type=float, help="output scale")
args=vars(argpar.parse_args())
filename=glob.glob(pathname=args["img"]+str("/*"))
truePositive=trueNegative=falsePositive=falseNegative=actualNegative=actualPositive=predictedPositive=predictedNegative=0
for f in filename:
    img=cv2.imread(f, 1)
    result, smileCount=detect(img)
    print(str(os.path.basename(f)) + " | ("+str(os.path.basename(f))[0]+","+str(smileCount)+") -> ", end='')
    if str(os.path.basename(f))[0] is 'p':
        actualPositive+=1
        if(smileCount==1):
            print("true positive")
            predictedPositive+=1
            truePositive+=1
        else:
            print("true negative")
            predictedNegative+=1
            trueNegative+=1
    else:
        actualNegative+=1
        if(smileCount==1):
            print("false positive")
            predictedPositive+=1
            falsePositive+=1
        else:
            print("false negative")
            predictedNegative+=1
            falseNegative+=1
    if(args["out"]):
        cv2.imwrite("out"+str(os.path.basename(f)), result)
print("==================summary==================")
print("actualPositive = "+str(actualPositive))
print("predictedPositive = "+str(predictedPositive))
print("-------------------------------------------")
print("actualNegative = "+str(actualNegative))
print("predictedNegative = "+str(predictedNegative))
print("-------------------------------------------")
print("truePositive = "+str(truePositive))
print("trueNegative = "+str(trueNegative))
print("falsePositive = "+str(falsePositive))
print("falseNegative = "+str(falseNegative))
print("-------------------------------------------")
print("Accuracy = "+str((truePositive+trueNegative)/(actualPositive+actualNegative)))
print("Misclassification Rate = "+str((falsePositive+falseNegative)/(actualPositive+actualNegative)))
print("True Positive Rate = "+str(truePositive/actualPositive))
print("False Positive Rate = "+str(falsePositive/actualNegative))
print("Precision = "+str(truePositive/predictedPositive))
cv2.destroyAllWindows()
