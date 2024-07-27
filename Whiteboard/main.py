from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from turtle import color

root=Tk()
root.title("White Board")
root.geometry("1050x570+130+50")
root.resizable(False,False)


logo = PhotoImage(file="wb.png")
root.iconphoto(False,logo)

color_panel = PhotoImage(file="color section.png")
Label(root,image=color_panel,bg='white').place(x=10,y=20)

eraser = PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="white").place(x=30,y=400)



root.mainloop()
    


