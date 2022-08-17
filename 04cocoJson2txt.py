__Author__ = "xq"


import cv2
import numpy as np
import json
import time
import math



# jsonPath = "D:\\Data\\COCO\\COCO2017\\annotations\\instances_val2017.json"
jsonPath = "D:\\Data\\COCO\\COCO2017\\annotations\\instances_train2017.json"

with open(jsonPath) as annos:
    annotations = json.load(annos)

# ['info', 'licenses', 'images', 'annotations', 'categories']
key = "annotations"


dic = {}
for dataDic in annotations["images"]:
    dic[dataDic["id"]] = [dataDic["width"], dataDic["height"]]
print(len(dic),dic)

# image_id, category_id, bbox
id = [1,2,3,4,5,6,7,8,9,10,
      11,13,14,15,16,17,18,19,20,
      21,22,23,24,25,27,28,
      31,32,33,34,35,36,37,38,39,40,
      41,42,43,44,46,47,48,49,50,
      51,52,53,54,55,56,57,58,59,60,
      61,62,63,64,65,67,70,
      72,73,74,75,76,77,78,79,80,
      81,82,84,85,86,87,88,89,90]

for i, List in enumerate(annotations[key]):
    imageWidth = dic[List["image_id"]][0]
    imageHeight = dic[List["image_id"]][1]

    with open("D:\\Data\\COCO\\labels\\train2017\\" +
          str("%012d"%(List["image_id"])) + ".txt", "a+", encoding="utf-8") as f:

        f.write(str(id.index(List["category_id"])) + " " +
                str("%.6f"%((List["bbox"][0]+List["bbox"][2]/2)/imageWidth)) + " " +
                str("%.6f"%((List["bbox"][1]+List["bbox"][3]/2)/imageHeight)) + " " +
                str("%.6f"%(List["bbox"][2]/imageWidth)) + " " +
                str("%.6f"%(List["bbox"][3]/imageHeight)) + "\n")
    f.close()
    if i % 1000 == 0:
        print(i)
