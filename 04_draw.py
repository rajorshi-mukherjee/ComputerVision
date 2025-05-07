import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

img = cv.imread('Images/mountain.jpg')

#cv.imshow('Mountain', img)

#cv.imshow('Blank', blank)

#1 point the pixels to a certain colour
#blank[200:300, 300:400]=0,255,0
#cv.imshow('Green', blank)

# 2 draw a rectangle
#cv.rectangle(blank, (150,50), (400,200), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# cv.waitKey(0)

# 3 draw a circle

#cv.circle(blank, (400,250), 40, (0,0,255), thickness=3)
# cv.imshow('Circle', blank)

# cv.waitKey(0)

#cv.line(blank, (100,0), (250, 250), (255,255,255), thickness=2)

#4 add text on image
cv.putText(blank, 'Hello', (100,225), cv.FONT_HERSHEY_DUPLEX,1.0, (255,0,255),2)
cv.imshow('Text', blank)

cv.waitKey(0)