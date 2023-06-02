from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import shared


def initiate_delete_attd_win():
    del_win = Toplevel()

    del_win.geometry("300x100")
    del_win.title("Delete Row Attendance")
    del_win.config(bg="white")

    del_label = Label(master=del_win, font=("Century Gothic", 13), text="Insert Column. No", background='white',
                      foreground='black', highlightthickness=0, borderwidth=0)
    del_label.place(x=25, y=10)

    def on_entry_click(event):
        if col_num.get() == "1, 2,...":
            col_num.delete(0, END)
            col_num.config(foreground='black')

    def on_focus_out(event):
        if col_num.get() == "":
            col_num.insert(0, "1, 2,...")
            col_num.config(foreground='gray')

    col_num = ttk.Entry(master=del_win, font=("Century Gothic", 10), width=35, foreground='gray')
    col_num.bind("<FocusIn>", on_entry_click)
    col_num.bind("<FocusOut>", on_focus_out)
    col_num.insert(0, "1, 2,...")
    col_num.place(x=24, y=45)

    def delete_attd():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="minimumM4.",
                database="attendance",
        )

        cursor = mydb.cursor()
        cursor.execute(f"DELETE FROM id_{shared.data_passing_var2} WHERE id=%s", (col_num.get(),))
        mydb.commit()

        del_win.destroy()
        messagebox.showinfo("Attendance Successfully Deleted", "Attendance was successfully deleted."
                                                               " Please restart the Edit Window to show changes.")

    del_win.bind("<Return>", lambda event: delete_attd())

    del_win.mainloop()
