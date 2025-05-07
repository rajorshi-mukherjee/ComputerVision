import cv2 as cv


capture = cv.VideoCapture('Videos/tiger.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Tiger', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()