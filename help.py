from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Centre heading
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width="1500", height="45")

        # Top images
        img_top = Image.open(r"online_images\hd.webp")
        img_top = img_top.resize((432,250), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1366, height=250)

        # Email information
        email_label = Label(self.root, text="For any assistance, contact us:", font=("times new roman", 25, "bold"),
                            bg="white", fg="blue")
        email_label.place(x=500, y=300)

        email_text = "Email: kumbhamanikanta03888@gmail.com"
        email_info = Label(self.root, text=email_text, font=("times new roman", 20, "bold"), bg="white", fg="black")
        email_info.place(x=500, y=360)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
