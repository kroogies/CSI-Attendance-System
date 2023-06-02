# This is the module for the RFID reader. The RFID reader is an external device and does not
# necessarily need to be connected to any other module as it can run on a separate thread.
# Note, that the separate thread that runs this module will only initiate if log in is successful.
# The RFID reader currently being used is not considered an NFC device but rather, a keyboard emulator.
# Here we use a library to help us make reading keyboard events easier.
# Whenever an RFID tag/ID is being scanned or read, it is considered as an individual key press.
# So we take the values of those key presses, and modify the RFID tag/ID, so we can use it as parameters
# for certain things. By certain things, recording attendance for every scan.
# As I said, this is a standalone module that runs on a separate thread. So once that thread gets initiated,
# it will keep running and running even on different parts of the program. But note, that it will not record
# attendance if the program is minimized or closed. As the thread only runs if the program is open, so I guess it
# isn't much of a standalone module. So those are the limitations, the program must always be open so this module
# can keep running and make the RFID reader function.
# Here's the general overview of the RFID reader module:
# Inside this module, separate conditional statements are made for each and every RFID tag that we have available.
# So, if the ID/RFID tag that is scanned is equivalent to this ID, record that employee's time_in, and date, and
# timeout. So that's all.

from tkinter import *
from pynput import keyboard
from datetime import datetime
import dialog
from attendance_notif import *
from tkinter import messagebox
import threading
import mysql.connector
import shared


shared.keys_pressed = []
last_action = None
last_action2 = None
last_action3 = None
last_action4 = None
last_action5 = None
last_action6 = None
last_action7 = None
last_action8 = None
last_action9 = None
last_action10 = None

id_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="minimumM4.",
    database="id_tags",
)


def read_tag():

    def on_press(key):
        try:
            # Add the key ID to the list of keys pressed
            shared.keys_pressed.append(key.char)
        except AttributeError:
            # Ignore special keys like 'ctrl', 'alt', etc.
            pass

        if len(shared.keys_pressed) == 10:
            the_id = ''.join(shared.keys_pressed).strip()
            shared.keys_pressed.clear()

            def update_attendance():

                global last_action
                global last_action2
                global last_action3
                global last_action4
                global last_action5
                global last_action6
                global last_action7
                global last_action8
                global last_action9
                global last_action10

                now = datetime.now()
                time_am_pm = now.strftime("%I:%M %p")
                date_str = now.strftime("%Y-%m-%d")

                if the_id == '0007606744':
                    mydb1 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor1 = mydb1.cursor()

                    if not last_action or last_action == 'time_out':
                        global log_id
                        # perform time in action
                        sql = 'INSERT INTO id_0007606744 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor1.execute(sql, val)
                        log_id = cursor1.lastrowid
                        mydb1.commit()
                        last_action = 'time_in'
                        take_values("0007606744", "0007606744", date_str, time_am_pm, None)

                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0007606744 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id)
                        cursor1.execute(sql, val)
                        mydb1.commit()
                        last_action = 'time_out'
                        take_values("0007606744", "0007606744", date_str, None, time_am_pm)

                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008264524':
                    mydb2 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor2 = mydb2.cursor()

                    if not last_action2 or last_action2 == 'time_out':  # change vars
                        global log_id2  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008264524 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor2.execute(sql, val)  # change cursor
                        log_id2 = cursor2.lastrowid  # change cursor and logid
                        mydb2.commit()  # change db
                        last_action2 = 'time_in'  # change
                        take_values("0008264524", "0008264524", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action2 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008264524 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id2)
                        cursor2.execute(sql, val)
                        mydb2.commit()
                        last_action2 = 'time_out'
                        take_values("0008264524", "0008264524", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008385348':
                    mydb3 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor3 = mydb3.cursor()

                    if not last_action3 or last_action3 == 'time_out':  # change vars
                        global log_id3  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008385348 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor3.execute(sql, val)  # change cursor
                        log_id3 = cursor3.lastrowid  # change cursor and logid
                        mydb3.commit()  # change db
                        last_action3 = 'time_in'  # change
                        take_values("0008385348", "0008385348", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action3 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008385348 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id3)
                        cursor3.execute(sql, val)
                        mydb3.commit()
                        last_action3 = 'time_out'
                        take_values("0008385348", "0008385348", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008407268':
                    mydb4 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor4 = mydb4.cursor()

                    if not last_action4 or last_action4 == 'time_out':  # change vars
                        global log_id4  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008407268 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor4.execute(sql, val)  # change cursor
                        log_id4 = cursor4.lastrowid  # change cursor and logid
                        mydb4.commit()  # change db
                        last_action4 = 'time_in'  # change
                        take_values("0008407268", "0008407268", date_str, time_am_pm, None)

                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action4 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008407268 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id4)
                        cursor4.execute(sql, val)
                        mydb4.commit()
                        last_action4 = 'time_out'
                        take_values("0008407268", "0008407268", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008531832':
                    mydb5 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor5 = mydb5.cursor()

                    if not last_action5 or last_action5 == 'time_out':  # change vars
                        global log_id5  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008531832 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor5.execute(sql, val)  # change cursor
                        log_id5 = cursor5.lastrowid  # change cursor and logid
                        mydb5.commit()  # change db
                        last_action5 = 'time_in'  # change
                        take_values("0008531832", "0008531832", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action5 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008531832 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id5)
                        cursor5.execute(sql, val)
                        mydb5.commit()
                        last_action5 = 'time_out'
                        take_values("0008531832", "0008531832", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008532623':
                    mydb6 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor6 = mydb6.cursor()

                    if not last_action6 or last_action6 == 'time_out':  # change vars
                        global log_id6  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008532623 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor6.execute(sql, val)  # change cursor
                        log_id6 = cursor6.lastrowid  # change cursor and logid
                        mydb6.commit()  # change db
                        last_action6 = 'time_in'  # change
                        take_values("0008532623", "0008532623", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action6 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008532623 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id6)
                        cursor6.execute(sql, val)
                        mydb6.commit()
                        last_action6 = 'time_out'
                        take_values("0008532623", "0008532623", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008717702':
                    mydb7 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor7 = mydb7.cursor()

                    if not last_action7 or last_action7 == 'time_out':  # change vars
                        global log_id7  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008717702 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor7.execute(sql, val)  # change cursor
                        log_id7 = cursor7.lastrowid  # change cursor and logid
                        mydb7.commit()  # change db
                        last_action7 = 'time_in'  # change
                        take_values("0008717702", "0008717702", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action7 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008717702 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id7)
                        cursor7.execute(sql, val)
                        mydb7.commit()
                        last_action7 = 'time_out'
                        take_values("0008717702", "0008717702", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008721967':
                    mydb8 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor8 = mydb8.cursor()

                    if not last_action8 or last_action8 == 'time_out':  # change vars
                        global log_id8  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008721967 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor8.execute(sql, val)  # change cursor
                        log_id8 = cursor8.lastrowid  # change cursor and logid
                        mydb8.commit()  # change db
                        last_action8 = 'time_in'  # change
                        take_values("0008721967", "0008721967", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action8 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008721967 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id8)
                        cursor8.execute(sql, val)
                        mydb8.commit()
                        last_action8 = 'time_out'
                        take_values("0008721967", "0008721967", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0008899484':
                    mydb9 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor9 = mydb9.cursor()

                    if not last_action9 or last_action9 == 'time_out':  # change vars
                        global log_id9  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0008899484 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor9.execute(sql, val)  # change cursor
                        log_id9 = cursor9.lastrowid  # change cursor and logid
                        mydb9.commit()  # change db
                        last_action9 = 'time_in'  # change
                        take_values("0008899484", "0008899484", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action9 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0008899484 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id9)
                        cursor9.execute(sql, val)
                        mydb9.commit()
                        last_action9 = 'time_out'
                        take_values("0008899484", "0008899484", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

                if the_id == '0009041509':
                    mydb10 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="minimumM4.",
                        database="attendance"
                    )

                    cursor10 = mydb10.cursor()

                    if not last_action10 or last_action10 == 'time_out':  # change vars
                        global log_id10  # change var
                        # perform time in action
                        sql = 'INSERT INTO id_0009041509 (date, time_in, time_out) VALUES (%s, %s, %s)'
                        val = (date_str, time_am_pm, 'None')
                        cursor10.execute(sql, val)  # change cursor
                        log_id10 = cursor10.lastrowid  # change cursor and logid
                        mydb10.commit()  # change db
                        last_action10 = 'time_in'  # change
                        take_values("0009041509", "0009041509", date_str, time_am_pm, None)
                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif last_action10 == 'time_in':
                        # perform time out action
                        sql = 'UPDATE id_0009041509 SET time_out=%s WHERE id=%s'
                        val = (time_am_pm, log_id10)
                        cursor10.execute(sql, val)
                        mydb10.commit()
                        last_action10 = 'time_out'
                        take_values("0009041509", "0009041509", date_str, None, time_am_pm)
                        try:
                            dialog.time_out_notif()
                        except Exception as e:
                            print(e)

            update_attendance()

    # Create a keyboard listener that will call on_press() and on_release() functions
    with keyboard.Listener(on_press=on_press, on_release=None) as listener:
        # Start listening for keyboard events
        listener.join()


def start_read_tag():
    # Start the read_tag() function in a separate thread
    thread = threading.Thread(target=read_tag)
    thread.daemon = True
    thread.start()

