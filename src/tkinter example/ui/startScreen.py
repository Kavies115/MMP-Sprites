import tkinter

import customtkinter as ctk  # python 3

class StartScreen(ctk.CTkFrame):

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
        answer = tkinter.messagebox.askyesno(title="Camera Consent",
                                             message="Do you give permission for this application to access your Camera?")

        if answer:
            controller.show_frame("VideoScreen")
        else:
            return