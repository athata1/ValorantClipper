import os;
import cv2;
from lobe import ImageModel
from PIL import Image as I
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import numpy as np
import math
import tkinter as tk;
from tkinter import *;
from tkinter import filedialog


def valo_clipper():
   #Delete Clips before starting
   if (".mp4" not in input_video):
      return;
   else:
      root.destroy();
   for f in os.listdir(r'ValorantClips'):
       os.remove(os.path.join(r'ValorantClips', f))
   
   model = ImageModel.load(r'TensorFlow');
   print("loaded model");
   
   
   #Split video into individual frames
   vidcap = cv2.VideoCapture(input_video)
   fps = int(vidcap.get(cv2.CAP_PROP_FPS))
   cooldown_time = duration
   success,image = vidcap.read()
   count = 0
   success = True
   cooldown = 0;
   numClips = 1;
   vid = VideoFileClip(input_video)
   
   while success:
     if(count % fps == 0):
         image = cv2.resize(image, (1920,1080))
         image = image[770:960, 860:1060]
         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
         im = I.fromarray(image) #PIL Image
         result = model.predict(im);
         if (cooldown == 0 and result.prediction != "background"):
             print(count);
             #ffmpeg_extract_subclip('ValorantClip2.mp4',count/fps-duration , count/fps+duration, targetname="ValorantClips/video%d.mp4" % numClips)
             new = vid.subclip(count/fps-duration, count/fps+duration)
             new.write_videofile("ValorantClips/video%d.mp4" % numClips, audio_codec='aac')
             cooldown = cooldown_time;
             numClips = numClips + 1;
         if (cooldown != 0):
             cooldown = cooldown - 1;
     success,image = vidcap.read()
     count = count + 1
   print("Images created");
   exit();
   
def UploadAction(event=None):
    global input_video;
    input_video = filedialog.askopenfilename()
    print('Selected:', input_video)
    
def retrieve_input():
    global duration
    temp=textBox.get("1.0","end-1c")
    if (not temp.isnumeric()):
      duration = 5;
    else:
      duration = int(temp);
    print(duration)

#initial values
input_video = 'hello';
duration = 5;

#Tkinter window display
root = tk.Tk()
root.geometry('300x150')
root.title("ValorantClipper");
textBox=Text(root, height=2, width=3)
buttonCommit=Button(root, height=1, width=15, text="Input Crop Radius", command=lambda: retrieve_input())
button1 = tk.Button(root, text='Select Video File',width = 19, command=UploadAction)
button2 = tk.Button(root, text='Start Clipping Video',width = 19, command=valo_clipper)
button1.pack()
button2.pack()
textBox.pack()
buttonCommit.pack()
posX = 75;
posY = 25;
button1.place(x=posX,y=posY)
button2.place(x=posX,y=posY+50)
textBox.place(x=posX,y=posY+25)
buttonCommit.place(x=posX+25,y=posY+25)
root.mainloop()