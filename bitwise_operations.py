import numpy as np
import cv2

# Drawing a rectangle
rectangle = np.zeros((300, 300), dtype='uint8')
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow('Rectangle', rectangle)

# Drawing a circle
circle = np.zeros((300, 300), dtype='uint8')
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow('Circle', circle)
cv2.waitKey(0)

# Bitwise AND
bitwise_AND = cv2.bitwise_and(rectangle, circle)
cv2.imshow('AND', bitwise_AND)
cv2.waitKey(0)

# Bitwise OR
bitwise_OR = cv2.bitwise_or(rectangle, circle)
cv2.imshow('OR', bitwise_OR)
cv2.waitKey(0)

# Bitwise XOR
bitwise_XOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('XOR', bitwise_XOR)
cv2.waitKey(0)

# Bitwise NOT
bitwise_NOT = cv2.bitwise_not(circle)
cv2.imshow('NOT', bitwise_NOT)
cv2.waitKey(0)
