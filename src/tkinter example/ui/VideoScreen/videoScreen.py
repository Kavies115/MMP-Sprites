from tkinter import Image

import customtkinter as tk
import cv2
from PIL import Image as Img
from PIL import ImageTk

from components.pose_segmentor.posesegmentor import PoseSegmentor


class VideoScreen(tk.CTkFrame):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self._video_screen_content(controller=controller)

    def _video_screen_content(self, controller):
        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        frame_for_video = tk.CTkFrame(self, width=1500)
        frame_for_video.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=20, pady=20)

        frame_for_frames = tk.CTkFrame(self)
        frame_for_frames.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=20, pady=20)

        frame_for_menubar = tk.CTkFrame(self)
        frame_for_menubar.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)

        global label_widget
        label_widget = tk.CTkLabel(frame_for_video, text="")
        label_widget.pack(padx=8, pady=8, side=tk.TOP, anchor="w", fill=tk.BOTH)

        button_export_screen = tk.CTkButton(frame_for_menubar, text="Next", font=("Berlin Sans FB", 56),
                                            command=lambda: self.controller.show_frame("ExportScreen"), height=100,
                                            width=500)

        button_export_screen.pack(padx=6, pady=24, side=tk.RIGHT)

        button_home_screen = tk.CTkButton(frame_for_menubar, text="Back", font=("Berlin Sans FB", 56),
                                          command=lambda: self.controller.show_frame("StartPage"), height=100,
                                          width=500)

        button_home_screen.pack(padx=6, pady=24, side=tk.LEFT)

        self.show_frames()

    def show_frames(self):
        # Capture the video frame by frame
        _, frame = self.cap.read()

        # Segment the frame (when this part of the )
        segmented_frame = PoseSegmentor().image_segmentor(frame)

        # Convert image from one color space to other
        opencv_image = cv2.cvtColor(segmented_frame, cv2.COLOR_BGR2RGBA)

        # Capture the latest frame and transform to image
        captured_image = Img.fromarray(opencv_image)

        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)

        # Displaying photoimage in the label
        label_widget.photo_image = photo_image

        # Configure image in the label
        label_widget.configure(image=photo_image)

        label_widget.after(10, self.show_frames)
