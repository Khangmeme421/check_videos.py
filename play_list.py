import tkinter as tk
import csv
from tkinter import ttk
from video_library import library
from video_library import PlayList
from tkinter import messagebox
from writer import play_single
from writer import del_file
from library_item import LibraryItem
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts


class playlist():
    def __init__(self, root):
        #create window named "Play list"
        root.geometry("1080x450")
        root.title("PLay list")

        self.plt = []
        self.read_db()
        #create an entry and guide user to enter a number
        self.entry = tk.Entry(root, width=10)
        self.entry.place(x=550,y=15)
        self.lb1 = tk.Label(root, text="Enter video's number:")
        self.lb1.place(x=350,y=10)
        #that button allows user add video to play list
        self.button1 = tk.Button(root, text="Add to play list",command=lambda:self.add_video())
        self.button1.place(x=670,y=5)
        #create a list of content with these attributes
        self.treeview = ttk.Treeview(root, columns=("name", "director", "rating", "Play count"))
        self.treeview.heading("#0", text="Video's number")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("director", text="Director")
        self.treeview.heading("rating", text="Rating")
        self.treeview.heading("Play count", text="Play count")
        self.treeview.place(x=40, y=100)

        self.display_tree()

        #this button increases all videos play count
        self.button2 = tk.Button(root, text="Play all videos",command=lambda:self.increment())
        self.button2.place(x=220, y=350)
        #this button empty play list
        self.button3 = tk.Button(root, text="Reset",command=lambda:self.reset())
        self.button3.place(x=500, y=350)
        #this button increases selected video's play count
        self.button4 = tk.Button(root, text="Play one video", command=lambda: self.show_selection())
        self.button4.place(x=750, y=350)
    def read_db(self):
        with open('playlist.csv', newline='\n', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)

            tmplist = [None] * 5
            for row in csv_reader:
                try:
                    len_tmp = 0
                    for i in row:
                        tmplist[len_tmp] = i
                        len_tmp += 1
                    tmp = PlayList(tmplist[1],tmplist[2],tmplist[3],tmplist[0])
                    tmp.play_count = int(tmplist[4])
                    self.plt.append(tmp)
                except TypeError:
                    pass
    def write_file(self,video):
        with open('playlist.csv', 'a', newline='\n') as file:
            lines = 0
            for row in open("playlist.csv"):
                lines += 1
            self.writer = csv.writer(file)
            self.writer.writerow([video.key,video.name,video.director,video.rating,video.play_count])
    def show_selection(self):
        try:
            # Get the Id of the first selected item.
            item = self.treeview.selection()[0]
        except IndexError:
            # If the tuple is empty, there is no selected item.
            messagebox.showwarning(
                message="Please select a video",
                title="No video selected"
            )
        else:
            # Get and display the text of the selected item.
            text = self.treeview.item(item, option="text")
            for i in self.plt:
                if text == i.key:
                    i.play()
                    play_single(i.key, i.play_count)
                    break
            self.delete_tree()
            self.display_tree()
    def add_video(self):
        txt1 = self.entry.get() # get text from entry try the data if text is valid
        if self.search_value_in_array(self.plt,txt1):
            #pop up message if video exists
            messagebox.showinfo("Error", "Video already exists")
        elif lib.get_rating(txt1,library) != -1:
            #if video's number valid, add it to play list
            i = PlayList(lib.get_name(txt1,library),lib.get_director(txt1,library),lib.get_rating(txt1,library),txt1)
            self.plt.append(i)
            self.write_file(i)
            self.treeview.insert(
                "",
                "end",
                text=txt1,
                values=(i.name, i.director, i.rating,i.play_count)
            )
        else:
            #pop up error message if data is invalid
            messagebox.showinfo("Error", "Invalid video's number")

    def search_value_in_array(self,arr, value):
        for element in arr:
            if element.key == value:
                return True
        return False
    def increment(self):
        # This function increases all videos play count
        for i in self.plt:
            i.play()
            play_single(i.key,i.play_count)
        self.delete_tree()
        self.display_tree()

    def reset(self):
        # This function reset all videos play count
        for i in self.plt:
            i.remove_item()
            del_file()
        self.pop_all(self.plt)
        self.delete_tree()
        self.display_tree()
    def delete_tree(self):
        # Delete treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def pop_all(self,l):
        r, l[:] = l[:], []
        return r
    def display_tree(self):
        #Add new treeview after delete it
        for i in self.plt:
            self.treeview.insert(
                "",
                "end",
                text=i.key,
                values=(i.name, i.director, i.rating,i.play_count)
            )
            
if __name__ == "__main__":  # only runs when this file is run as a standalone
    root = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    playlist(root)     # open the CheckVideo GUI
    root.mainloop()       # run the root main loop, reacting to button presses, etc