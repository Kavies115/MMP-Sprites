import customtkinter as tk
from customtkinter import filedialog

class ExportPage(tk.CTkFrame):

    path = ""

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.export_page_content()


    def export_page_content(self):
        controller = self.controller

        frame_for_picture_list = tk.CTkFrame(self)
        frame_for_picture_list.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=20, pady = 20)

        frame_for_filters = tk.CTkFrame(self)
        frame_for_filters.grid(row=0, column=1, sticky="nsew", padx=20, pady = 20)

        frame_for_export = tk.CTkFrame(self)
        frame_for_export.grid(row=1, column=1, sticky="nsew", padx=20, pady = 20)

        label = tk.CTkLabel(master= frame_for_picture_list, text="Hello", font=("Cooper Black", 48))
        label.pack(side="top", padx=60, pady= 12)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        button_back = tk.CTkButton(master=frame_for_export, text="Export", font=("Cooper Black", 46) ,command=self.export_sprite)
        button_back.pack(padx=8, pady= 8, side=tk.RIGHT, anchor="e", fill=tk.BOTH)

        button_back = tk.CTkButton(master=frame_for_export, text="Back", font=("Cooper Black", 46))
        button_back.pack(padx=8, pady=8, side=tk.LEFT, anchor="w", fill=tk.BOTH)

    def export_sprite(self):
        path = filedialog.askdirectory(initialdir="/", title="Select a File")



