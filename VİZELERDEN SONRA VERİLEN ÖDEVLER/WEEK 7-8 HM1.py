import cv2

img = cv2.imread('c.jpg')
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgbimg = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2RGB)

cv2.imshow('RGB1 image', img)
cv2.imshow('HSV image', hsvImg)
cv2.imshow('RGB2 image', rgbimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

