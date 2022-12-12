import cv2
import numpy as np

img= cv2.imread('c.jpg',0)
cv2.imshow("original", img)
cv2.waitKey(0)

kernel= np.ones((5,5), dtype= np.uint8)

blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = blackNoise*-255
noise_img = blackNoise + img
noise_img[noise_img <=245] = 0
closing= cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()