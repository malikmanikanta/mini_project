import tkinter as tk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance System")
        self.root.geometry("400x300")
        
        self.background_label = tk.Label(root, bg="#34495e")
        self.background_label.place(relwidth=1, relheight=1)
        
        self.frame = tk.Frame(root, bg="#ecf0f1", bd=5)
        self.frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)
        
        self.username_label = tk.Label(self.frame, text="Username:", font=("Helvetica", 14), bg="#ecf0f1")
        self.username_label.place(relx=0.1, rely=0.2)
        
        self.username_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.username_entry.place(relx=0.35, rely=0.2, relwidth=0.5)
        
        self.password_label = tk.Label(self.frame, text="Password:", font=("Helvetica", 14), bg="#ecf0f1")
        self.password_label.place(relx=0.1, rely=0.4)
        
        self.password_entry = tk.Entry(self.frame, show="*", font=("Helvetica", 12))
        self.password_entry.place(relx=0.35, rely=0.4, relwidth=0.5)
        
        self.login_button = tk.Button(self.frame, text="Login", font=("Helvetica", 12), bg="#3498db", fg="white", command=self.login)
        self.login_button.place(relx=0.25, rely=0.6, relwidth=0.2)
        
        self.signup_button = tk.Button(self.frame, text="Sign Up", font=("Helvetica", 12), bg="#27ae60", fg="white", command=self.open_signup_page)
        self.signup_button.place(relx=0.55, rely=0.6, relwidth=0.2)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.validate_user(username, password):
            self.open_main_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def validate_user(self, username, password):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="face_recognizer",
                port=3306  # Change to the actual port number if needed
            )
            
            cursor = connection.cursor()
            
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            
            cursor.close()
            connection.close()
            
            return user is not None
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
    
    def open_main_page(self):
        self.root.withdraw()  # Hide the login window
        self.face_recognition_window = tk.Toplevel()  # Create a new top-level window
        self.face_recognition_app = Face_Recognition_System(self.face_recognition_window)

        
        
    def open_signup_page(self):
        self.root.destroy()
        signup_root = tk.Tk()
        signup_page = SignupPage(signup_root)
        signup_root.mainloop()

class SignupPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("400x300")
        
        self.background_label = tk.Label(root, bg="#34495e")
        self.background_label.place(relwidth=1, relheight=1)
        
        self.frame = tk.Frame(root, bg="#ecf0f1", bd=5)
        self.frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)
        
        self.username_label = tk.Label(self.frame, text="Username:", font=("Helvetica", 14), bg="#ecf0f1")
        self.username_label.place(relx=0.1, rely=0.2)
        
        self.username_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.username_entry.place(relx=0.35, rely=0.2, relwidth=0.5)
        
        self.password_label = tk.Label(self.frame, text="Password:", font=("Helvetica", 14), bg="#ecf0f1")
        self.password_label.place(relx=0.1, rely=0.4)
        
        self.password_entry = tk.Entry(self.frame, show="*", font=("Helvetica", 12))
        self.password_entry.place(relx=0.35, rely=0.4, relwidth=0.5)
        
        self.signup_button = tk.Button(self.frame, text="Sign Up", font=("Helvetica", 12), bg="#27ae60", fg="white", command=self.signup)
        self.signup_button.place(relx=0.4, rely=0.6, relwidth=0.2)
        
    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.create_user(username, password):
            messagebox.showinfo("Sign Up Successful", "Account created successfully!")
            self.root.destroy()
        else:
            messagebox.showerror("Sign Up Failed", "Failed to create account")
    
    def create_user(self, username, password):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="face_recognizer",
                port=3306  # Change to the actual port number if needed
            )
            
            cursor = connection.cursor()
            
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))
            
            connection.commit()
            
            cursor.close()
            connection.close()
            
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()  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