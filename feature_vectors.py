import cv2
import numpy as np
from scipy.spatial import distance

path_base = 'images/0037.jpg'
path_second = 'images/0038.jpg'
path_third = 'images/0039.jpg'

base = cv2.imread(path_base)
second = cv2.imread(path_second)
third = cv2.imread(path_third)

index = {}

# Construct the feature vector for the searched for (base) image
(means, stds) = cv2.meanStdDev(base)
index[path_base] = np.concatenate([means, stds]).flatten()
distances = []

for path, img in [(path_second, second), (path_third, third)]:
    # The following 2 lines construct our feature vector
    (means, stds) = cv2.meanStdDev(img)
    index[path] = np.concatenate([means, stds]).flatten()

paths = index.keys()
for i, path in enumerate(paths):
    if path == path_base:
        continue

    # Calculate the distance between each image and the searched for (base) image
    dist = distance.euclidean(index[path_base], index[path])
    distances.append((path, dist))

# Sort the images by distance from base image
distances = sorted(distances, key=lambda x: x[1])

for item in distances:
    print(item[0], item[1])


