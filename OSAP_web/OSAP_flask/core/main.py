from core.predict import predict
from core.process import preprocess
from PIL import Image
import cv2
import traceback


def process(file_path, model_name):
    """

    :param file_path: the path of cataract fundus image
    :param model_name: the model you want to use
    """
    try: 
        image = Image.open(file_path)
        image_name = file_path.split('/')[-1].split('.')[0]
        processed_image = preprocess(image)
        restored_image = predict(processed_image, model_name)  # need returning a numpy array
        restored_image = Image.fromarray(restored_image)
        save_path = str(f'./data/{image_name}.png')
        restored_image.save(save_path)
        return "Success"
    except Exception as e:
        return traceback.format_exception()
    


if __name__ == '__main__':
    pass
