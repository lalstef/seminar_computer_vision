import os
import cv2
import numpy as np
from sklearn.cluster import KMeans


def describe(image):
    lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    hist = cv2.calcHist([lab], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist).flatten()
    return hist


def cluster(dataset_directory):
    data = []
    image_paths = [os.path.join(dataset_directory, path) for path in os.listdir(dataset_directory)]
    image_paths = filter(lambda i: i.endswith('.jpg') or i.endswith('.png'), image_paths)
    image_paths = np.array(sorted(image_paths))

    for path in image_paths:
        image = cv2.imread(os.path.join(dataset_directory, path))
        hist = describe(image)
        data.append(hist)

    clt = KMeans(n_clusters=2)
    labels = clt.fit_predict(data)
    return image_paths, labels


def display(image_paths, labels):
    for label in np.unique(labels):
        label_paths = image_paths[np.where(labels == label)]

        for (i, path) in enumerate(label_paths[:10]):
            image = cv2.imread(path)
            cv2.imshow("Cluster {}, Image #{}".format(label + 1, i + 1), image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_paths, labels = cluster('images/dataset')
    display(image_paths, labels)




