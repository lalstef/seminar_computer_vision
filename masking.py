import cv2
import numpy as np

image1 = cv2.imread('images/girl.jpg')
image2 = cv2.imread('images/girl2.jpg')

# Create first mask
mask1 = np.zeros(image1.shape[:2], dtype='uint8')
cv2.circle(mask1, (180, 70), 70, 255, -1)

# Apply first mask
masked1 = cv2.bitwise_and(image1, image1, mask=mask1)

cv2.imshow('Mask 1', masked1)
cv2.imshow('Image 1', image1)
cv2.imshow('Mask', mask1)
cv2.waitKey(0)

# Create second mask
mask2 = np.zeros(image2.shape[:2], dtype='uint8')
cv2.circle(mask2, (180, 70), 70, 255, -1)
mask2 = cv2.bitwise_not(mask2)

# Apply second mask
masked2 = cv2.bitwise_and(image2, image2, mask=mask2)

cv2.imshow('Masked 2', masked2)
cv2.imshow('Image 2', image2)
cv2.imshow('Mask 2', mask2)
cv2.waitKey(0)

# Add both masked images together
final = cv2.add(masked1, masked2)
cv2.imshow('Final', final)
cv2.waitKey(0)
