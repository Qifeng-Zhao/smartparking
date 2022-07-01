import ffmpeg
import time
import cv2
import sys
import random
from sys import path
path.append('/Users/zhaoqifeng8/PycharmProjects/yolov5/yolov5')
from yolov5.detect import detect
# 子进程

for i in range(3):
    print(time.strftime("B %Y-%m-%d-%H_%M_%S", time.localtime()))
    (
           ffmpeg
           .input('rtsp://admin:Jingdongyun@192.168.1.64:554/h264/ch1/main/av_stream')
                # 保存的文件名
                #.filter('fps',fps='2')
                #.output('./temprate/test-%d.png',start_number=0)
           #.output('./temprate/test.png', vframes=1, format='image2', vcodec='mjpeg', start_number=0)
           .output('./temprate/test.png', vframes=1)
                # 覆盖同名文件
                .overwrite_output()
                # 运行保存
                .run(capture_stdout=True)

    )
    print(time.strftime("A %Y-%m-%d-%H_%M_%S", time.localtime()))


    detect( weights='yolov5s.pt',  # model.pt path(s)
               source='./temprate/test.png',  # file/dir/URL/glob, 0 for webcam
               imgsz=640,  # inference size (pixels)
               conf_thres=0.25,  # confidence threshold
               iou_thres=0.45,  # NMS IOU threshold
               max_det=1000,  # maximum detections per image
               device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
               view_img=False,  # show results
               save_txt=False,  # save results to *.txt
               save_conf=False,  # save confidences in --save-txt labels
               save_crop=False,  # save cropped prediction boxes
               nosave=False,  # do not save images/videos
               classes=None,  # filter by class: --class 0, or --class 0 2 3
               agnostic_nms=False,  # class-agnostic NMS
               augment=False,  # augmented inference
               update=False,  # update all models
               project='runs/detect',  # save results to project/name
               name='exp',  # save results to project/name
               exist_ok=True,  # existing project/name ok, do not increment
               line_thickness=3,  # bounding box thickness (pixels)
               hide_labels=False,  # hide labels
               hide_conf=False,  # hide confidences
               half=False,  # use FP16 half-precision inference
               )
    print(time.strftime("AA %Y-%m-%d-%H_%M_%S", time.localtime()))