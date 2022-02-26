import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk


class AppWindow(tk.Frame):#frame
    def __init__(self, master=None, size=None, path=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()#opencv frame # 자기 자신이 프레임이니까 붙임
        self.sub_fr = None#frame
        self.src = None #tk의 label에 출력할 영상
        self.label = None #tk의 영상을 출력할 레이블
        self.create_widgets(path)
        self.image = None
        self.flag = False

    def make_img(self, path):#path 경로의 이미지를 레이블에 출력
        src = cv2.imread(path)
        src = cv2.resize(src, (640, 480))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)#넘파이 배열을 이미지로 변환
        self.src = ImageTk.PhotoImage(image=img)#tkinter에서 인식할 수 있는 이미지로 생성

    def create_widgets(self, path):#프레임에 위젯 추가
        self.make_img(path)
        self.label = tk.Label(self, image=self.src)
        self.label.pack()
        self.sub_fr = tk.Frame(self.master)#frame
        self.sub_fr.pack()

    def change_img(self, img):#레이블의 이미지 변경

        try:
            img = cv2.resize(img, (640, 480))
            image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            self.label.configure(image=image)
            self.label.image = image

        except Exception as e:
            print(str(e))

        #
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = Image.fromarray(img)
        #
        # self.src = ImageTk.PhotoImage(image=img)
        # self.label['image']=self.src
