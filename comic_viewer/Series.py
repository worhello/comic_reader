from Comic import Comic, EndOfComicException, BeforeStartOfComicException
import os


class Series:
    def __init__(self, root_directory, series_name):
        self.comics_names = [comic_page for comic_page in os.listdir(os.path.join(root_directory, series_name))]
        self.current_comic_index = 0
        self.current_comic_name = self.get_first_comic()
        self.parent_directory = os.path.join(root_directory, series_name)
        self.comic_directory = os.path.join(self.parent_directory, self.get_current_comic_name())
        self.current_comic = Comic(self.comic_directory)

        self.previous_comic = self.current_comic
        self.next_comic = self.current_comic

    def get_comic_from_index(self, index):
        return self.comics_names[index]

    def get_current_comic_name(self):
        return self.get_comic_from_index(self.current_comic_index)

    def get_first_comic(self):
        return self.get_comic_from_index(0)

    def get_current_image(self):
        return self.current_comic.get_current_image()

    def update_current_comic(self):
        self.comic_directory = os.path.join(self.parent_directory, self.get_current_comic_name())
        self.current_comic = None
        self.current_comic = Comic(self.comic_directory)

    def get_next_page(self):
        try:
            return self.current_comic.get_next_image()
        except EndOfComicException:
            self.previous_comic = self.current_comic
            self.current_comic_index += 1
            self.update_current_comic()
            return self.current_comic.get_first_page()

    def get_previous_page(self):
        try:
            return self.current_comic.get_previous_image()
        except BeforeStartOfComicException:
            self.next_comic = self.current_comic
            self.current_comic_index -= 1
            self.update_current_comic()
            return self.current_comic.get_last_page()
