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

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# return the edged image
	return edged

detector = cv2.SimpleBlobDetector_create()

for f in filename:
	#img=cv2.imread(f, 1)
	img=cv2.imread(f, 0)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	img = clahe.apply(img)
	img = auto_canny(img)
	kernel1 =np.ones((3,3),np.uint8)
	#cv2.morphologyEx(src=img, dst=img, op=cv2.MORPH_OPEN, kernel=kernel1)
	#cv2.morphologyEx(src=img, dst=img, op=cv2.MORPH_DILATE, kernel=kernel1, iterations=5)
	#cv2.morphologyEx(src=img, dst=img, op=cv2.MORPH_ERODE, kernel=kernel1, iterations=5)
	#keypoints = detector.detect(img)
	#img = cv2.drawKeypoints(img, keypoints, np.array([]), (255,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	if(args["out"]):
		cv2.imwrite("out.edge."+str(os.path.basename(f)), img)
cv2.destroyAllWindows()
