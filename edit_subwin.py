# The name edit_sub_win stands for Edit Sub Window, ok? Inside this module you can edit an employee's
# personal details, like the employee's name, number, or sex, or position, and so on and so forth.
# The layout of this module is similar to the add_sub_win module. If the field conditions are met, like:
# Don't put numbers inside the name field, or follow the email format or else I won't update the values you want to
# edit. And so on and so forth. If the conditions are met, an SQL query that contains the command to change
# the values you want to edit is therefore executed, and a pop-up message saying "Edits successfully made" will
# show up if the command was indeed successfully executed.
# Also, inside this module lies a button with text inside it saying 'Open Employee's Attendance' can be found.
# If pressed, this button opens up a new window or rather initiates or runs the edit_attendance_module window.
# Inside that new window, you can edit the selected employee's attendance. More is explained about that inside
# the edit_attendance_module.py file. Wondering how this module knows
# whose personal details is to edit? The shared.py module contains a very important variable named:
# data_passing_var2, whose value is None. But the value of this variable gets changed inside the main_program
# module which contains a checkbox feature that selects whose profile you want to create actions on. The
# checkbox feature will be given more details later on inside the main_program module. But anyway,
# the data_passing_var2's value changes based on the profile selected inside the main_program module.
# But here we do not use the name, the phone number, or such. We use the unique RFID tag assigned to that profile.
# So the data_passing_var2's value will then be set to that RFID tag or let's just say the employee's ID, and
# we use conditional statements to see if that ID is equal to this id or such:
# We update the personal details of this employee. That's the general idea of it.

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

    if shared.data_passing_var2 is None:
        messagebox.showinfo("Edit Employee Profile", "Please select an employee profile to edit.")
        edit_win.destroy()

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

    # schedule section
    table_canvas = Canvas(master=edit_win, bg='white', highlightthickness=0,
                          borderwidth=0, width=473, height=260)
    table_canvas.place(x=515, y=230)

    frame = Frame(table_canvas, highlightthickness=0, borderwidth=0)
    table_canvas.create_window((0, 0), window=frame, anchor="nw")

    i = 0
    entries = []

    # Display 10 entry boxes
    db_schedule = mysql.connector.connect(
        host="localhost",
        user="root",
        password="minimumM4.",
        database="employee_schedule"
    )

    schedule_cursor = db_schedule.cursor()
    schedule_cursor.execute(f"SELECT * FROM x_{shared.data_passing_var2}")
    res = schedule_cursor.fetchall()

    # Clear existing entries
    entries = []

    # Insert fetched data into entries
    for row_index, row_data in enumerate(res):
        row_entries = []
        for col_index, col_data in enumerate(row_data):
            table = ttk.Entry(frame, font=("Century Gothic", 8), foreground="black",
                              background="white", width=14)
            table.config(state="normal")
            table.grid(row=row_index, column=col_index)
            table.insert(END, str(col_data))
            row_entries.append(table)
        entries.append(row_entries)

        for xz in entries:
            xz[0].config(state='readonly')

    number = Label(master=edit_win, text="NO#", borderwidth=0, highlightthickness=0,
                   font=("Century Gothic", 12), bg="white")
    number.place(x=540, y=197)

    subject = Label(master=edit_win, text="SUBJECT", borderwidth=0, highlightthickness=0,
                    font=("Century Gothic", 12), bg="white")
    subject.place(x=615, y=197)

    desc = Label(master=edit_win, text="DESC.", borderwidth=0, highlightthickness=0,
                 font=("Century Gothic", 12), bg="white")
    desc.place(x=715, y=197)

    days = Label(master=edit_win, text="DAYS", borderwidth=0, highlightthickness=0,
                 font=("Century Gothic", 12), bg="white")
    days.place(x=805, y=197)

    time = Label(master=edit_win, text="TIME", borderwidth=0, highlightthickness=0,
                 font=("Century Gothic", 12), bg="white")
    time.place(x=898, y=197)

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

        db_schedule2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employee_schedule"
        )

        schedule_cursor2 = db_schedule2.cursor()

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

            row_nums = []
            subject_list = []
            desc_list = []
            days_list = []
            time_list = []

            row_nums.clear()
            subject_list.clear()
            desc_list.clear()
            days_list.clear()
            time_list.clear()

            for row in entries:
                row_num = row[0].get()
                subject_x = row[1].get()
                desc_x = row[2].get()
                days_x = row[3].get()
                time_x = row[4].get()

                row_nums.append(row_num)
                subject_list.append(subject_x)
                desc_list.append(desc_x)
                days_list.append(days_x)
                time_list.append(time_x)

            for lx in range(len(row_nums)):
                sql_x = \
                    f"UPDATE x_{shared.data_passing_var2} SET subject=%s, description=%s, days=%s, time=%s WHERE id=%s"
                values_x = (subject_list[lx], desc_list[lx], days_list[lx], time_list[lx], row_nums[lx])
                schedule_cursor2.execute(sql_x, values_x)
                db_schedule2.commit()

            messagebox.showinfo("Employee Profile successfully updated", "Employee Profile was successfully updated.")
            edit_win.destroy()

        else:
            messagebox.showerror("Error", "Please ensure all values in each entry fields are correct.")

    def open_attendance():
        eam.edit_attendance_win()

    save_btn = ttk.Button(master=edit_win, text="Save", command=edit_data)
    save_btn.place(x=40, y=82)

    edit_win.bind("<Return>", lambda event: edit_data())

    cancel_btn = ttk.Button(master=edit_win, text="Cancel", style="Custom.TButton", command=exit_win)
    cancel_btn.place(x=120, y=82)

    attendance_win_btn = ttk.Button(master=edit_win, text="Open Employee's Attendance", command=open_attendance)
    attendance_win_btn.place(x=200, y=82)

    edit_win.protocol("WM_DELETE_WINDOW", exit_win)
    edit_win.bind("<Return>", lambda event: edit_data())

    edit_win.mainloop()
