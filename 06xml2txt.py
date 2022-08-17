import xml.etree.ElementTree as ET
import os
import cv2


basePath = 'D:\\Data\\BL\\fire_to\\fire1'
labelsBasePath = 'D:\\Data\\BL\\fire_smoke\\labels\\test'

for file in os.listdir(basePath):
    if not file.endswith('xml'):
        img = cv2.imread(os.path.join(basePath, file))
        h, w, _ = img.shape
        name = file.split('.')[0]
        with open(os.path.join(labelsBasePath, name + '.txt'), 'a+', encoding='utf-8') as f:
            xmlFile = os.path.join(basePath, name+'.xml')
            if os.path.isfile(xmlFile):
                tree = ET.parse(xmlFile)
                root = tree.getroot()

                for element in root.findall('object'):
                    id = 0 if element[0].text == 'fire' else 1
                    xmin, ymin, xmax, ymax = int(element[4][0].text), int(
                        element[4][1].text), int(element[4][2].text), int(element[4][3].text)
                    x, y, aw, ah = (xmin + xmax)/2/w, (ymin + ymax) / \
                        2/h, (xmax - xmin)/w, (ymax - ymin)/h
                    f.write(str(id) + ' ' +
                            str('%.6f' % x) + ' ' +
                            str('%.6f' % y) + ' ' +
                            str('%.6f' % aw) + ' ' +
                            str('%.6f' % ah) + ' ' + '\n'
                            )
