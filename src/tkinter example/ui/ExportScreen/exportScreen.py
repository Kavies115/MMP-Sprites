import customtkinter as tk
import cv2
from PIL import Image, ImageTk
from global_sprite import main_sprite
from sprite.costume import Costume
from tkinter import filedialog


class ExportScreen(tk.CTkFrame):

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.button = None
        self.controller = controller
        self.export_page_content()

    def export_page_content(self):
        frame_for_picture_list = tk.CTkScrollableFrame(self, width=350)
        frame_for_picture_list.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=20, pady=20)

        frame_for_filters = tk.CTkFrame(self)
        frame_for_filters.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        frame_for_export = tk.CTkFrame(self)
        frame_for_export.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        label = tk.CTkLabel(master=frame_for_picture_list, text="Costumes", font=("Cooper Black", 40))
        label.pack(side="top", padx=60, pady=12)

        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        button_export = tk.CTkButton(master=frame_for_export, text="Export", font=("Cooper Black", 46),
                                   command=self._export_sprite)
        button_export.pack(padx=8, pady=8, side=tk.RIGHT, anchor="e", fill=tk.BOTH)

        button_back = tk.CTkButton(master=frame_for_export, text="Back", font=("Cooper Black", 46),  command=lambda: self.controller.show_frame("VideoScreen"))
        button_back.pack(padx=8, pady=8, side=tk.LEFT, anchor="w", fill=tk.BOTH)

        button_refresh = tk.CTkButton(master=frame_for_export, text="Refresh", font=("Cooper Black", 46),
                                   command=lambda: self._list_of_images(frame_for_picture_list))
        button_refresh.pack(padx=8, pady=8, side=tk.LEFT, anchor="w", fill=tk.BOTH)


        self._list_of_images(frame_for_picture_list)
        self._costume_editor_frame(frame_for_filters)

    def _costume_editor_frame(self, frame):
        label = tk.CTkLabel(master=frame, text="Costumes", font=("Cooper Black", 40))
        label.pack(side="top", padx=60, pady=12)

    def _export_sprite(self):
        path = filedialog.askdirectory(initialdir="/", title="Select a File")
        main_sprite.export(path)



    def add_costume_to_list(self, frame, costume):
        image = costume.image_cv2_to_tkinter(40)

        self.button.append = tk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent",
                                          text="").pack(padx=8, pady=8, side=tk.TOP, anchor="n", fill=tk.Y)

    def _list_of_images(self, frame):

        # Clear frame
        for widgets in frame.winfo_children():
            widgets.destroy()

        for i in main_sprite.list_costumes:
            image = i.image_cv2_to_tkinter(20)

            button = tk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent", text="")
            button.pack(padx=8, pady=8, side=tk.TOP, anchor="n", fill=tk.Y)
