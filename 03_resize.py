import cv2 as cv

# img = cv.imread('Images/boating.jpg')

def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/tiger.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Tiger', frame)

    frame_resized = rescaleFrame(frame)
    cv.imshow('Tiger Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()