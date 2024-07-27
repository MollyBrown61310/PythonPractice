from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()

# Window title 
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

# Window icon
root.iconphoto(False, tk.PhotoImage(file="wb.png"))

color_box=PhotoImage(file="color section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

eraser=PhotoImage(file="eraser.png")
Button(root, image=eraser,bg="#f2f3f5").place(x=30,y=400)

colors=Canvas(root,bg="#ffffff",width=37,height=300,bd=0)
colors.place(x=30,y=60)



canvas= Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>')
canvas.bind('<B1-Motion>')




root.mainloop()