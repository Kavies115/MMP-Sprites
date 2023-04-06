import time

import customtkinter as ctk
import cv2
from PIL import Image as Img
from PIL import ImageTk

from ui.posesegmentor import PoseSegmentor
from ui.model.global_sprite import main_sprite
from ui.model.sprite.costume import Costume


class VideoScreen(ctk.CTkFrame):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
    segmentor = PoseSegmentor()

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self._video_screen_content(controller=controller)

    '''Contents of the video screen'''
    def _video_screen_content(self, controller):

        # CLears all widgets in the frame if we need to rebuild the screen
        for widgets in self.winfo_children():
            widgets.destroy()

        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        frame_for_video = ctk.CTkFrame(self, width=1500)
        frame_for_video.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=20, pady=20)

        # Need to be gloabl so we can automatically refresh list of costumes
        global frame_for_costumes
        frame_for_costumes = ctk.CTkScrollableFrame(self)
        frame_for_costumes.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=20, pady=20)

        frame_for_menubar = ctk.CTkFrame(self)
        frame_for_menubar.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)

        # Needs to be global so that we can always keep up to date with webcam feed
        global webcam_feed
        webcam_feed = ctk.CTkLabel(frame_for_video, text="")
        webcam_feed.pack(padx=8, pady=8, side=ctk.TOP, anchor="w", fill=ctk.BOTH)

        button_export_screen = ctk.CTkButton(frame_for_menubar, text="Next", font=("Berlin Sans FB", 56),
                                             command=lambda: controller.show_frame("ExportScreen"), height=100,
                                             width=500)

        button_export_screen.pack(padx=6, pady=24)

        # Back button (Dont know if i want to keep it yet)
        # button_home_screen = tk.CTkButton(frame_for_menubar, text="Back", font=("Berlin Sans FB", 56),
        #                                   command=lambda: controller.show_frame("StartPage"), height=100,
        #                                   width=500)
        #
        # button_home_screen.pack(padx=6, pady=24, side=tk.LEFT)

        # Take photo
        button_take_photo = ctk.CTkButton(frame_for_video, text="Take Photo", font=("Berlin Sans FB", 56),
                                          command=lambda: self._take_photo(frame_for_costumes), height=100, width=500)

        button_take_photo.pack(padx=8, pady=14, side=ctk.BOTTOM)

        # Starts Camera
        self.show_frames()
        # Updates costume list
        self._update()


    '''Update the costume view frame so that its always up to date'''
    def _update(self):
        self._list_of_images(frame_for_costumes)
        frame_for_costumes.after(1000, self._update)  # run itself again after 1000 ms

    '''Gets webcam feed and keeps it updated'''
    # https://www.tutorialspoint.com/how-to-show-webcam-in-tkinter-window taken from here
    def show_frames(self):
        # Capture the video frame by frame
        _, frame = self.cap.read()

        # Convert from cv2 colour space to one Tkinter can use
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Capture the latest frame and transform to image
        captured_image = Img.fromarray(opencv_image)

        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)

        # Displaying photoimage in the label
        webcam_feed.photo_image = photo_image

        # Configure image in the label
        webcam_feed.configure(image=photo_image)

        # Update every 50 ms
        webcam_feed.after(50, self.show_frames)

    '''Takes photo from the camera feed'''
    def _take_photo(self, frame):

        #self.countdown()

        _, photo = self.cap.read()

        # Segment the frame
        _, segmented_frame = self.segmentor.image_segmentor(image=photo)

        # create into costume
        costume = Costume(segmented_frame)

        # Add costume to the sprite
        main_sprite.add_costume(costume)

        # Adds to the costume list
        self._add_costume_to_list(frame, costume)

    '''Adds costume to the list of costumes'''

    def countdown(self):
        t = 3

        while t:
            time.sleep(1)
            t -= 1



    def _add_costume_to_list(self, frame, costume):
        image = costume.image_cv2_to_tkinter(50)

        button = ctk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent",
                               text="").pack(padx=8, pady=8, side=ctk.TOP, anchor="n", fill=ctk.Y)

    '''Lists all the costumes in a sprite and diplays them'''
    def _list_of_images(self, frame):

        # Clear old frames
        for widgets in frame.winfo_children():
            widgets.destroy()

        for i in main_sprite.get_list_costumes():
            image = i.image_cv2_to_tkinter(50)

            button = ctk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent", text="").pack(padx=8, pady=8, side=ctk.TOP, anchor="n", fill=ctk.Y)

