from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        #first image
        img=Image.open(r"online_images\gradient-blurred-WallpaperMaiden_.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"online_images\wallpaperflare.com_wallpaper.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=400,height=130)

        #third image
        img2=Image.open(r"online_images\gradient-blurred-WallpaperMaiden_.png")
        img2=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=500,height=130)

        #bg image
        img3=Image.open(r"online_images\gradient.png")
        img3=img3.resize((1380,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1380,height=768)
        #centre headinng
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width="1530",height="45")

        def time():
            string=strftime("%H:%M:%S:%p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background='white',foreground='blue')
        lbl.place(x=5,y=0,width=100,height=50)
        time()








        #student button
        img4=Image.open(r"online_images\stu.jpg")
        img4=img4.resize((190,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width="220",height="220")

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=200,y=277,width="220",height="40")
        #detectface button
        img5=Image.open(r"online_images\face.png")
        img5=img5.resize((190,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=515,y=100,width="190",height="190")

        b1=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=500,y=277,width="220",height="40")
       #attendence button 
        img6=Image.open(r"online_images\atten.jpg")
        img6=img6.resize((190,190),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=815,y=100,width="190",height="190")

        b1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=800,y=277,width="220",height="40")


        #help desk button
        img7=Image.open(r"online_images\help.jpg")
        img7=img7.resize((190,190),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1115,y=100,width="190",height="190")

        b1=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=1100,y=277,width="220",height="40")

        #train face button
        img8=Image.open(r"online_images\train.webp")
        img8=img8.resize((190,190),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=215,y=350,width="190",height="190")

        b1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=200,y=525,width="220",height="40")

        #photos face button
        img9=Image.open(r"online_images\mface.jpg")
        img9=img9.resize((190,190),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=515,y=350,width="190",height="190")

        b1=Button(bg_img,text="Face Data_set",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=500,y=525,width="220",height="40")

        #developer details button
        img10=Image.open(r"online_images\dev.png")
        img10=img10.resize((190,190),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=815,y=350,width="190",height="190")

        b1=Button(bg_img,text="Developer Details",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=800,y=525,width="220",height="40")

        #exit button
        img11=Image.open(r"online_images\exit.jpg")
        img11=img11.resize((190,190),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,command=self.iExit,image=self.photoimg11,cursor="hand2")
        b1.place(x=1115,y=350,width="190",height="190")

        b1=Button(bg_img,command=self.iExit,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1.place(x=1100,y=525,width="220",height="40")

    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?", parent=self.root)
        if self.iExit:
            self.root.destroy()               

#===================================Functions Buttons==========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()