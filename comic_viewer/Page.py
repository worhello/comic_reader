from PIL import ImageTk, Image


class Page:
    def __init__(self, page_to_display):
        self.page_file_name = page_to_display
        original_image = Image.open(self.page_file_name)
        re_sized = original_image.resize((800, 600), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(re_sized)

    def __str__(self):
        return self.page_file_name

    def get_image(self):
        return self.image
