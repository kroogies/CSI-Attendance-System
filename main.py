# The main.py module is actually a log in window. This program has only one admin account and only one.
# We cannot add, edit, nor delete accounts, unless we have access to the MySQL localhost server.
# The function of this module is simple. We have two entry fields, namely: USERNAME, and PASSWORD.
# If the username AND password matches with an account inside the accounts database, log in will be successful
# and then opens the main_program window. So you'll need to log in first before gaining access to the whole program.

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import sys
import main_program_copy

# initialize database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="minimumM4.",
    database="user_accounts"
)

cursor = mydb.cursor()

# main root, opens first before main program
win2 = Tk()
win2.geometry("465x270+480+250")
win2.title("CSI Attendance System - Log In")
win2.resizable(False, False)

# icon
icon = Image.open("logo.png")
icon2 = ImageTk.PhotoImage(icon)
win2.iconphoto(False, icon2)

# labels
bg = Image.open("loginpage.jpg")
bg2 = ImageTk.PhotoImage(bg)
bg_label = Label(image=bg2, borderwidth=0, highlightthickness=0)
bg_label.place(x=0, y=0)

username_label = Label(borderwidth=0, highlightthickness=0, text="USERNAME",
                       font=("Century Gothic", 10), background="#49c5fe")
username_label.place(x=115.5, y=48)

pass_label = Label(borderwidth=0, highlightthickness=0, text="PASSWORD",
                       font=("Century Gothic", 10), background="#49c5fe")
pass_label.place(x=115.5, y=115)

# entry boxes
username_entry = Entry(borderwidth=0, highlightthickness=0, width=25, font=("MS Sans Serif", 13))
username_entry.place(x=115.5, y=67)

pass_entry = Entry(borderwidth=0, highlightthickness=0, width=25, font=("MS Sans Serif", 13), show="•")
pass_entry.place(x=115.5, y=133)

# user login preset
username_entry.insert(0, "csi_accounting")

# disable paste function for password entry
pass_entry.bind('<Control-x>', lambda e: 'break')
pass_entry.bind('<Control-c>', lambda e: 'break')
pass_entry.bind('<Control-v>', lambda e: 'break')


def get_login_value():
    user_input = username_entry.get()
    pass_input = pass_entry.get()
    cursor.execute("SELECT * FROM accounts WHERE username=%s AND password=%s", (user_input, pass_input))
    result = cursor.fetchall()

    if len(result) == 1:
        win2.destroy()
        main_program_copy.initiate_mprg()

    else:
        messagebox.showerror("Error",
                             "Account does not exist. Try again or submit a report by pressing the report button above.")


# login btn
login_btn_img = Image.open("loginbtn.jpg")
final_loginbtn = ImageTk.PhotoImage(login_btn_img)
login_btn = Button(image=final_loginbtn, highlightthickness=0, borderwidth=0, command=get_login_value)
login_btn.place(x=60, y=210)

# enter key bind
win2.bind("<Return>", lambda event: get_login_value())


def cancel_exit():
    sys.exit()


# cancel btn
cancel_btn_img = Image.open("cancelbtn.jpg")
final_cancelbtn = ImageTk.PhotoImage(cancel_btn_img)
cancel_btn = Button(image=final_cancelbtn, highlightthickness=0, borderwidth=0, command=cancel_exit)
cancel_btn.place(x=250, y=210)

win2.mainloop()
