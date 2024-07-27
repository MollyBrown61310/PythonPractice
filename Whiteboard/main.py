from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os

root=Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False,False)

#icon
image_icon = PhotoImage(file="wb.png")
root.iconphoto(False,image_icon)

#sidebar
color_box = PhotoImage(file="color section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f5").place(x=30,y=400)

importimage=PhotoImage(file="addimage.png")
Button(root,image=importimage,bg="white").place(x=30,y=450)

colors=Canvas(root,bg="#fff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

#main screen 
canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

root.mainloop()