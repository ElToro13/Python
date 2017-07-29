# USAGE
# python detect_color.py --image pokemon_games.png

# import the necessary packages
import numpy as np
from pyimagesearch import imutils
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--logooo.PNG", help = "C:\Python27\logooo.PNG")
args = vars(ap.parse_args())



# load the image

image = cv2.imread("pokemon_games.png")
ret1,th1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
hist = cv2.calcHist([th1],[0],None,[256],[0,256])
cv2.imshow('Output_threshold',hist)

ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

#cap = cv2.VideoCapture(0)

# define the list of boundaries

boundaries=[([17, 15, 100], [50, 56, 200])]
# loop over the boundaries
for (lower, upper) in boundaries:
        
                #create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
        
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)
        
	#print output
        cv2.imshow('Output_Final',output)

	# show the images
	#cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(0)
	



        



