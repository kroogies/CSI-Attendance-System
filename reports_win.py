from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import shared2
import reports_view as rvp


def reports_window():
    shared2.data_passing_var2 = None

    reports_win = Toplevel()
    reports_win.geometry("1150x650+250+100")
    reports_win.title("Reports")
    reports_win.resizable(False, False)
    reports_win.config(bg="#f0f0f0")

    attendance_win_icon = Image.open("logo.png")
    final_icon = ImageTk.PhotoImage(attendance_win_icon)
    reports_win.iconphoto(False, final_icon)

    header = Image.open("banner.jpg")
    header = header.resize((1150, 86), Image.LANCZOS)
    header = ImageTk.PhotoImage(header)
    header_placeholder = Label(master=reports_win, image=header, borderwidth=0, highlightthickness=0)
    header_placeholder.place(x=0, y=0)

    line_separator = "_______________________________________________________________________________________________" \
                     "_______________________________________________________________________________________________" \
                     "________________________________"

    Label(master=reports_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='#f0f0f0').place(x=20, y=120)
    Label(master=reports_win, text=line_separator, highlightthickness=0, borderwidth=0, bg='#f0f0f0').place(x=20, y=167)
    Label(master=reports_win, text="REPORTS", highlightthickness=0, borderwidth=0, bg='#f0f0f0',
          font=("Century Gothic", 14)).place(x=70, y=100)

    global employee_subwindow
    global checkbox_canvas

    def update_employee_data():
        mydb6 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employees"
        )

        cursor6 = mydb6.cursor()
        cursor6.execute("SELECT * FROM employees ORDER BY id_number ASC LIMIT 0, 10")
        result6 = cursor6.fetchall()

        for widget in employee_subwindow.grid_slaves():
            widget.destroy()

        i = 0
        for employees in result6:
            for j in range(len(employees)):
                table = ttk.Entry(employee_subwindow, font=("Century Gothic", 10), foreground="black",
                                  background="white")
                table.config(state="normal")
                table.grid(row=i, column=j)
                table.insert(END, employees[j])
                table.config(state="readonly")
            i = i + 1

        mydb7 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employees"
        )

        cursor7 = mydb7.cursor()
        cursor7.execute("SELECT id_number FROM employees ORDER BY id_number")
        result7 = cursor7.fetchall()

        for checkbtns in checkbox_canvas.grid_slaves():
            checkbtns.destroy()

        var_list = []
        for saa, row in enumerate(result7):
            var1 = StringVar(value=row[0], name=row[0])
            style = ttk.Style()
            style.configure("Vertical.TCheckbutton", padding=(0, 3.5))
            checkbox = ttk.Checkbutton(checkbox_canvas, variable=var1, cursor="hand2", style="Vertical.TCheckbutton")
            checkbox.grid(row=saa, column=0)
            var_list.append(var1)

        def get_id_for_edit():
            mydb2 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="employees"
            )

            cursor2 = mydb2.cursor()

            id_list = [var.get() for var in var_list if
                       var.get()]  # contains the id's of the checkboxes,
            # and for every checked checkbox, the original value which is the id changes to "1"
            id_list_backup = [value for row in result7 for value in
                              row]  # contains the constant assigned id's of every checkbox

            for xz in range(len(id_list)):  # loops through the id_list to see if 1 is inside the list
                if id_list[xz] == '1':  # if 1 is inside the list, the index of the value 1 is taken and is matched
                    taken_id = id_list_backup[xz]
                    cursor2.execute("SELECT * FROM employees WHERE id_number=%s",
                                    (taken_id,))  # which is the assigned id
                    data = cursor2.fetchall()
                    shared2.data_passing_var2 = data[0][6]
                    # for the popup window

        def view_profile():
            get_id_for_edit()
            if shared2.data_passing_var2 is None:
                messagebox.showerror("Error", "Please select desired employee to view.")

            else:
                rvp.view_rpts_win()

        # labels
        name_label = Label(master=reports_win, text="NAME", font=("Century Gothic", 12), background="#f0f0f0",
                           borderwidth=0, highlightthickness=0)
        name_label.place(x=130, y=150)

        address_label = Label(master=reports_win, text="ADDRESS", font=("Century Gothic", 12), background="#f0f0f0",
                              borderwidth=0, highlightthickness=0)
        address_label.place(x=265, y=150)

        pos_label = Label(master=reports_win, text="POSITION", font=("Century Gothic", 12), background="#f0f0f0",
                          borderwidth=0, highlightthickness=0)
        pos_label.place(x=410, y=150)

        sex_label = Label(master=reports_win, text="SEX", font=("Century Gothic", 12), background="#f0f0f0",
                          borderwidth=0, highlightthickness=0)
        sex_label.place(x=580, y=150)

        email_label = Label(master=reports_win, text="EMAIL", font=("Century Gothic", 12), background="#f0f0f0",
                            borderwidth=0, highlightthickness=0)
        email_label.place(x=710, y=150)

        phonenum_label = Label(master=reports_win, text="PHONE NUMBER", font=("Century Gothic", 12), background="#f0f0f0",
                               borderwidth=0, highlightthickness=0)
        phonenum_label.place(x=820, y=150)

        id_label = Label(master=reports_win, text="ID NUMBER", font=("Century Gothic", 12), background="#f0f0f0",
                         borderwidth=0, highlightthickness=0)
        id_label.place(x=985, y=150)

        # buttons
        view_btn = ttk.Button(master=reports_win, text="View Employee", command=view_profile, cursor="hand2", width=25)
        view_btn.place(x=900, y=100)

    def refresh_employee_data():
        update_employee_data()
        employee_subwindow.after(10000,
                                 refresh_employee_data)  # Schedule the function to run again after 5000 milliseconds (5 seconds)

        # Define the main function to create the GUI elements and start the event loop

    # Create the GUI elements to display the data
    employee_subwindow = Canvas(reports_win, background="#f0f0f0", width=1050, height=525, borderwidth=0,
                                highlightthickness=0)
    employee_subwindow.place(x=80, y=200)

    checkbox_canvas = Canvas(reports_win, background="#f0f0f0", width=50, height=525, borderwidth=0,
                             highlightthickness=0)
    checkbox_canvas.place(x=40, y=198)

    # Retrieve the data and update the GUI element(s) initially
    update_employee_data()

    # Schedule the refresh function to update the GUI element(s) periodically
    employee_subwindow.after(10000, refresh_employee_data)
    # Update the data every 5000 milliseconds (5 seconds)

    reports_win.mainloop()
