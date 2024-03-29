from tkinter import Image
import cv2
import numpy as np
from PIL import Image, ImageTk
import hashlib
import textwrap


class Costume:

    def __init__(self, img):
        # Converts CV2 image to tkinter to display (easier to wok with)
        # Taken from https://www.tutorialspoint.com/read-an-image-with-opencv-and-display-it-with-tkinter
        self.image = img
        self._assetId = hashlib.md5(self.image.tobytes()).hexdigest()
        self._costume_name = ""

    # Take input of how much you want to scale it down
    # then converts the openCV image format into ine tkinter can use.
    # For buttons, you probally want to use a scale of 20
    '''Input the scale as a percentage you want the image to return as and make it a form tkinter can display'''
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

    '''returns image with a transparent background'''
    def image_with_transparent_background(self):
        # find all pixels that are white
        white_pixels = np.where(
            (self.image[:, :, 0] == 255) &
            (self.image[:, :, 1] == 255) &
            (self.image[:, :, 2] == 255)
        )

        # change image space to have alpha layer
        img = cv2.cvtColor(self.image, cv2.COLOR_RGB2RGBA)

        # set those pixels to transparent
        img[white_pixels] = [255, 255, 255, 0]

        return img

    '''returns assetID'''
    def get_costume_assetId(self):
        return self._assetId

    '''returns name of costume'''
    def get_costume_name(self):
        return self._costume_name

    '''sets the costume name'''
    def set_costume_name(self, name):
        self._costume_name = name[:25]

    # For testing
    '''Gets the costume image'''
    def get_costume_image(self):
        return self.image
