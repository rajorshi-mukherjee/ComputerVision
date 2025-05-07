import cv2 as cv

# Convert image to grayscale

img = cv.imread('Images/parrot_smol.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale', gray)

# Blur image

# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)