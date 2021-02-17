from tkinter import *
from tkinter import messagebox as msg
import requests
class Downloader(Tk):
    def __init__(self):
        super().__init__()
        self.title("Image_downloader")
        self.geometry("590x670")
        self.config(bg="#3742fa")
        self._url=StringVar()

class _Main(Downloader):
    def __init__(self):
        super().__init__()
        self.f1=Frame(self,bg="#1B1464",borderwidth=4)
        self.f1.pack()
        self.l1=Label(self,text="Image downloader App",fg="white",font="serif 12 bold",bg="#0984e3",width=36,height=3)
        self.l1.pack(side=TOP,fill=BOTH)
        self.but_q=Button(self,text="Quit",borderwidth=5,bg="#d35400",fg="white",font="serif 12 bold",cursor="spider",command=self.quit)
        self.but_q.pack(side=BOTTOM,fill="both")
        self._l2=Label(self,text="Enter URL for Dwonloading",bg="pink",font="serif 10 bold")
        self._l2.place(x=0,y=112,height=60)
        self._ent=Entry(self,font="serif 13 bold",fg="red",textvariable=self._url)
        self._ent.place(x=200,y=112,height=60,width=370)
        self._butt=Button(self,text="Download",bg="#009432",fg="black",cursor="pirate",font="serif 12 bold",relief=GROOVE,borderwidth=5,command=self._work)
        self._butt.place(x=210,y=200,width=190)
    
    def _work(self):
        self.__url=self._url.get()
        try:
            self._a=requests.get(self.__url,stream=True)
            with open("download.png", 'wb') as self.fd:
                for self.chunk in self._a.iter_content(chunk_size=500*24):
                    self.fd.write(self.chunk)
            msg.showinfo("sucess","sucessfully downloaded...")

        except:
            msg.showerror("error","plz check connection or Url properly...")
            



if __name__=='__main__':
    _window=_Main()
    _window.mainloop()

