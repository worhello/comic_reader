from PIL import Image

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 800


def resize_image(img):
    image_width = img.size[0]
    image_height = img.size[1]
    resized_width = WINDOW_WIDTH
    resized_height = WINDOW_HEIGHT

    if image_width > image_height:
        adjustment_ratio = WINDOW_WIDTH / float(img.size[0])
        resized_height = int((float(img.size[1]) * float(adjustment_ratio)))
    else:
        adjustment_ratio = WINDOW_HEIGHT / float(img.size[1])
        resized_width = int((float(img.size[0]) * float(adjustment_ratio)))

    re_sized = img.resize((resized_width, resized_height), Image.ANTIALIAS)
    return re_sized
