from Page import Page
import os


class Comic:
    def __init__(self, comic_name):
        self.current_page_index = 0
        self.all_pages = [
            Page(os.path.join(comic_name, comic_page))
            for comic_page in os.listdir(comic_name)
        ]

    def get_first_page(self):
        self.current_page_index = 0
        return self.get_current_image()

    def get_current_image(self):
        return self.get_page(self.current_page_index)

    def get_page(self, page_index):
        return self.all_pages[page_index].get_image()

    def get_next_image(self):
        self.current_page_index += 1
        return self.get_current_image()

    def get_previous_image(self):
        self.current_page_index -= 1
        return self.get_current_image()
