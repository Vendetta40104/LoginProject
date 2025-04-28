import tkinter as tk
from tkinter import messagebox

USERNAME = "admin"
PASSWORD = "1234"

def show_welcome_page():
    login_frame.pack_forget()

    welcome_frame = tk.Frame(root)
    welcome_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(welcome_frame, text="Welcome! You've logged in successfully.", font=("Arial", 10))
    welcome_label.pack(pady=50)

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login successful", "Welcome!")
        show_welcome_page()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

root = tk.Tk()
root.title("Simple Login")
root.geometry("300x200")
root.resizable(False, False)

# ====== Login ======
login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

label_username = tk.Label(login_frame, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(login_frame)
entry_username.pack(pady=5)

label_password = tk.Label(login_frame, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(login_frame, show="*")
entry_password.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(pady=20)

root.mainloop()