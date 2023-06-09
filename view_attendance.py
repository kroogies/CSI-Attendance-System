# So, this module is pretty self_explanatory. This window contains a table display of a certain
# employee's attendance. The layout of this module is similar to the edit_attendance_module but the only difference
# is inside this window, you cannot make changes to the attendance but only view it. Also, real-time
# events can be seen inside this window, so you can consider a scenario wherein this window is open,
# and an RFID tag/ID is scanned and records attendance of a certain employee, you can expect the new row
# of attendance data to show up in that table display.

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import shared


def view_attendance_win():

    view_atd_win = Toplevel()
    view_atd_win.geometry("1060x450+250+100")
    view_atd_win.title("View Employee Profile Attendance")
    view_atd_win.resizable(False, False)
    view_atd_win.config(bg="white")

    attendance_win_icon = Image.open("logo.png")
    final_icon = ImageTk.PhotoImage(attendance_win_icon)
    view_atd_win.iconphoto(False, final_icon)

    header = Image.open("banner.jpg")
    header = header.resize((1060, 60), Image.LANCZOS)
    header = ImageTk.PhotoImage(header)
    header_placeholder = Label(master=view_atd_win, image=header, borderwidth=0, highlightthickness=0)
    header_placeholder.place(x=0, y=0)

    line_separator = "_______________________________________________________________________________________________" \
                     "_______________________________________________________________________________________________" \
                     "___________"

    line_separator2 = "______________________________________________________________________________________________" \
                      "_________________________________________________________________" \
                      "________________________"

    line_sep = Label(master=view_atd_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='white')
    line_sep.place(x=25, y=93)

    line_sep2 = Label(master=view_atd_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='white')
    line_sep2.place(x=25, y=60)

    line_sep3 = Label(master=view_atd_win, text=line_separator2, highlightthickness=0, borderwidth=0, bg='white')
    line_sep3.place(x=70, y=382)

    row_num_label = Label(master=view_atd_win, text='COLUMN NO.', highlightthickness=0, borderwidth=0,
                          bg='white', font=('Century Gothic', 12))
    row_num_label.place(x=65, y=79)

    date_label = Label(master=view_atd_win, text='DATE', highlightthickness=0, borderwidth=0,
                       bg='white', font=('Century Gothic', 12))
    date_label.place(x=260, y=79)

    time_in_label = Label(master=view_atd_win, text='TIME IN', highlightthickness=0, borderwidth=0,
                          bg='white', font=('Century Gothic', 12))
    time_in_label.place(x=415, y=79)

    time_out_label = Label(master=view_atd_win, text='TIME OUT', highlightthickness=0, borderwidth=0,
                           bg='white', font=('Century Gothic', 12))
    time_out_label.place(x=565, y=79)

    hrs_worked = Label(master=view_atd_win, text='HRS. WORKED', highlightthickness=0, borderwidth=0,
                       bg='white', font=('Century Gothic', 12))
    hrs_worked.place(x=715, y=79)

    late = Label(master=view_atd_win, text='LATE', highlightthickness=0, borderwidth=0,
                 bg='white', font=('Century Gothic', 12))
    late.place(x=900, y=79)

    desc_label = Label(master=view_atd_win, text="View Employee Profile's Attendance Data",
                       highlightthickness=0, borderwidth=0, bg='white', font=('Century Gothic', 11))
    desc_label.place(x=340, y=407)

    table_canvas = Canvas(master=view_atd_win, bg='white', highlightthickness=0,
                          borderwidth=0, width=1000, height=260)
    table_canvas.place(x=46, y=120)

    scrollbar = ttk.Scrollbar(master=view_atd_win, orient=VERTICAL, command=table_canvas.yview)
    scrollbar.place(x=1006, y=120, height=260)

    table_canvas.configure(yscrollcommand=scrollbar.set)
    table_canvas.bind('<Configure>', lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

    frame = Frame(table_canvas, highlightthickness=0, borderwidth=0)
    table_canvas.create_window((0, 0), window=frame, anchor="nw")

    def show_attendance():

        # CODE BLOCK FOR DISPLAYING AND UPDATING DATA
        if shared.data_passing_var2 == '0007606744':
            mydb1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor1 = mydb1.cursor()

            cursor1.execute("SELECT * FROM id_0007606744")
            result1 = cursor1.fetchall()
            print(result1)

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
                    table.insert(END, str(attendance[j]))
                    row_entries.append(table)
                entries.append(row_entries)
                i += 1

                for xz in entries:
                    xz[0].config(state='readonly')
                    xz[1].config(state='readonly')
                    xz[2].config(state='readonly')
                    xz[3].config(state='readonly')
                    xz[4].config(state='readonly')
                    xz[5].config(state='readonly')

        if shared.data_passing_var2 == '0008264524':
            mydb2 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor2 = mydb2.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries2.append(row_entries)
                i += 1

                for xz in entries2:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008385348':
            mydb3 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor3 = mydb3.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries3.append(row_entries)
                i += 1

                for xz in entries3:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008407268':
            mydb4 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor4 = mydb4.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries4.append(row_entries)
                i += 1

                for xz in entries4:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008531832':
            mydb5 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor5 = mydb5.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries5.append(row_entries)
                i += 1

                for xz in entries5:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008532623':
            mydb6 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor6 = mydb6.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries6.append(row_entries)
                i += 1

                for xz in entries6:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008717702':
            mydb7 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor7 = mydb7.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries7.append(row_entries)
                i += 1

                for xz in entries7:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008721967':
            mydb8 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor8 = mydb8.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries8.append(row_entries)
                i += 1

                for xz in entries8:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0008899484':
            mydb9 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor9 = mydb9.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries9.append(row_entries)
                i += 1

                for xz in entries9:
                    xz[0].config(state='readonly')

        if shared.data_passing_var2 == '0009041509':
            mydb10 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            cursor10 = mydb10.cursor()

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
                    table.config(state='readonly')
                    row_entries.append(table)
                entries10.append(row_entries)
                i += 1

                for xz in entries10:
                    xz[0].config(state='readonly')

    def refreshing_page():
        show_attendance()
        view_atd_win.after(1000, refreshing_page)

    def cancel_btn_func():
        view_atd_win.destroy()

    refreshing_page()

    # update the scroll_region to include all elements
    frame.update_idletasks()
    table_canvas.config(scrollregion=table_canvas.bbox("all"))

    cancel_btn = ttk.Button(master=view_atd_win, text='Exit', command=cancel_btn_func)
    cancel_btn.place(x=200, y=405)

    view_atd_win.mainloop()
