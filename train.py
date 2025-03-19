from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load top image
        img_top = Image.open(r"UI images/blank img.jpg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Load bottom image (FIX INDENTATION)
        img_bottom = Image.open(r"UI images/blank img.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)  # FIXED: Use img_bottom instead of img_top

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

        # Button
        b1_1 = Button(self.root, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b1_1.place(x=0, y=380, width=1530, height=60)

# Main function
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
