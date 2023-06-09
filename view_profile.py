# This module follows a layout similar to the edit_sub_win.py module wherein in that module, you can
# edit the employee's personal details, but in here, you can only view the selected employee's
# personal details. And inside this module lies a button with text inside it saying 'Open Employee's Attendance'
# that opens the view_attendance.py module or opens the view attendance window. So more details about that module
# is discussed in its respective module. So in this view_profile module, you can only VIEW and not make
# any changes to the employee's personal details.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import shared
import mysql.connector
import view_attendance as view


def open_view_subwin():

    taken_id = shared.data_passing_var2

    view_win = Toplevel()
    view_win.geometry("1000x600+400+100")
    view_win.title("View Employee Profile")
    view_win.resizable(False, False)
    view_win.config(bg="white")

    if shared.data_passing_var2 is None:
        messagebox.showinfo("View Employee Profile", "Please select an employee profile to view.")
        view_win.destroy()

    view_win_icon = Image.open("logo.png")
    final_icon = ImageTk.PhotoImage(view_win_icon)
    view_win.iconphoto(False, final_icon)

    header = Image.open("banner.jpg")
    header = header.resize((1000, 75), Image.LANCZOS)
    header = ImageTk.PhotoImage(header)
    header_placeholder = Label(master=view_win, image=header, borderwidth=0, highlightthickness=0)
    header_placeholder.place(x=0, y=0)

    # labels
    first_name_label = Label(master=view_win, text="NAME", borderwidth=0, highlightthickness=0,
                             font=("Century Gothic", 13), bg="white")
    first_name_label.place(x=40, y=200)

    position_label = Label(master=view_win, text="POSITION", borderwidth=0, highlightthickness=0,
                           font=("Century Gothic", 13), bg="white")
    position_label.place(x=40, y=240)

    sex_label = Label(master=view_win, text="SEX", borderwidth=0, highlightthickness=0,
                      font=("Century Gothic", 13), bg="white")
    sex_label.place(x=40, y=280)

    address_label = Label(master=view_win, text="ADDRESS", borderwidth=0, highlightthickness=0,
                          font=("Century Gothic", 13), bg="white")
    address_label.place(x=40, y=320)

    phonenum_label = Label(master=view_win, text="PHONE NUMBER", borderwidth=0, highlightthickness=0,
                           font=("Century Gothic", 13), bg="white")
    phonenum_label.place(x=40, y=395)

    email_label = Label(master=view_win, text="EMAIL ADDRESS", borderwidth=0, highlightthickness=0,
                        font=("Century Gothic", 13), bg="white")
    email_label.place(x=40, y=435)

    tag_label = Label(master=view_win, text="ID NUMBER", borderwidth=0, highlightthickness=0,
                      font=("Century Gothic", 13), bg="white")
    tag_label.place(x=40, y=475)

    # entries
    first_name_entry = ttk.Entry(master=view_win, font=("Century Gothic", 10), width=40)
    first_name_entry.place(x=190, y=200)

    pos_entry = ttk.Entry(master=view_win, font=("Century Gothic", 10), width=40)
    pos_entry.place(x=190, y=240)

    sex_entry_field = ttk.Entry(master=view_win, font=("Century Gothic", 10), width=40)
    sex_entry_field.place(x=190, y=280)

    address_field = Text(view_win, width=40, height=3, font=("Century Gothic", 10),
                         borderwidth=1, highlightthickness=2, background="#f0f0f0")
    address_field.place(x=190, y=320)

    phonenum_entry = ttk.Entry(master=view_win, font=("Century Gothic", 10), width=40)
    phonenum_entry.place(x=190, y=395)

    email_add_entry = ttk.Entry(master=view_win, font=("Century Gothic", 10), width=40)
    email_add_entry.place(x=190, y=435)

    id_entry = ttk.Entry(master=view_win, font=("Century Gothic", 10), width=40)
    id_entry.place(x=190, y=475)

    # line seperator
    linesep = "______________________________________________________________________________" \
              "___________________________" \
              "______________________________________________________________________________________"
    Label(master=view_win, text=linesep, fg='black', background="white", borderwidth=0,
          highlightthickness=0).place(x=20, y=100)

    # schedule section
    table_canvas = Canvas(master=view_win, bg='white', highlightthickness=0,
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
            table.config(state='readonly')
            row_entries.append(table)
        entries.append(row_entries)

    number = Label(master=view_win, text="NO#", borderwidth=0, highlightthickness=0,
                   font=("Century Gothic", 12), bg="white")
    number.place(x=540, y=197)

    subject = Label(master=view_win, text="SUBJECT", borderwidth=0, highlightthickness=0,
                    font=("Century Gothic", 12), bg="white")
    subject.place(x=615, y=197)

    desc = Label(master=view_win, text="DESC.", borderwidth=0, highlightthickness=0,
                 font=("Century Gothic", 12), bg="white")
    desc.place(x=715, y=197)

    days = Label(master=view_win, text="DAYS", borderwidth=0, highlightthickness=0,
                 font=("Century Gothic", 12), bg="white")
    days.place(x=805, y=197)

    time = Label(master=view_win, text="TIME", borderwidth=0, highlightthickness=0,
                 font=("Century Gothic", 12), bg="white")
    time.place(x=898, y=197)

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

            first_name_entry.config(state='readonly')
            pos_entry.config(state='readonly')
            sex_entry_field.config(state='readonly')
            address_field.config(state='disabled')
            phonenum_entry.config(state='readonly')
            email_add_entry.config(state='readonly')
            id_entry.config(state='readonly')

    preset_fields()

    def refresh_page():
        view_win.after(500, refresh_page)

    refresh_page()

    def exit_win():
        view_win.destroy()
        shared.data_passing_var2 = None

    def open_attendance():
        view.view_attendance_win()

    cancel_btn = ttk.Button(master=view_win, text="Exit", style="Custom.TButton", command=exit_win)
    cancel_btn.place(x=230, y=82)

    attendance_win_btn = ttk.Button(master=view_win, text="Open Employee's Attendance", command=open_attendance)
    attendance_win_btn.place(x=60, y=82)

    view_win.protocol("WM_DELETE_WINDOW", exit_win)

    view_win.mainloop()
