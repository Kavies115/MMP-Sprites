import customtkinter as tk


class PageTwo(tk.CTkFrame):

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = tk.CTkLabel(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = tk.CTkButton(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()