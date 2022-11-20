import random
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os.path

def add_noise(image):
	row , col = image.shape
	# Randomly pick some pixels in the image for coloring them white
	# Pick a random number between 300 and 10000
	number_of_pixels = random.randint(300, 10000)
	for i in range(number_of_pixels):
		# Pick a random y coordinate

		y_coord=random.randint(0, row - 1)

		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to white
		image[y_coord][x_coord] = 255
		
	# Randomly pick some pixels in the image for coloring them black
	# Pick a random number between 300 and 10000
	number_of_pixels = random.randint(300 , 10000)
	for i in range(number_of_pixels):
	
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to black
		image[y_coord][x_coord] = 0
		
	return image

# salt-and-pepper noise can
# be applied only to grayscale images
# Reading the color image in grayscale image
image = cv2.imread('A.jpeg',
				cv2.IMREAD_GRAYSCALE)

#Storing the image
cv2.imwrite('B.jpg',
			add_noise(image))

#Display Histogram
print(image)
print(image.ravel())
hist = cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256])
plt.title('Histogram for paper and salt picture')
plt.show()