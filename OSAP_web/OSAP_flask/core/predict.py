import os

import torch

# import model run in server
# from predict_models.res_dg.models.RCDG_model import RCDGModel
from predict_models.res_dg.test import test

import argparse

# from models.res.test import test

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
torch.set_num_threads(4)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.cuda.empty_cache()


def predict(model):
    # TODO: 模型预测，结果储存到特定文件夹中
    # test(file_path, '00_low_quality_dir')
    # opt = test_options.TestOptions()
    # os.system(
    #     'python ../models/res_dg/test.py --dataroot ../data/dataset/'
    #     ' --name RCDG_drive --model RCDG --dataset_mode cataract_guide_padding --eval')
    # os.system(
    #     'python ../models/res/test.py --dataroot ../data/unprocessed/'
    #     ' --name arcnet --model arcnet --dataset_mode cataract_guide_padding --eval')

    # dic = dict()
    # dic['dataroot'] = '../data/dataset'
    # dic['name'] = 'RCDG_drive'
    # dic['model'] = 'RCDG'
    # dic['dataset_mode'] = 'cataract_guide_padding'
    # dic['eval'] = True
    # parser = argparse.ArgumentParser()
    test()

    # model = RCDGModel()
    # model.set_input()
    # model.test()


