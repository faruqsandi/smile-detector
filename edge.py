import cv2
import numpy as np

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# return the edged image
	return edged

img = cv2.imread("mouth.jpg",0 )

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img = clahe.apply(img)
kernel1 =np.ones((3,3),np.uint8)
#cv2.equalizeHist(src=img, dst=img)

cv2.imshow("sample", img)
edge = auto_canny(img)

cv2.imshow("edge", edge)
cv2.waitKey(0)
