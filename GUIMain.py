from tkinter import*
from tkinter import filedialog
import os
import subprocess

root=Tk()
root.geometry("1350x700+0+0")
root.title("Vehicle Detection and Counting")
bg_color="#066073"
title=Label(root,text="Vehicle Detection and Counting",bd=12,bg=bg_color,fg="white",relief=GROOVE,font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

def vehicle():
    exec(open("test2.py").read())
    root.update()

def speed():
    exec(open("speed.py").read())
    root.update()

def number():
    exec(open("numberplate.py").read())
    root.update()
       

label1=Label(root)
F1=LabelFrame(root ,text="DETECTION & COUNTING",font=("Times New Roman",15,"bold"),bg="#00BFFF",fg="black",bd=7,relief=GROOVE)
F1.place(x=60,y=150,width=400,height=400)

F2=LabelFrame(root,text="SPEED ESTIMATION",font=("Times New Roman",15,"bold"),bg="Grey",fg="white",bd=7,relief=GROOVE)
F2.place(x=550,y=150,width=400,height=400)

F3=LabelFrame(root,text="NUMBER PLATE DETECTION",font=("Times New Roman",15,"bold"),bg="#FA8072",fg="black",bd=7,relief=GROOVE)
F3.place(x=1050,y=150,width=400,height=400)

Button1=Button(root,text="COUNT",font=("arial",15,"bold"),bg="orchid1",fg="black",bd=7,pady=20,command=vehicle)
Button1.place(x=200,y=600)

Button2=Button(root,text="SPEED",font=("arial",15,"bold"),bg="orchid1",fg="black",bd=7,pady=20,command=speed)
Button2.place(x=700,y=600)

Button3=Button(root,text="NUMBER",font=("arial",15,"bold"),bg="orchid1",fg="black",bd=7,pady=20,command=number)
Button3.place(x=1200,y=600)



root.mainloop()