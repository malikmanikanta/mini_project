from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Load the background image
        img_top = Image.open(r"online_images/coder.png")
        img_top = img_top.resize((1366, 768), Image.LANCZOS)  # Use LANCZOS resampling
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Place the background image on the root window
        background_label = Label(self.root, image=self.photoimg_top)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        main_frame = Frame(self.root, bd=2, bg="white")  # Use a white background
        main_frame.place(x=220, y=100, width=900, height=500)

        # Developer label
        dev_label = Label(main_frame, text="K. Manikanta", font=("times new roman", 35, "bold"), bg="white", fg="red")
        dev_label.pack(pady=10)

        role_label = Label(main_frame, text="(Designer, Developer)", font=("times new roman", 20), bg="white", fg="blue")
        role_label.pack()

        # Paste your picture here
        img_path = r"online_images\manipic.jpg.jfif"
        img = Image.open(img_path)
        img = img.resize((200, 200), Image.LANCZOS)  # Use LANCZOS resampling
        self.photoimg = ImageTk.PhotoImage(img)
        pic_label = Label(main_frame, image=self.photoimg)
        pic_label.pack(pady=10)

        contact_label = Label(main_frame, text="Contact: kumbhamanikanta03888@gmail.com\nPhone: 9398839779", font=("times new roman", 14), bg="white", fg="black")
        contact_label.pack(pady=5)

        skills_label = Label(main_frame, text="Skills: AI Enthusiast | Web Developer | Problem Solver", font=("times new roman", 14), bg="white", fg="black")
        skills_label.pack()

        contributions_label = Label(main_frame, text="Contributions: Active contribution to AI community and coding projects", font=("times new roman", 14), bg="white", fg="black")
        contributions_label.pack()

        about_label = Label(main_frame, text="About: I believe in the power of coding to shape a better world", font=("times new roman", 14), bg="white", fg="black")
        about_label.pack()

        acknowledgments_label = Label(main_frame, text="Acknowledgments: Special thanks to mentors and peers for continuous support", font=("times new roman", 14), bg="white", fg="black")
        acknowledgments_label.pack()

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
