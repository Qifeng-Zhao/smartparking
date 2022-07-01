import xml.etree.ElementTree as ET
from typing import List

from PyQt5.QtCore import QRect


def Cood():
    tree = ET.parse('C:\\Users\\zhaoqifeng8\\PycharmProjects\\yolov5\\test.xml')
    root = tree.getroot()
    # print(root.tag, root.attrib)
    # for child in root:
    #     print(" ", child.tag, ":", child.attrib)
    #     for children in child:
    #         print(" ", children.tag, ":", children.attrib)
    #         for chii in children:
    #             print(" ", chii.tag, ":", chii.attrib)

    cood = list()
    for obj in root.iter('bndbox'):
        xmin = int(obj.find('xmin').text)
        ymin = int(obj.find('ymin').text)
        xmax = int(obj.find('xmax').text)
        ymax = int(obj.find('ymax').text)
        cood.append([ymin, ymax, xmin, xmax])
    #print(cood)

    return cood


def rectCood():
    coords = Cood()
    rect = QRect()
    rectList = list()
    for coord in coords:
        rect.setTop(coord[0])  # ymin
        rect.setBottom(coord[1])  # ymax
        rect.setLeft(coord[2])  # xmin
        rect.setRight(coord[3])  # xmax
        rectList.append(rect)
        rect = QRect()
    print(rectList)
    return rectList
#print (Cood())
