
from pytube import YouTube
from tkinter import *

root = Tk()

root.geometry("300x400")
root.title("Youtube video download")

def youtube():
    a=var.get()  #
    ytvideo = YouTube(a).streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first()
    ytvideo.download(r"E:\youtube dwnlder")
    
    print("Entry box",a)

l1 =Label(root,text="YouTube Video Link",fg="red" ,font=("bold",20))
l1.place(x=30,y=20)

var = StringVar()
e1 = Entry(root,textvariable=var,width=60)
e1.place(x=40,y= 80)

b1=Button(root,text = "DOWNLOAD",command = youtube,bg ="green",width=20,fg="white")
b1.place(x=80 ,y=120)



root.mainloop()
