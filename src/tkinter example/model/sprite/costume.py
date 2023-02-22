from tkinter import Image
import cv2
from PIL import Image, ImageTk


class Costume:
    costume_name = ""
    assetId = ""

    def __init__(self, img):
        # Converts CV2 image to tkinter to display (easier to wok with)
        # Taken from https://www.tutorialspoint.com/read-an-image-with-opencv-and-display-it-with-tkinter
        self.image = img

    # Take input of how much you want to scale it down
    # then converts the openCV image format into ine tkinter can use.
    # For buttons, you probably want to use a scale of 20
    def image_cv2_to_tkinter(self, scale):
        new_image = self.image

        # resizing algorithm taken from https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
        # finds the new width and height
        scale_percent = scale  # percent of original size
        width = int(new_image.shape[1] * scale_percent / 100)
        height = int(new_image.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resizes image
        resized = cv2.resize(new_image, dim, interpolation=cv2.INTER_AREA)

        blue, green, red = cv2.split(resized)
        img = cv2.merge((red, green, blue))
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)

        return imgtk
