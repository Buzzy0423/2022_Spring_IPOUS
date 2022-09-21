import os
import sys
import cv2
import torch
#import model run in server 
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
torch.set_num_threads(4)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.cuda.empty_cache()

def predict(data, model):
    #TODO: 模型预测，结果储存到特定文件夹中