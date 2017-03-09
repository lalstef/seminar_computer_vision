import cv2
import imutils


image = cv2.imread('images/stotinki_bg4.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

T, thresh_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh_adaptive = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 15)

image = imutils.resize(image, width=300)
thresh_otsu = imutils.resize(thresh_otsu, width=300)
thresh_adaptive = imutils.resize(thresh_adaptive, width=300)

cv2.imshow('Original', image)
cv2.imshow('Threshold Otsu\'s ({})'.format(T), thresh_otsu)
cv2.imshow('Threshold Adaptive', thresh_adaptive)
cv2.waitKey(0)



