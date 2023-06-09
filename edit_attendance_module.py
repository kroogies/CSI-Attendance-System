# The edit_attendance_module name is pretty self-explanatory. This module is used
# to edit an employee's attendance. So say that you just opened the edit_sub_window, inside that window
# lies a button with text saying: 'Open Employee's Attendance'.
# If you press it, another window opens and voila, you just opened this module which initiates the edit_attendance_
# module window. And inside this window, you can edit the employee's attendance. The time in values, or the timeout,
# or the date, basically you can edit those values and such. Wondering how this module knows
# whose attendance is to edit? The shared.py module contains a very important variable named:
# data_passing_var2, whose value is None. But the value of this variable gets changed inside the main_program
# module which contains a checkbox feature that selects whose profile you want to create actions on. The
# checkbox feature will be given more details later on inside the main_program module. But anyway,
# the data_passing_var2's value changes based on the profile selected inside the main_program module.
# But here we do not use the name, the phone number, or such. We use the unique RFID tag assigned to that profile.
# So the data_passing_var2's value will then be set to that RFID tag or let's just say the employee's ID, and
# we use conditional statements to see if that ID is equal to this id or such:
# We update the attendance of this employee. That's the general idea of it.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import shared
import delete_attendance as dattd


def edit_attendance_win():

    attendance_win = Toplevel()
    attendance_win.geometry("1060x450+250+100")
    attendance_win.title("Edit Employee Profile Attendance")
    attendance_win.resizable(False, False)
    attendance_win.config(bg="white")

    attendance_win_icon = Image.open("logo.png")
    final_icon = ImageTk.PhotoImage(attendance_win_icon)
    attendance_win.iconphoto(False, final_icon)

    header = Image.open("banner.jpg")
    header = header.resize((1060, 60), Image.LANCZOS)
    header = ImageTk.PhotoImage(header)
    header_placeholder = Label(master=attendance_win, image=header, borderwidth=0, highlightthickness=0)
    header_placeholder.place(x=0, y=0)

    line_separator = "_______________________________________________________________________________________________" \
                     "_______________________________________________________________________________________________" \
                     "___________"

    line_separator2 = "______________________________________________________________________________________________" \
                      "_________________________________________________________________" \
                      "________________________"

    line_sep = Label(master=attendance_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='white')
    line_sep.place(x=25, y=93)

    line_sep2 = Label(master=attendance_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='white')
    line_sep2.place(x=25, y=60)

    line_sep3 = Label(master=attendance_win, text=line_separator2, highlightthickness=0, borderwidth=0, bg='white')
    line_sep3.place(x=70, y=382)

    row_num_label = Label(master=attendance_win, text='COLUMN NO.', highlightthickness=0, borderwidth=0,
                          bg='white', font=('Century Gothic', 12))
    row_num_label.place(x=65, y=79)

    date_label = Label(master=attendance_win, text='DATE', highlightthickness=0, borderwidth=0,
                       bg='white', font=('Century Gothic', 12))
    date_label.place(x=260, y=79)

    time_in_label = Label(master=attendance_win, text='TIME IN', highlightthickness=0, borderwidth=0,
                          bg='white', font=('Century Gothic', 12))
    time_in_label.place(x=415, y=79)

    time_out_label = Label(master=attendance_win, text='TIME OUT', highlightthickness=0, borderwidth=0,
                           bg='white', font=('Century Gothic', 12))
    time_out_label.place(x=565, y=79)

    hrs_worked = Label(master=attendance_win, text='HRS. WORKED', highlightthickness=0, borderwidth=0,
                       bg='white', font=('Century Gothic', 12))
    hrs_worked.place(x=715, y=79)

    late = Label(master=attendance_win, text='LATE', highlightthickness=0, borderwidth=0,
                 bg='white', font=('Century Gothic', 12))
    late.place(x=900, y=79)

    desc_label = Label(master=attendance_win, text="Edit Employee Profile's Attendance Data",
                       highlightthickness=0, borderwidth=0, bg='white', font=('Century Gothic', 10))
    desc_label.place(x=360, y=410)

    table_canvas = Canvas(master=attendance_win, bg='white', highlightthickness=0,
                          borderwidth=0, width=1000, height=260)
    table_canvas.place(x=46, y=120)

    scrollbar = ttk.Scrollbar(master=attendance_win, orient=VERTICAL, command=table_canvas.yview)
    scrollbar.place(x=1006, y=120, height=260)

    table_canvas.configure(yscrollcommand=scrollbar.set)
    table_canvas.bind('<Configure>', lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

    frame = Frame(table_canvas, highlightthickness=0, borderwidth=0)
    table_canvas.create_window((0, 0), window=frame, anchor="nw")

    def show_attendance():
        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor1 = mydb1.cursor()

        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor2 = mydb2.cursor()

        mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor3 = mydb3.cursor()

        mydb4 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor4 = mydb4.cursor()

        mydb5 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor5 = mydb5.cursor()

        mydb6 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor6 = mydb6.cursor()

        mydb7 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor7 = mydb7.cursor()

        mydb8 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor8 = mydb8.cursor()

        mydb9 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor9 = mydb9.cursor()

        mydb10 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor10 = mydb10.cursor()

        # CODE BLOCK FOR DISPLAYING AND UPDATING DATA
        if shared.data_passing_var2 == '0007606744':
            cursor1.execute("SELECT * FROM id_0007606744")
            result1 = cursor1.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries
            entries = []

            for attendance in result1:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries.append(row_entries)
                i += 1

                for xz in entries:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008264524':
            cursor2.execute("SELECT * FROM id_0008264524")
            result2 = cursor2.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries2
            entries2 = []

            for attendance in result2:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries2.append(row_entries)
                i += 1

                for xz in entries2:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008385348':
            cursor3.execute("SELECT * FROM id_0008385348")
            result3 = cursor3.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries3
            entries3 = []

            for attendance in result3:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries3.append(row_entries)
                i += 1

                for xz in entries3:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008407268':
            cursor4.execute("SELECT * FROM id_0008407268")
            result4 = cursor4.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries4
            entries4 = []

            for attendance in result4:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries4.append(row_entries)
                i += 1

                for xz in entries4:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008531832':
            cursor5.execute("SELECT * FROM id_0008531832")
            result5 = cursor5.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries5
            entries5 = []

            for attendance in result5:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries5.append(row_entries)
                i += 1

                for xz in entries5:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008532623':
            cursor6.execute("SELECT * FROM id_0008532623")
            result6 = cursor6.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries6
            entries6 = []

            for attendance in result6:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries6.append(row_entries)
                i += 1

                for xz in entries6:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008717702':
            cursor7.execute("SELECT * FROM id_0008717702")
            result7 = cursor7.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries7
            entries7 = []

            for attendance in result7:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries7.append(row_entries)
                i += 1

                for xz in entries7:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008721967':
            cursor8.execute("SELECT * FROM id_0008721967")
            result8 = cursor8.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries8
            entries8 = []

            for attendance in result8:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries8.append(row_entries)
                i += 1

                for xz in entries8:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008899484':
            cursor9.execute("SELECT * FROM id_0008899484")
            result9 = cursor9.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries9
            entries9 = []

            for attendance in result9:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries9.append(row_entries)
                i += 1

                for xz in entries9:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0009041509':
            cursor10.execute("SELECT * FROM id_0009041509")
            result10 = cursor10.fetchall()

            for widget in frame.grid_slaves():
                widget.destroy()

            i = 0
            global entries10
            entries10 = []

            for attendance in result10:
                row_entries = []
                for j in range(len(attendance)):
                    table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                      background="white", width=22)
                    table.config(state="normal")
                    table.grid(row=i, column=j)
                    table.insert(END, attendance[j])
                    row_entries.append(table)
                entries10.append(row_entries)
                i += 1

                for xz in entries10:
                    xz[0].config(state='readonly')

    def update_attendance():
        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor1 = mydb1.cursor()

        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor2 = mydb2.cursor()

        mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor3 = mydb3.cursor()

        mydb4 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor4 = mydb4.cursor()

        mydb5 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor5 = mydb5.cursor()

        mydb6 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor6 = mydb6.cursor()

        mydb7 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor7 = mydb7.cursor()

        mydb8 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor8 = mydb8.cursor()

        mydb9 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor9 = mydb9.cursor()

        mydb10 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor10 = mydb10.cursor()

        if shared.data_passing_var2 == '0007606744':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0007606744 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor1.execute(sql, values)
                mydb1.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008264524':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries2:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008264524 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor2.execute(sql, values)
                mydb2.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008385348':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries3:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008385348 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor3.execute(sql, values)
                mydb3.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008407268':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries4:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008407268 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor4.execute(sql, values)
                mydb4.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008531832':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries5:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008531832 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor5.execute(sql, values)
                mydb5.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008532623':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries6:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008532623 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor6.execute(sql, values)
                mydb6.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008717702':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries7:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008717702 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor7.execute(sql, values)
                mydb7.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008721967':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries8:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008721967 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor8.execute(sql, values)
                mydb8.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0008899484':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries9:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0008899484 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor9.execute(sql, values)
                mydb9.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

        if shared.data_passing_var2 == '0009041509':
            row_nums = []
            date_list = []
            time_in_list = []
            time_out_list = []
            hours_worked_list = []
            late_list = []

            row_nums.clear()
            date_list.clear()
            time_in_list.clear()
            time_out_list.clear()
            hours_worked_list.clear()
            late_list.clear()

            for row in entries10:
                row_num = row[0].get()
                date = row[1].get()
                time_in = row[2].get()
                time_out = row[3].get()
                hours_worked = row[4].get()
                late_in = row[5].get()

                row_nums.append(row_num)
                date_list.append(date)
                time_in_list.append(time_in)
                time_out_list.append(time_out)
                hours_worked_list.append(hours_worked)
                late_list.append(late_in)

            for i in range(len(row_nums)):
                sql = f"UPDATE id_0009041509 SET date=%s, time_in=%s, time_out=%s, hours_worked=%s, late=%s WHERE id=%s"
                values = (date_list[i], time_in_list[i], time_out_list[i],
                          hours_worked_list[i], late_list[i], row_nums[i])
                cursor10.execute(sql, values)
                mydb10.commit()

            messagebox.showinfo("Data Rows Updated", "Edits have been successfully made, please restart the program"
                                                     " as to show the edits that have been made in the employee's"
                                                     "attendance.")
            attendance_win.destroy()

    show_attendance()

    def cancel_btn_func():
        attendance_win.destroy()

    # update the scroll_region to include all elements
    frame.update_idletasks()
    table_canvas.config(scrollregion=table_canvas.bbox("all"))

    save_btn = ttk.Button(master=attendance_win, text='Save', command=update_attendance)
    save_btn.place(x=100, y=405)

    delete_btn = ttk.Button(master=attendance_win, text='Delete', command=dattd.initiate_delete_attd_win)
    delete_btn.place(x=180, y=405)

    cancel_btn = ttk.Button(master=attendance_win, text='Cancel', command=cancel_btn_func)
    cancel_btn.place(x=260, y=405)

    attendance_win.bind("<Return>", lambda event: update_attendance())

    attendance_win.mainloop()
