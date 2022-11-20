import numpy as np
import cv2

img = cv2.imread("a.jpg")
cv2.imshow("Original", img)

def gaussian_noise(image):
    row,col,ch = image.shape
    mean=0
    var=0.05
    sigma=var**0.5

    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss

    return noisy

img = cv2.imread("a.jpg")
img = img/255
noise_img = gaussian_noise(img)
cv2.imshow("Gaussian Noise", noise_img)
cv2.waitKey(0)