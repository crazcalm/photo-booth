from tkinter import *
from tkinter.ttk import *


class CanvasComponent(Canvas):
    def __init__(self, root, height=200, width=200):
        super().__init__(master=root, height=height, width=width)

        self.pack(fill=BOTH)
