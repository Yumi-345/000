__Author__ = "xq"


import cv2
import os

basePath = "D:\\Data\\COCO\\"
for dataName in os.listdir(basePath + "labels\\train2017\\"):
    dataPath = basePath + "labels\\train2017\\" + dataName
    datas = open(dataPath, "r", encoding="utf-8")


    baseName = dataName.split(".")[0]
    imgPath = basePath + "images\\" + "train2017\\" + baseName + ".jpg"

    img = cv2.imread(imgPath)
    imgInfo = img.shape
    imgHeight = imgInfo[0]
    imgWidth = imgInfo[1]

    for data in datas.readlines():
        data = data.split(" ")
        x = float(data[1])*imgWidth
        y = float(data[2])*imgHeight
        width = float(data[3])*imgWidth
        height= float(data[4])*imgHeight
        cv2.rectangle(img, (int(x-width/2), int(y-height/2)),(int(x+width/2), int(y+height/2)),
                      (0,0,int(data[0])*256//80),2)


    cv2.imshow("dstImg", img)
    cv2.waitKey(300)