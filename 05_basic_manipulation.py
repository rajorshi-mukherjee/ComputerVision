import cv2 as cv

# Convert image to grayscale

img = cv.imread('Images/parrot.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale', gray)

# Blur image

cv.waitKey(0)