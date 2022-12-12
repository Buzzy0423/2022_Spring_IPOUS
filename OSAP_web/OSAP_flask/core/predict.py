import os
import sys
import cv2
import torch
# import model run in server
import numpy as np
# from predict_models.res.predict_models import arcnet_model
from predict_models.res.options import test_options

# from predict_models.res.test import test

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
torch.set_num_threads(4)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.cuda.empty_cache()


def predict(model):
    # TODO: 模型预测，结果储存到特定文件夹中
    # test(file_path, '00_low_quality_dir')
    # opt = test_options.TestOptions()
    os.system(
        'python predict_models/res_dg/test.py --dataroot ./data/dataset/'
        ' --name RCDG_drive --model RCDG --dataset_mode cataract_guide_padding --eval')
    # os.system(
    #     'python ../predict_models/res/test.py --dataroot ../data/unprocessed/'
    #     ' --name arcnet --model arcnet --dataset_mode cataract_guide_padding --eval')

    # model = arcnet_model.ArcNetModel()
    # model.set_input()
    # model.test()


# predict('arcnet')
