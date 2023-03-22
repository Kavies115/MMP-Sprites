import customtkinter as tk
import cv2
from PIL import Image, ImageTk
from global_sprite import main_sprite
from sprite.costume import Costume
from tkinter import filedialog


class ExportScreen(tk.CTkFrame):

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.export_page_content()

    def export_page_content(self):

        for widgets in self.winfo_children():
            widgets.destroy()

        frame_for_picture_list = tk.CTkScrollableFrame(self, width=350)
        frame_for_picture_list.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=20, pady=20)

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

        button_back = tk.CTkButton(master=frame_for_export, text="Back", font=("Cooper Black", 46),
                                   command=lambda: self.controller.show_frame("VideoScreen"))
        button_back.pack(padx=8, pady=8, side=tk.LEFT, anchor="w", fill=tk.BOTH)

        button_refresh = tk.CTkButton(master=self, text="Refresh", font=("Cooper Black", 46),
                                      command=lambda: self._list_of_images(frame_for_picture_list, frame_for_filters))
        button_refresh.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self._list_of_images(frame_for_picture_list, frame_for_filters)
        # self._costume_editor_frame_start(frame_for_filters)

    def _costume_editor_frame(self, frame, costume):

        for widgets in frame.winfo_children():
            widgets.destroy()

        label_title = tk.CTkLabel(master=frame, text="Editor", font=("Cooper Black", 40))
        label_title.pack(side="top", padx=60, pady=12)

        label_sprite = tk.CTkLabel(master=frame, text="Sprite Name", font=("Cooper Black", 32))
        label_sprite.pack(side="top", padx=60, pady=12)

        textbox_sprite_name = tk.CTkTextbox(master=frame, width=400, height=40, font=("Cooper Black", 32))
        textbox_sprite_name.insert(tk.INSERT, main_sprite.get_sprite_name())
        textbox_sprite_name.pack(side="top", padx=60, pady=12)

        ## Space for the Img
        image = costume.image_cv2_to_tkinter(60)
        label_image = tk.CTkLabel(master=frame, text="", image=image).pack(padx=8, pady=8, side=tk.TOP, anchor="w", fill=tk.BOTH)

        label_costume = tk.CTkLabel(master=frame, text="Sprite", font=("Cooper Black", 32))
        label_costume.pack(side="top", padx=60, pady=12)

        textbox_costume_name = tk.CTkTextbox(master=frame, width=400, height=40, font=("Cooper Black", 32))
        textbox_costume_name.insert(tk.INSERT, costume.get_costume_name())
        textbox_costume_name.pack(side="top", padx=60, pady=12)
                                                                                                                            # 'end-1c' is here because otherwise the name of the sprite would end in a newLine character
        button_save = tk.CTkButton(master=frame, text="Save", font=("Cooper Black", 46), command=lambda : self._editor_save(textbox_sprite_name.get("1.0", 'end-1c'), textbox_costume_name.get("1.0",'end-1c'), costume))
        button_save.pack(padx=8, pady=8, anchor="s")

        button_delete = tk.CTkButton(master=frame, text="Delete", font=("Cooper Black", 46), command=lambda : self._editor_delete(costume))
        button_delete.pack(padx=8, pady=8, anchor="s")

    def _editor_save(self, sprite_name, costume_name, costume):
        main_sprite.set_sprite_name(sprite_name)
        costume.set_costume_name(costume_name)

    def _editor_delete(self, costume):
        main_sprite.remove_costume(costume)
        self.export_page_content()

    def _export_sprite(self):
        path = filedialog.askdirectory(initialdir="/", title="Select a File")
        main_sprite.export(path)

    def _list_of_images(self, frame, export_frame):

        # Clear frame
        for widgets in frame.winfo_children():
            widgets.destroy()

        for costume in main_sprite.list_costumes:
            image = costume.image_cv2_to_tkinter(30)

            button = tk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent", text="",
                                  command=lambda cos=costume:self._costume_editor_frame(export_frame, cos))
            button.pack(padx=8, pady=8, side=tk.TOP, anchor="n", fill=tk.Y)
