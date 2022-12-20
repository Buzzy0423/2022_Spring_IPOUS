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
    image = image.resize((512, 512))
    file_name = file_path.split('/')[-1].split('.')[0]
    image.save('data/dataset/target/image1.png')
    preprocess('data/dataset/target/image1.png', 'data/dataset/target_mask/image1.png')
    if model_name == 'RCDG_model':

        predict('RCDG_model')
        img = Image.open('results/RCDG_drive/test_latest/images/image1_fake_TB.png')
        img = img.resize((512, 512))
        img.save(str(f'data/processed/{file_name}.png'))
    # os.remove('data/dataset/target/image1.png')
    # os.remove('data/dataset/target_mask/image1.png')
    elif model_name == 'ArcNet':
        predict('ArcNet')
        img = Image.open('results/arcnet/test_latest/images/image1_fake_TB.png')
        # img = img.resize((512, 512))
        img.save(str(f'data/processed/{file_name}.png'))
    else:
        return 'No such model'
    return 'Success'


if __name__ == '__main__':
    process('data/unprocessed/new_test.jpg', "AecNet")
    # image = Image.open('../data/unprocessed/test.jpg')
