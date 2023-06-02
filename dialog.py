from tkinter import *
import shared


def time_in_notif():
    window = Toplevel()
    window.geometry("300x150+650+350")
    window.title("Employee Swiped Attendance")

    label1 = Label(master=window, text=f"Employee: {shared.name}", font=("Century Gothic", 12))
    label1.place(x=20, y=20)

    label2 = Label(master=window, text=f"Date: {shared.the_date}", font=("Century Gothic", 12))
    label2.place(x=20, y=50)

    label3 = Label(master=window, text=f"Time In: {shared.the_time_in}", font=("Century Gothic", 12))
    label3.place(x=20, y=80)

    def destroy_window():
        window.destroy()
        #shared.the_date = None
        #shared.the_time_out = None
        #shared.the_time_in = None
        #shared.name = None

    # Schedule the destruction of the window after 6 seconds
    window.after(6000, destroy_window)

    # Start the Tkinter event loop
    window.mainloop()


def time_out_notif():
    window2 = Toplevel()
    window2.geometry("300x150+650+350")
    window2.title("Employee Swiped Attendance")

    label1 = Label(master=window2, text=f"Employee: {shared.name}", font=("Century Gothic", 12))
    label1.place(x=20, y=20)

    label2 = Label(master=window2, text=f"Date: {shared.the_date}", font=("Century Gothic", 12))
    label2.place(x=20, y=50)

    label3 = Label(master=window2, text=f"Time Out: {shared.the_time_out}", font=("Century Gothic", 12))
    label3.place(x=20, y=80)

    def destroyer2():
        window2.destroy()
        #shared.the_date = None
        #shared.the_time_out = None
        #shared.the_time_in = None
        #shared.name = None

    window2.after(6000, destroyer2)

    window2.mainloop()
