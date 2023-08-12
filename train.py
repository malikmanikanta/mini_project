from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Heading
        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # Top image
        img_top = Image.open(r"online_images\wallejpg.jpg")
        img_top = img_top.resize((1366,768), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=50, width=1366, height=768)

        # Train button
        train_btn = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), bg="blue", fg="white")
        train_btn.place(x=20, y=640, width=250, height=70)

        # # Bottom image
        # img_bottom = Image.open(r"online_images\chip.jpg")
        # img_bottom = img_bottom.resize((432, 70), Image.ANTIALIAS)
        # self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # bottom_label = Label(self.root, image=self.photoimg_bottom)
        # bottom_label.place(x=0, y=370, width=1500, height=50)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
