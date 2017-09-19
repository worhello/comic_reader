import os
from tkinter import Label
from PIL import ImageTk, Image

from Series import Series


class MainWindow:
    def __init__(self, master):
        self.window_root = master

        self.window_root.title("Comic Viewer")
        self.window_root.geometry("800x600")

        root_directory = "Mangas"
        comic_name = "Pokemon Adventures"

        self.shown_series = Series(root_directory, comic_name)

        img = self.shown_series.get_current_image()
        self.panel = Label(self.window_root, image=img)
        self.panel.image = img
        self.panel.focus_set()
        self.panel.pack(side="bottom", fill="both", expand="yes")

        # self.show_image(img)
        self.window_root.bind("<Left>", self.handle_left_key_event)
        self.window_root.bind("<Right>", self.handle_right_key_event)

    def show_image(self, img):
        self.panel.configure(image=img)
        self.panel.image = img
        self.panel.focus_set()
        self.panel.pack(side="bottom", fill="both", expand="yes")

    def handle_left_key_event(self, _):
        previous_page = self.shown_series.get_previous_page()
        self.show_image(previous_page)

    def handle_right_key_event(self, _):
        next_page = self.shown_series.get_next_page()
        self.show_image(next_page)
