import cv2
import numpy as np

resim1=cv2.imread("wiki.jpg")
cv2.imshow("wiki",resim1)

print(resim1.size)
print(resim1.dtype)
print(resim1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()