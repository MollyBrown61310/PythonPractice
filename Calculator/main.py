import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

logo = PhotoImage(file="calc.png")
root.iconphoto(False,logo)


label_result= Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

root.mainloop()



 
