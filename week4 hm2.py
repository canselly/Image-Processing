import cv2
import numpy as np
Path = r'salad.jpg'
img =cv2.imread(Path)

im1= cv2.blur(img(5,5))
im1 = cv2.boxFilter(img, -1,(2,2), normalize = True)

cv2.imshow('image', np.hpstack((im1,im2)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
