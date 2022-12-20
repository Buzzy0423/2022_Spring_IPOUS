import os

import torch

# import model run in server
# from predict_models.res_dg.models.RCDG_model import RCDGModel
from predict_models.res_dg.test import test
from predict_models.res.test import test_ArcNet

import argparse

# from models.res.test import test

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
torch.set_num_threads(4)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.cuda.empty_cache()


def predict(model):
    # TODO: 模型预测，结果储存到特定文件夹中
    if model == 'RCDG_model':
        test()
    elif model == 'ArcNet':
        test_ArcNet()



