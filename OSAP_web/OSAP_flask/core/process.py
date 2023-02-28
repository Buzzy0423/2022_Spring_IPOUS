# preprocess of upload image
from PIL import Image
import cv2
import numpy as np
from scipy import ndimage

def preprocess(image_path, save_path):
    image = Image.open(image_path).convert('RGB')
    mask = get_mask(image)
    cv2.imwrite(save_path, mask * 255)


def get_mask(img):
    gray = np.array(img.convert('L'))
    return ndimage.binary_opening(gray > 10, structure=np.ones((8, 8)))
