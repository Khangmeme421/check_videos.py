import tkinter as tk
import csv
import font_manager as fonts
from tkinter import messagebox
class enter_video():
    def __init__(self,root):
        root.geometry("420x500")
        root.title("Enter new video")
        self.lb1 = tk.Label(root,text="Video's name:")
        self.lb1.place(x=20,y=50)
        self.entry1 = tk.Entry(root)
        self.entry1.place(x=190, y=50)

        self.lb2 = tk.Label(root,text="Author's name:")
        self.lb2.place(x=20,y=125)
        self.entry2 = tk.Entry(root)
        self.entry2.place(x=190, y=125)

        self.lb3 = tk.Label(root,text="Rating:")
        self.lb3.place(x=20,y=200)
        self.entry3 = tk.Entry(root)
        self.entry3.place(x=190, y=200)

        # Create buttons
        self.button1 = tk.Button(root, text="Submit",command=self.get_data)
        self.button1.place(x=150, y=300)
    def write_file(self,dt1,dt2,dt3):
        with open('database.csv', 'a', newline='\n') as file:
            lines = 0
            for row in open("database.csv"):
                lines += 1
            self.writer = csv.writer(file)
            self.writer.writerow([str(lines),dt1,dt2,dt3])
    def get_data(self):
        data1 = self.entry1.get()
        data2 = self.entry2.get()
        data3 = self.entry3.get()
        a = True
        b = True
        c = True
        if not data1:
            messagebox.showinfo("Error", "Please enter video's name.")
            a = False
        else:
            a = True
        if not data2:
            messagebox.showinfo("Error", "Please enter author's name")
            b = False
        else:
            b = True
        try:
            num = int(data3)
            if not num in range(1,6):
                messagebox.showinfo("Invalid Input", "Please enter a number between 1 and 5.")
                c = False
            else:
                c = True
        except ValueError:
            messagebox.showinfo("Error", "Rating must be between 1 and 5.")
            c = False
        if a and b and c:
            messagebox.showinfo("Success", "New video added")
            self.write_file(data1,data2,data3)



if __name__ == "__main__":  # only runs when this file is run as a standalone
    root = tk.Tk()        # create a TK object
    fonts.configure()  # configure the fonts
    enter_video(root)     # open the CheckVideo GUI
    root.mainloop()       # run the root main loop, reacting to button presses, etc
