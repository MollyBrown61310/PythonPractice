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


root.mainloop()