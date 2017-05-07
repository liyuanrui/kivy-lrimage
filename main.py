#coding=utf-8
#qpy:kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.clock import Clock
import time
import os
import cv2
import uuid

if not os.path.exists('/sdcard/temp'):os.mkdir('/sdcard/temp')
os.system('rm -rf /sdcard/temp/*')
dirname='/sdcard/temp'


class MyLayout(BoxLayout):
    source=''
    ssource=''
    img=''
    def load(self,path,filename):
        self.source=os.path.join(path,filename[0])
        
        self.ids.image.source=self.source
    def canny(self):
        self.img=cv2.imread(self.source)
        self.img=cv2.Canny(self.img,81,200)
        fname=uuid.uuid1().hex
        char=self.source.split('.')[-1]
        filesource='%s/%s.%s'%(dirname,fname,char)
        cv2.imwrite(filesource,self.img)
        self.ids.image2.source=filesource
    def witnot(self):
        self.img=cv2.imread(self.source)
        self.img=cv2.bitwise_not(self.img)
        fname=uuid.uuid1().hex
        char=self.source.split('.')[-1]
        filesource='%s/%s.%s'%(dirname,fname,char)
        cv2.imwrite(filesource,self.img)
        self.ids.image2.source=filesource
    def save(self,path):
        filename=self.source.split('/')[-1]
        self.ssource=os.path.join(path,filename)
        cv2.imwrite(self.ssource,self.img)
        
class MainApp(App):
    def build(self):
        return MyLayout()

MainApp().run()