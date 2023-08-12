from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face Recognition System")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



         #first image
        img=Image.open(r"online_images\hl.jpeg")
        img=img.resize((1366,768),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=768)
        
        # #second image
        # img1=Image.open(r"online_images\chip.jpg")
        # img1=img.resize((246,70),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=220,height=70)

        #bg image
        img3=Image.open(r"online_images\chip.jpg")
        img3=img.resize((1366,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=70,width=1336,height=710)

        #centre heading
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width="1500",height="45")

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=60,width=1280,height=680)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=580)

        img_left=Image.open(r"online_images\badge.jpg")
        img_left=img_left.resize((590,200),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=650,height=200)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=130,width=635,height=300)

        #labels and entries
        #attendance ID
        
        attendaceId_label=Label(left_inside_frame,text="AttendenceId ID:",font=("times new roman",12,"bold"),bg="white")
        attendaceId_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)
        #name
        rollLabel=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,sticky=W)

        #date
        nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,sticky=W)

        #Department
        depLabel=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,sticky=W)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,sticky=W)

        #date
        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,sticky=W)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendence Status:",font=("times new roman",12,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="read only",width=20)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=10,sticky=W)


        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=250,width=600,height=70)

        save_btn=Button(btn_frame,text="Importcsv",command=self.importCsv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",command=self.get_cursor,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)













        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=700,y=10,width=550,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=10,width=600,height=400)

        #=====scrollbar======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
       
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

    #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(("csv file", "*.csv"), ("All File", "*.*")), parent=self.root)
        if fln:
            with open(fln, mode="r", newline="") as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)

#export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV files", "*.csv"), ("All Files", "*.*")), parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data has been exported to " + os.path.basename(fln) + " successfully.")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
        


    def get_cursor(self):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease",self.get_cursor)




    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

















if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
