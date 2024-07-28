import tkinter

window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')

login_label = tkinter.Label(window, text="Login", bg='#333333' , fg="#FFFFFF" )
username_label = tkinter.Label(window, text="Username", bg='#333333', fg="#FFFFFF")
username_entry = tkinter.Entry(window)
password_entry = tkinter.Entry(window, show="*")
password_label = tkinter.Label(window, text="Password", bg='#333333', fg="#FFFFFF" )
login_button = tkinter.Button(window, text="Login", bg='#FF3399', fg="#FFFFFF" )


login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)




window.mainloop()