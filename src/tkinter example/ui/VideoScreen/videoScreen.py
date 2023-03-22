from tkinter import Image

import customtkinter as tk
import cv2
from PIL import Image as Img
from PIL import ImageTk

from components.pose_segmentor.posesegmentor import PoseSegmentor
from global_sprite import main_sprite
from sprite.costume import Costume


class VideoScreen(tk.CTkFrame):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
    segmentor = PoseSegmentor()
    button = []

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self._video_screen_content(controller=controller)

    def _video_screen_content(self, controller):

        for widgets in self.winfo_children():
            widgets.destroy()

        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        frame_for_video = tk.CTkFrame(self, width=1500)
        frame_for_video.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=20, pady=20)

        frame_for_frames = tk.CTkScrollableFrame(self)
        frame_for_frames.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=20, pady=20)

        frame_for_menubar = tk.CTkFrame(self)
        frame_for_menubar.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)

        global label_widget
        label_widget = tk.CTkLabel(frame_for_video, text="")
        label_widget.pack(padx=8, pady=8, side=tk.TOP, anchor="w", fill=tk.BOTH)

        button_export_screen = tk.CTkButton(frame_for_menubar, text="Next", font=("Berlin Sans FB", 56),
                                            command=lambda: controller.show_frame("ExportScreen"), height=100,
                                            width=500)

        button_export_screen.pack(padx=6, pady=24, side=tk.RIGHT)

        # button_home_screen = tk.CTkButton(frame_for_menubar, text="Back", font=("Berlin Sans FB", 56),
        #                                   command=lambda: controller.show_frame("StartPage"), height=100,
        #                                   width=500)
        #
        # button_home_screen.pack(padx=6, pady=24, side=tk.LEFT)

        button_take_photo = tk.CTkButton(frame_for_video, text="Take Photo", font=("Berlin Sans FB", 56),
                                         command=lambda: self._take_photo(frame_for_frames), height=100, width=500)

        button_take_photo.pack(padx=8, pady=8, side=tk.CENTER)

        self.show_frames()

    def show_frames(self):
        # Capture the video frame by frame
        _, frame = self.cap.read()


        # Convert image from one color space to other
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        # Capture the latest frame and transform to image
        captured_image = Img.fromarray(opencv_image)

        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)

        # Displaying photoimage in the label
        label_widget.photo_image = photo_image

        # Configure image in the label
        label_widget.configure(image=photo_image)

        label_widget.after(10, self.show_frames)

    def _take_photo(self, frame):
        # For testing just take the img from the camera
        _, photo = self.cap.read()

        # Segment the frame
        segmented_frame = self.segmentor.image_segmentor(image=photo)

        costume = Costume(segmented_frame)

        main_sprite.add_costume(costume)

        self._add_costume_to_list(frame, costume)



    def _add_costume_to_list(self, frame, costume):
        image = costume.image_cv2_to_tkinter(40)

        button = tk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent",
                                          text="").pack(padx=8, pady=8, side=tk.TOP, anchor="n", fill=tk.Y)

    def _list_of_images(self, frame):

        for widgets in frame.winfo_children():
            widgets.destroy()

        self.button.clear()

        for i in main_sprite.list_costumes:
            image = i.image_cv2_to_tkinter(20)

            button = tk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent", text="").pack(padx=8, pady=8, side=tk.TOP, anchor="n", fill=tk.Y)

