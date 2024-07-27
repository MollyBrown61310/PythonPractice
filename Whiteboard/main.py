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
Label(root,image=color_panel,bg="#f2f3f5").place(x=10,y=20)

eraser = PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#ffffff",).place(x=30,y=400)

colors = Canvas(root,bg="#f2f3f5",width=37,height=300,border=10,bd=0)
colors.place(x=30,y=60)

canvas = Canvas(root,bg="white",width=930,height=500,cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind("<Button-1>")
canvas.bind("<B1-Motion>")

def color_palete():
    pass


root.mainloop()




