import cv2
import numpy as np

image = cv2.imread('image.png')
kernel1 = np.ones((5,5), np.float32)/30
img =cv2.filter2D(src=image, ddepth=-1, kernel= kernel1)

cv2.imshow('original', image)
cv2.imshow('kernel blur', img)
cv2.waitKey()
cv2.destroyAllWindows()