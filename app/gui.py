from tkinter import *
from tkinter.ttk import *


class Gui(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        # GUI Properties

        # Reference to GUI Components

        self.set_title()

        # Create GUI Components

        # Packs the GUI
        self.pack_propagate(0)
        self.pack()

    def set_title(self, title="Photo Booth"):
        """
        Sets the title of the GUI

        :param title: str
        :return: None
        """
        self.root.title(title)


if __name__ == "__main__":
    root = Tk()
    test = Gui(root)
    test.mainloop()
