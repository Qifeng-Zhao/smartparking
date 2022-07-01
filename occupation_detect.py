import cv2
import imutils
from skimage.metrics import structural_similarity
import time
from skimage import filters, img_as_ubyte
import numpy as np

start = time.time()
# 读入图像，转为灰度图像
from skimage import io

#file_path1 = './frame1.jpg'
#file_path2 = './frame2.jpg'
#coord = [16, 1017, 1145, 1682]
#coord=[445,581,971,1749] #ymin ymax xmin xmax

def occupation(file_path1,file_path2,coord,threshold=0.2):

    img = io.imread(file_path1)
    #img=img[500:719, 0:539]
    #img=img[339:530,239:705]
    #img=img[488:639,468:1381]
    #img=img[558:797,18:868]
    img=img[coord[0]:coord[1],coord[2]:coord[3]]

    #src = cv2.imread(file_path1)


    src = io.imread(file_path2)
    src = src[coord[0]:coord[1], coord[2]:coord[3]]
    #src=src[445:581,971:1749]
    #src=src[558:797,18:868]
    #src=src[488:639,468:1381]
    #src= src[500:719, 0:539 ]
    #src=src[339:530,239:705]
    #src = cv2.imread(file_path2)

    #img = cv2.imread('./Camer2.jpg')
    grayA = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    grayB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 计算两个灰度图像之间的结构相似度
    (score, diff) = structural_similarity(grayA, grayB, win_size=101, full=True)
    diff = (diff * 255).astype("uint8")
    print(score)



    #cv2.namedWindow("right", cv2.WINDOW_NORMAL)
    #cv2.imshow('right', src)
    #cv2.namedWindow("left", cv2.WINDOW_NORMAL)
    #cv2.imshow('left', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    if score<threshold:
        print("detected")
        return 1
    else:
        print("undetected")
        return 0

#occupation(file_path1,file_path2,coord)

