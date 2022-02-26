import pandas as pd
import tkinter
import tkinter.font
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import warnings
warnings.filterwarnings('ignore')


class Covid(tkinter.Frame):

    def __init__(self,path,window=None, title=None, geometry=None):
        super().__init__(window)
        self.window = window
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.resizable(False,False)
        self.window['bg'] = '#666666'
        self.font = tkinter.font.Font(family="한컴 솔잎 B", size=9)

        self.month = ['Apr.','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Total']
        self.month2 = [4,5,6,7,8,9,10,11,12,'total']
        self.raVal = tkinter.IntVar()

        self.df = None
        self.status = None
        self.preprocessing(path)

        self.subfr1 = None
        self.subfr2 = None
        self.subfr3 = None

        self.ui()
        self.background()

    def background(self):
        self.img = Image.open('covid.jpg')
        self.background = ImageTk.PhotoImage(image=self.img)
        self.background_label = tkinter.Label(self.window, image=self.background)
        self.background_label.pack()

    def preprocessing(self,path):
        self.df = pd.read_csv(path, index_col='date', parse_dates=['date'])
        self.df = self.df.dropna()
        self.df = self.df[self.df.index >= '2020-04-01']
        a = self.df.groupby('country').max()[['cumulative_total_cases', 'cumulative_total_deaths']]
        b = self.df.loc['2020-12-26', ['active_cases', 'country']].groupby('country').max()
        self.status = a.merge(b, on='country')

    def ui(self):
        self.subfr1 = tkinter.Frame(self.window)
        self.subfr1.pack(side='left')
        self.subfr1['bg'] = '#999999'
        self.subfr2 = tkinter.Frame(self.window)
        self.subfr2.pack(side='right')
        self.subfr3 = tkinter.Frame(self.subfr1)
        self.subfr3.pack(side='bottom')

        self.button0 = tkinter.Button(self.subfr1, text='Show Countries',bg='#999999',width=20, command=self.showCountries)
        self.button0.pack(side='top')

        for idx, i in enumerate(self.month):
            r = tkinter.Radiobutton(self.subfr1, text=i,bg='#999999', variable=self.raVal, value=idx)
            r.pack(side='top')

        self.label1 = tkinter.Label(self.subfr1,bg='#999999', text='country : ')
        self.label1.pack(side='left')

        self.entry1 = tkinter.Entry(self.subfr1)
        self.entry1.pack(side='left')

        self.button1 = tkinter.Button(self.subfr1, text='검색',bg='#999999', command=self.plot)
        self.button1.pack(side='left')

    def showCountries(self):
        ff2 = self.subfr2.pack_slaves()
        for i in ff2:
            i.destroy()
        countries = self.df['country'].unique()
        self.label0 = tkinter.Label(self.subfr2, text=countries, font=self.font)
        self.label0.pack(side='top', anchor='w')

    def plot(self):
        try:
            self.label0.destroy()
        except Exception as e:
            pass
        ff2, ff3 = self.subfr2.pack_slaves(), self.subfr3.pack_slaves()
        for i, j in zip(ff2, ff3):
            i.destroy()
            j.destroy()

        if self.entry1.get() == '':
            messagebox.showinfo(title='error', message='나라명을 작성해주세요.')
            return
        try:
            month = self.month2[self.raVal.get()]
            country = self.entry1.get()

            status = self.status.loc[country].values.astype('int32')

            self.label2 = tkinter.Label(self.subfr3, text=f'누적 확진자 수:{status[0]}명\n\n누적 사망자 수:{status[1]}명\n\n현재 감염자 수:{status[2]}명', font=self.font)
            self.label2.pack(side='bottom', anchor='w')

            if month == 'total':
                df = self.df
                df = df[df['country'] == country]
                fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
                axes[0].plot(df.index, df['daily_new_cases'], color='r')
                axes[0].set_title(f'Number of infected in {country}')
                axes[0].set_ylabel('infected number')
                axes[1].plot(df.index, df['daily_new_deaths'], color='b')
                axes[1].set_title(f'Number of dead in {country}')
                axes[1].set_ylabel('dead number')
                plt.xticks(rotation=90)

            else:
                df = self.df.loc['2020-'+str(month)]
                df = df[df['country'] == country]
                fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
                axes[0].plot(df.index, df['daily_new_cases'], color='r', marker='o', )
                axes[0].set_title(f'Number of infected in {country}')
                axes[0].set_ylabel('infected number')
                axes[1].plot(df.index, df['daily_new_deaths'], color='b', marker='o')
                axes[1].set_title(f'Number of dead in {country}')
                axes[1].set_ylabel('dead number')
                plt.xticks(df.index, rotation=90)

            plt.tight_layout()
            self.line = FigureCanvasTkAgg(fig,self.subfr2)
            self.line.get_tk_widget().pack(side='left')

        except Exception as e:
            messagebox.showinfo(title='error', message='나라명을 제대로 작성해주세요.')
            return

def main():
    window = tkinter.Tk()
    title = 'COVID19 Infomation'
    geometry = ('1000x540')
    path = 'covid.csv'
    a = Covid(path,window,title,geometry)
    a.mainloop()

main()
