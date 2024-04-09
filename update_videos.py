import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from video_library import *
from enter_video import enter_video
from writer import re_write
from num2text import text_to_number
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts

class UpdateVideos():
    def add_vd(self):
        enter_video(tk.Toplevel(self.root))
    def __init__(self, root):
        self.root=root
        #Create a window (width = 1080, height = 450)
        root.geometry("1080x450")
        root.title("Update videos")
        #Create entry that takes video's number
        self.entry1 = tk.Entry(root, width=10)
        self.entry1.place(x=550,y=15)
        #Create a label for entry1
        self.lb1 = tk.Label(root, text="Enter video's number:")
        self.lb1.place(x=350,y=10)
        # Create entry that takes video's new rating
        self.entry2 = tk.Entry(root, width=10)
        self.entry2.place(x=550, y=55)
        # Create a label for entry2
        self.lb2 = tk.Label(root, text="Update video's rating:")
        self.lb2.place(x=350, y=50)

        #Create treeview which is displays the whole table of content
        self.treeview = ttk.Treeview(root, columns=("name", "director", "rating"))
        self.treeview.heading("#0", text="Video's number")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("director", text="Director")
        self.treeview.heading("rating", text="Rating")

        #Button update allows users update data
        self.button1 = tk.Button(root, text="Update video's rating",command=self.update_videos)
        self.button1.place(x=300,y=350)

        self.button2 = tk.Button(root, text="Add new video", command=self.add_vd)
        self.button2.place(x=600, y=350)

    def update_videos(self):
        #txt1 and txt2 is a temp variables which store data of entry1 and entry2
        txt1 = self.entry1.get()
        txt1 = text_to_number(txt1)
        txt2 = self.entry2.get()
        txt2 = text_to_number(txt2)

        if txt1 != "" or txt2 != "": #ensure entry1 and entry2 must be filled
            if lib.get_name(txt1,library)==None: #check video's ID is valid or not
                messagebox.showinfo("Error", "Invalid video's number")
            elif not txt2 in ["1", "2", "3", "4", "5"]: #ensure rating is in range of 1 to 5
                messagebox.showinfo("Error", "Rating is not valid") #pop up error message if rating is invalid
            else:
                try:
                    #display video's information after update
                    re_write(txt1,txt2)
                    lib.set_rating(txt1, library,int(txt2))
                    self.treeview.insert(
                        "",
                        tk.END,
                        text=txt1,
                        values=(lib.get_name(txt1,library), lib.get_director(txt1,library), lib.get_rating(txt1,library), txt1)
                    )
                    self.treeview.place(x=150, y=100)
                except NameError:
                    return None
        else:
            #Pop up shows error if user have not filled the blank
            messagebox.showinfo("Error", "Please enter two numbers")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    root = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateVideos(root)     # open the CheckVideo GUI
    root.mainloop()       # run the root main loop, reacting to button presses, etc
