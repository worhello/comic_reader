from PIL import ImageTk, Image
from image_utilities import resize_image

class Page:
    def __init__(self, page_to_display):
        self.page_file_name = page_to_display
        original_image = Image.open(self.page_file_name)
        re_sized = resize_image(original_image)
        self.image = ImageTk.PhotoImage(re_sized)

    def __str__(self):
        return self.page_file_name

    def get_image(self):
        return self.image
