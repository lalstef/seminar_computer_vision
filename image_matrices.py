import cv2
import numpy as np

black = np.full((200, 200, 3), 0, dtype='uint8')
print(black)
cv2.imshow('Black', black)
cv2.waitKey(0)

white = np.full((200, 200, 3), 255, dtype='uint8')
print(white)
cv2.imshow('White', white)
cv2.waitKey(0)

gray = np.full((200, 200, 3), 100, dtype='uint8')
print(gray)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

R = np.full((200, 200), 0, dtype='uint8')
G = np.full((200, 200), 255, dtype='uint8')
B = np.full((200, 200), 0, dtype='uint8')
color = np.stack([B, G, R], axis=2)
print(color)
cv2.imshow('Color', color)
cv2.waitKey(0)
