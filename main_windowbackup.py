# The very important part of this project. The main program itself, the core of this project.
# Note that this window will only start or run if log in is successful. More about the log in feature will be
# discussed inside the login.py module.
# Inside this main_program module lies two main important buttons. The Employees and Reports Buttons.
# When the Employees button is pressed, the display of the main_program window changes and shows
# a table of the employees with their personal details and their ID/RFID tag.
# A list of buttons also shows up, namely; the Add, Edit, View, and Delete buttons. More about them will be individually
# explained inside their respective modules.
# Another important feature of this main_program module is the checkbox feature, which is very important
# to be able to select the employee profile that you want to execute actions on.
# To explain the checkbox feature in detail: Here's an overview.
# The general idea of the checkbox feature is that for every employee inside the database,
# a checkbox is created with an ID/RFID tag respectively assigned to them. So, if a checkbox with an ID/RFID tag
# assigned to it is checked, inside the shared.py module, a variable named data_passing_var2 whose value is None,
# changes to the assigned ID/RFID tag of the checked checkbox. The assigned ID/RFID tag is very important
# as it is the main mode of communication for multiple module variable communication. data_passing_var2 is used
# to know whose employee profile is to view, or to edit, or to delete.
# Also, this window or module has a refresh feature that automatically refreshes the window to show real-time
# changes based on database changes, like for example: a new employee profile was created, or an existing one
# was edited. All of it will instantly show inside the table display of this window.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import shared
import mysql.connector
import add_subwin_copy as asc
import edit_subwin as es
import view_profile as vpf
import rfid_x


# initialize database for useraccounts
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="minimumM4.",
  database="employees"
)

mydb3 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="minimumM4.",
    database="employees"
)

cursor = mydb.cursor()
cursor3 = mydb3.cursor()


def initiate_mprg():
    rfid_x.start_read_tag()

    # window
    win = Tk()
    win.state("zoomed")
    win.resizable(False, True)

    # config
    win.title("CSI Attendance System")

    panel_bg = Image.open("panel.jpg")
    resized_panel = panel_bg.resize((300, 730), Image.LANCZOS)
    final_panel = ImageTk.PhotoImage(resized_panel)
    label2 = Label(image=final_panel, borderwidth=0, highlightthickness=0)
    label2.place(x=-3, y=117)

    image_label = Image.open("banner.jpg")
    image_label2 = ImageTk.PhotoImage(image_label)
    label = Label(image=image_label2, borderwidth=0, highlightthickness=0)
    label.place(x=-2, y=0)

    # buttons

    # Define a function to retrieve data from database and update GUI element(s)
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
                    shared.data_passing_var2 = data[0][6]
                    # for the popup window

        def view_profile():
            get_id_for_edit()
            vpf.open_view_subwin()

        # labels
        # line seperator
        line = "__________________________________________________________________________________________________" \
               "__________________________________________________________________________________________________" \
               "_____________________"
        line_seperator = Label(master=win, text=line, highlightthickness=0, borderwidth=0)
        line_seperator.place(x=375, y=170)
        linesep2 = Label(master=win, text=line, highlightthickness=0, borderwidth=0)
        linesep2.place(x=375, y=205)

        name_label = Label(master=win, text="NAME", font=("Century Gothic", 12), background="#f0f0f0",
                           borderwidth=0, highlightthickness=0)
        name_label.place(x=425, y=190)

        address_label = Label(master=win, text="ADDRESS", font=("Century Gothic", 12), background="#f0f0f0",
                              borderwidth=0, highlightthickness=0)
        address_label.place(x=575, y=190)

        pos_label = Label(master=win, text="POSITION", font=("Century Gothic", 12), background="#f0f0f0",
                          borderwidth=0, highlightthickness=0)
        pos_label.place(x=725, y=190)

        sex_label = Label(master=win, text="SEX", font=("Century Gothic", 12), background="#f0f0f0",
                          borderwidth=0, highlightthickness=0)
        sex_label.place(x=870, y=190)

        email_label = Label(master=win, text="EMAIL", font=("Century Gothic", 12), background="#f0f0f0",
                            borderwidth=0, highlightthickness=0)
        email_label.place(x=1015, y=190)

        phonenum_label = Label(master=win, text="PHONE NUMBER", font=("Century Gothic", 12), background="#f0f0f0",
                               borderwidth=0, highlightthickness=0)
        phonenum_label.place(x=1165, y=190)

        id_label = Label(master=win, text="ID NUMBER", font=("Century Gothic", 12), background="#f0f0f0",
                         borderwidth=0, highlightthickness=0)
        id_label.place(x=1315, y=190)

        # buttons
        global view_btn
        view_btn = ttk.Button(master=win, text="View", command=view_profile, cursor="hand2")
        view_btn.place(x=990, y=146)

        def edit_profile():
            get_id_for_edit()
            es.open_edit_subwin()

        global edit_btn
        edit_btn = ttk.Button(master=win, text='Edit', cursor='hand2', command=edit_profile)
        edit_btn.place(x=1149, y=146)

        def delete_profile():
            get_id_for_edit()

            delete_db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="employees"
            )

            del_cursor = delete_db.cursor()

            id_db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="id_tags"
            )

            id_cursor = id_db.cursor()

            attd_db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            attd_cursor = attd_db.cursor()

            attd_db2 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance"
            )

            attd_cursor2 = attd_db2.cursor()

            if shared.data_passing_var2 is None:
                messagebox.showinfo('Delete Profile', 'Please select a desired profile to delete if desired.')

            else:
                option = messagebox.askyesno('Delete Employee Profile', 'Are you sure you want to delete this profile?:'
                                                                        f' {shared.data_passing_var2}')

                if option:
                    del_cursor.execute("DELETE FROM employees WHERE id_number=%s", (shared.data_passing_var2,))
                    id_cursor.execute("UPDATE available_ids SET status='unused' WHERE ids=%s",
                                      (shared.data_passing_var2,))

                    attd_cursor.execute(f"DELETE FROM id_{shared.data_passing_var2}")
                    attd_db.commit()

                    attd_cursor2.execute(f"ALTER TABLE id_{shared.data_passing_var2} AUTO_INCREMENT=1")
                    attd_db2.commit()

                    delete_db.commit()
                    id_db.commit()
                    messagebox.showinfo('Delete Employee Profile', 'Employee Profile successfully deleted.')

                else:
                    shared.data_passing_var2 = None

        global delete_button
        delete_button = ttk.Button(master=win, text='Delete', cursor='hand2', command=delete_profile)
        delete_button.place(x=1228, y=146)

    # Define a refresh function to periodically update the GUI element(s)
    def refresh_employee_data():
        update_employee_data()
        employee_subwindow.after(10000,
                  refresh_employee_data)  # Schedule the function to run again after 5000 milliseconds (5 seconds)

    # Define the main function to create the GUI elements and start the event loop
    def employee_btn_func():
        global employee_subwindow
        global checkbox_canvas

        # Create the GUI elements to display the data
        employee_subwindow = Canvas(win, background="#f0f0f0", width=1050, height=525, borderwidth=0,
                                    highlightthickness=0)
        employee_subwindow.place(x=420, y=234)

        checkbox_canvas = Canvas(win, background="#f0f0f0", width=50, height=525, borderwidth=0,
                                 highlightthickness=0)
        checkbox_canvas.place(x=380, y=230)

        # Retrieve the data and update the GUI element(s) initially
        update_employee_data()

        def add_profile():
            asc.open_add_window()

        global add_btn
        add_btn = ttk.Button(master=win, text="Add", cursor="hand2", command=add_profile)
        add_btn.place(x=1070, y=146)

        # Schedule the refresh function to update the GUI element(s) periodically
        global id1
        global id2
        id1 = employee_subwindow.after(10000, refresh_employee_data)
        # Update the data every 5000 milliseconds (5 seconds)

        report_subwindow.after_cancel(id2)

        try:
            view_btn2.destroy()

        except Exception as e:
            print(f"None {e}")

    def update_employee_data2():

        mydb6 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employees"
        )

        cursor6 = mydb6.cursor()
        cursor6.execute("SELECT * FROM employees ORDER BY id_number ASC LIMIT 0, 10")
        result6 = cursor6.fetchall()

        for widget in report_subwindow.grid_slaves():
            widget.destroy()

        i = 0
        for employees in result6:
            for j in range(len(employees)):
                table = ttk.Entry(report_subwindow, font=("Century Gothic", 10), foreground="black",
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

        for checkbtns in checkbox2_canvas.grid_slaves():
            checkbtns.destroy()

        var_list = []
        for saa, row in enumerate(result7):
            var1 = StringVar(value=row[0], name=row[0])
            style = ttk.Style()
            style.configure("Vertical.TCheckbutton", padding=(0, 3.5))
            checkbox = ttk.Checkbutton(checkbox2_canvas, variable=var1, cursor="hand2", style="Vertical.TCheckbutton")
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
                    shared.data_passing_var2 = data[0][6]
                    # for the popup window

        def view_profile():
            get_id_for_edit()
            vpf.open_view_subwin()

        # labels
        # line seperator
        line = "__________________________________________________________________________________________________" \
               "__________________________________________________________________________________________________" \
               "_____________________"
        line_seperator = Label(master=win, text=line, highlightthickness=0, borderwidth=0)
        line_seperator.place(x=375, y=170)
        linesep2 = Label(master=win, text=line, highlightthickness=0, borderwidth=0)
        linesep2.place(x=375, y=205)

        name_label = Label(master=win, text="NAME", font=("Century Gothic", 12), background="#f0f0f0",
                           borderwidth=0, highlightthickness=0)
        name_label.place(x=425, y=190)

        address_label = Label(master=win, text="ADDRESS", font=("Century Gothic", 12), background="#f0f0f0",
                              borderwidth=0, highlightthickness=0)
        address_label.place(x=575, y=190)

        pos_label = Label(master=win, text="POSITION", font=("Century Gothic", 12), background="#f0f0f0",
                          borderwidth=0, highlightthickness=0)
        pos_label.place(x=725, y=190)

        sex_label = Label(master=win, text="SEX", font=("Century Gothic", 12), background="#f0f0f0",
                          borderwidth=0, highlightthickness=0)
        sex_label.place(x=870, y=190)

        email_label = Label(master=win, text="EMAIL", font=("Century Gothic", 12), background="#f0f0f0",
                            borderwidth=0, highlightthickness=0)
        email_label.place(x=1015, y=190)

        phonenum_label = Label(master=win, text="PHONE NUMBER", font=("Century Gothic", 12), background="#f0f0f0",
                               borderwidth=0, highlightthickness=0)
        phonenum_label.place(x=1165, y=190)

        id_label = Label(master=win, text="ID NUMBER", font=("Century Gothic", 12), background="#f0f0f0",
                         borderwidth=0, highlightthickness=0)
        id_label.place(x=1315, y=190)

        def logs():
            print('test view')

        # buttons
        global view_btn2
        view_btn2 = ttk.Button(master=win, text="View", command=logs, cursor="hand2", width=53)
        view_btn2.place(x=990, y=146)

    def refresh_employee_data2():
        update_employee_data2()
        report_subwindow.after(10000,
                               refresh_employee_data2)
        # Schedule the function to run again after 5000 milliseconds (5 seconds)

    def report_btn_func():
        global report_subwindow
        global checkbox2_canvas

        # Create the GUI elements to display the data
        report_subwindow = Canvas(master=win, background="#f0f0f0", width=1050, height=525, borderwidth=0,
                                  highlightthickness=0)
        report_subwindow.place(x=420, y=234)

        checkbox2_canvas = Canvas(master=win, background="#f0f0f0", width=50, height=525, borderwidth=0,
                                  highlightthickness=0)
        checkbox2_canvas.place(x=380, y=230)

        # Retrieve the data and update the GUI element(s) initially
        update_employee_data2()

        # Schedule the refresh function to update the GUI element(s) periodically
        global id2
        id2 = report_subwindow.after(10000, refresh_employee_data2)
        # Update the data every 5000 milliseconds (5 seconds)

        try:
            employee_subwindow.after_cancel(id1)

        except Exception as e:
            print(f"Disregard: {e}")

        try:
            add_btn.destroy()
            delete_button.destroy()
            view_btn.destroy()
            edit_btn.destroy()

        except Exception as e:
            print(f"None {e}")

    btn1 = Image.open("employees_btn.png")
    btn1_final = ImageTk.PhotoImage(btn1)
    employee_btn = Button(image=btn1_final, borderwidth=0, highlightcolor="#49c5fe", highlightbackground='#49c5fe',
                          command=employee_btn_func, highlightthickness=0, cursor="hand2")
    employee_btn.place(x=-8, y=170)

    btn2 = Image.open("reports_btn.png")
    btn2_final = ImageTk.PhotoImage(btn2)
    reports_btn = Button(image=btn2_final, borderwidth=0, highlightcolor="#49c5fe", highlightbackground='#49c5fe',
                         command=report_btn_func, highlightthickness=0, cursor="hand2")
    reports_btn.place(x=-8, y=245)

    # icon
    icon = Image.open("logo.png")
    icon2 = ImageTk.PhotoImage(icon)
    win.iconphoto(False, icon2)

    win.mainloop()
