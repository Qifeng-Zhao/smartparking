import subprocess

def convert_to_seq():
 #input = r"rtsp://admin:Jingdongyun@192.168.1.64:554/h264/ch1/main/av_stream"
 input = r"D:\CCTV.mp4"
 output = r"D:\temp/%04d.png"

 cmd= f'ffmpeg -i "{input}" "{output}"'
 print(cmd)
 subprocess.check_output(cmd,shell=True)

convert_to_seq()

