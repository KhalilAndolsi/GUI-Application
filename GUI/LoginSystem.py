from tkinter import *
from tkinter import messagebox
from customtkinter import *
import os

set_appearance_mode("dark")
set_default_color_theme("green")
root = CTk()
root.geometry("450x350+450+100")
root.title("Login and SignUp")
root.resizable(False, False)

path = os.getcwd()
name = os.path.basename(__file__)

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return root, name

loc, file = find(name, path)
os.chdir(f"{loc}")
newpath = f"{os.getcwd()}\\files_data"
if not os.path.exists(newpath):
    os.makedirs(newpath)
    if not os.path.exists(f"{newpath}\\text.txt"):
        open(f"{newpath}\\text.txt", "a").close()

root.iconbitmap("text.ico")
login_frame = CTkFrame(root, corner_radius=20)
login_frame.pack(pady=30, padx=20, fill="both", expand=True)
page_frame = CTkFrame(root, corner_radius= 20, border_width=20)
text_frame = CTkFrame(page_frame)
text_frame.pack(fill="both", expand=True)
font_name = "sitka text"
file_name = f"{newpath}\\text.txt"
#===== Functions ====
def showpass():
    if var.get() == 0:
        pass_entry.configure(show="*")
    elif var.get() == 1:
        pass_entry.configure(show="")
def signup():
    name = user.get()
    pw = passw.get()
    with open(file_name, "r+") as file1:
        if (name+" "+pw+"\n") not in file1.readlines():
            with open(file_name, "a+") as file2:
                file2.write(name+" "+pw+"\n")
                file2.close()
        file1.close
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
def login():
    name = user.get()
    pw = passw.get()
    with open(file_name, "r") as file:
        if (name+" "+pw+"\n") in file.readlines():
            if f"{name}.txt" in os.listdir(newpath):
                with open(f"{newpath}\\{name}.txt", "r") as f:
                    lines = f.readlines()
                    for i in range(1, len(lines)+1):
                        text_box.insert("1.0", lines[-i])
                    f.close()
            else:
                open(f"{newpath}\\{name}.txt", "x")
            the_key()
        elif name == pw == "":
            messagebox.showerror(title="Failed", message="please write the name and the password!")
        elif name == "":
            messagebox.showerror(title="Failed", message="please write the name!")
        elif pw == "":
            messagebox.showerror(title="Failed", message="please write the password!")
        else:
            messagebox.showerror(title="Failed", message="this account not exist please try again!!")
        file.close()
def the_key():
    name = user.get()
    root.title(name)
    login_frame.destroy()
    root.geometry("800x500+300+100")
    root.resizable(True, True)
    page_frame.pack(pady=30, padx=20, fill="both", expand=True)
def save_button():
    name = user.get()
    text = text_box.get(1.0, "end-1c")
    with open(f"{newpath}\\{name}.txt", "w") as fd:
        fd.write(text)
        fd.close()
    root.quit()
#===== label of entrys ====
lbl_username = CTkLabel(login_frame, text="Username:", font=(font_name, 15, "bold"))
lbl_password = CTkLabel(login_frame, text="Password:", font=(font_name, 15, "bold"))
lbl_username.place(x=50, y=100)
lbl_password.place(x=50, y=150)
#====== Entrys =====
user = StringVar()
user_entry = CTkEntry(login_frame, textvariable=user, width=150, font=(font_name, 15))
user_entry.place(x=140, y=100)
passw = StringVar()
pass_entry = CTkEntry(login_frame, textvariable=passw, width=150, font=(font_name, 15), show="*")
pass_entry.place(x=140, y=150)
#====== Buttons ========
login_bt = CTkButton(login_frame, text="Login", font=(font_name, 13, "bold"), width=60,command=login)
login_bt.place(x=140, y=240)
SignUp_bt = CTkButton(login_frame, text="Sign Up", font=(font_name, 13, "bold"), width=30,command=signup)
SignUp_bt.place(x=210, y=240)
bt_save = CTkButton(page_frame, text="save", font=(font_name, 13, "bold"), command=save_button)
bt_save.place(relx=0.5, rely=0.98, anchor=S)
#==== CheckBox =====
var = IntVar()
box = CTkCheckBox(login_frame,text="show", font=(font_name, 12),variable=var, command=showpass)
box.place(x=150, y=200)
#======= text box ===========
text_box = CTkTextbox(text_frame)
text_box.configure(font=(font_name, 15))
text_box.pack(pady=30, padx=20, fill="both", expand=True)
text_box_title = CTkLabel(text_frame, text="just write", font=(font_name, 20, "bold"))
text_box_title.place(relx=0.5, rely=0.001, anchor=N)
root.mainloop()
