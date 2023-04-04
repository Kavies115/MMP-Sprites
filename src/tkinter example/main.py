import tkinter

from ui.exportScreen import ExportScreen
from ui.videoScreen import VideoScreen

import customtkinter as ctk  # python 3
from tkinter import font as tkfont  # python 3


class SampleApp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ExportScreen, VideoScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.start_page_content()

    def start_page_content(self):

        titleLabel = ctk.CTkLabel(self, text="Turn Me into a Sprite", font=("Berlin Sans FB", 56), padx=6,
                                  pady=180)
        titleLabel.pack(side=ctk.TOP)

        button1 = ctk.CTkButton(self, text="New Project", font=("Berlin Sans FB", 56),
                                command=lambda: self.camera_consent(controller=self.controller), height=100, width=500)

        button1.pack(padx=6, pady=24, side=ctk.TOP)

    def camera_consent(self, controller):
        answer = tkinter.messagebox.askyesno(title="Camera Concent",
                                             message="Do you give permission for this application to access your Camera?")

        if answer:
            controller.show_frame("VideoScreen")
        else:
            return


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1320x1080")
    app.mainloop()
