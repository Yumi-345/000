import numpy
import os
# import dlib
import cv2

basePath = 'D:\\Data\\FaceDataset\\megaage_asian\\test\\'
txt = open('./test_gender.txt', 'a+', encoding='utf-8')
for index in range(3877, 40002):
    path = os.path.join(basePath, str(index)+'.jpg')
    print(path)
    img = cv2.imread(path)
    cv2.imshow('test', img)
    cv2.waitKey(1)
    data = input()
    if data == ' ':
        data = '1'
    else:
        data = '0'
    txt.write(str(data) + '\n')
    txt.flush()

txt.close()