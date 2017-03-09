import cv2

# Read the image
image = cv2.imread('images/beach.png')

# Image data type
print(type(image))

"""
  <class 'numpy.ndarray'>
"""

# Print the image
print(image)

"""
  [[[173  85  16]
    [176  84  15]
    [176  85  16]
    ...,
    [176  70   7]
    [175  70   7]
    [175  71   8]]
    ...,
    [82  92  112]
    [64  73  89]
    [37  48  75]]]
"""

# Print image shape (dimensions)
print(image.shape)

"""
(475, 600, 3)
"""

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
print(type(gray))
print(gray)
print(gray.shape)
