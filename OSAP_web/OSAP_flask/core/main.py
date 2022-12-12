import os

from core.predict import predict
from core.process import preprocess
from PIL import Image


def process(file_path, model_name):
    """

    :param file_path: the path of cataract fundus image
    :param model_name: the model you want to use
    """
    # TODO: fill this
    image = Image.open(file_path)
    file_name = file_path.split('/')[-1].split('.')[0]
    image.save('data/dataset/target/image1.png')
    preprocess('data/dataset/target/image1.png', 'data/dataset/target_mask/image1.png')
    predict('RCDG_model')
    img = Image.open('results/RCDG_drive/test_latest/images/image1_fake_TB.png')
    img = img = img.resize((512, 512))
    img.save(str(f'data/processed/{file_name}.png'))
    # os.remove('data/dataset/target/image1.png')
    # os.remove('data/dataset/target_mask/image1.png')

    return 'Success'


if __name__ == '__main__':
    process('data/unprocessed/new_test.jpg', "RCDG_model")
    # image = Image.open('../data/unprocessed/test.jpg')
