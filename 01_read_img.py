import cv2 as cv

img = cv.imread('Images/parrot.jpg')
cv.imshow('Parrot', img)
cv.waitKey(0)
