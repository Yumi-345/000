__Author__ = "yumi"


import os
import cv2

basePath = "D:\\Data\\FaceDataset\\megaage_asian\\train\\"

for imgName in os.listdir(basePath):
    path = os.path.join(basePath, imgName)

    srcImg = cv2.imread(path)

