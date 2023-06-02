from tkinter import *
from tkinter import ttk, Label
from tkinter.filedialog import askdirectory, asksaveasfilename
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import shared2
import datetime
import csv


def view_rpts_win():

    view_atd_win = Toplevel()
    view_atd_win.geometry("820x500+250+100")
    view_atd_win.title("Export Employee Attendance")
    view_atd_win.resizable(False, False)
    view_atd_win.config(bg="white")

    attendance_win_icon = Image.open("logo.png")
    final_icon = ImageTk.PhotoImage(attendance_win_icon)
    view_atd_win.iconphoto(False, final_icon)

    header = Image.open("banner.jpg")
    header = header.resize((1000, 78), Image.LANCZOS)
    header = ImageTk.PhotoImage(header)
    header_placeholder = Label(master=view_atd_win, image=header, borderwidth=0, highlightthickness=0)
    header_placeholder.place(x=0, y=0)

    line_separator = "_______________________________________________________________________________________________" \
                     "______________________________________________________________"

    Label(master=view_atd_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='white').place(x=20, y=115)

    # labels
    str_var = StringVar()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="minimumM4.",
        database="employees",
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employees WHERE id_number=%s", (shared2.data_passing_var2,))
    # change placeholder
    result = cursor.fetchall()

    for i in result:
        str_var.set(f"{i[0]} | {i[2]}")

    name_label = Label(master=view_atd_win, highlightthickness=0, borderwidth=0,
                       font=("Century Gothic", 13), textvariable=str_var, background="white")
    name_label.place(x=50, y=90)

    # all important stuff
    line_separator = "_______________________________________________________________________________________________" \
                     "____________________________________________"

    line_separator2 = "______________________________________________________________________________________________" \
                      "_" \
                      "________________________"

    line_sep = Label(master=view_atd_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='white')
    line_sep.place(x=55, y=160)

    line_sep3 = Label(master=view_atd_win, text=line_separator2, highlightthickness=0, borderwidth=0, bg='white')
    line_sep3.place(x=110, y=440)

    row_num_label = Label(master=view_atd_win, text='COLUMN NO.', highlightthickness=0, borderwidth=0,
                          bg='white', font=('Century Gothic', 12))
    row_num_label.place(x=100, y=140)

    date_label = Label(master=view_atd_win, text='DATE', highlightthickness=0, borderwidth=0,
                       bg='white', font=('Century Gothic', 12))
    date_label.place(x=290, y=140)

    time_in_label = Label(master=view_atd_win, text='TIME IN', highlightthickness=0, borderwidth=0,
                          bg='white', font=('Century Gothic', 12))
    time_in_label.place(x=445, y=140)

    time_out_label = Label(master=view_atd_win, text='TIME OUT', highlightthickness=0, borderwidth=0,
                           bg='white', font=('Century Gothic', 12))
    time_out_label.place(x=595, y=140)

    desc_label = Label(master=view_atd_win, text="Report Generation",  # will change this to the total number of hours
                       highlightthickness=0, borderwidth=0, bg='white', font=('Century Gothic', 11))
    desc_label.place(x=340, y=463)

    table_canvas = Canvas(master=view_atd_win, bg='white', highlightthickness=0,
                          borderwidth=0, width=650, height=260)
    table_canvas.place(x=73, y=185)

    scrollbar = ttk.Scrollbar(master=view_atd_win, orient=VERTICAL, command=table_canvas.yview)
    scrollbar.place(x=723, y=185, height=260)

    table_canvas.configure(yscrollcommand=scrollbar.set)
    table_canvas.bind('<Configure>', lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

    frame = Frame(table_canvas, highlightthickness=0, borderwidth=0)
    table_canvas.create_window((0, 0), window=frame, anchor="nw")

    global current_datex
    current_datex = datetime.datetime.now().date()

    def show_attendance_last_7_days():
        # show attendance
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor2 = mydb2.cursor()

        cursor2.execute(f"SELECT date FROM id_{shared2.data_passing_var2}")
        result2 = cursor2.fetchall()

        mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor3 = mydb3.cursor()

        # Convert the retrieved dates to datetime objects
        formatted_dates = [datetime.datetime.strptime(date[0], "%Y-%m-%d").date() for date in result2]

        # Get the current date
        current_date = datetime.datetime.now().date()

        # Calculate the start date for the last 7 days
        start_date = current_date - datetime.timedelta(days=7)

        # Filter the dates within the last 7 days
        filtered_dates = [date for date in formatted_dates if start_date <= date < current_date]

        filtered_dates2 = []

        # Print the filtered dates
        for date in filtered_dates:
            date_str = date.strftime("%Y-%m-%d")
            filtered_dates2.append(date_str)

        # Prepare the SQL query with placeholders for the filtered dates
        query = "SELECT * FROM id_{} WHERE date IN ({})".format(shared2.data_passing_var2,
                                                                ",".join(["%s"] * len(filtered_dates2)))

        # Execute the query with the filtered dates
        global result3
        cursor3.execute(query, tuple(filtered_dates2))
        result3 = cursor3.fetchall()
        print(result3)
        print(filtered_dates2)

        for widget in frame.grid_slaves():
            widget.destroy()

        i = 0
        global entries
        entries = []

        for attendance in result3:
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

        mydb4 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor4 = mydb4.cursor()
        cursor4.execute(f"SELECT * FROM id_{shared2.data_passing_var2}")
        result_x = cursor4.fetchall()

        data = result_x

        global total_hours_worked1
        total_hours_worked1 = 0

        for row in data:
            row_id, date_str, time_in_str, time_out_str = row

            if time_in_str == 'None' or time_out_str == 'None':
                continue

            # Parse time in and time out using datetime.strptime
            time_in = datetime.datetime.strptime(time_in_str, '%I:%M %p').time()
            time_out = datetime.datetime.strptime(time_out_str, '%I:%M %p').time()

            # Calculate the time difference
            start = datetime.datetime.combine(datetime.date.today(), time_in)
            end = datetime.datetime.combine(datetime.date.today(), time_out)
            duration = end - start

            # Convert the duration to total hours
            hours_worked = round(duration.total_seconds() / 3600, 2)

            # Add the hours worked to the total
            total_hours_worked1 += hours_worked

        cover = Canvas(master=view_atd_win, highlightthickness=0, borderwidth=0, width=480, height=30, bg='white')
        cover.place(x=180, y=463)

        desc_label_x = Label(master=view_atd_win,
                             text=f"Total Hours Worked within the Last 7 Days: {total_hours_worked1} hours",
                             highlightthickness=0, borderwidth=0, bg='white', font=('Century Gothic', 11))
        desc_label_x.place(x=200, y=463)

    def show_attendance_last_2_weeks():
        # show attendance
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor2 = mydb2.cursor()

        cursor2.execute(f"SELECT date FROM id_{shared2.data_passing_var2}")
        result2 = cursor2.fetchall()

        mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor3 = mydb3.cursor()

        # Convert the retrieved dates to datetime objects
        formatted_dates = [datetime.datetime.strptime(date[0], "%Y-%m-%d").date() for date in result2]

        # Get the current date
        current_date = datetime.datetime.now().date()

        # Calculate the start date for the last 7 days
        start_date = current_date - datetime.timedelta(days=14)

        # Filter the dates within the last 7 days
        filtered_dates = [date for date in formatted_dates if start_date <= date < current_date]

        filtered_dates2 = []

        # Print the filtered dates
        for date in filtered_dates:
            date_str = date.strftime("%Y-%m-%d")
            filtered_dates2.append(date_str)

        # Prepare the SQL query with placeholders for the filtered dates
        query = "SELECT * FROM id_{} WHERE date IN ({})".format(shared2.data_passing_var2,
                                                                ",".join(["%s"] * len(filtered_dates2)))

        # Execute the query with the filtered dates
        cursor3.execute(query, tuple(filtered_dates2))
        global result3_2
        result3_2 = cursor3.fetchall()
        print(result3_2)
        print(filtered_dates2)

        for widget in frame.grid_slaves():
            widget.destroy()

        i = 0
        global entries1
        entries1 = []

        for attendance in result3_2:
            row_entries = []
            for j in range(len(attendance)):
                table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                  background="white", width=22)
                table.config(state="normal")
                table.grid(row=i, column=j)
                table.insert(END, str(attendance[j]))
                row_entries.append(table)
            entries1.append(row_entries)
            i += 1

            for xz in entries1:
                xz[0].config(state='readonly')
                xz[1].config(state='readonly')
                xz[2].config(state='readonly')
                xz[3].config(state='readonly')

        mydb4 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor4 = mydb4.cursor()
        cursor4.execute(f"SELECT * FROM id_{shared2.data_passing_var2}")
        result_x = cursor4.fetchall()

        data = result_x

        global total_hours_worked2
        total_hours_worked2 = 0

        for row in data:
            row_id, date_str, time_in_str, time_out_str = row

            if time_in_str == 'None' or time_out_str == 'None':
                continue

            # Parse time in and time out using datetime.strptime
            time_in = datetime.datetime.strptime(time_in_str, '%I:%M %p').time()
            time_out = datetime.datetime.strptime(time_out_str, '%I:%M %p').time()

            # Calculate the time difference
            start = datetime.datetime.combine(datetime.date.today(), time_in)
            end = datetime.datetime.combine(datetime.date.today(), time_out)
            duration = end - start

            # Convert the duration to total hours
            hours_worked = round(duration.total_seconds() / 3600, 2)

            # Add the hours worked to the total
            total_hours_worked2 += hours_worked

        cover = Canvas(master=view_atd_win, highlightthickness=0, borderwidth=0, width=480, height=30, bg='white')
        cover.place(x=180, y=463)

        desc_label_x = Label(master=view_atd_win,
                             text=f"Total Hours Worked within the Last 2 Weeks: {total_hours_worked2} hours",
                             highlightthickness=0, borderwidth=0, bg='white', font=('Century Gothic', 11))
        desc_label_x.place(x=200, y=463)

    def show_attendance_last_30_days():
        # show attendance
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor2 = mydb2.cursor()

        cursor2.execute(f"SELECT date FROM id_{shared2.data_passing_var2}")
        result2 = cursor2.fetchall()

        mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor3 = mydb3.cursor()

        # Convert the retrieved dates to datetime objects
        formatted_dates = [datetime.datetime.strptime(date[0], "%Y-%m-%d").date() for date in result2]

        # Get the current date
        current_date = datetime.datetime.now().date()

        # Calculate the start date for the last 7 days
        start_date = current_date - datetime.timedelta(days=30)

        # Filter the dates within the last 7 days
        filtered_dates = [date for date in formatted_dates if start_date <= date < current_date]

        filtered_dates2 = []

        # Print the filtered dates
        for date in filtered_dates:
            date_str = date.strftime("%Y-%m-%d")
            filtered_dates2.append(date_str)

        # Prepare the SQL query with placeholders for the filtered dates
        query = "SELECT * FROM id_{} WHERE date IN ({})".format(shared2.data_passing_var2,
                                                                ",".join(["%s"] * len(filtered_dates2)))

        # Execute the query with the filtered dates
        cursor3.execute(query, tuple(filtered_dates2))
        global result3_3
        result3_3 = cursor3.fetchall()
        print(result3_3)
        print(filtered_dates2)

        for widget in frame.grid_slaves():
            widget.destroy()

        i = 0
        global entries2
        entries2 = []

        for attendance in result3_3:
            row_entries = []
            for j in range(len(attendance)):
                table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                  background="white", width=22)
                table.config(state="normal")
                table.grid(row=i, column=j)
                table.insert(END, str(attendance[j]))
                row_entries.append(table)
            entries2.append(row_entries)
            i += 1

            for xz in entries2:
                xz[0].config(state='readonly')
                xz[1].config(state='readonly')
                xz[2].config(state='readonly')
                xz[3].config(state='readonly')

        mydb4 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor4 = mydb4.cursor()
        cursor4.execute(f"SELECT * FROM id_{shared2.data_passing_var2}")
        result_x = cursor4.fetchall()

        data = result_x

        global total_hours_worked3
        total_hours_worked3 = 0

        for row in data:
            row_id, date_str, time_in_str, time_out_str = row

            if time_in_str == 'None' or time_out_str == 'None':
                continue

            # Parse time in and time out using datetime.strptime
            time_in = datetime.datetime.strptime(time_in_str, '%I:%M %p').time()
            time_out = datetime.datetime.strptime(time_out_str, '%I:%M %p').time()

            # Calculate the time difference
            start = datetime.datetime.combine(datetime.date.today(), time_in)
            end = datetime.datetime.combine(datetime.date.today(), time_out)
            duration = end - start

            # Convert the duration to total hours
            hours_worked = round(duration.total_seconds() / 3600, 2)

            # Add the hours worked to the total
            total_hours_worked3 += hours_worked

        cover = Canvas(master=view_atd_win, highlightthickness=0, borderwidth=0, width=480, height=30, bg='white')
        cover.place(x=180, y=463)

        desc_label_x = Label(master=view_atd_win,
                             text=f"Total Hours Worked within the Last 30 Day: {total_hours_worked3} hours",
                             highlightthickness=0, borderwidth=0, bg='white', font=('Century Gothic', 11))
        desc_label_x.place(x=200, y=463)

    def show_attendance_last_1_year():
        # show attendance
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor2 = mydb2.cursor()

        cursor2.execute(f"SELECT date FROM id_{shared2.data_passing_var2}")  # also edit id_ to ...
        result2 = cursor2.fetchall()

        mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor3 = mydb3.cursor()

        # Convert the retrieved dates to datetime objects
        formatted_dates = [datetime.datetime.strptime(date[0], "%Y-%m-%d").date() for date in result2]

        # Get the current date
        current_date = datetime.datetime.now().date()

        # Calculate the start date for the last 7 days
        start_date = current_date - datetime.timedelta(days=365)

        # Filter the dates within the last 7 days
        filtered_dates = [date for date in formatted_dates if start_date <= date < current_date]

        filtered_dates2 = []

        # Print the filtered dates
        for date in filtered_dates:
            date_str = date.strftime("%Y-%m-%d")
            filtered_dates2.append(date_str)

        # Prepare the SQL query with placeholders for the filtered dates
        query = "SELECT * FROM id_{} WHERE date IN ({})".format(shared2.data_passing_var2,
                                                                ",".join(["%s"] * len(filtered_dates2)))

        # Execute the query with the filtered dates
        cursor3.execute(query, tuple(filtered_dates2))
        global result3_4
        result3_4 = cursor3.fetchall()
        print(result3_4)
        print(filtered_dates2)

        for widget in frame.grid_slaves():
            widget.destroy()

        i = 0
        global entries3
        entries3 = []

        for attendance in result3_4:
            row_entries = []
            for j in range(len(attendance)):
                table = ttk.Entry(frame, font=("Century Gothic", 10), foreground="black",
                                  background="white", width=22)
                table.config(state="normal")
                table.grid(row=i, column=j)
                table.insert(END, str(attendance[j]))
                row_entries.append(table)
            entries3.append(row_entries)
            i += 1

            for xz in entries3:
                xz[0].config(state='readonly')
                xz[1].config(state='readonly')
                xz[2].config(state='readonly')
                xz[3].config(state='readonly')

        mydb4 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="attendance"
        )

        cursor4 = mydb4.cursor()
        cursor4.execute(f"SELECT * FROM id_{shared2.data_passing_var2}")
        result_x = cursor4.fetchall()

        data = result_x

        global total_hours_worked4
        total_hours_worked4 = 0

        for row in data:
            row_id, date_str, time_in_str, time_out_str = row

            if time_in_str == 'None' or time_out_str == 'None':
                continue

            # Parse time in and time out using datetime.strptime
            time_in = datetime.datetime.strptime(time_in_str, '%I:%M %p').time()
            time_out = datetime.datetime.strptime(time_out_str, '%I:%M %p').time()

            # Calculate the time difference
            start = datetime.datetime.combine(datetime.date.today(), time_in)
            end = datetime.datetime.combine(datetime.date.today(), time_out)
            duration = end - start

            # Convert the duration to total hours
            hours_worked = round(duration.total_seconds() / 3600, 2)

            # Add the hours worked to the total
            total_hours_worked4 += hours_worked

        cover = Canvas(master=view_atd_win, highlightthickness=0, borderwidth=0, width=1000, height=30, bg='white')
        cover.place(x=180, y=463)

        desc_label_x = Label(master=view_atd_win,
                             text=f"Total Hours Worked within One Year: {total_hours_worked4} hours",
                             highlightthickness=0, borderwidth=0, bg='white', font=('Century Gothic', 11))
        desc_label_x.place(x=200, y=463)

    def callback(value):
        global filter_value
        filter_value = value

        if filter_value == "Filter":
            print('None')

        elif filter_value == "Last 7 Days":
            show_attendance_last_7_days()

        elif filter_value == "Last 2 Weeks":
            show_attendance_last_2_weeks()

        elif filter_value == "Last 30 Days":
            show_attendance_last_30_days()

        elif filter_value == "One Year":
            show_attendance_last_1_year()

    # Create a list of options for the dropdown
    options = ['Filter', 'Last 7 Days', 'Last 2 Weeks', 'Last 30 Days', 'One Year']

    # Create a StringVar to store the selected option
    selected_option = StringVar()

    # Create the Combobox widget
    dropdown = ttk.OptionMenu(view_atd_win, selected_option, *options, command=callback)
    dropdown.configure(cursor="hand2")
    dropdown.place(x=470, y=93)

    # Set an initial value for the dropdown
    selected_option.set(options[0])

    # export feature
    def export():
        # Ask the user to select the output directory
        output_dir = askdirectory(title="Select Output Directory")

        # Ask the user to specify the output filename
        output_filename = asksaveasfilename(
            initialdir=output_dir,
            title="Save Output File",
            defaultextension=".csv",
            filetypes=[("CSV File", "*.csv")]
        )

        # EDIT ALL EXPORT FILTERS wherein the total hours worked based on the filter is so on
        if not output_filename:
            print("File selection canceled by the user.")
        else:
            if filter_value == "Last 7 Days":
                data = result3

                # Open the CSV file in write mode
                with open(output_filename, "w", newline="") as file:
                    # Create a CSV writer
                    writer = csv.writer(file)

                    # Write additional values before the actual data
                    for xx in result:
                        writer.writerow([f"CSI Legazpi | Attendance System"])
                        writer.writerow([f"Employee: {xx[0]}"])
                        writer.writerow([f"Position: {xx[2]}"])
                        writer.writerow([f"Date Today: {current_datex}"])
                        writer.writerow([f"Filtered by {filter_value}"])  # Add your desired values
                        writer.writerow([f"Total hours worked within the Last 7 Days: {total_hours_worked1}"])

                    writer.writerow([" "])

                    # Write the header row
                    header = ["Row Number", "Date", "Time In", "Time Out"]  # Replace with your column names
                    writer.writerow(header)

                    # Write the data rows
                    for row in data:
                        writer.writerow(row)  # EDIT ALL FILTER  # EDIT ALL EXPORT FILTERS SO #

            if filter_value == "Last 2 Weeks":
                data = result3_2

                # Open the CSV file in write mode
                with open(output_filename, "w", newline="") as file:
                    # Create a CSV writer
                    writer = csv.writer(file)

                    # Write additional values before the actual data
                    for xx in result:
                        writer.writerow([f"CSI Legazpi | Attendance System"])
                        writer.writerow([f"Employee: {xx[0]}"])
                        writer.writerow([f"Position: {xx[2]}"])
                        writer.writerow([f"Date Today: {current_datex}"])
                        writer.writerow([f"Filtered by {filter_value}"])  # Add your desired values
                        writer.writerow([f"Total hours worked within the Last 2 Weeks: {total_hours_worked2}"])

                    writer.writerow([" "])

                    # Write the header row
                    header = ["Row Number", "Date", "Time In", "Time Out"]  # Replace with your column names
                    writer.writerow(header)

                    # Write the data rows
                    for row in data:
                        writer.writerow(row)

            if filter_value == "Last 30 Days":
                data = result3_3

                # Open the CSV file in write mode
                with open(output_filename, "w", newline="") as file:
                    # Create a CSV writer
                    writer = csv.writer(file)

                    # Write additional values before the actual data
                    for xx in result:
                        writer.writerow([f"CSI Legazpi | Attendance System"])
                        writer.writerow([f"Employee: {xx[0]}"])
                        writer.writerow([f"Position: {xx[2]}"])
                        writer.writerow([f"Date Today: {current_datex}"])
                        writer.writerow([f"Filtered by {filter_value}"])  # Add your desired values
                        writer.writerow([f"Total hours worked within the Last 30 Days: {total_hours_worked3}"])

                    writer.writerow([" "])

                    # Write the header row
                    header = ["Row Number", "Date", "Time In", "Time Out"]  # Replace with your column names
                    writer.writerow(header)

                    # Write the data rows
                    for row in data:
                        writer.writerow(row)

            if filter_value == "One Year":
                data = result3_4

                # Open the CSV file in write mode
                with open(output_filename, "w", newline="") as file:
                    # Create a CSV writer
                    writer = csv.writer(file)

                    # Write additional values before the actual data
                    for xx in result:
                        writer.writerow([f"CSI Legazpi | Attendance System"])
                        writer.writerow([f"Employee: {xx[0]}"])
                        writer.writerow([f"Position: {xx[2]}"])
                        writer.writerow([f"Date Today: {current_datex}"])
                        writer.writerow([f"Filtered by {filter_value}"])  # Add your desired values
                        writer.writerow([f"Total hours worked within One Year: {total_hours_worked4}"])

                    writer.writerow([" "])

                    # Write the header row
                    header = ["Row Number", "Date", "Time In", "Time Out"]  # Replace with your column names
                    writer.writerow(header)

                    # Write the data rows
                    for row in data:
                        writer.writerow(row)

            messagebox.showinfo("CSV Successfully Exported", "Attendance Report successfully exported as CSV.")

    export_btn = ttk.Button(master=view_atd_win, text="Export CSV", width=15, cursor="hand2", command=export)
    export_btn.place(x=570, y=93)

    def exit_win():
        view_atd_win.destroy()
        shared2.data_passing_var2 = None

    view_atd_win.protocol("WM_DELETE_WINDOW", exit_win)

    view_atd_win.mainloop()
