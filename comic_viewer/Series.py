from Comic import Comic
import os


class Series:
    def __init__(self, root_directory, series_name):
        self.comic_directory = os.path.join(root_directory, series_name, self.get_current_comic())
        self.comic = Comic(self.comic_directory)

    def get_current_comic(self):
        return self.get_first_comic()

    def get_first_comic(self):
        return "vol.001 ch.001"

    def get_current_image(self):
        return self.comic.get_current_image()

    def get_next_page(self):
        return self.comic.get_next_image()

    def get_previous_page(self):
        return self.comic.get_previous_image()
