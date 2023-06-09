from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import shared


def show_del():
    delete = Toplevel()
    delete.geometry("260x100+650+350")
    delete.title("Delete PIN")

    Label(master=delete, font=("Century Gothic", 15), borderwidth=0, highlightthickness=0, text="PIN").place(x=110, y=10)

    pin = ttk.Entry(master=delete, show="*", width=35)
    pin.place(x=23, y=35)

    def delete_profile():
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

        schedule = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="employee_schedule"
        )

        schedule_cursor = schedule.cursor()

        mydb_x = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="pin",
        )

        cursor_x = mydb_x.cursor()
        cursor_x.execute(f"SELECT pass FROM deletion_pin WHERE pass={pin.get()}")
        res = cursor_x.fetchall()

        if len(res) >= 1:
            del_cursor.execute("DELETE FROM employees WHERE id_number=%s", (shared.data_passing_var2,))
            id_cursor.execute("UPDATE available_ids SET status='unused' WHERE ids=%s",
                              (shared.data_passing_var2,))

            schedule_cursor.execute(f"DROP TABLE x_{shared.data_passing_var2}")
            schedule.commit()

            attd_cursor.execute(f"DELETE FROM id_{shared.data_passing_var2}")
            attd_db.commit()

            attd_cursor2.execute(f"ALTER TABLE id_{shared.data_passing_var2} AUTO_INCREMENT=1")
            attd_db2.commit()

            delete_db.commit()
            id_db.commit()

            messagebox.showinfo('Delete Employee Profile', 'Employee Profile successfully deleted.')

            shared.data_passing_var2 = None

    def verify():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="minimumM4.",
            database="pin",
        )

        cursor = mydb.cursor()
        cursor.execute("SELECT pass FROM deletion_pin")
        res = cursor.fetchall()
        for i in res:
            shared.pin = i[0]

        if pin.get() != shared.pin:
            messagebox.showerror("Wrong PIN", "Please input the correct PIN.")
            delete.destroy()
            shared.data_passing_var2 = None

        else:
            delete_profile()
            delete.destroy()

    btn = ttk.Button(master=delete, text="Delete", command=verify)
    btn.place(x=90, y=63)

    def on_close():
        shared.data_passing_var2 = None
        delete.destroy()

    delete.protocol("WM_DELETE_WINDOW", on_close)

    delete.mainloop()