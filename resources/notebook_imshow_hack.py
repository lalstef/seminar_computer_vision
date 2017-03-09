import os
import cv2
from IPython.display import Image

TMP_DIR = '/tmp'

def imshow(filename, image):
    full_path = os.path.join(TMP_DIR, filename)
    cv2.imwrite(full_path, image)
    return Image(filename=full_path)
