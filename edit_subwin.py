from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import edit_attendance_module as eam
import shared
import mysql.connector
import re


def open_edit_subwin():

    taken_id = shared.data_passing_var2

    edit_win = Toplevel()
    edit_win.geometry("1000x600+400+100")
    edit_win.title("Edit Employee Profile")
    edit_win.resizable(False, False)
    edit_win.config(bg="white")

    editwin_icon = Image.open("logo.png")
    final_icon = ImageTk.PhotoImage(editwin_icon)
    edit_win.iconphoto(False, final_icon)

    header = Image.open("banner.jpg")
    header = header.resize((1000, 75), Image.LANCZOS)
    header = ImageTk.PhotoImage(header)
    header_placeholder = Label(master=edit_win, image=header, borderwidth=0, highlightthickness=0)
    header_placeholder.place(x=0, y=0)

    # labels
    first_name_label = Label(master=edit_win, text="NAME", borderwidth=0, highlightthickness=0,
                             font=("Century Gothic", 13), bg="white")
    first_name_label.place(x=40, y=200)

    position_label = Label(master=edit_win, text="POSITION", borderwidth=0, highlightthickness=0,
                           font=("Century Gothic", 13), bg="white")
    position_label.place(x=40, y=240)

    sex_label = Label(master=edit_win, text="SEX", borderwidth=0, highlightthickness=0,
                      font=("Century Gothic", 13), bg="white")
    sex_label.place(x=40, y=280)

    address_label = Label(master=edit_win, text="ADDRESS", borderwidth=0, highlightthickness=0,
                          font=("Century Gothic", 13), bg="white")
    address_label.place(x=40, y=320)

    phonenum_label = Label(master=edit_win, text="PHONE NUMBER", borderwidth=0, highlightthickness=0,
                           font=("Century Gothic", 13), bg="white")
    phonenum_label.place(x=40, y=395)

    email_label = Label(master=edit_win, text="EMAIL ADDRESS", borderwidth=0, highlightthickness=0,
                        font=("Century Gothic", 13), bg="white")
    email_label.place(x=40, y=435)

    tag_label = Label(master=edit_win, text="ID NUMBER", borderwidth=0, highlightthickness=0,
                      font=("Century Gothic", 13), bg="white")
    tag_label.place(x=40, y=475)

    # entries
    first_name_entry = ttk.Entry(master=edit_win, font=("Century Gothic", 10), width=40)
    first_name_entry.place(x=190, y=200)

    pos_entry = ttk.Entry(master=edit_win, font=("Century Gothic", 10), width=40)
    pos_entry.place(x=190, y=240)

    sex_entry_field = ttk.Entry(master=edit_win, font=("Century Gothic", 10), width=40)
    sex_entry_field.place(x=190, y=280)

    address_field = Text(edit_win, width=40, height=3, font=("Century Gothic", 10),
                         borderwidth=1, highlightthickness=2, background="white")
    address_field.place(x=190, y=320)

    phonenum_entry = ttk.Entry(master=edit_win, font=("Century Gothic", 10), width=40)
    phonenum_entry.place(x=190, y=395)

    email_add_entry = ttk.Entry(master=edit_win, font=("Century Gothic", 10), width=40)
    email_add_entry.place(x=190, y=435)

    id_entry = ttk.Entry(master=edit_win, font=("Century Gothic", 10), width=40)
    id_entry.place(x=190, y=475)

    # line seperator
    linesep = "______________________________________________________________________________" \
              "___________________________" \
              "______________________________________________________________________________________"
    Label(master=edit_win, text=linesep, fg='black', background="white", borderwidth=0,
          highlightthickness=0).place(x=20, y=100)

    def red_asterisk():
        # conditional block to check if the length of values inside the entries are equal to 0, or the textbox is empty
        if len(first_name_entry.get()) < 3:
            first_name_entry.config(foreground='red')

        if len(pos_entry.get()) < 3:
            pos_entry.config(foreground='red')

        if len(address_field.get("1.0", "end-1c")) < 5:
            address_field.config(foreground='red')

        if len(phonenum_entry.get()) < 11 or len(phonenum_entry.get()) > 11:
            phonenum_entry.config(foreground='red')

        if len(email_add_entry.get()) < 3:
            email_add_entry.config(foreground='red')

        # conditional block to check if the textbox is filled but shows error when it contains wrong data type
        if re.search("[^a-zA-Z]", first_name_entry.get()):
            first_name_entry.config(foreground='red')

        if re.search("[^a-zA-Z]", pos_entry.get()):
            pos_entry.config(foreground='red')

        if re.search("[^0-9]", phonenum_entry.get()):
            pos_entry.config(foreground='red')

        if not re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_add_entry.get()):
            email_add_entry.config(foreground='red')

        if sex_entry_field.get() not in ["Male", "Female"]:
            sex_entry_field.config(foreground='red')

        # conditional block to check if info is valid and change font color
        if len(first_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', first_name_entry.get()):
            first_name_entry.config(foreground='black')

        if len(pos_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', pos_entry.get()):
            pos_entry.config(foreground='black')

        if len(address_field.get("1.0", "end-1c")) >= 5:
            address_field.config(foreground='black')

        if len(phonenum_entry.get()) == 11 and not re.search('[^0123456789]', phonenum_entry.get()):
            phonenum_entry.config(foreground='black')

        if len(email_add_entry.get()) >= 3 and \
                re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_add_entry.get()):
            email_add_entry.config(foreground='black')

        if sex_entry_field.get() in ["Male", "Female"]:
            sex_entry_field.config(foreground='black')

    def preset_fields():
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employees"
        )

        cursor = database.cursor()
        cursor.execute("SELECT * FROM employees WHERE id_number=%s", (taken_id,))
        result = cursor.fetchall()

        for items in result:
            first_name_entry.insert(END, items[0])
            pos_entry.insert(END, items[2])
            sex_entry_field.insert(END, items[3])
            address_field.insert(END, items[1])
            phonenum_entry.insert(END, items[5])
            email_add_entry.insert(END, items[4])
            id_entry.insert(END, taken_id)
            id_entry.config(state='readonly')

    preset_fields()

    def refresh_page():
        red_asterisk()
        edit_win.after(500, refresh_page)

    refresh_page()

    def exit_win():
        edit_win.destroy()
        shared.data_passing_var2 = None

    def edit_data():
        database2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employees"
        )

        cursor2 = database2.cursor()

        sql = "UPDATE employees SET name=%s, address=%s, position=%s, sex=%s, email=%s, phone_num=%s WHERE id_number=%s"
        values = (first_name_entry.get(), address_field.get("1.0", "end-1c"), pos_entry.get(), sex_entry_field.get(),
                  email_add_entry.get(), phonenum_entry.get(), shared.data_passing_var2)

        if len(first_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', first_name_entry.get()) and \
                len(pos_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', pos_entry.get()) and \
                len(address_field.get("1.0", "end-1c")) >= 5 and \
                len(phonenum_entry.get()) == 11 and not re.search('[^0-9]', phonenum_entry.get()) and \
                sex_entry_field.get() in ["Male", "Female"] and \
                re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_add_entry.get()):

            cursor2.execute(sql, values)
            database2.commit()
            messagebox.showinfo("Employee Profile successfully updated", "Employee Profile was successfully updated.")
            edit_win.destroy()

        elif sex_entry_field.get() not in ["Male", "Female"]:
            messagebox.showwarning("Input proper gender", "Please type either Male or Female in the gender field.")

    def open_attendance():
        eam.edit_attendance_win()

    save_btn = ttk.Button(master=edit_win, text="Save", command=edit_data)
    save_btn.place(x=40, y=82)

    edit_win.bind("<Return>", lambda event: edit_data())

    cancel_btn = ttk.Button(master=edit_win, text="Cancel", style="Custom.TButton", command=exit_win)
    cancel_btn.place(x=120, y=82)

    attendance_win_btn = ttk.Button(master=edit_win, text="Open Employee's Attendance", command=open_attendance)
    attendance_win_btn.place(x=200, y=82)

    background_pic = Image.open('transparent_logo.png')
    background_pic = ImageTk.PhotoImage(background_pic)
    bg_label = Label(master=edit_win, image=background_pic, borderwidth=0, highlightthickness=0)
    bg_label.place(x=560, y=160)

    edit_win.protocol("WM_DELETE_WINDOW", exit_win)
    edit_win.bind("<Return>", lambda event: edit_data())

    if shared.data_passing_var2 is None:
        messagebox.showinfo("Edit Employee Profile", "You didn't select an employee profile to edit.")
        edit_win.destroy()

    edit_win.mainloop()
