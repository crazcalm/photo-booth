from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


def helloCallBack():
    messagebox.showinfo("Hello Python", "Hello World")


class ButtonComponent(Button):
    def __init__(self, root, text="testing"):
        super().__init__(master=root, text=text, command=helloCallBack)

        # Set Button text
        self.set_text()

        # Place the button on the gui
        self.pack(fill=BOTH)

    def set_text(self, title="testing"):
        self.text = title