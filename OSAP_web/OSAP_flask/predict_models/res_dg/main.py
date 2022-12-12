import os
from PIL import Image
import cv2

def png2jpg(url):
    image = Image.open(url)
    image = image.convert('RGB')
    save_url = url[:-4]+'.jpg'
    image.save(save_url, quality = 95)
    return save_url

def image_resize(img):
    return img.resize([512,512])



url = './test/test.png'
# save_url = png2jpg(url)
img = Image.open(url)
# img = image_resize(img)
# img.save(save_url)
print(img)


