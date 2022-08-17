# -*- coding: utf-8 -*-
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont
import os

from matplotlib import pyplot as plt



PATH = "D:\\Data\\Images\\"
x,y = 145,145

for imgName in os.listdir(PATH):
    imgPath = os.path.join(PATH, imgName)
    img = cv2.imread(imgPath)

    matRotate = cv2.getRotationMatrix2D((990 * 0.5, 990 * 0.5), 45, 1)  # mat rotate 1 center 2 angle 3 缩放系数
    img = cv2.warpAffine(img, matRotate, (990, 990))

    cv2.rectangle(img, (x,y), (x+175,y+175), (0, 0, 255), 1)
    cv2.rectangle(img, (x+175,y), (x+175*2,y+175), (0, 0, 255), 1)
    cv2.rectangle(img, (x+175*2,y), (x+175*3,y+175), (0, 0, 255), 1)
    cv2.rectangle(img, (x+175*3,y), (x+175*4,y+175), (0, 0, 255), 1)

    plt.imshow(img)
    plt.show()
    # cv2.imshow("test", img)
    # cv2.waitKey(1000)






