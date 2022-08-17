__Author__ = "xq"


import cv2
import numpy as np
import json
import time
import math



jsonPath = "D:\\Data\\COCO\\COCO2017\\annotations\\instances_val2017.json"

with open(jsonPath) as annos:
    annotations = json.load(annos)

# ['info', 'licenses', 'images', 'annotations', 'categories']
key = "images"
dic = {}
for dataDic in annotations["images"]:
    dic[dataDic["id"]] = [dataDic["width"], dataDic["height"]]
print(len(dic),dic)


for data in annotations[key]:
    print(dic[data["image_id"]])

print(len(annotations[key]))

# 15335