# This shared.py module is very important as it is the main mode for out-of-scope variable communication.
# Inside this module are two variables, named data_passing_var2 and keys_pressed.
# The data_passing_var2 is very important and used widely across almost all modules inside this project as it is used
# to know which ID/RFID tag or whose employee profile is to edit, view, or delete.
# The same for keys_pressed, very important yet serves a different function. Note that the RFID reader that is
# currently being in use is considered a keyboard emulator, and so READS KEYBOARD EVENTS.
# So if you type something with your keyboard, the code reads those keyboard presses as well.
# So a way to fix this is to declare a global variable inside this shared.py module so that the keys_pressed
# list gets cleared every certain event in other modules as so to avoid conflict to retrieve the attendance
# data.

data_passing_var2 = None
keys_pressed = []
