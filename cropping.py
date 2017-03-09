import cv2
import numpy as np

image = cv2.imread('images/girl.jpg')
cv2.imshow('Original', image)

# Cropping an image is accomplished using simple NumPy array slices
# Let's crop the face
face = image[10:120, 130:250]
cv2.imshow('Face', face)
cv2.waitKey(0)

# ...and now let's crop the dress
dress = image[120:530, 50:330]
cv2.imshow('Dress', dress)
cv2.waitKey(0)

# Blacking out the face
defaced = image.copy()
defaced[10:120, 130:250] = np.array((113, 53, 145))
cv2.imshow('Defaced', defaced)
cv2.waitKey(0)
