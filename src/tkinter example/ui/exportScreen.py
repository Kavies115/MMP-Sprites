import tkinter

import customtkinter as ctk
from ui.model.global_sprite import main_sprite
from tkinter import filedialog


class ExportScreen(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.export_page_content()

    '''Contains upper level of content the window'''
    def export_page_content(self):

        # Clears all frames
        for widgets in self.winfo_children():
            widgets.destroy()

        # Frame for The list of pictures
        frame_for_picture_list = ctk.CTkScrollableFrame(self, width=350)
        frame_for_picture_list.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=20, pady=20)

        frame_for_editor = ctk.CTkFrame(self)
        frame_for_editor.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        frame_for_export = ctk.CTkFrame(self)
        frame_for_export.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        button_export = ctk.CTkButton(master=frame_for_export, text="Export", font=("Cooper Black", 46),
                                      command=self._export_sprite)
        button_export.pack(padx=8, pady=8, side=ctk.RIGHT, anchor="e", fill=ctk.BOTH)

        button_back = ctk.CTkButton(master=frame_for_export, text="Back", font=("Cooper Black", 46),
                                    command=lambda: self.controller.show_frame("VideoScreen"))
        button_back.pack(padx=8, pady=8, side=ctk.LEFT, anchor="w", fill=ctk.BOTH)

        # Pressing refreshes the picture list
        button_refresh = ctk.CTkButton(master=self, text="Refresh\nCostumes", font=("Cooper Black", 46),
                                       command=lambda: self._list_of_images(frame_for_picture_list, frame_for_editor))
        button_refresh.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self._list_of_images(frame_for_picture_list, frame_for_editor)

        ctk.CTkLabel(master=frame_for_editor, text="Press \"Refresh Costumes\" to view all costumes \nClick a costume "
                                                   "for more options",
                     font=("Cooper Black", 30)).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    '''Contents of the editor frame'''
    def _costume_editor_frame(self, frame, costume):

        # Clears frames
        for widgets in frame.winfo_children():
            widgets.destroy()

        label_title = ctk.CTkLabel(master=frame, text="Editor", font=("Cooper Black", 40))
        label_title.pack(side="top", padx=60, pady=12)

        label_sprite = ctk.CTkLabel(master=frame, text="Sprite Name", font=("Cooper Black", 32))
        label_sprite.pack(side="top", padx=60, pady=12)

        textbox_sprite_name = ctk.CTkTextbox(master=frame, width=400, height=40, font=("Cooper Black", 32))
        textbox_sprite_name.insert(ctk.INSERT, main_sprite.get_sprite_name())
        textbox_sprite_name.pack(side="top", padx=60, pady=12)

        # Picture of the costume users editing
        image = costume.image_cv2_to_tkinter(60)
        ctk.CTkLabel(master=frame, text="", image=image).pack(padx=8, pady=8, side=ctk.TOP, anchor="w", fill=ctk.BOTH)

        label_costume = ctk.CTkLabel(master=frame, text="Costume Name", font=("Cooper Black", 32))
        label_costume.pack(side="top", padx=60, pady=12)

        textbox_costume_name = ctk.CTkTextbox(master=frame, width=400, height=40, font=("Cooper Black", 32))
        textbox_costume_name.insert(ctk.INSERT, costume.get_costume_name())
        textbox_costume_name.pack(side="top", padx=60, pady=12)
                                                                                                                            # 'end-1c' is here because otherwise the name of the sprite would end in a newLine character
        button_save = ctk.CTkButton(master=frame, text="Save", font=("Cooper Black", 46), command=lambda : self._editor_save(textbox_sprite_name.get("1.0", 'end-1c'), textbox_costume_name.get("1.0", 'end-1c'), costume))
        button_save.pack(padx=8, pady=8, anchor="s")

        button_delete = ctk.CTkButton(master=frame, text="Delete", font=("Cooper Black", 46), command=lambda : self._editor_delete(costume))
        button_delete.pack(padx=8, pady=8, anchor="s")



    '''Saves the Sprite name and Costume name'''
    def _editor_save(self, sprite_name, costume_name, costume):

        if sprite_name.__contains__("/"):
            tkinter.messagebox.showerror(title="Error",
                                        message="Please remove \"/\" from the Sprite name")
            return

        if sprite_name == "":
            tkinter.messagebox.showerror(title="Error",
                                        message="Sprite name cant be nothing")
            return

        main_sprite.set_sprite_name(sprite_name)
        costume.set_costume_name(costume_name)

        tkinter.messagebox.showinfo(title="Save",
                                    message="Saved costume")

    '''Deletes the costume'''
    def _editor_delete(self, costume):

        if tkinter.messagebox.askyesno(title="Delete?",
                                        message="Are you sure you want to delete this costume theres no way to recover the image after this"):

            main_sprite.remove_costume(costume)
            self.export_page_content()

    '''Exports the Sprite'''
    def _export_sprite(self):
        path = filedialog.askdirectory(initialdir="/", title="Select a File")
        #if user cancels just return
        if path == "":
            return

        if not main_sprite.get_list_costumes():
            tkinter.messagebox.showerror(title="Export",
                                        message="Cant export project. There are no Costumes")
            return

        main_sprite.export(path)

        tkinter.messagebox.showinfo(title="Export",
                                     message="Export was successful")

    '''Displays the list of images'''
    def _list_of_images(self, frame, export_frame):

        # Clear frame
        for widgets in frame.winfo_children():
            widgets.destroy()

        # Goes through the whole list and makes a button for each costume
        for costume in main_sprite.get_list_costumes():
            image = costume.image_cv2_to_tkinter(30)

            button = ctk.CTkButton(master=frame, image=image, bg_color="transparent", fg_color="transparent", text="",
                                   command=lambda cos=costume:self._costume_editor_frame(export_frame, cos))
            button.pack(padx=8, pady=8, side=ctk.TOP, anchor="n", fill=ctk.Y)
