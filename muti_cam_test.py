import av
import cv2
import pymysql
import imutils
from skimage.metrics import structural_similarity
import time
from skimage import filters, img_as_ubyte
import numpy as np
import time
import datetime
from sys import path
path.append('/Users/zhaoqifeng8/PycharmProjects/yolov5/yolov5')

from yolov5.detect import detect


container = av.open("./cut1.mp4")
from occupation_detect import occupation
from coord import Cood


coord=Cood()
slot_number= len(coord)
receive = [0]*slot_number
start_time= [0]*slot_number
flag= [0]*slot_number


print(coord)
#for frame in container.decode(streams=0):
while(1):
    #container = av.open("rtsp://admin:Jingdongyun@192.168.1.64:554/h264/ch1/main/av_stream")

    frames = container.decode(streams=0)
    frame=next(frames)
    frame.to_image().save('./temprate/frame1.jpg') #% frame.index)
    k=0
    while k!=10 :
        frame = next(frames)
        k=k+1
    frame.to_image().save('./temprate/frame2.jpg')  # % frame.index)






    file_path1='./temprate/frame1.jpg'
    file_path2='./temprate/frame2.jpg'
    for i in range(slot_number):
        coord1=coord[i] # ymin ymax xmin xmax
        receive[i] = occupation(file_path1, file_path2,coord1,threshold=0.45)

    for j in range(slot_number):
        if receive[j] ==1:
            start_time[j] = datetime.datetime.now()
            flag[j]=1


    for ii in range(slot_number):
        if flag[ii]==1:

            if current_time - start_time[ii] > datetime.timedelta(seconds=3):
                img = cv2.imread("./temprate/frame2.jpg")
                cropped = img[coord[ii][0]:coord[ii][1], coord[ii][2]:coord[ii][3]]
                cv2.imwrite("./temprate/cropped.jpg", cropped)

                ff,red=detect(weights='yolov5s.pt',  # model.pt path(s)
                           source='./temprate/cropped.jpg',  # file/dir/URL/glob, 0 for webcam
                           imgsz=640,  # inference size (pixels)
                           conf_thres=0.10,  # confidence threshold
                           iou_thres=0.45,  # NMS IOU threshold
                           max_det=1000,  # maximum detections per image
                           device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
                           view_img=False,  # show results
                           save_txt=True,  # save results to *.txt
                           save_conf=False,  # save confidences in --save-txt labels
                           save_crop=False,  # save cropped prediction boxes
                           nosave=False,  # do not save images/videos
                           classes=2,  # filter by class: --class 0, or --class 0 2 3
                           agnostic_nms=False,  # class-agnostic NMS
                           augment=False,  # augmented inference
                           update=False,  # update all models
                           project='runs/detect',  # save results to project/name
                           name='exp',  # save results to project/name
                           exist_ok=False,  # existing project/name ok, do not increment
                           line_thickness=3,  # bounding box thickness (pixels)
                           hide_labels=False,  # hide labels
                           hide_conf=False,  # hide confidences
                           half=False,  # use FP16 half-precision inference
                           )
                print("slot:",ii, "detected")
                mark_time = datetime.datetime.now()
                print(mark_time)
                flag[ii]=0
                iii=ii+1
                print(len(red))

                print("ff="+str(ff))
                st=0


                if red != [0,0]:
                    print("red!=0")
                    red_num=len(red)
                    for jj in range(0,red_num):
                        if red[jj][0] and red[jj][1] >0.5:
                            st=1
                            print('st=1')
                            break

                    print("st="+str(st))


                if ff==1 and st==0:
                    ff=0





                print(red)
                current_time = datetime.datetime.now()
                t=str(current_time)
                t=t[0:-7]
                print("t=",t)

                conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="Jingdongyun",
                    database="smartparking",
                    charset="utf8"
                )




                # 得到一个可以执行SQL语句的光标对象
                cursor = conn.cursor()
                # 执行完毕返回的结果集默认以元组显示

                # 定义要执行的SQL语句
                sql = ("SET SQL_SAFE_UPDATES = 0;")
                cursor.execute(sql)
                conn.commit()

                sql = ("update id set occupation = "+ str(ff) + " where local_id ="+ str(iii)+";")
                print(sql)
                # 执行SQL语句
                cursor.execute(sql)
                conn.commit()

                sql = ("update id set start_time = '" + t + "' where local_id =" + str(iii) + ";")
                print(sql)
                # 执行SQL语句
                cursor.execute(sql)
                conn.commit()
                sql=("select local_id,gloable_id,occupation,camera,start_time from id where local_id ="+ str(iii))
                cursor.execute(sql)
                results = cursor.fetchone()
                print(results)
                file_handle = open('./1.txt', mode='w')
                file_handle.write(str(results))
                file_handle.write('\n')

                file_handle.close()

                conn.commit()


                cursor.close()

                # 关闭数据库连接
                conn.close()









        else:
           print('nothing happened')

    current_time = datetime.datetime.now()

    time.sleep(0.1)

    # 关闭光标对象






