import tkinter

window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
#window.configure(bg='#333333')

login_label = tkinter.Label(window, text="Login")




login_label.grid(row=0, column=0)


window.mainloop()