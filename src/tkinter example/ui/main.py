from ui.ExportScreen.exportScreen import ExportScreen
from VideoScreen.videoScreen import VideoScreen

import customtkinter as tk  # python 3
from tkinter import font as tkfont  # python 3

class SampleApp(tk.CTk):

    def __init__(self, *args, **kwargs):
        tk.CTk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.CTkFrame(self)
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


class StartPage(tk.CTkFrame):

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.start_page_content()


    def start_page_content(self):

        titleLabel = tk.CTkLabel(self, text="Turn Me into a Sprite", font=("Berlin Sans FB", 56), padx=6,
                                            pady=180)
        titleLabel.pack(side=tk.TOP)

        button1 = tk.CTkButton(self, text="New Project", font=("Berlin Sans FB", 56),
                               command=lambda: self.controller.show_frame("VideoScreen"), height=100, width=500)

        button1.pack(padx=6, pady=24, side=tk.TOP)




if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1920x1080")
    app.mainloop()
