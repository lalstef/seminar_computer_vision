import cv2

image = cv2.imread('images/bricks_small.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute gradients along the X and Y axis, respectively
gradient_X = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gradient_Y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

gradient_X = cv2.convertScaleAbs(gradient_X)
gradient_Y = cv2.convertScaleAbs(gradient_Y)

sobel_combined = cv2.addWeighted(gradient_X, 0.5, gradient_Y, 0.5, 0)

cv2.imshow("Original", image)
cv2.imshow("Sobel X", gradient_X)
cv2.imshow("Sobel Y", gradient_Y)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.waitKey(0)



