import cv2

THRESHOLD = 254
MAX_VALUE = 255
KERNEL = (3, 3)

image = cv2.imread('images/google.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, KERNEL, 0)

_, thresh = cv2.threshold(blurred, THRESHOLD, MAX_VALUE, cv2.THRESH_BINARY)
_, thresh_inv = cv2.threshold(blurred, THRESHOLD, MAX_VALUE, cv2.THRESH_BINARY_INV)

cv2.imshow('Original', image)
cv2.imshow('Gray', gray)
cv2.imshow('Threshold', thresh)
cv2.imshow('Threshold Inverse', thresh_inv)
cv2.waitKey(0)



