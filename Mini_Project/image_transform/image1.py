import cv2
import tkinter
import tkinter.font
from tkinter import messagebox

import albumentations as A
from PIL import Image
from PIL import ImageTk
from PIL import ImageGrab
import os
import image_transform.db as db

class imageTransform(tkinter.Frame):

    def __init__(self, window=None,title=None,geo=None):
        super().__init__(window)
        self.window = window
        self.window.title(title)
        self.window.geometry(geo)
        self.window['bg'] = '#D7AC87'
        self['bg'] = '#D7AC87'
        self.window.resizable(False,False)
        self.pack(side='left')
        self.raVal = tkinter.IntVar()
        self.cnt = 0
        self.imageNum=0
        self.path = './images'
        self.images = os.listdir(self.path)
        self.src = cv2.imread(self.path+'/'+self.images[self.cnt])
        self.srcResize = cv2.resize(self.src, (640, 400))
        self.subfr = None
        self.subfr2 = None
        self.subfr3 = None
        self.first = False
        self.font = tkinter.font.Font(family="한컴 솔잎 B", size=15)
        self.target = {0: '앵무새', 1: '고양이', 2: '개', 3: '사슴', 4: '여우', 5: '고슴고치', 6: '라쿤'}
        self.ui()
        self.ui2()
        self.ui3()
        self.ui4()

    def ui(self):
        self.subfr = tkinter.Frame(self.window)
        self.subfr.pack(side='right')
        self.subfr2 = tkinter.Frame(self)
        self.subfr2.pack(side='bottom')
        self.subfr3 = tkinter.Frame(self.subfr)
        self.subfr3.pack(side='bottom',anchor='s')
        self.subfr['bg'] = '#D7AC87'
        self.subfr2['bg'] = '#D7AC87'
        self.subfr3['bg'] = '#D7AC87'
        img = cv2.cvtColor(self.srcResize, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)

        self.label = tkinter.Label(self, image=imgtk)
        self.label.pack(side="top")

        self.label.config(image=imgtk)
        self.label.image = imgtk

        self.prev = tkinter.Button(self, bg='#fa8072', fg='white', width=10, text='prev', command=self.before)
        self.prev.pack(side="left", anchor='n', expand=True)

        self.next = tkinter.Button(self, bg='#fa8072', fg='white', width=10, text='next', command=self.after)
        self.next.pack(side="right", anchor='n', expand=True)

        self.button2 = tkinter.Button(self,bg='#ffebcd',fg='black', text="이미지 변환",width=50, command=self.album)
        self.button2.pack(side="top",anchor='n', expand=False)#fill='both'

        self.button = tkinter.Button(self, bg='#ffebcd', fg='black', text="이진화 처리",width=50, command=self.convert_to_tkimage)
        self.button.pack(side="top", expand=False)

        self.button3 = tkinter.Button(self, bg='#ffebcd', fg='black', text="이미지 저장",width=50, command=self.save)
        self.button3.pack(side="top", expand=False)

        self.label2 = tkinter.Label(self,bg='#D7AC87', text='파일 이름:')
        self.label2.pack(side='left')
        self.fileName = tkinter.Entry(self)
        self.fileName.pack(side='left')

    def ui2(self):
        src = cv2.imread('mysql.jpg') # 처음 시작때의 sql이미지
        srcResize = cv2.resize(src, (640, 400))
        img = cv2.cvtColor(srcResize, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.transformedLabel = tkinter.Label(self.subfr,image=imgtk)
        self.transformedLabel.pack()
        self.transformedLabel.config(image=imgtk)
        self.transformedLabel.image = imgtk

        self.tfedName = tkinter.Label(self.subfr,bg='#D7AC87',text='파일 이름:')#,width='15',height='7'
        self.tfedName.pack(side='left')
        self.loadName = tkinter.Entry(self.subfr)
        self.loadName.pack(side='left')

        self.loadBtn = tkinter.Button(self.subfr, bg='#ffebcd', fg='black', text='불러오기',width=50,height=3,command=lambda: self.tfload(self.loadName.get()))
        self.loadBtn.pack(side='right',  expand=True)

    def ui3(self):
        for idx, i in enumerate(self.target.values()):
            r = tkinter.Radiobutton(self.subfr2,bg='#D7AC87', text=i, variable=self.raVal, value=idx)
            r.grid(row=0, column=idx)

    def ui4(self):
        ff = self.subfr3.grid_slaves()
        for i in ff:
            i.destroy()  # 위젯삭제
        countName = ['전체','앵무새','고양이','개','사슴','여우','고슴도치','라쿤']
        for idx, i in enumerate(countName):
            r = tkinter.Label(self.subfr3,bg='#D7AC87', text=i,borderwidth=1,font=self.font)
            r.grid(row=1, column=idx,padx=10)

        count = db.count()
        for idx, i in enumerate(count):
            r = tkinter.Label(self.subfr3,bg='#D7AC87', text=i,borderwidth=1,font=self.font)
            r.grid(row=2, column=idx)

    def tfload(self, filename):
        if filename == '':
            messagebox.showinfo(title='error', message='파일 이름을 작성해주세요.')
        elif not filename.isalnum():
            messagebox.showinfo(title='error', message='특수문자는 사용할 수 없습니다. 파일 이름만 작성해주세요.')
        else:
            image = db.loadDB(filename+'.jpg')
            if image == False:
                messagebox.showinfo(title='error', message='없는 파일입니다.')
            else:
                imgtk = ImageTk.PhotoImage(image)
                self.transformedLabel.config(image=imgtk)
                self.transformedLabel.image = imgtk

    def update(self,image):
        img = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.config(image=imgtk)
        self.label.image = imgtk

    def convert_to_tkimage(self): # 이진화처리
        gray = cv2.cvtColor(self.srcResize, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        self.update(binary)

    def album(self): #이미지 변환
        transform = A.Compose([
            #A.RandomRotate90(),
            A.Flip(p=0.2),
            #A.Transpose(),
            A.ChannelShuffle(p=0.3),
            A.ElasticTransform(p=0.3,border_mode=cv2.BORDER_REFLECT_101,alpha_affine=40),
            A.OneOf([
                A.IAAAdditiveGaussianNoise(),
                A.GaussNoise(),
            ], p=0.2),
            A.OneOf([
                A.MotionBlur(p=.2),
                A.MedianBlur(blur_limit=3, p=0.1),
                A.Blur(blur_limit=3, p=0.1),
            ], p=0.2),
            A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
            A.OneOf([
                A.OpticalDistortion(p=0.3),
                A.GridDistortion(p=.1),
                A.IAAPiecewiseAffine(p=0.3),
            ], p=0.2),
            A.OneOf([
                A.CLAHE(clip_limit=2),
                A.IAASharpen(),
                A.IAAEmboss(),
                A.RandomBrightnessContrast(),
            ], p=0.3),
            A.HueSaturationValue(p=0.3),
        ])
        image = cv2.cvtColor(self.srcResize, cv2.COLOR_BGR2RGB)
        transformed = transform(image=image)['image']
        self.update(transformed)

    def before(self):
        if self.cnt == 0:
            messagebox.showinfo(title='error', message='This is first image')
        else:
            self.cnt-=1
            self.viewImg()

    def after(self):
        if self.cnt == len(self.images)-1:
            messagebox.showinfo(title='error', message='This is last image')
        else:
            self.cnt+=1
            self.viewImg()

    def viewImg(self):
        print(self.images[self.cnt])
        self.src = cv2.imread(self.path + '/' + self.images[self.cnt])
        self.srcResize = cv2.resize(self.src, (640, 400))
        img = cv2.cvtColor(self.srcResize, cv2.COLOR_BGR2RGB)
        self.update(img)

    def save(self):
        x = self.window.winfo_rootx()  # 창의 왼쪽 위의 x 좌표
        y = self.window.winfo_rooty()+5  # 창의 왼쪽 위의 y 좌표
        w = x+640
        h = y+400-2

        box = (x, y, w, h)
        img = ImageGrab.grab(box)  # 창의 크기만큼만 이미지저장
        filename = self.fileName.get()
        if filename == '':
            messagebox.showinfo(title='error', message='파일 이름을 작성해주세요.')
        elif not filename.isalnum(): # 숫자와 문자열로 이루어져있으면 True 아니면 False
            messagebox.showinfo(title='error', message='특수문자는 사용할 수 없습니다. 파일 이름만 작성해주세요.')
        else:
            target = self.target[self.raVal.get()]
            filename = filename+'.jpg'
            db.saveDB(filename,img,target)
            print(self.imageNum)
            self.ui4()


def main():
    window = tkinter.Tk()
    title = "image transformer"
    geometry = ("1300x540+100+100")
    a = imageTransform(window,title,geometry)
    a.mainloop()
#("1300x500+100+100")
main()
