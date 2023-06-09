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

from pynput import keyboard
from datetime import datetime, timedelta
import dialog
from attendance_notif import *
import threading
import mysql.connector
import shared


shared.keys_pressed = []
id_last_action = {}
id_log_ids = {}
ids = ['0007606744', '0008264524', '0008385348', '0008407268', '0008531832', '0008532623', '0008717702',
       '0008721967', '0008899484', '0009041509']

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

                global id_last_action

                now = datetime.now()
                time_am_pm = now.strftime("%I:%M %p")
                date_str = now.strftime("%Y-%m-%d")

                if the_id in ids:
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

                    if the_id not in id_last_action or id_last_action[the_id] == 'time_out':
                        # perform time in action
                        sql = f'INSERT INTO id_{the_id} (date, time_in, time_out, hours_worked, late) VALUES (%s, %s, %s, %s, %s)'

                        # Round up the "time_in" to the nearest absolute hour
                        time_in = datetime.strptime(time_am_pm, "%I:%M %p").time()
                        rounded_time_in = time_in.replace(second=0, microsecond=0)

                        if time_in.minute >= 40:
                            rounded_time_in = rounded_time_in.replace(minute=0)
                            rounded_time_in = datetime.combine(datetime.today(), rounded_time_in)
                            rounded_time_in += timedelta(hours=1)

                        if rounded_time_in.hour == 0:
                            rounded_time_in = rounded_time_in.replace(hour=12)

                        val = (date_str, rounded_time_in.strftime("%I:%M %p"), 'None', 'None', 'None')
                        cursor1.execute(sql, val)
                        log_id = cursor1.lastrowid
                        id_log_ids[the_id] = log_id
                        mydb1.commit()
                        id_last_action[the_id] = 'time_in'
                        take_values(the_id, the_id, date_str, rounded_time_in.strftime("%I:%M %p"), None)

                        try:
                            dialog.time_in_notif()
                        except Exception as e:
                            print(e)

                    elif id_last_action[the_id] == 'time_in':
                        # Fetch the time in value from the database
                        sql2 = f'SELECT time_in FROM id_{the_id} WHERE id={id_log_ids[the_id]}'
                        cursor2.execute(sql2)
                        res2 = cursor2.fetchall()
                        time_in_str = res2[0][0]  # Extract the time in value from the result

                        # Convert time in and time out strings to datetime objects
                        time_format = "%I:%M %p"
                        time_in = datetime.strptime(time_in_str, time_format)
                        time_out = datetime.strptime(time_am_pm, time_format)
                        time_out_param = time_am_pm

                        # Calculate the time difference
                        time_difference = time_out - time_in

                        # Get the total hours worked in decimal format
                        total_hours = time_difference.total_seconds() / 3600

                        # Round the total hours to 2 decimal places
                        total_hours = round(total_hours, 2)

                        # Get the absolute difference in hours
                        difference_hours = abs(time_difference.total_seconds() / 3600)

                        # Calculate the remaining hours after subtracting the difference
                        remaining_hours = 3 - difference_hours

                        # Round the remaining hours to 2 decimal places
                        remaining_hours = f'{round(remaining_hours, 2)} hrs'

                        total_hrs_param = f'{total_hours} hrs'

                        # Check if total hours is greater than 3
                        if total_hours > 3:
                            excess_hours = total_hours - 3
                            total_hours -= excess_hours
                            time_out_param = time_in + timedelta(hours=3)

                        if total_hours >= 3:
                            remaining_hours = '0 hrs'

                        # perform time out action
                        sql = f'UPDATE id_{the_id} SET time_out=%s, hours_worked=%s, late=%s WHERE id=%s'
                        val = (time_out_param, total_hrs_param, remaining_hours, id_log_ids[the_id])
                        cursor1.execute(sql, val)
                        mydb1.commit()
                        id_last_action[the_id] = 'time_out'
                        take_values(the_id, the_id, date_str, None, time_out_param)

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

