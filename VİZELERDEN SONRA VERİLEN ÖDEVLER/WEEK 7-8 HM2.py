import cv2

img = cv2.imread('c.jpg')
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('RGB image', img)
cv2.imshow('HSV image', hsvImg)
cv2.waitKey(0)
cv2.destroyAllWindows()