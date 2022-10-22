#shutdown app using python
from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restsrt_time():
    os.system("shutdown /r /t 20")
def lgout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

a = Tk()
a.title("SHUTDOWN")
a.geometry("500x500")
a.resizable(False,False)
a.config(bg="Black")
#-----------------------------------------
but_ = Button(a,text="RESTART", font=("Time New Roman",50,"bold"),bg="Aqua",fg="Black",command=restart)
but_.place(x=50,y=36,height=80,width=400)
#--------------------------------------
but_ = Button(a,text="RESTART-T", font=("Time New Roman",50,"bold"),bg="Aqua",fg="Black",command=restsrt_time)
but_.place(x=50,y=152,height=80,width=400)
#-------------------------------------------
but = Button(a,text="LOG-OUT", font=("Time New Roman",50,"bold"),bg="Aqua",fg="Black",command=lgout)
but.place(x=50,y=268,height=80,width=400)
#----------------------------------------------
but = Button(a,text="SHUTDOWN", font=("Time New Roman",50,"bold"),bg="Aqua",fg="Black",command=shutdown)
but.place(x=50,y=384,height=80,width=400)

a.mainloop()