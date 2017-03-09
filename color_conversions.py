import cv2
# Read the image
image = cv2.imread('images/beach.png')

# Convert different color spaces
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

# Show the converted images
cv2.imshow('RGB', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('L*a*b', lab)

# Pause so we can see the images
cv2.waitKey(0)

