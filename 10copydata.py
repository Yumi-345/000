__Author__ = "xq"


# import pandas as pd
# import scipy.io as scio
# import cv2
# import numpy as np
import os
import random
import shutil
basePath = '/home/zhuby/point_data'
for i in range(9):
    print(i)
    newPath = "./dataset/pointData/data" + str(i)
    newPathTrain = newPath + "/train/"
    newPathTest = newPath + "/test/"
    os.mkdir(newPath)
    os.mkdir(newPathTrain)
    os.mkdir(newPathTest)
    for dir in os.listdir(basePath):
        path = os.path.join(basePath, dir)
        newPathTrainNO = newPathTrain + str(dir)
        newPathTestNO = newPathTest + str(dir)
        os.mkdir(newPathTrainNO)
        os.mkdir(newPathTestNO)

        sampleDataTrain = random.sample(os.listdir(path), 786)
        for imgName in sampleDataTrain:
            shutil.move(os.path.join(path, imgName), newPathTrainNO)

        sampleDataTest = random.sample(os.listdir(path), 150)
        for imgName in sampleDataTest:
            shutil.move(os.path.join(path, imgName), newPathTestNO)



# imgList = random.sample(os.listdir(path), 100)



