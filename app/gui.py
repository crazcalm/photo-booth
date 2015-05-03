from tkinter import *
from tkinter.ttk import *
import picamera
from gui_components.canvas_component import CanvasComponent
from gui_components.button_components import ButtonComponent


class Gui(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        # GUI Properties

        # Reference to GUI Components
        self.canvas = None
        self.take_photo_button = None

        self.set_title()

        # Create GUI Components
        self.canvas = CanvasComponent(self.root)

        # Create buttons
        self.take_photo_button = ButtonComponent(self.root)
        self.testing = Button(self.root, text="info", command=self.window_info)
        self.testing.pack()

        # Disables the entire top level window
        self.root.overrideredirect(True)

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

    def window_info(self):
        print(self.root.winfo_rootx())

    def on_resize(self, event):
        print(dir(event))
        print(event.height, event.width)
        print(event.x_root, event.y_root)
        print(event.x, event.y)
        print(self.root.winfo_rootx, self.root.winfo_rooty)
        print(dir(self.root))


if __name__ == "__main__":
    root = Tk()
    test = Gui(root)
    test.mainloop()
