import os
from tkinter import Button, Label
from PIL import ImageTk, Image


class MainWindow:
    def __init__(self, master):
        self.window_root = master

        self.window_root.title("Comic Viewer")
        self.window_root.geometry("800x600")

        self.greet_button = Button(self.window_root, text="Greet", command=self.greet)
        self.greet_button.pack()

        path = os.path.join("Mangas", "Pokemon Adventures", "vol.001 ch.001", "001.jpg")
        original_image = Image.open(path)
        re_sized = original_image.resize((800, 600), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(re_sized)
        self.panel = Label(self.window_root, image=img)
        self.panel.image = img
        self.panel.pack(side="bottom", fill="both", expand="yes")

    @staticmethod
    def greet():
        print("Greetings!")
