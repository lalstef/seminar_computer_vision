import cv2
import imutils

KERNEL = (9, 9)

image = cv2.imread('images/beach.png')

# Resize the image
image = imutils.resize(image, width=300)

# Blur images using different methods
average = cv2.blur(image, KERNEL)
gaussian = cv2.GaussianBlur(image, KERNEL, 0.0)
median = cv2.medianBlur(image, KERNEL[0])
bilateral = cv2.bilateralFilter(image, KERNEL[0], 61, 39)

# Show blurred images
cv2.imshow('Average ({}, {})'.format(*KERNEL), average)
cv2.imshow('Gaussian ({}, {})'.format(*KERNEL), gaussian)
cv2.imshow('Median ({}, {})'.format(*KERNEL), median)
cv2.imshow('Bilateral ({}, {})'.format(*KERNEL), bilateral)
cv2.waitKey(0)


