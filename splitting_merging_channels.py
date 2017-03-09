import cv2

image = cv2.imread('images/girl.jpg')
cv2.imshow('Original', image)

# Channels are given in reverse order (BGR instead of RGB)
(B, G, R) = cv2.split(image)

# Red Channel
cv2.imshow('Red', R)
cv2.waitKey(0)

# Green Channel
cv2.imshow('Green', G)
cv2.waitKey(0)

# Blue Channel
cv2.imshow('Blue', B)
cv2.waitKey(0)

# Merged
merged = cv2.merge((B, G, R))
cv2.imshow('Merged', merged)
cv2.waitKey(0)

# Try with 4 channels
merged_again = cv2.merge((G, B, G, R))
cv2.imshow('Merged Again', merged_again)
cv2.waitKey(0)
