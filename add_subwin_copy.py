# ADD_SUB_WIN
# ADD_SUB_WIN stands for the 'add sub window' meaning that it is a separate window or an external window that's
# connected to the main program. Inside this add sub window, you can create employee profiles which contain fields
# such as first name, last name, their position, their sex, or etc. And inside this module, a unique rfid tag
# is assigned to them automatically and the algorithm can be located within the lines 109-170, or rather inside
# the assign_id() function. To further explain the algorithm, 2 database connections which connect to the
# id_tags database and the employees database are initiated and data's from both databases are retrieved with the
# MySQL connector function, .fetchall(). And the function outputs a list with the datas retrieved from the databases.
# The list contains groups of id's with their status, henceforth looking like this:
# [('id1', 'status'), ('id2', 'status')] 'and so on and so forth'
# Inside the list which is [], are tuples, which are then identified as the parentheses. Inside the tuples
# are the IDs retrieved from the id_tags database and their status. Each id has two states, one being 'used',
# and the second being 'unused'.
# The algorithm first loops through the list to get all, of the tuples and the tuples are then divided into their own
# places as so to access the values inside the tuples. The algorithm then loops through the id's and see if their
# status is 'used' or 'unused'. If it is used, it will then shift to the next id in the list and will continue
# shifting until it finds and unused ID. If the ID is unused, it will then be assigned to the currently being created
# employee profile.
# In a scenario where all, of the IDs have been used up and one used ID was unassigned to a profile and turns
# to unused, the algorithm can shift backwards or forwards if necessary to recycle any unassigned ID's as so
# not to waste them.
# And so, if all fields meet all the necessary conditions, like, don't put numbers inside the name fields or
# don't put letters inside the number field, and, etc., You can then press save, and the SQL Query
# that inserts the data inside the employees database gets executed. Congrats,
# you just added new data into the database or have created a new employee profile.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import re
import shared


def open_add_window():
    def clear_initial_text(event):
        widget = event.widget
        initial_text = widget.get()
        if initial_text == '*':
            widget.delete(0, END)

    def clear_initial_address(event):
        widget = event.widget
        initial_text = widget.get("1.0", "end-1c")
        if initial_text == '*':
            widget.delete("1.0", "end")

    shared.data_passing_var2 = None

    add_win = Toplevel()
    add_win.geometry("1000x600+400+100")
    add_win.title("Add Employee")
    add_win.resizable(False, False)
    add_win.config(bg="white")

    addwin_icon = Image.open("logo.png")
    final_icon = ImageTk.PhotoImage(addwin_icon)
    add_win.iconphoto(False, final_icon)

    header = Image.open("banner.jpg")
    header = header.resize((1000, 75), Image.LANCZOS)
    header = ImageTk.PhotoImage(header)
    header_placeholder = Label(master=add_win, image=header, borderwidth=0, highlightthickness=0)
    header_placeholder.place(x=0, y=0)

    # labels
    first_name_label = Label(master=add_win, text="FIRST NAME", borderwidth=0, highlightthickness=0,
                             font=("Century Gothic", 13), bg="white")
    first_name_label.place(x=40, y=150)

    middle_name_label = Label(master=add_win, text="MIDDLE NAME", borderwidth=0, highlightthickness=0,
                              font=("Century Gothic", 13), bg="white")
    middle_name_label.place(x=40, y=190)

    last_name_label = Label(master=add_win, text="LAST NAME", borderwidth=0, highlightthickness=0,
                            font=("Century Gothic", 13), bg="white")
    last_name_label.place(x=40, y=230)

    position_label = Label(master=add_win, text="POSITION", borderwidth=0, highlightthickness=0,
                           font=("Century Gothic", 13), bg="white")
    position_label.place(x=40, y=270)

    sex_label = Label(master=add_win, text="SEX", borderwidth=0, highlightthickness=0,
                      font=("Century Gothic", 13), bg="white")
    sex_label.place(x=40, y=310)

    address_label = Label(master=add_win, text="ADDRESS", borderwidth=0, highlightthickness=0,
                          font=("Century Gothic", 13), bg="white")
    address_label.place(x=40, y=350)

    phonenum_label = Label(master=add_win, text="PHONE NUMBER", borderwidth=0, highlightthickness=0,
                           font=("Century Gothic", 13), bg="white")
    phonenum_label.place(x=40, y=430)

    email_label = Label(master=add_win, text="EMAIL ADDRESS", borderwidth=0, highlightthickness=0,
                        font=("Century Gothic", 13), bg="white")
    email_label.place(x=40, y=470)

    tag_label = Label(master=add_win, text="ID NUMBER", borderwidth=0, highlightthickness=0,
                      font=("Century Gothic", 13), bg="white")
    tag_label.place(x=40, y=510)

    # entries
    first_name_entry = ttk.Entry(master=add_win, font=("Century Gothic", 10), width=40)
    first_name_entry.bind('<Button-1>', clear_initial_text)
    first_name_entry.place(x=190, y=150)

    middle_name_entry = ttk.Entry(master=add_win, font=("Century Gothic", 10), width=40)
    middle_name_entry.bind('<Button-1>', clear_initial_text)
    middle_name_entry.place(x=190, y=190)

    last_name_entry = ttk.Entry(master=add_win, font=("Century Gothic", 10), width=40)
    last_name_entry.bind('<Button-1>', clear_initial_text)
    last_name_entry.place(x=190, y=230)

    pos_entry = ttk.Entry(master=add_win, font=("Century Gothic", 10), width=40)
    pos_entry.bind('<Button-1>', clear_initial_text)
    pos_entry.place(x=190, y=270)

    # drop down for sex selection
    def callback(value):
        global sex_input
        sex_input = str(value)

    options = ["Sex", "Male", "Female"]
    selected_option = StringVar()
    selected_option.set(options[0])
    sex_entry = ttk.OptionMenu(add_win, selected_option, *options, command=callback)
    sex_entry.configure(cursor="hand2")
    sex_entry.place(x=190, y=310)

    # text box field for address, very big field ye
    address_field = Text(add_win, width=40, height=3, font=("Century Gothic", 10),
                         borderwidth=1, highlightthickness=2, background="white")
    address_field.bind('<Button-1>', clear_initial_address)
    address_field.place(x=190, y=350)

    phonenum_entry = ttk.Entry(master=add_win, font=("Century Gothic", 10), width=40)
    phonenum_entry.bind('<Button-1>', clear_initial_text)
    phonenum_entry.place(x=190, y=430)

    email_add_entry = ttk.Entry(master=add_win, font=("Century Gothic", 10), width=40)
    email_add_entry.bind('<Button-1>', clear_initial_text)
    email_add_entry.place(x=190, y=470)

    id_entry = ttk.Entry(master=add_win, font=("Century Gothic", 10), width=40)
    id_entry.bind('<Button-1>', clear_initial_text)
    id_entry.place(x=190, y=510)

    # line seperator
    linesep = "______________________________________________________________________________" \
              "___________________________" \
              "______________________________________________________________________________________"
    Label(master=add_win, text=linesep, fg='black', background="white", borderwidth=0,
          highlightthickness=0).place(x=20, y=100)

    # functions

    def exit_win():
        add_win.destroy()

    def insert_asterisk():
        first_name_entry.insert(END, '*')
        middle_name_entry.insert(END, '*')
        last_name_entry.insert(END, '*')
        pos_entry.insert(END, '*')
        address_field.insert(END, '*')
        phonenum_entry.insert(END, '*')
        email_add_entry.insert(END, '*')
        id_entry.insert(END, '*')

    def red_asterisk():
        # conditional block to check if the length of values inside the entries are equal to 0, or the textbox is empty
        if len(first_name_entry.get()) < 3:
            first_name_entry.config(foreground='red')

        if len(middle_name_entry.get()) < 3:
            middle_name_entry.config(foreground='red')

        if len(last_name_entry.get()) < 3:
            last_name_entry.config(foreground='red')

        if len(pos_entry.get()) < 3:
            pos_entry.config(foreground='red')

        if len(address_field.get("1.0", "end-1c")) < 5:
            address_field.config(foreground='red')

        if len(phonenum_entry.get()) < 11 or len(phonenum_entry.get()) > 11:
            phonenum_entry.config(foreground='red')

        if len(email_add_entry.get()) < 3:
            email_add_entry.config(foreground='red')

        if len(id_entry.get()) < 10 or len(id_entry.get()) > 10:
            id_entry.config(foreground='red')

        # conditional block to check if the textbox is filled but shows error when it contains wrong data type
        if re.search("[^a-zA-Z]", first_name_entry.get()):
            first_name_entry.config(foreground='red')

        if re.search("[^a-zA-Z]", middle_name_entry.get()):
            middle_name_entry.config(foreground='red')

        if re.search("[^a-zA-Z]", last_name_entry.get()):
            last_name_entry.config(foreground='red')

        if re.search("[^a-zA-Z]", pos_entry.get()):
            pos_entry.config(foreground='red')

        if re.search("[^0-9]", phonenum_entry.get()):
            pos_entry.config(foreground='red')

        if not re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_add_entry.get()):
            email_add_entry.config(foreground='red')

        # conditional block to check if info is valid and change font color
        if len(first_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', first_name_entry.get()):
            first_name_entry.config(foreground='black')

        if len(middle_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', middle_name_entry.get()):
            middle_name_entry.config(foreground='black')

        if len(last_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', last_name_entry.get()):
            last_name_entry.config(foreground='black')

        if len(pos_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', pos_entry.get()):
            pos_entry.config(foreground='black')

        if len(address_field.get("1.0", "end-1c")) >= 5:
            address_field.config(foreground='black')

        if len(phonenum_entry.get()) == 11 and not re.search('[^0123456789]', phonenum_entry.get()):
            phonenum_entry.config(foreground='black')

        if len(email_add_entry.get()) >= 3 and \
                re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_add_entry.get()):
            email_add_entry.config(foreground='black')

        if len(id_entry.get()) == 10 and not re.search('[^0123456789]', id_entry.get()):
            id_entry.config(foreground='black')

    def refresh_page():
        red_asterisk()
        add_win.after(500, refresh_page)

    refresh_page()
    insert_asterisk()

    def add_data():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employees"
        )

        cursor = db.cursor()
        name_value = f"{first_name_entry.get()} {middle_name_entry.get()} {last_name_entry.get()}"
        pos_value = pos_entry.get()
        # sex value is variable named sex_input
        address_value = address_field.get("1.0", "end-1c")
        num_value = phonenum_entry.get()
        email_value = email_add_entry.get()
        id_value = id_entry.get()
        red_asterisk()

        # another conditional block to check info validity and finally execute sql query
        if len(first_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', first_name_entry.get()) and \
                len(middle_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', middle_name_entry.get()) and \
                len(last_name_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', last_name_entry.get()) and \
                len(pos_entry.get()) >= 3 and not re.search('[^a-zA-Z ]', pos_entry.get()) and \
                len(address_field.get("1.0", "end-1c")) >= 5 and \
                len(phonenum_entry.get()) == 11 and not re.search('[^0-9]', phonenum_entry.get()) and \
                sex_input in ["Male", "Female"] and \
                re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_add_entry.get()) and \
                len(id_entry.get()) == 10 and not re.search('[^0-9]', id_entry.get()):

            sql = "INSERT INTO employees (name, address, position, sex, email, phone_num, id_number) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (name_value, address_value, pos_value, sex_input,
                   email_value, num_value, id_value)

            try:
                cursor.execute(sql, val)
                db.commit()
                messagebox.showinfo("Employee Profile Successfully created", "The employee profile was successfully"
                                                                             " created.")

                shared.keys_pressed.clear()
                add_win.destroy()

            except Exception as e:
                messagebox.showerror("Error", "ID is currently in use by another employee, "
                                              " please use another RFID TAG.")
                print(e)

        else:
            messagebox.showerror("Error", "Please ensure all values in each entry fields are correct.")

    # buttons
    save_btn = ttk.Button(master=add_win, text="Save", command=add_data)
    save_btn.place(x=40, y=82)

    cancel_btn = ttk.Button(master=add_win, text="Cancel", style="Custom.TButton", command=exit_win)
    cancel_btn.place(x=120, y=82)

    background_pic = Image.open('transparent_logo.png')
    background_pic = ImageTk.PhotoImage(background_pic)
    bg_label = Label(master=add_win, image=background_pic, borderwidth=0, highlightthickness=0)
    bg_label.place(x=560, y=160)

    add_win.mainloop()
