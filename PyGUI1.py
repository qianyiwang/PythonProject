from Tkinter import *
from myFunc import *
import tkMessageBox
root = Tk()

def showMessage():
	tkMessageBox.showinfo("Say Hello", "Hello World")

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

check = Checkbutton(root, text="keep me logged in")
check.grid(columnspan=2)

button_1 = Button(root, text="click me", command=showMessage)
button_1.grid(row=3,columnspan=2)

root.mainloop()


